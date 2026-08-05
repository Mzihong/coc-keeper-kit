#!/usr/bin/env python3
"""Roll against reference/tables/ — real randomness, never a model-reported number.

Usage:
    python scripts/roll.py <table> [<table> ...] [--times N] [--campaign <slug>] [--fresh]
    python scripts/roll.py --check-all

Examples:
    python scripts/roll.py locations mythos-angles --campaign dagon-bay
    python scripts/roll.py cult-goals --campaign dagon-bay          # two-dimensional table
    python scripts/roll.py complications --times 2 --campaign dagon-bay
    python scripts/roll.py npc-quirks --fresh --campaign dagon-bay  # also dodge other campaigns

Every table file declares its own die — either a `掷 **1dN**` line or, for a two-dimensional
table like cult-goals.md, one `## <label>(1DN)` heading per dimension — and roll.py parses
that declaration rather than trusting an argument, so a mistyped die can never silently roll
the wrong range. Before rolling, every requested table is self-checked: its actual row count
must equal its declared die, or the whole invocation fails without rolling anything.

`--campaign <slug>` turns on same-campaign no-replacement (an index already logged for that
table in campaigns/<slug>/rolls.log is excluded from the pool) and appends every roll made
this invocation to that log. If the campaign folder doesn't exist yet, it is created — this
lets intake roll seed tables before the rest of the campaign skeleton is written.

`--fresh` additionally excludes indices already used by *other* campaigns' rolls.log for the
same table — the cross-campaign "don't feel the same as last time" check. Either pool can run
dry; when it does, roll.py falls back to the full range and says so in the output, it never
refuses to roll.

Some files in reference/tables/ are not dice tables at all (cultist-archetypes.md,
monster-traits.md, monster-index.md) — asking to roll one of those is a hard error naming why,
not a silent skip.

`--seed` is for tests only: it swaps random.SystemRandom() for a seeded random.Random() so a
test run is reproducible. Never write a --seed invocation into a spec, a campaign file, or
anything a Keeper is meant to run for real.

stdlib only, no dependencies.
"""
import argparse
import datetime
import random
import re
import sys
from pathlib import Path

if sys.stdout.encoding and sys.stdout.encoding.lower() != "utf-8":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.stderr.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
TABLES_DIR = ROOT / "reference" / "tables"
CAMPAIGNS_DIR = ROOT / "campaigns"

NOT_DICE_TABLES = {
    "cultist-archetypes": "12 组按角色分组的现成邪教徒数值,外加法力加持菜单——不是骰表。",
    "monster-traits": "数值词条菜单,按怪物等级手选叠加,不掷骰。",
    "monster-index": "build-reference-index.py 生成的检索表,不要手改,也不掷骰。",
}

HEADER_DIE_RE = re.compile(r"^\|\s*[dD](\d+)\s*\|")
SEPARATOR_RE = re.compile(r"^\|[\s:|-]+\|\s*$")
HEADING_DIM_RE = re.compile(r"^#{1,6}\s*(.+?)[\(（]\s*1?[Dd](\d+)\s*[\)）]")

LOG_HEADER = "# table\tdimension\tdie\tindex\tentry\tspec\ttimestamp\n"


class TableError(Exception):
    pass


class Dimension:
    def __init__(self, label, die, entries):
        self.label = label  # None for a single-dimension table
        self.die = die
        self.entries = entries  # {index: entry text}


def parse_table_block(lines, start):
    """Parse the markdown table whose header row is lines[start]. Returns (die, entries) or None."""
    m = HEADER_DIE_RE.match(lines[start])
    if not m:
        return None
    die = int(m.group(1))
    if start + 1 >= len(lines) or not SEPARATOR_RE.match(lines[start + 1]):
        return None
    entries = {}
    i = start + 2
    while i < len(lines) and lines[i].strip().startswith("|"):
        cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
        if not cells or not cells[0].isdigit():
            break
        entries[int(cells[0])] = " — ".join(c for c in cells[1:] if c)
        i += 1
    return die, entries


def load_table(name):
    if name in NOT_DICE_TABLES:
        raise TableError(f"{name}.md 不是骰表:{NOT_DICE_TABLES[name]}")
    path = TABLES_DIR / f"{name}.md"
    if not path.exists():
        raise TableError(f"找不到 reference/tables/{name}.md")
    lines = path.read_text(encoding="utf-8").splitlines()

    headings = [
        (i, m.group(1).strip(" —-"), int(m.group(2)))
        for i, line in enumerate(lines)
        for m in [HEADING_DIM_RE.match(line)]
        if m
    ]

    if len(headings) >= 2:
        dimensions = []
        for hi, (line_no, label, declared_die) in enumerate(headings):
            end = headings[hi + 1][0] if hi + 1 < len(headings) else len(lines)
            block = None
            for j in range(line_no, end):
                if HEADER_DIE_RE.match(lines[j]):
                    block = parse_table_block(lines, j)
                    break
            if block is None:
                raise TableError(f"{name}.md 分节「{label}」声明了 (1D{declared_die}),但没找到对应的骰表")
            die, entries = block
            if die != declared_die:
                raise TableError(
                    f"{name}.md 分节「{label}」标题写 1D{declared_die},表头却是 d{die} —— 两处不一致"
                )
            if len(entries) != die:
                raise TableError(
                    f"{name}.md 分节「{label}」应有 {die} 行,实际 {len(entries)} 行 —— 自检未过"
                )
            dimensions.append(Dimension(label, die, entries))
        return dimensions

    for i, line in enumerate(lines):
        if HEADER_DIE_RE.match(line):
            block = parse_table_block(lines, i)
            if block is None:
                continue
            die, entries = block
            if len(entries) != die:
                raise TableError(f"{name}.md 应有 {die} 行,实际 {len(entries)} 行 —— 自检未过")
            return [Dimension(None, die, entries)]

    raise TableError(
        f"{name}.md 没能识别出骰面(既没有 (1DN) 分节标题,也没有 dN 表头)——如果这确实不是"
        f"骰表,把它加进 roll.py 的 NOT_DICE_TABLES"
    )


def campaign_log_path(slug):
    return CAMPAIGNS_DIR / slug / "rolls.log"


def read_used_indices(log_path, table_name):
    used = {}
    if not log_path.exists():
        return used
    for line in log_path.read_text(encoding="utf-8").splitlines():
        if not line or line.startswith("#"):
            continue
        parts = line.split("\t")
        if len(parts) < 4 or parts[0] != table_name:
            continue
        used.setdefault(parts[1], set()).add(int(parts[3]))
    return used


def read_fresh_excluded(table_name, exclude_slug):
    excluded = {}
    if not CAMPAIGNS_DIR.exists():
        return excluded
    for camp_dir in CAMPAIGNS_DIR.iterdir():
        if not camp_dir.is_dir() or camp_dir.name.startswith("_") or camp_dir.name == exclude_slug:
            continue
        for dim, idxs in read_used_indices(camp_dir / "rolls.log", table_name).items():
            excluded.setdefault(dim, set()).update(idxs)
    return excluded


def append_log(log_path, rows, spec):
    is_new = not log_path.exists()
    log_path.parent.mkdir(parents=True, exist_ok=True)
    ts = datetime.datetime.now().isoformat(timespec="seconds")
    with log_path.open("a", encoding="utf-8") as f:
        if is_new:
            f.write(LOG_HEADER)
        for table, dim, die, idx, entry in rows:
            f.write(f"{table}\t{dim or '-'}\t{die}\t{idx}\t{entry}\t{spec or '-'}\t{ts}\n")


def pick(rng, die, excluded):
    pool = [i for i in range(1, die + 1) if i not in excluded]
    if pool:
        return rng.choice(pool), False
    return rng.randint(1, die), True


def roll_table(rng, name, dimensions, times, campaign_slug, fresh, spec):
    used_in_campaign = read_used_indices(campaign_log_path(campaign_slug), name) if campaign_slug else {}
    fresh_excluded = read_fresh_excluded(name, campaign_slug) if fresh else {}

    output, log_rows = [], []
    for _ in range(times):
        for dim in dimensions:
            key = dim.label or "-"
            excluded = set(used_in_campaign.get(key, ())) | set(fresh_excluded.get(key, ()))
            idx, exhausted = pick(rng, dim.die, excluded)
            entry = dim.entries[idx]
            used_in_campaign.setdefault(key, set()).add(idx)
            label = f"{name}.md" + (f" {dim.label}" if dim.label else "")
            note = "  （本表当前查重范围已掷空，允许重复）" if exhausted else ""
            output.append((label, dim.die, idx, entry, note))
            log_rows.append((name, dim.label, dim.die, idx, entry))
    return output, log_rows


def check_all():
    ok = skipped = 0
    problems = []
    for path in sorted(TABLES_DIR.glob("*.md")):
        name = path.stem
        if name == "README":
            continue
        if name in NOT_DICE_TABLES:
            skipped += 1
            continue
        try:
            load_table(name)
            ok += 1
        except TableError as e:
            problems.append(str(e))
    print(f"{ok} 张表通过自检,{skipped} 张非骰表跳过。")
    if problems:
        print(f"{len(problems)} 处不一致:", file=sys.stderr)
        for p in problems:
            print(f"  - {p}", file=sys.stderr)
        return 1
    return 0


def build_arg_parser():
    p = argparse.ArgumentParser(
        description="Roll against reference/tables/ with real randomness — never a model-reported number."
    )
    p.add_argument("tables", nargs="*", help="table names, with or without .md (e.g. locations mythos-angles)")
    p.add_argument("--times", type=int, default=1, help="roll each table this many times (default 1)")
    p.add_argument("--campaign", metavar="SLUG", help="enables within-campaign no-replacement + rolls.log")
    p.add_argument("--fresh", action="store_true", help="also dodge entries already used by OTHER campaigns")
    p.add_argument("--spec", metavar="NAME", help="which spec is rolling, recorded in rolls.log (e.g. core/01-intake)")
    p.add_argument("--seed", type=int, help="TESTING ONLY — never write this into a spec or campaign file")
    p.add_argument("--check-all", action="store_true", help="validate every table's die vs its row count and exit")
    return p


def main():
    args = build_arg_parser().parse_args()

    if args.check_all:
        sys.exit(check_all())

    if not args.tables:
        print(
            "用法: python scripts/roll.py <table> [<table> ...] [--times N] [--campaign <slug>] [--fresh]",
            file=sys.stderr,
        )
        sys.exit(1)

    names = [t[:-3] if t.endswith(".md") else t for t in args.tables]

    loaded = {}
    try:
        for name in names:
            loaded[name] = load_table(name)
    except TableError as e:
        print(f"错误:{e}", file=sys.stderr)
        sys.exit(1)

    if args.campaign:
        camp_dir = CAMPAIGNS_DIR / args.campaign
        if not camp_dir.exists():
            camp_dir.mkdir(parents=True)
            print(f"（campaigns/{args.campaign}/ 尚不存在，已新建这一个文件夹用于记账；"
                  f"战役的其余文件仍由 intake 或 Keeper 生成。）")

    if args.seed is not None:
        print("⚠ --seed 仅用于测试，禁止把它写进任何 spec、产物或 campaign 文件。", file=sys.stderr)
        rng = random.Random(args.seed)
    else:
        rng = random.SystemRandom()

    all_output, all_log_rows = [], []
    for name in names:
        output, log_rows = roll_table(rng, name, loaded[name], args.times, args.campaign, args.fresh, args.spec)
        all_output.extend(output)
        all_log_rows.extend(log_rows)

    width = max((len(label) for label, *_ in all_output), default=0)
    for label, die, idx, entry, note in all_output:
        print(f"{label.ljust(width)}  1d{die} → {idx:>3}   {entry}{note}")

    if args.campaign:
        append_log(campaign_log_path(args.campaign), all_log_rows, args.spec)
        print(f"\n已记入 campaigns/{args.campaign}/rolls.log")


if __name__ == "__main__":
    main()
