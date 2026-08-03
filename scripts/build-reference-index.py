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
    reference/bestiary/index.json      one directory
    reference/mythos/index.json        one directory
    reference/tables/index.json        one directory
    reference/index.json               the whole chain, both directions, all six directories

Nothing here is authored by hand. In `decks/` and `sourcebooks/` — third-party material — each
entry's provenance is *parsed out of the file's own* `## 引用出处` table, so the citation block
stays the single source of truth. In `rules/`, `bestiary/`, `mythos/`, `tables/` — the kit's own
writing — there is no citation to parse; the index exists purely to answer "does anything in the
repo reference this file, or is it an orphan?" `referenced_by` in every directory is found the
same way: scanning the repo for mentions of the file. Rewrite the index whenever you add, rename,
or retire a file in any of these six directories — see `core/14-archive-reference.md` for the
third-party ones.

Validation (always on, and the whole point of --check):
  - every .md in a third-party dir (`decks/`, `sourcebooks/`) carries a `## 引用出处` section
    with every required row filled
  - no file in ANY of the seven indexed directories is orphaned (nothing references it) without
    saying so — this applies to the kit's own content too, not just archived material
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


def build():
    problems, directories, all_entries = [], [], []
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
