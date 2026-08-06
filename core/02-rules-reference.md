# 02 — CoC 7e Rules Reference

Keep generated content mechanically correct for **Call of Cthulhu 7th Edition**. This spec
points to the cheat-sheets in `reference/rules/`; read the relevant one before you commit
numbers. It references mechanics — it does not reproduce the rulebook.

**The cheat-sheets are the last word.** As of P12 (2026-08-06, stage 2 完成) all seven files
in `reference/rules/` are written directly against the rulebook, section by section, with
line-anchor comments for local fact-checking — there should be nothing left that "isn't
settled" by one. `reference/sourcebooks/keeper-rulebook-7e-zh.md` is still in the repo as an
audit trail (if a local copy is present, it's the thing to diff a cheat-sheet against when
something looks wrong), not a place to fall back to for an answer. **If a cheat-sheet is
wrong, fix the cheat-sheet — don't read past it.**

**Cheat-sheets are only ever written by reading the source, never from memory of how CoC
"usually" works.** Every section keeps a `<!-- 规则书 <起>–<止> -->` line-anchor; a section
without one is unverified and should be treated as an error on review. The first draft of a
sheet is never the last step — a follow-up pass that checks **every individual number and
every stated relationship** against the source (not a handful of spot-checked values) is
mandatory before calling a sheet done. See `reference/rules/README.md` for the full
convention and the incident that established it.

**Default era: 1920s.** Every cheat-sheet below — `character-creation.md` most of all — is
written against the 1920s baseline unless a campaign declares otherwise.

**This section is the sole definition of the campaign `CLAUDE.md`'s Era field and how it
resolves.** `reference/rules/eras/README.md` and `campaigns/_template-campaign/CLAUDE.md`
restate this for convenience where a reader lands first; they don't define it independently
— if either ever disagrees with the steps below, this file wins. The field itself is always a
short slug-like label, never a file path. Resolve it in this order before generating anything:

1. **Unset, or `1920s`** → the baseline only, exactly today's behaviour. Nothing else to load.
2. **Matches a filename stem in `reference/rules/eras/README.md`'s index** (`cthulhu-invictus`,
   `dark-ages`, `mystic-iceland`, `gaslight`, `icarus`, `end-times`) → **path A**. Read
   `character-creation.md` (and any other baseline sheet the era's sections touch) in full,
   then layer that era file's five sections on top as overrides.
3. **Doesn't match the index, but `campaigns/<slug>/rules-era.md` exists** (`<slug>` being this
   campaign's own folder) → **path B**. Load the baseline exactly as in path A, then layer
   that file's five sections instead of an indexed era file. The Era field stays whatever short
   label the Keeper used at intake (e.g. `1970s`) — path B never writes a file path into the
   field, because the file's location is always that fixed pattern; nothing needs to encode it.
4. **Doesn't match the index, and no `rules-era.md` exists** → **path C**. Keep only the
   mechanical skeleton (checks, Sanity, combat) from the baseline; do not invent equipment,
   occupation, or money numbers to look authoritative. Tell the Keeper plainly the kit isn't
   backing these numbers. Any label the Keeper used lives in the Era field for the record —
   there's no separate "no era" value, and there's nothing else to write.

Never read an era delta file (an indexed one, or a path-B `rules-era.md`) without the baseline
loaded first — a delta file only lists what changes, and reading one alone silently drops
everything the era didn't bother to restate. `reference/rules/eras/README.md` holds the era
index itself, the five-section delta convention, and the reasoning behind the diff format —
read it whenever step 2 or 3 fires.

## Read this before you

- Write any NPC or monster **stat block** → confirm characteristics, HP, Build, Damage Bonus.
- Stat a **non-human monster** (creature, servitor, unique entity, or deity) → read
  `reference/rules/monster-scale.md` before picking a tier or a threat band.
- Set a **skill check difficulty** → pick Regular / Hard / Extreme deliberately.
- Assign a **Sanity cost** → keep it proportionate to the horror.
- Build a **human antagonist stronger than an ordinary person** (a cult leader, a gang boss)
  → read `reference/rules/character-creation.md` §11 before assigning skills or gear.
- Write any **spell, ritual, or magic book/tome** → read `reference/rules/magic.md` before
  setting an MP/SAN/POW cost or a study time.

## Cheat-sheets (source of truth)

- `reference/rules/skill-checks.md` — d100 under target; Regular/Hard/Extreme; pushing (and
  what can't be pushed); fumbles/criticals; group checks & Human Limits; Luck/Idea/Know
  checks; opposed rolls; bonus/penalty dice; combined checks; social-skill difficulty;
  Improvement checks; Credit Rating & expenses; Contacts; Training; Aging (mid-campaign
  milestones, distinct from creation-time age mods); optional Luck-spend rules. Covers all of
  chapter 5, not just the difficulty-band basics.
- `reference/rules/sanity.md` — SAN = POW; X/Y loss notation; typical loss table; bout of
  madness; temporary vs indefinite insanity; recovery.
- `reference/rules/combat.md` — DEX order; dodge vs fight back; Build & Damage Bonus table;
  HP = (CON+SIZ)/10; major wounds; manoeuvres.
- `reference/rules/chases.md` — round structure; Move rates; obstacles & mishaps; ending a
  chase. Read before writing any pursuit or escape scene.
- `reference/rules/character-creation.md` — characteristic rolls (with the full per-attribute
  "what does this number mean" reference table), creation-time age mods, derived stats,
  occupation formula families, the full verified base-skill-value table (including Fighting/
  Firearms/Science sub-specialisations), Credit Rating/lifestyle table, backstory, the six
  alternate character-creation methods (point-buy, quick-start, etc.), Pregen vs elite-NPC,
  and §11 human antagonist strength (baseline + increment — no separate power-budget table).
  Read it whenever the antagonist is a person, not a monster. **1920s baseline for
  `reference/rules/eras/`** — that directory's five-section deltas assume this file's
  structure and numbering; don't renumber a section here without checking what points at it.
- `reference/rules/magic.md` — MP mechanics and recovery, the three ways to learn a spell,
  the casting check (first-cast only) and its push-fail consequence tables, becoming a
  Believer, Deeper Magic, tome skim/full-study mechanics (CMI/CMF/MR) with a sampled
  study-time/SAN/MR calibration table, the spell cost-tier ladder (sampled from
  grand-grimoire, not this rulebook — flagged in the file), and the cost-conversion rule for
  designing a new spell.
- `reference/rules/monster-scale.md` — chapter 14's general monster framework (attribute
  conventions, the Build comparison table, monster combat/manoeuvre rules, undying Great Old
  Ones/Outer Gods, which Mythos creatures a human can realistically fight, monster spells)
  plus the five-tier non-human threat ladder (creature / servitor / unique entity / deity)
  sampled from `malleus-monstrorum-zh.md`, baseline SAN/HP/armour/attack-skill ranges per tier
  and threat band, and the trait load ceiling that caps `reference/tables/monster-traits.md`.
- `reference/rules/eras/README.md` — **read only when the campaign declares an Era other
  than 1920s.** Index of book-backed era packs, the delta convention each one follows, the
  load order (baseline first, then the era file as an override), and the path A/B/C fallback
  for eras the source material doesn't cover.

**Language note on `reference/rules/` itself (P12, 2026-08-06):** all seven files above are
written **中文正文 + 英文术语括注** (Chinese prose, English terms in parentheses) — this is a
deliberate reversal of the rest of the kit's "English scaffolding" convention, because these
files are rule-text transcriptions/distillations, not kit-original scaffolding. Don't
"correct" a cheat-sheet back to English; don't write a new one in English either.

## Fast facts (verify against the sheets)

- **Check:** roll 1d100 ≤ value. **Hard** = ½ value, **Extreme** = ⅕ value, **Critical** = 01.
- **Characteristics** run ~15–90 (3d6×5, or (2d6+6)×5 for SIZ/INT/EDU). Average human ≈ 50.
- **HP** = (CON + SIZ) ÷ 10. **MP** = POW ÷ 5. **SAN** starts = POW; max = 99 − Cthulhu Mythos.
- **Dodge** base = ½ DEX. **Move** ≈ 8 for a typical adult (adjust for STR/DEX vs SIZ, age).
- **Damage Bonus / Build** come from STR + SIZ — see the combat sheet's table, don't guess.
- **Sanity loss** is written X/Y (success/failure). Minor Mythos sights ~0/1D6; gods ~1D10/1D100.

## Language note

Stat blocks stay in **English notation** regardless of the campaign's output language —
`STR 60`, `HP 12`, `1D6/2D10`, `Fighting (Brawl) 45%`. Only the surrounding prose, names, and
labels are translated. When writing 简体中文, use `reference/glossary-zh.md` for skill and
mechanic names; never translate a skill name ad hoc.

## Quality bar for anything with stats

- Numbers are internally consistent: HP, Build, Damage Bonus, Dodge all derive correctly.
- Difficulty is set **before** the roll and only when failure is interesting.
- Never gate the sole path forward behind one roll (see `core/04-design-scenario.md`'s
  three-clue rule).
- When unsure of an exact value, state the assumption in a keeper note rather than inventing
  a rule.
