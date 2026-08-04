#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Build the reverse index over reference/ — third-party archives and the kit's own content.

Usage:
    python scripts/build-reference-index.py            # write the index files
    python scripts/build-reference-index.py --check    # validate only, exit 1 on problems

Writes:
    reference/decks/index.json         one directory
    reference/sourcebooks/index.json   one directory
    reference/rules/index.json         one directory
    reference/craft/index.json         one directory
    reference/bestiary/index.json      one directory
    reference/mythos/index.json        one directory
    reference/tables/index.json        one directory
    reference/index.json               the whole chain, both directions, all seven directories
    reference/tables/monster-index.md  the 223-entry malleus navigation table (see below)

Nothing here is authored by hand. In `decks/` and `sourcebooks/` — third-party material — each
entry's provenance is *parsed out of the file's own* `## 引用出处` table, so the citation block
stays the single source of truth. In `rules/`, `craft/`, `bestiary/`, `mythos/`, `tables/` — the
kit's own writing — there is no citation to parse; the index exists purely to answer "does
anything in the repo reference this file, or is it an orphan?" `referenced_by` in every directory
is found the same way: scanning the repo for mentions of the file. Rewrite the index whenever you
add, rename, or retire a file in any of these seven directories — see
`core/14-archive-reference.md` for the third-party ones.

`reference/tables/monster-index.md` is a special case within `tables/`: instead of citing one
source file, it's assembled from `reference/sourcebooks/malleus-monstrorum-zh.md` (parsed fresh
every run — name/tier/SAN/anchor for all 223 entries), `reference/tables/monster-index-data.json`
(hand-written `Serves`/summary, the two fields the parser can't derive), and any matching
`reference/bestiary/*.md` entry (overrides the row once a creature is actually written up). See
`parse_malleus_entries()` / `build_monster_index()` below and
`update_plan/2026-08-02-monster-templates-traits.md` stage B for why.

Validation (always on, and the whole point of --check):
  - every .md in a third-party dir (`decks/`, `sourcebooks/`) carries a `## 引用出处` section
    with every required row filled
  - no file in ANY of the seven indexed directories is orphaned (nothing references it) without
    saying so — this applies to the kit's own content too, not just archived material
  - every row in `monster-index.md` has a non-empty `Serves` and index summary — a half-filled
    index is worse than no index (misleads instead of admitting a gap)
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REF = os.path.join(ROOT, "reference")

# Third-party material, governed by the citation rule.
ARCHIVE_DIRS = [
    ("decks", "official card decks — ready-made entries, drawn from directly"),
    ("sourcebooks", "full official books — deep reference, looked up a chapter at a time"),
]

# The kit's own writing. No citation to parse — indexed only for the referenced_by /
# orphan check, so a stale cheat-sheet or table nothing points at gets flagged the same
# way an unwired archive file would.
ORIGINAL_DIRS = [
    ("rules", "kit's own CoC 7e mechanics cheat-sheets — checks, Sanity, combat, character creation"),
    ("craft", "distilled craft knowledge — how to write it, as opposed to what the numbers are"),
    ("bestiary", "reusable monsters and Mythos entities, portable across campaigns"),
    ("mythos", "Great Old Ones, tomes, spells, cults, and factions — slow-growing shared lore"),
    ("tables", "roll tables for prep and live improv, including the four seed tables"),
]

# rules/, craft/ and tables/ ship in dist/bundle.md (see scripts/build-bundle.sh);
# bestiary/ and mythos/ don't.
ORIGINAL_IN_BUNDLE = {"rules": True, "craft": True, "bestiary": False,
                      "mythos": False, "tables": True}

# Whether "nothing references this file" is a defect. For rules/ and tables/ it is — a
# cheat-sheet or table no spec reads is dead weight the generators will never load. For
# bestiary/ and mythos/ it is not: those are content libraries the Keeper draws from by
# hand, and most entries are legitimately unreferenced by any spec. Flag them as orphans
# in the index (so they're still visible), but don't fail --check over it.
ORPHAN_IS_ERROR = {"decks": True, "sourcebooks": True, "rules": True, "craft": True,
                   "tables": True, "bestiary": False, "mythos": False}

# Where a reference to an archived file could plausibly be written.
SCAN_DIRS = ["core", "templates", "reference", "campaigns", "scripts", "update_plan", ".claude"]
SCAN_FILES = ["CLAUDE.md", "GEMINI.md", "AGENTS.md", "README.md", "CONTRIBUTING.md",
              "CHANGELOG.md", "WORKLOG.md"]
SCAN_EXT = (".md", ".json", ".py", ".sh", ".yaml", ".yml")

REQUIRED_ROWS = ["作品", "版权方", "版本", "本文来源", "收录范围", "收录用途"]
ROW_KEY = {"作品": "work", "版权方": "rights_holder", "版本": "edition",
           "本文来源": "source", "收录范围": "scope", "收录用途": "purpose",
           "已知问题": "known_issues"}

CITATION_HEADING = "## 引用出处"
STRIP_MD = re.compile(r"[*`]")


def read(path):
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def parse_citation(text):
    """Pull the `## 引用出处` table into a dict. Returns (provenance, problems)."""
    if CITATION_HEADING not in text:
        return None, ["missing the `## 引用出处` section"]
    block = text.split(CITATION_HEADING, 1)[1]
    prov, problems = {}, []
    for line in block.split("\n"):
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) != 2 or set(cells[0]) <= set("-: "):
            continue
        label, value = cells[0], STRIP_MD.sub("", cells[1]).strip()
        key = ROW_KEY.get(label)
        if key and value:
            prov[key] = value
    for label in REQUIRED_ROWS:
        if not prov.get(ROW_KEY[label]):
            problems.append("citation table is missing or empty: %s" % label)
    return prov, problems


def parse_title(text):
    for line in text.split("\n"):
        if line.startswith("# "):
            return STRIP_MD.sub("", line[2:]).strip()
    return None


def parse_uses(text):
    """Backtick-quoted paths in the header block — what the file says it is for."""
    head = text.split("---", 1)[0]
    return sorted(set(re.findall(r"`((?:core|reference|templates|update_plan)/[^`]+?\.md)`", head)))


def scan_targets():
    files = [os.path.join(ROOT, f) for f in SCAN_FILES]
    for d in SCAN_DIRS:
        for dirpath, dirnames, filenames in os.walk(os.path.join(ROOT, d)):
            dirnames[:] = [x for x in dirnames
                           if x not in (".git", "og_Norval", "external", "dist", "sourcebooks")]
            for name in filenames:
                # The index files are this script's own output — counting them as
                # references would make every entry look cited by itself.
                if name == "index.json":
                    continue
                if name.endswith(SCAN_EXT):
                    files.append(os.path.join(dirpath, name))
    return [f for f in files if os.path.isfile(f)]


def find_references(relpath, basename, targets, self_path):
    """Who points at this archived file? Matches the full path or the bare filename."""
    hits = []
    for path in targets:
        if os.path.abspath(path) == os.path.abspath(self_path):
            continue
        try:
            text = read(path)
        except (UnicodeDecodeError, OSError):
            continue
        if relpath not in text and basename not in text:
            continue
        for n, line in enumerate(text.split("\n"), 1):
            if relpath in line or basename in line:
                hits.append({
                    "file": os.path.relpath(path, ROOT).replace(os.sep, "/"),
                    "line": n,
                    "context": line.strip()[:160],
                })
    return hits


def list_md_files_recursive(dirpath):
    """Sorted relative paths (posix-style, e.g. 'great-old-ones/cthulhu.md') of every .md
    file under dirpath, at any depth — README.md and index.json excluded at every level."""
    out = []
    for sub, dirnames, filenames in os.walk(dirpath):
        dirnames.sort()
        for name in sorted(filenames):
            if name == "index.json" or name == "README.md" or not name.endswith(".md"):
                continue
            rel = os.path.relpath(os.path.join(sub, name), dirpath).replace(os.sep, "/")
            out.append(rel)
    return sorted(out)


def build_entry(dirname, name, path, targets, require_citation):
    """One file's index entry, plus any problems found in it. `name` may be a nested
    relative path (e.g. 'great-old-ones/cthulhu.md'); references also match the bare
    leaf filename so a loose in-text mention doesn't have to spell out the subdirectory."""
    text = read(path)
    relpath = "reference/%s/%s" % (dirname, name)
    file_problems = []
    prov = None
    if require_citation:
        prov, file_problems = parse_citation(text)
    leaf = name.rsplit("/", 1)[-1]
    refs = find_references(relpath, leaf, targets, path)
    if not refs and ORPHAN_IS_ERROR.get(dirname, True):
        file_problems.append("orphaned: nothing in the repo references it")
    entry = {
        "file": name,
        "path": relpath,
        "title": parse_title(text),
        "lines": text.count("\n") + 1,
        "declared_consumers": parse_uses(text),
        "referenced_by": refs,
        "reference_count": len(refs),
    }
    if require_citation:
        entry["cited"] = prov is not None and not any("citation" in p for p in file_problems)
        entry["provenance"] = prov or {}
    return entry, file_problems


MALLEUS_PATH = os.path.join(REF, "sourcebooks", "malleus-monstrorum-zh.md")
MONSTER_INDEX_DATA_PATH = os.path.join(REF, "tables", "monster-index-data.json")
MONSTER_INDEX_OUT_PATH = os.path.join(REF, "tables", "monster-index.md")

MI_CLASS_TOKENS = ["独立种族", "仆从种族", "唯一存在", "传说生物",
                    "旧神", "旧日支配者", "梦境诸神", "外神", "化身"]
MI_STAT_ROW_RE = re.compile(r'^\|\s*力量')
MI_CLASS_LINE_RE = re.compile(r'^(上级|下级)?(' + "|".join(MI_CLASS_TOKENS) + r')\*{0,2}\s*$')
MI_SAN_LINE_RE = re.compile(r'理智值?(丧失|损失)\s*[:：]\s*(.+)')
MI_STRIP_RE = re.compile(r'<br/>|\*')
MI_BAD_NAME_PREFIXES = ("攻击方式", "其他特性", "教团", "特效", "精神力量", "武器",
                         "护甲", "装甲", "咒文", "技能", "移动", "耐久")
# A real name heading is a *whole* bold span wrapping the parenthesised English name
# ('**NAME (EN NAME)**', end-anchored). A bare `re.search` for "**" and "(" anywhere on the
# line — the first version of this — false-matched bolded subsection labels like
# "**触肢攻击**：...（小数点后无条件省略）..." (a mid-paragraph aside in unrelated parens,
# not a name) and fed the wrong string into the index. Anchoring the closing `**` to end-of-line
# rules those out.
MI_NAME_HEADING_RE = re.compile(r'\*\*[^*]*[（(][^*]*\*\*\s*$')

# type/threat/tier are the kit's own dimension (core/07); this maps the book's own
# classification labels onto that ladder (reference/rules/monster-scale.md).
MI_TIER_MAP = {
    "下级独立种族": ("L2", "下级"), "上级独立种族": ("L2", "上级"), "独立种族": ("L2", None),
    "下级仆从种族": ("L3", "下级"), "上级仆从种族": ("L3", "上级"), "仆从种族": ("L3", None),
    "唯一存在": ("L4", None),
    "旧神": ("L5", "旧神"), "旧日支配者": ("L5", "旧日支配者"),
    "梦境诸神": ("L5", "梦境诸神"), "外神": ("L5", "外神"), "化身": ("L5", "化身"),
}


def mi_strip(s):
    return MI_STRIP_RE.sub("", s).strip()


def mi_looks_like_name(raw):
    if not raw or len(raw) > 60 or raw.startswith(("|", "-")):
        return False
    if raw.startswith(MI_BAD_NAME_PREFIXES):
        return False
    if raw.endswith(("。", "，", "、", ":", "：")) or "：" in raw or ":" in raw:
        return False
    if "%" in raw or re.search(r'\d[dD]\d', raw):
        return False
    return bool(re.search(r'[一-鿿]', raw))


def parse_malleus_entries():
    """Scaffold the 223 stat-block entries in malleus-monstrorum-zh.md: name (CN/EN), the
    book's own classification label mapped to this kit's tier ladder, SAN loss, and the source
    line to anchor back to. Best-effort — verified against the file's own '223 属性块' header
    count; SAN is occasionally left blank where the source states none inline near the table
    (checked by hand during the stage-B content pass, see update_plan/2026-08-02-
    monster-templates-traits.md)."""
    if not os.path.isfile(MALLEUS_PATH):
        return []
    with open(MALLEUS_PATH, encoding="utf-8") as fh:
        lines = fh.readlines()
    n = len(lines)
    stat_rows = [i for i in range(n) if MI_STAT_ROW_RE.match(lines[i])]

    entries = []
    for row_idx in stat_rows:
        name_line_idx = None
        for j in range(row_idx - 1, max(row_idx - 15, -1), -1):
            raw = lines[j].strip()
            if raw and MI_NAME_HEADING_RE.search(raw):
                name_line_idx = j
                break
        if name_line_idx is None:
            for j in range(row_idx - 1, max(row_idx - 40, -1), -1):
                raw = lines[j].strip()
                if raw and mi_looks_like_name(mi_strip(raw)):
                    name_line_idx = j
                    break

        class_label = None
        for j in range(row_idx - 1, -1, -1):
            m = MI_CLASS_LINE_RE.match(mi_strip(lines[j].strip()))
            if m:
                class_label = (m.group(1) or "") + m.group(2)
                break

        san_text = None
        for j in range(row_idx, min(row_idx + 150, n)):
            m = MI_SAN_LINE_RE.search(lines[j])
            if m:
                san_text = mi_strip(m.group(2)).rstrip("。").strip()
                break
            if j != row_idx and MI_STAT_ROW_RE.match(lines[j]):
                break

        name_raw = mi_strip(lines[name_line_idx].strip()) if name_line_idx is not None else None
        entries.append({"idx": len(entries) + 1, "line": row_idx + 1,
                         "name_raw": name_raw, "class_label": class_label, "san": san_text})

    for i, e in enumerate(entries):
        if not e["name_raw"] and i > 0:
            e["name_raw"] = entries[i - 1]["name_raw"] + "（续/亚型）"

    for e in entries:
        m = re.match(r'^([^（(]+)[（(](.+)[）)]\s*$', e["name_raw"] or "")
        e["name_cn"], e["name_en"] = (m.group(1).strip(), m.group(2).strip()) if m else (e["name_raw"], None)
        tier, subtier = MI_TIER_MAP.get(e["class_label"], (None, None))
        e["tier"], e["subtier"] = tier, subtier
    return entries


MI_BESTIARY_FIELD_RE = {
    "tier": re.compile(r'-\s*\*\*Tier:\*\*\s*(.+)'),
    "threat": re.compile(r'-\s*\*\*Threat:\*\*\s*(.+)'),
    "sanity": re.compile(r'-\s*\*\*Sanity to see:\*\*\s*(.+)'),
    "serves": re.compile(r'-\s*\*\*Serves:\*\*\s*(.+)'),
    "summary": re.compile(r'-\s*\*\*Index summary:\*\*\s*(.+)'),
}


def parse_bestiary_headers():
    """The kit's own reference/bestiary/*.md entries: title plus the header fields
    templates/monster.md defines, read to override the malleus-derived row for any entry
    that's actually been written up (a bestiary entry is more authoritative than the raw
    transcript scaffold — see monster-index-data.json's _meta)."""
    dirpath = os.path.join(REF, "bestiary")
    out = []
    if not os.path.isdir(dirpath):
        return out
    for name in sorted(os.listdir(dirpath)):
        if not name.endswith(".md") or name == "README.md":
            continue
        text = read(os.path.join(dirpath, name))
        fields = {"file": name, "title": parse_title(text)}
        head = text.split("## Reveal", 1)[0]
        for key, rx in MI_BESTIARY_FIELD_RE.items():
            m = rx.search(head)
            fields[key] = m.group(1).strip() if m else None
        out.append(fields)
    return out


def mi_match_bestiary(entry, b):
    """Strict match: every significant (4+ letter) word in the bestiary title must hit a
    same-or-prefix word in the malleus entry's English name (order-independent, plural-tolerant
    — 'Thrall of Cthulhu' vs 'THRALLS OF CTHULHU, Servants of Cthulhu'). Whole-word only — a
    naive substring check would let 'Black Wing' false-match 'BURROWING Horrors' on 'WING'.
    Requires 2+ significant words so a single common word (e.g. bare 'Cthulhu') can't match
    alone; titles with only one, or with none, never match and the entry stays kit-original."""
    if not b.get("title") or not entry.get("name_en"):
        return False
    words_b = [w for w in re.sub(r'[^A-Z]', ' ', b["title"].upper()).split() if len(w) > 3]
    if len(words_b) < 2:
        return False
    malleus_words = [w for w in re.sub(r'[^A-Z]', ' ', entry["name_en"].upper()).split() if len(w) > 3]
    def word_hit(wb):
        return any(wb == wm or wb.startswith(wm) or wm.startswith(wb) for wm in malleus_words)
    return sum(1 for wb in words_b if word_hit(wb)) == len(words_b)


def build_monster_index():
    """Generate reference/tables/monster-index.md — the navigation table over all 223 malleus
    entries (name/tier/SAN from the transcript, Serves/summary hand-written in
    monster-index-data.json, both overridden by a matching reference/bestiary/ entry once one
    exists). Returns validation problems: an empty Serves or summary is as bad as a missing
    citation block — a half-filled index is worse than no index (see the stage-B plan)."""
    problems = []
    entries = parse_malleus_entries()
    if not entries:
        return problems  # sourcebook not present locally — nothing to build, not an error
    overrides = {}
    if os.path.isfile(MONSTER_INDEX_DATA_PATH):
        with open(MONSTER_INDEX_DATA_PATH, encoding="utf-8") as fh:
            overrides = {k: v for k, v in json.load(fh).items() if k != "_meta"}
    bestiary = parse_bestiary_headers()
    matched = set()

    rows = []
    for e in entries:
        ov = overrides.get(str(e["idx"]), {})
        row = dict(e, serves=ov.get("serves", ""), summary=ov.get("summary", ""),
                   threat=None, bestiary_file=None,
                   source="`reference/sourcebooks/malleus-monstrorum-zh.md`:%d" % e["line"])
        for b in bestiary:
            if b["file"] not in matched and mi_match_bestiary(e, b):
                matched.add(b["file"])
                row["bestiary_file"] = b["file"]
                tier_m = re.match(r'(L[2-5])', b.get("tier") or "")
                if tier_m:
                    row["tier"] = tier_m.group(1)
                if b.get("threat"):
                    row["threat"] = b["threat"]
                if b.get("sanity"):
                    row["san"] = b["sanity"]
                if b.get("serves"):
                    row["serves"] = b["serves"]
                if b.get("summary"):
                    row["summary"] = b["summary"]
                break
        rows.append(row)
    extra = [b for b in bestiary if b["file"] not in matched]

    for row in rows:
        if not row["serves"] or not row["summary"]:
            problems.append("reference/tables/monster-index.md: idx %d (%s) missing %s" % (
                row["idx"], row.get("name_cn") or row.get("name_raw"),
                "Serves" if not row["serves"] else "index summary"))
    for b in extra:
        if not b.get("serves") or not b.get("summary"):
            problems.append("reference/bestiary/%s: missing %s (needed by monster-index.md)" % (
                b["file"], "Serves" if not b.get("serves") else "Index summary"))

    tiers = [("L2", "L2 — creature (独立种族 / 传说生物)"),
             ("L3", "L3 — servitor (仆从种族)"),
             ("L4", "L4 — unique (唯一存在)"),
             ("L5", "L5 — deity (旧神 / 旧日支配者 / 梦境诸神 / 外神 / 化身)")]
    lines = [
        "# Monster Index — navigation table",
        "",
        "> Generated by `scripts/build-reference-index.py` from "
        "`reference/sourcebooks/malleus-monstrorum-zh.md` (223 entries) plus hand-written "
        "`Serves`/summary fields in `reference/tables/monster-index-data.json`, overridden by "
        "any matching `reference/bestiary/*.md` entry (more authoritative once a creature is "
        "actually written up). **Do not hand-edit this file.**",
        ">",
        "> Use this to answer \"what's a fitting elite/servitor for boss X\" — read `Serves` to "
        "find who answers to a given deity, `Index summary` to pick between candidates at the "
        "same tier. The summary is not the Reveal — it helps a model or Keeper match, not "
        "something to read aloud at the table. See `core/07-create-monster.md` and "
        "`core/04-design-scenario.md`.",
        "",
    ]
    for tier_key, tier_title in tiers:
        tier_rows = [r for r in rows if r["tier"] == tier_key]
        if not tier_rows:
            continue
        lines.append("## %s" % tier_title)
        lines.append("")
        lines.append("| Name | SAN | Serves | Index summary | Source |")
        lines.append("|---|---|---|---|---|")
        for r in tier_rows:
            source = ("`reference/bestiary/%s`" % r["bestiary_file"]) if r["bestiary_file"] else r["source"]
            lines.append("| %s | %s | %s | %s | %s |" % (
                r.get("name_raw") or "?", r["san"] or "—",
                r["serves"] or "**MISSING**", r["summary"] or "**MISSING**", source))
        lines.append("")

    if extra:
        lines.append("## Kit-original entries (not in the malleus transcript)")
        lines.append("")
        lines.append("| Name | Tier | SAN | Serves | Index summary | Source |")
        lines.append("|---|---|---|---|---|---|")
        for b in extra:
            lines.append("| %s | %s | %s | %s | %s | `reference/bestiary/%s` |" % (
                b.get("title") or b["file"], b.get("tier") or "—", b.get("sanity") or "—",
                b.get("serves") or "**MISSING**", b.get("summary") or "**MISSING**", b["file"]))
        lines.append("")

    with open(MONSTER_INDEX_OUT_PATH, "w", encoding="utf-8", newline="\n") as fh:
        fh.write("\n".join(lines) + "\n")
    return problems


def build():
    problems, directories, all_entries = [], [], []
    problems.extend(build_monster_index())
    targets = scan_targets()

    for dirname, role in ARCHIVE_DIRS:
        dirpath = os.path.join(REF, dirname)
        if not os.path.isdir(dirpath):
            continue
        entries = []
        for name in sorted(os.listdir(dirpath)):
            if not name.endswith(".md") or name == "README.md":
                continue
            path = os.path.join(dirpath, name)
            entry, file_problems = build_entry(dirname, name, path, targets, require_citation=True)
            problems.extend("%s: %s" % (entry["path"], p) for p in file_problems)
            entries.append(entry)
        index = {
            "directory": "reference/%s" % dirname,
            "role": role,
            "kind": "third-party-source-material",
            "governed_by": "reference/%s/README.md" % dirname,
            "citation_rule": "every file ends with a `## 引用出处` block; no citation, no file",
            "usage_rule": "take structure and scale, never text (core/00-how-to-run.md)",
            "in_bundle": False,
            "generated_by": "scripts/build-reference-index.py — do not edit by hand",
            "entry_count": len(entries),
            "entries": entries,
        }
        with open(os.path.join(dirpath, "index.json"), "w", encoding="utf-8", newline="\n") as fh:
            json.dump(index, fh, ensure_ascii=False, indent=2)
            fh.write("\n")
        directories.append(index)
        all_entries.extend(entries)

    for dirname, role in ORIGINAL_DIRS:
        dirpath = os.path.join(REF, dirname)
        if not os.path.isdir(dirpath):
            continue
        entries = []
        for name in list_md_files_recursive(dirpath):
            path = os.path.join(dirpath, *name.split("/"))
            entry, file_problems = build_entry(dirname, name, path, targets, require_citation=False)
            problems.extend("%s: %s" % (entry["path"], p) for p in file_problems)
            entries.append(entry)
        index = {
            "directory": "reference/%s" % dirname,
            "role": role,
            "kind": "kit-original-content",
            "governed_by": "reference/%s/README.md" % dirname,
            "citation_rule": None,
            "usage_rule": "authored by this kit — read and used directly, no citation required",
            "in_bundle": ORIGINAL_IN_BUNDLE.get(dirname, False),
            "generated_by": "scripts/build-reference-index.py — do not edit by hand",
            "entry_count": len(entries),
            "entries": entries,
        }
        with open(os.path.join(dirpath, "index.json"), "w", encoding="utf-8", newline="\n") as fh:
            json.dump(index, fh, ensure_ascii=False, indent=2)
            fh.write("\n")
        directories.append(index)
        all_entries.extend(entries)

    # The chain, keyed the other way round: consumer -> the material it depends on.
    chain = {}
    for entry in all_entries:
        for ref in entry["referenced_by"]:
            consumer = ref["file"]
            if consumer.startswith("reference/") and "/index.json" in consumer:
                continue
            chain.setdefault(consumer, set()).add(entry["path"])

    root_index = {
        "generated_by": "scripts/build-reference-index.py — do not edit by hand",
        "what": "reverse index over reference/ — third-party archives (citation required) "
                "plus the kit's own rules/craft/bestiary/mythos/tables content (referenced_by / "
                "orphan check only, no citation)",
        "rules": {
            "citation": "core/00-how-to-run.md → ground rules → Citing official material",
            "process": "core/14-archive-reference.md (skill: archive-reference)",
        },
        "kit_original_loose_files": {
            "note": "authored by this kit and deliberately left at reference/ root — a spine "
                    "document, a peer of reference/README.md rather than a member of any "
                    "category. Not covered by this index.",
            "files": ["reference/glossary-zh.md"],
        },
        "third_party_elsewhere": {
            "reference/og_Norval": "H.P. Lovecraft corpus (82 stories), public domain, craft "
                                   "research only; distilled into reference/craft/lovecraft-zh.md",
            "reference/external": "third-party repos as git submodules (see .gitmodules)",
        },
        "directories": [
            {
                "directory": d["directory"],
                "role": d["role"],
                "kind": d["kind"],
                "in_bundle": d["in_bundle"],
                "entry_count": d["entry_count"],
                "index": "%s/index.json" % d["directory"],
                "files": [e["path"] for e in d["entries"]],
            } for d in directories
        ],
        "reverse_index": {
            "note": "file -> everything in the repo that references it, with line numbers — "
                    "spans both third-party archives and the kit's own indexed content",
            "by_source": {
                e["path"]: {
                    "title": e["title"],
                    "rights_holder": e.get("provenance", {}).get("rights_holder"),
                    "referenced_by": ["%s:%d" % (r["file"], r["line"]) for r in e["referenced_by"]],
                } for e in all_entries
            },
            "by_consumer": {k: sorted(v) for k, v in sorted(chain.items())},
        },
        "validation": {
            "clean": not problems,
            "problems": problems,
        },
    }
    with open(os.path.join(REF, "index.json"), "w", encoding="utf-8", newline="\n") as fh:
        json.dump(root_index, fh, ensure_ascii=False, indent=2)
        fh.write("\n")

    return all_entries, problems


def main():
    check_only = "--check" in sys.argv
    entries, problems = build()
    print("indexed %d files across %d directories (%d third-party, %d kit-original)"
          % (len(entries), len(ARCHIVE_DIRS) + len(ORIGINAL_DIRS),
             len(ARCHIVE_DIRS), len(ORIGINAL_DIRS)))
    for e in entries:
        print("  %-52s %6d lines  %2d refs" % (e["path"], e["lines"], e["reference_count"]))
    if problems:
        print("\n%d problem(s):" % len(problems))
        for p in problems:
            print("  - %s" % p)
        return 1 if check_only else 0
    print("\nevery archived file carries a citation block, and nothing that should be "
          "wired in is orphaned.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
