# reference/ — shared canon

Everything here is **reusable across every campaign**. Campaign-specific material belongs
in `campaigns/<slug>/`, not here.

- **`rules/`** — CoC 7th Edition mechanics cheat-sheets. The source of truth for difficulty
  bands, Sanity, and combat used by every generator. See `core/02-rules-reference.md`, which
  points back here.
- **`bestiary/`** — reusable monsters and Mythos entities you can drop into any game.
  Produced by `core/07-create-monster.md`. One creature per file. Written in **English**,
  since they're shared across campaigns that may output in different languages.
- **`mythos/`** — Great Old Ones, tomes, spells, cults, and factions. Slow-growing lore
  you reference from multiple campaigns.
- **`tables/`** — roll tables. Includes the four **seed tables** (`hooks`, `locations`,
  `mythos-angles`, `npc-quirks`) that `core/01-intake.md` rolls against when the Keeper gives
  little or no input — the anti-generic layer.
- **`glossary-zh.md`** — the EN ↔ 简体中文 term lock. One translation per game term, for the
  whole kit. Every generator writing Chinese follows it; new terms get added *here* first,
  never invented inside a campaign. Built on top of the community
  [大译名表](https://www.goddessfantasy.net/bbs/index.php?topic=95256.0) term set.
- **`og_Norval/`** — H. P. Lovecraft's original stories (82 works), kept for craft research
  only, same non-reproduction rule as `external/` below. **`lovecraft-craft-notes-zh.md`** is
  the distilled output — tone, scene/action description, and monster-design techniques pulled
  from a full read of the corpus, in 简体中文. `core/09-description.md` and
  `core/07-create-monster.md` both read it.
- **`external/`** — third-party repos kept as git submodules, not kit content. `coc-zh` is a
  collection of CoC novels/scenario source material for inspiration and research only — it is
  **not** part of the kit's own canon, and generators must not copy or reproduce its text
  (see this repo's `CLAUDE.md`: the kit doesn't reproduce copyrighted material). Treat it the
  same way you'd treat a physical bookshelf: read it, then write original content informed by
  it.

Keep entries generic here (no campaign plot). When a creature or cult becomes tangled in one
campaign's plot, copy it into that campaign and add the secrets there.
