# 02 — CoC 7e Rules Reference

Keep generated content mechanically correct for **Call of Cthulhu 7th Edition**. This spec
points to the cheat-sheets in `reference/rules/`; read the relevant one before you commit
numbers. It references mechanics — it does not reproduce the rulebook.

When a cheat-sheet doesn't settle it, `reference/sourcebooks/keeper-rulebook-7e-zh.md` is the
7e rulebook itself, transcribed (local file, absent from `dist/bundle.md`). It is the last
word on any number here — and it is a *transcription*, so cross-check anything surprising
before you commit it. **If it contradicts a cheat-sheet, fix the cheat-sheet.**

## Read this before you

- Write any NPC or monster **stat block** → confirm characteristics, HP, Build, Damage Bonus.
- Set a **skill check difficulty** → pick Regular / Hard / Extreme deliberately.
- Assign a **Sanity cost** → keep it proportionate to the horror.
- Build a **human antagonist stronger than an ordinary person** (a cult leader, a gang boss)
  → read `reference/rules/character-creation.md` §11 before assigning skills or gear.
- Write any **spell, ritual, or magic book/tome** → read `reference/rules/magic.md` before
  setting an MP/SAN/POW cost or a study time.

## Cheat-sheets (source of truth)

- `reference/rules/skill-checks.md` — d100 under target; Regular/Hard/Extreme; fumbles;
  bonus/penalty dice; pushing; Luck; opposed rolls; base skill values.
- `reference/rules/sanity.md` — SAN = POW; X/Y loss notation; typical loss table; bout of
  madness; temporary vs indefinite insanity; recovery.
- `reference/rules/combat.md` — DEX order; dodge vs fight back; Build & Damage Bonus table;
  HP = (CON+SIZ)/10; major wounds; manoeuvres.
- `reference/rules/chases.md` — round structure; Move rates; obstacles & mishaps; ending a
  chase. Read before writing any pursuit or escape scene.
- `reference/rules/character-creation.md` — attribute rolls, the standard-pool skill-point
  formula, base skill values; §11 is human antagonist strength (baseline + increment — no
  separate power-budget table). Read it whenever the antagonist is a person, not a monster.
- `reference/rules/magic.md` — MP/SAN/POW cost notation, casting time, opposed POW rolls,
  spell cost-tier ladder, tome study time/SAN/Cthulhu Mythos conventions, and the
  cost-conversion rule for designing a new spell.

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
