# Era Packs — index, delta convention, loading order, fallback paths

This is the hub file for running Call of Cthulhu 7e outside the kit's 1920s baseline
(`reference/rules/character-creation.md`). Read this before reading any file in this
directory — an era file on its own is a **diff**, not a standalone rules document, and
reading one without the baseline behind it will misread it.

## Why a diff and not a full rewrite

The baseline (`character-creation.md`, `combat.md`, `chases.md`, etc.) already covers
everything that doesn't change between eras — the check math, Sanity, HP, the shape of a
character sheet. What changes across eras is a small, specific set of things: which
occupations exist, what skills are period-appropriate, what technology and equipment are
available, what money looks like. Writing each era as a full character-creation document
would repeat the unchanging 80% every time, and the copies would drift out of sync with the
baseline. Writing each era as a **delta against the baseline** keeps every file small and
keeps the baseline the single source of truth for everything that isn't era-specific.

The cost: a delta file is unreadable alone. `core/02-rules-reference.md`'s loading order
below exists to make sure nothing ever reads one alone.

## Index — eras covered by the source material

Source: *Cthulhu Through the Ages* (官方设定合集,七宫涟个人汉化版,52 页,收录于
`update_plan/2026-08-04-era-rule-packs.md` 的勘察结果一节). Every era the book covers is
built here — **no filtering**; the source material is only 52 pages, so building all of them
costs less than making a Keeper wait on a future ad-hoc request. See that plan file for full
survey detail.

| Era file | 中文名 | 年代 | 书本背书 |
|---|---|---|---|
| `cthulhu-invictus.md` | 克苏鲁不败 | 罗马帝国(约 1–2 世纪) | ✅ 官方 |
| `dark-ages.md` | 克苏鲁黑暗时代 | 欧洲 10–11 世纪 | ✅ 官方 |
| `mystic-iceland.md` | 神秘冰岛 | 冰岛萨迦时代(约 930 年前后) | ✅ 官方 |
| `gaslight.md` | 克苏鲁煤气灯 | 维多利亚伦敦,约 1890 年代 | ✅ 官方 |
| `icarus.md` | 克苏鲁伊卡洛斯 | 近未来星际探索 | ✅ 官方 |
| `end-times.md` | 克苏鲁末日之收割 | 旧日支配者苏醒后的后启示录未来(时间点 KP 自定) | ✅ 官方 |
| *(未声明 = 1920s)* | 经典 1920s | 1920s | ✅ `character-creation.md` 本身 |

**Two things in the source are deliberately not built as era files here:**

- **剑见箭 Swords and Arrows** is not an era — it's a shared melee-combat supplement
  (shields, ancient/medieval weapon tables) the book uses for the three pre-gunpowder
  settings above. Its content is folded into `cthulhu-invictus.md`,
  `dark-ages.md`, and `mystic-iceland.md`'s own **装备与武器** / **可选机制** sections
  instead of living in a fourth file nobody would declare an era.
- **幻梦境 Dreamlands** is not an era either — it's an alternate plane reachable from
  *any* era (a Roman-era investigator and a 1920s one can both fall asleep into it). It
  doesn't fit the delta-against-a-timeline model this directory uses. If a campaign needs
  it, it's a scene/location built with `core/03-build-world.md` and
  `core/09-description.md`, not an era declaration — the campaign's actual era (1920s,
  Gaslight, whatever) still governs character creation.

## The five-section delta convention

Every era file in this directory uses exactly these five sections, in this order. **Only
write what changes.** If an era doesn't touch a section (e.g. Mystic Iceland has no fixed
occupation table), say so in one line rather than omitting the heading — an era file with a
missing section reads as "not yet written," not "nothing changed here."

1. **技能表增减** — new skills the era adds, existing skills it drops or renames, and any
   skill whose *base value* or *use* changes (e.g. Gaslight's Electrical Repair starting at
   01% instead of the baseline value, because household electricity barely exists yet).
2. **装备与武器** — period weapons, armour, and everyday equipment, with damage/price where
   the source gives it. This is where the three ancient eras carry their 剑见箭 shield and
   weapon tables.
3. **技术与常识水平** — what an investigator of this era would and wouldn't know or expect:
   available technology, common knowledge, travel speed, communication lag. This is the
   section a Keeper reads to avoid anachronism in prose, not just in stat blocks.
4. **职业表** — period occupation templates (skills, skill-point formula, status/credit
   range). Note explicitly if the era uses free skill-point allocation instead (Mystic
   Iceland does).
5. **可选机制** — era-specific optional rules that don't fit the other four sections (Dark
   Ages' clan/feud system, Iceland's Luck-never-recovers rule, End Times' Strong Sanity
   trait).

Every entry cites where it came from — a chapter name and page number in the source, the
same **来源** convention `character-creation.md` already uses. Nothing here is invented; if
the source doesn't give a number, the era file says so rather than filling one in.

## Loading order (what `core/02-rules-reference.md` does)

1. Read the campaign's declared **Era** field (see below).
2. **Read `character-creation.md` (and any other baseline cheat-sheet touched by the era's
   sections) first, in full** — this is the 80% that doesn't change.
3. **Then read the matching era file and apply its five sections as overrides** — a skill
   listed in 技能表增减 replaces the baseline entry; a section that says "unchanged" leaves
   the baseline as-is.
4. Never read an era file without step 2. A delta file assumes the reader already has the
   baseline loaded; skipping straight to it silently drops everything the era *didn't*
   bother to restate.
5. No **Era** declared → step 2 only, exactly today's behaviour. This is what makes the
   whole scheme backward-compatible: a campaign that never mentions era is unaffected.

## How a campaign declares its era

`campaigns/_template-campaign/CLAUDE.md` → **Setting → Era** takes a fixed slug, not free
text — `1920s` (baseline, the default), or one of the file-name stems in the index table
above (`cthulhu-invictus`, `dark-ages`, `mystic-iceland`, `gaslight`, `icarus`,
`end-times`), or a **path B** slug the Keeper approved during intake (see below). Free-text
descriptions ("1890s Gaslight London") still belong in the surrounding prose — the slug is
what `core/02` matches against this index, so it has to be exact.

## The three paths — what `core/01-intake.md` does when a Keeper names an era

| Path | Trigger | What happens | What the Keeper is told |
|---|---|---|---|
| **A — book-backed** | Era slug matches a file in the index above | Declare it in the campaign `CLAUDE.md`; `core/02` layers the delta per the loading order | Play proceeds; numbers carry the book's backing |
| **B — derivable** | Not in the index, but within the same technological lineage as a covered era (a Keeper says "1970s" or "1990s" — close enough to 1920s/modern that the delta can be reasoned out) | Construct a delta **on the spot**, following the same five-section convention, and save it to `campaigns/<slug>/rules-era.md` (not into this directory — it's campaign-specific, not reusable, and never book-backed) | **Explicitly told this is derived, not sourced** — show the Keeper the constructed delta before play starts, and say plainly that Chaosium never published these numbers |
| **C — out of scope** | Future/alien/fully invented setting with no real technological lineage to reason from | Keep only the mechanical skeleton (checks, Sanity, combat) — no equipment or occupation numbers invented to look authoritative | **Explicitly told the kit does not back these numbers at all** — the Keeper is on their own for anything era-specific |

Path B is the actual point of "era is open," not a fallback bolted onto path A — building
only the six book-backed files above would just be a bigger closed set. When constructing a
path B delta, follow the five-section convention above and reason from the nearest covered
era (a Keeper's "1970s" campaign reasons forward from `character-creation.md`'s 1920s
baseline the same way Gaslight's 1890s reasons backward from it — technology, social
structure, and money all move by degree, not by starting over).

## Where this should get checked

Technology, equipment, or common knowledge leaking in from the wrong period (a path-B
delta's assumptions going unflagged, a 1920s-trained model defaulting to cars in a Dark Ages
scene) is exactly the failure mode this directory exists to prevent — but nothing enforces it
yet. Wiring an era/anachronism check into `core/11-review.md` is `update_plan/
2026-08-04-era-rule-packs.md`'s **阶段 3**, not yet done as of this file's creation. Until
then, treat cross-era contamination as a manual thing to watch for.
