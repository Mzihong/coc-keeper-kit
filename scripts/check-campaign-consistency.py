#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mechanical consistency checks over one campaign folder.

Usage:
    python scripts/check-campaign-consistency.py --campaign <slug>
    python scripts/check-campaign-consistency.py --campaign <slug> --check   # exit non-zero on problems

Exit codes:
    0  no mechanical failures (manual-read items may still be listed — see below)
    1  at least one check FAILED
    2  no failures, but at least one check was SKIPPED and could not run

WHAT THIS IS FOR
----------------
`core/11-review.md` is a model reading for meaning. That reading kept getting spent on things a
regex does better — a name spelled two ways, a glossary row that drifted between two copies, an
open question that was answered months ago and still reads open. This script takes those, so the
review arrives at a fixed mechanical baseline every time and can spend itself on semantics.

`core/00-how-to-run.md` requires running this **and** `core/11-review.md` after any pass that
touches three or more files in a campaign, or changes a declared convention. Its output is the
artifact that makes that requirement auditable afterwards.

WHAT IT CANNOT SEE — read this before treating a green run as "the campaign is consistent"
------------------------------------------------------------------------------------------
  * **Semantic conflict.** `CLAUDE.md` calling an object an enchanted relic while `world/` calls
    it old-world hardware is two files disagreeing about what a thing *is*. No string comparison
    reaches that. It is the review's job.
  * **Whether two lists are even counting the same thing.** A proper-noun lock and a
    demand-driven NPC roster hold different numbers *by design*. Mistaking that for a
    contradiction is a real failure mode, so this script never compares list lengths.
  * **Descriptive residue.** A sentence describing a deleted location without naming it survives
    every grep here. Only cross-file reading catches it.
  * **Cross-language aliases.** Check 4 extracts Chinese nouns; an English alias of the same
    concept elsewhere in the repo will not be matched.

SKIPPED IS NOT PASS
-------------------
Checks 1, 3 and 4 read conventions that only exist if the campaign writes them: a proper-noun
lock table in `canon-log.md`, an `①②③`-style open-questions list, an Auto-filled table recording
what was deleted or superseded. A campaign without them would score zero hits on all three and
look immaculate. That is the worst possible failure, so a check that cannot find its input
reports SKIPPED, says which input was missing, and `--check` exits 2 rather than 0.
"""

import argparse
import io
import re
import sys
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

PASS, FAIL, SKIPPED = "PASS", "FAIL", "SKIPPED"

# Files that are records rather than live material: hits inside them are history, not drift.
LOG_FILES = {"rolls.log"}


class Result:
    def __init__(self, num, title):
        self.num = num
        self.title = title
        self.status = PASS
        self.reason = ""
        self.problems = []   # mechanical failures
        self.reads = []      # hits a human must read; never a failure on their own

    def fail(self, msg):
        self.status = FAIL
        self.problems.append(msg)

    def skip(self, reason):
        self.status = SKIPPED
        self.reason = reason

    def read(self, msg):
        self.reads.append(msg)


def campaign_files(root):
    """Every markdown file in the campaign, sorted, logs excluded."""
    return sorted(p for p in root.rglob("*.md") if p.name not in LOG_FILES)


def rel(root, path):
    return path.relative_to(root).as_posix()


def read(path):
    return path.read_text(encoding="utf-8")


def strip_md(text):
    """Normalise a fragment so formatting differences don't read as content differences."""
    text = re.sub(r"[*`>\[\]]", "", text)
    text = re.sub(r"\s+", "", text)
    return text.strip()


# --------------------------------------------------------------------------------------
# 1 — proper-noun drift
# --------------------------------------------------------------------------------------

CJK = r"一-鿿"
HONORIFICS = "老小大阿"


def check_proper_nouns(root, files):
    """Locked names from canon-log's table, checked for longer variants elsewhere.

    The failure this catches: a name locked as 塔恩 and written 老塔恩 in eighteen other places.
    Whichever spelling is *correct* is the Keeper's call — this only reports that the campaign
    holds two.
    """
    r = Result(1, "专名漂移 / proper-noun drift")
    canon = root / "canon-log.md"
    if not canon.exists():
        r.skip("canon-log.md not found")
        return r

    text = read(canon)
    # The lock lives under a 人 heading followed by a table whose first column is the name.
    # Prose or a blockquote may sit between the two — a header that explains what the table is
    # for is exactly the kind of thing a campaign adds, and it must not hide the table.
    m = re.search(r"\*\*人\*\*[^|]*?\n((?:\|.*\n)+)", text)
    if not m:
        r.skip("canon-log.md has no `**人**` proper-noun lock table — nothing to lock against")
        return r

    names = []
    for line in m.group(1).splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not cells or not cells[0]:
            continue
        name = strip_md(cells[0])
        if re.fullmatch(r"[%s·]+" % CJK, name) and name not in ("名",):
            names.append(name)

    if not names:
        r.skip("proper-noun table found but no names parsed out of it")
        return r

    for name in names:
        variants = defaultdict(list)
        for path in files:
            for i, line in enumerate(read(path).splitlines(), 1):
                for hit in re.finditer(re.escape(name), line):
                    start = hit.start()
                    # Only an honorific counts as part of the name. Any other preceding
                    # character is grammar — 见卡蕤 is a verb meeting a name, not a variant
                    # spelling of it, and reporting those buries the one real hit in noise.
                    prev = line[start - 1] if start else ""
                    key = prev + name if prev in HONORIFICS else name
                    variants[key].append(f"{rel(root, path)}:{i}")

        # A one-off is a typo or a quotation; a genuine competing spelling recurs.
        variants = {k: v for k, v in variants.items() if k == name or len(v) >= 2}
        if len(variants) > 1:
            summary = ", ".join(
                f"{v}({len(locs)})" for v, locs in sorted(variants.items(), key=lambda kv: -len(kv[1])))
            r.fail(f"「{name}」 written {len(variants)} ways: {summary}")
            for v, locs in sorted(variants.items(), key=lambda kv: -len(kv[1])):
                r.fail(f"    {v} → {', '.join(locs[:6])}{' …' if len(locs) > 6 else ''}")
    return r


# --------------------------------------------------------------------------------------
# 2 — translation glossary agreement
# --------------------------------------------------------------------------------------

def extract_glossary(text):
    """Rows of the two-column 里层/表层 table as {surface_term: row}.

    Deliberately strict about the header: a location table can also carry both words
    (`| 地点 | 表层 | KEEPER ONLY 里层 |`) and matching it drags scene descriptions in as
    glossary rows. The glossary proper is exactly two columns, 里层 first.
    """
    rows = {}
    in_table = False
    for line in text.splitlines():
        if line.startswith("|"):
            head = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(head) == 2 and head[0].startswith("里层") and head[1].startswith("表层"):
                in_table = True
                continue
        if in_table:
            if not line.startswith("|"):
                in_table = False
                continue
            if re.fullmatch(r"\|[\s\-:|]+\|", line.strip()):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 2:
                continue
            surface = re.search(r"\*\*(.+?)\*\*", cells[1])
            key = strip_md(surface.group(1)) if surface else strip_md(cells[1])[:12]
            rows[key] = (strip_md(cells[0]), strip_md(cells[1]))
    return rows


def check_glossary(root, files):
    """The campaign CLAUDE.md's glossary is the convention; every copy must match it row for row."""
    r = Result(2, "转译词表一致性 / translation glossary")
    authority = root / "CLAUDE.md"
    if not authority.exists():
        r.skip("campaign CLAUDE.md not found")
        return r

    master = extract_glossary(read(authority))
    if not master:
        r.skip("campaign CLAUDE.md declares no 里层/表层 glossary — nothing to compare against")
        return r

    copies = [p for p in files if p != authority and extract_glossary(read(p))]
    if not copies:
        r.reads.append("glossary declared in CLAUDE.md; no other file carries a copy (nothing to drift)")
        return r

    for path in copies:
        copy = extract_glossary(read(path))
        name = rel(root, path)
        for key in sorted(set(copy) - set(master)):
            r.fail(f"{name}: row 「{key}」 is not in CLAUDE.md's glossary (copy grew a row)")
        for key in sorted(set(master) - set(copy)):
            r.fail(f"{name}: row 「{key}」 from CLAUDE.md is missing here")
        for key in sorted(set(master) & set(copy)):
            if master[key] != copy[key]:
                r.fail(f"{name}: row 「{key}」 differs from CLAUDE.md")
                r.fail(f"    CLAUDE.md : {master[key][0]} | {master[key][1]}")
                r.fail(f"    {name} : {copy[key][0]} | {copy[key][1]}")
    return r


# --------------------------------------------------------------------------------------
# 3 — open questions
# --------------------------------------------------------------------------------------

MARKERS = "①②③④⑤⑥⑦⑧⑨"


QUESTION_CONTEXT = ("问号", "留白", "still open", "未决")
PUNCT = "，,。.、；;：:—－·（）()「」【】\"'!?！？~…-*`>[]"


# How many identical leading characters mean "the same question" — unless one fragment runs
# out first, in which case being a complete prefix of the other is enough. Files clip the
# question at different places (a parenthetical survives, an em-dash clause doesn't), so the
# shorter form is regularly a truncation of the longer rather than a different question.
SAME_QUESTION = 16


def common_prefix(a, b):
    n = 0
    for x, y in zip(a, b):
        if x != y:
            break
        n += 1
    return n


def normalise_question(text):
    """Strip everything that is presentation, keep the words."""
    return "".join(ch for ch in text if ch not in PUNCT and not ch.isspace())


def extract_questions(text):
    """{marker: normalised text} for an ①②③-style open-questions list.

    Three filters, every one of them added because it fired wrongly on a real campaign:
      * `①②③` is also how a numbered causal chain gets written. A marker only counts if a line
        in the preceding window announces questions.
      * `问号 ③）` and `问号③的那条线` are cross-references, not listings — a marker introduced
        by 问号/问题 carries no question text after it.
      * The captured text stops at the **next** marker. Reading a fixed window past it drags
        the following question in, and then two files that agree perfectly report as different
        because one of them wraps its lines somewhere else.
    """
    lines = text.splitlines()
    found = {}
    for idx, line in enumerate(lines):
        window = "\n".join(lines[max(0, idx - 15):idx + 1])
        if not any(w in window for w in QUESTION_CONTEXT):
            continue
        for marker in MARKERS:
            if marker in found:
                continue
            pos = line.find(marker)
            if pos < 0:
                continue
            if line[max(0, pos - 2):pos].strip().endswith(("号", "题")):
                continue
            # Join wrapped continuation lines, but stop at a blank line or a new list item —
            # what follows a question is usually commentary, and every file words its
            # commentary differently. Dragging it in makes files that agree look like they
            # don't.
            parts = [line[pos + 1:]]
            for nxt in lines[idx + 1:idx + 3]:
                body = nxt.lstrip("> ").strip()
                if not body or body.startswith(("- ", "* ", "#", "|")):
                    break
                parts.append(body)
            tail = " ".join(parts)
            for other in MARKERS:
                if other != marker:
                    tail = tail.split(other)[0]
            # A question ends where its sentence ends; an em-dash or full stop starts the
            # commentary, and commentary is where identical questions diverge.
            for terminator in ("——", "。"):
                tail = tail.split(terminator)[0]
            frag = normalise_question(strip_md(tail))[:30]
            if len(frag) >= 6:
                found[marker] = frag
    return found


def check_open_questions(root, files):
    """Every file listing the campaign's open questions must list the same ones.

    Answers are one-directional — questions only ever get fewer. An answered question reads
    exactly like a live one, so nothing but comparison finds it. This reports divergence and
    which files hold which variant; it does not decide which wording is right.
    """
    r = Result(3, "留白问号一致性 / open questions")
    authority = root / "CLAUDE.md"
    if not authority.exists():
        r.skip("campaign CLAUDE.md not found")
        return r

    master = extract_questions(read(authority))
    if not master:
        r.skip("campaign CLAUDE.md has no ①②③-style open-questions list — no baseline to compare")
        return r

    variants = defaultdict(lambda: defaultdict(list))
    for path in files:
        qs = extract_questions(read(path))
        for marker, frag in qs.items():
            variants[marker][frag].append(rel(root, path))

    for marker in sorted(variants, key=lambda c: MARKERS.index(c)):
        # Files truncate at different points and append their own commentary. Two fragments
        # that agree for this long are the same question worded to different lengths — real
        # divergence shows up early, in the first clause, not at character 25.
        forms = {}
        for frag in sorted(variants[marker], key=len, reverse=True):
            match = next((k for k in forms
                          if common_prefix(k, frag) >= min(SAME_QUESTION, len(k), len(frag))),
                         None)
            if match:
                forms[match].extend(variants[marker][frag])
            else:
                forms[frag] = list(variants[marker][frag])

        if len(forms) > 1:
            r.fail(f"question {marker} appears in {len(forms)} different wordings:")
            for frag, where in sorted(forms.items(), key=lambda kv: -len(kv[1])):
                mark = "  <- CLAUDE.md" if master.get(marker) == frag else ""
                r.fail(f"    「{frag}…」 in {', '.join(sorted(where))}{mark}")
            if marker not in master:
                r.fail(f"    (CLAUDE.md itself lists no {marker} — downstream grew a question)")
    return r


# --------------------------------------------------------------------------------------
# 4 — residue of deleted settings
# --------------------------------------------------------------------------------------

DELETION_WORDS = ("删除", "并入", "推翻", "废弃", "取代")


def check_deleted_concepts(root, files):
    """Names the campaign records as deleted or superseded, still present in the text.

    Reported for reading, never as a failure: a line explaining that something *was* removed is
    supposed to name it. Counting hits is exactly the wrong response — read each one.
    """
    r = Result(4, "被删设定残留 / residue of deleted settings")
    authority = root / "CLAUDE.md"
    if not authority.exists():
        r.skip("campaign CLAUDE.md not found")
        return r

    text = read(authority)
    table_rows = [ln for ln in text.splitlines() if ln.startswith("|")]
    terms = set()
    for line in table_rows:
        for word in DELETION_WORDS:
            for m in re.finditer(r"([%s]{2,6})%s" % (CJK, word), line):
                terms.add(m.group(1))
        for m in re.finditer(r"「(.+?)」", line):
            if any(w in line for w in DELETION_WORDS):
                terms.add(strip_md(m.group(1)))

    if not terms:
        r.skip("no 删除/并入/推翻 records found in CLAUDE.md — cannot know what was superseded")
        return r

    for term in sorted(terms):
        hits = []
        for path in files:
            for i, line in enumerate(read(path).splitlines(), 1):
                if term in line:
                    hits.append(f"{rel(root, path)}:{i}")
        if hits:
            r.read(f"「{term}」 (recorded as removed/superseded) still appears in {len(hits)} place(s) "
                   f"— read every one, do not count them: {', '.join(hits)}")
    return r


# --------------------------------------------------------------------------------------
# 5 — dead relative links
# --------------------------------------------------------------------------------------

def check_links(root, files):
    r = Result(5, "死链 / relative links resolve")
    for path in files:
        for i, line in enumerate(read(path).splitlines(), 1):
            for m in re.finditer(r"\]\(([^)]+)\)", line):
                target = m.group(1).split("#")[0].strip()
                if not target or target.startswith(("http://", "https://", "mailto:")):
                    continue
                if not (path.parent / target).resolve().exists():
                    r.fail(f"{rel(root, path)}:{i} → {target} does not exist")
    return r


# --------------------------------------------------------------------------------------
# 6 — self-describing counts
# --------------------------------------------------------------------------------------

COUNT_RE = re.compile(r"(\d+)\s*(位|条|行|份|处|个|张)")


def check_counts(root, files):
    """Counts written next to a file path — 'roster.md 已有 10 行 stub'.

    These go stale silently and get copied forward. The script lists candidates; verifying one
    means counting the actual thing, which only a reader can decide how to do.
    """
    r = Result(6, "计数自述 / counts asserted beside a path")
    for path in files:
        for i, line in enumerate(read(path).splitlines(), 1):
            if not COUNT_RE.search(line):
                continue
            if not re.search(r"`[^`]+\.(md|json|py|svg)`", line):
                continue
            r.read(f"{rel(root, path)}:{i} {line.strip()[:110]}")
    return r


# --------------------------------------------------------------------------------------

CHECKS = [check_proper_nouns, check_glossary, check_open_questions,
          check_deleted_concepts, check_links, check_counts]


def main():
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

    ap = argparse.ArgumentParser(description="Mechanical consistency checks over one campaign.")
    ap.add_argument("--campaign", required=True, help="campaign slug under campaigns/")
    ap.add_argument("--check", action="store_true", help="exit non-zero on problems")
    args = ap.parse_args()

    root = REPO / "campaigns" / args.campaign
    if not root.is_dir():
        print(f"no such campaign: {root}")
        return 1

    files = campaign_files(root)
    print(f"campaign: {args.campaign}  ({len(files)} markdown files)\n")

    results = [fn(root, files) for fn in CHECKS]

    failed = skipped = 0
    for res in results:
        if res.status == FAIL:
            failed += 1
            print(f"check {res.num}: FAIL  — {res.title}")
            for line in res.problems:
                print(f"  {line}")
        elif res.status == SKIPPED:
            skipped += 1
            print(f"check {res.num}: SKIPPED — {res.title}")
            print(f"  cannot run: {res.reason}")
            print("  SKIPPED IS NOT PASS: this check found nothing because it had nothing to read.")
        else:
            print(f"check {res.num}: PASS  — {res.title}")
        print()

    reads = [(res, line) for res in results for line in res.reads]
    if reads:
        print(f"MANUAL — {len(reads)} item(s) this script cannot judge. Read each one; "
              f"the count is not the point.\n")
        for res, line in reads:
            print(f"  [{res.num}] {line}")
        print()

    print(f"summary: {len(results) - failed - skipped} passed, {failed} failed, "
          f"{skipped} skipped, {len(reads)} for manual reading")
    if failed or skipped:
        print("\nExit 0 would mean 'no mechanical failures' — never 'this campaign is consistent'.")
        print("Semantic conflicts, descriptive residue and cross-language aliases are the "
              "review's job (core/11-review.md).")

    if not args.check:
        return 0
    if failed:
        return 1
    if skipped:
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
