# 7e Character Creation — cheat-sheet

> Quick-fire pregen/investigator reference. Not a rules reproduction — see the *Keeper
> Rulebook* for the full character-creation chapter and occupation list.

## Characteristics
- Roll **3D6 × 5** for STR, CON, DEX, APP, POW.
- Roll **(2D6+6) × 5** for SIZ, INT, EDU.
- Point-buy is a valid alternative when a table wants control over randomness.
- Average human ≈ 50; the normal human range is roughly 15–90.

## Derived stats
- **HP** = (CON+SIZ) ÷ 10 · **MP** = POW ÷ 5 · **SAN** starts = POW (max 99 − Cthulhu Mythos%)
- **Move** ≈ 7–9 for a typical adult — see `reference/rules/combat.md` and
  `reference/rules/chases.md` for situational Move.
- **Build / Damage Bonus** from STR+SIZ — table in `reference/rules/combat.md`.
- **Dodge** = ½ DEX.
- **Luck** = roll 3D6×5 (or take a flat 50); spendable per `reference/rules/skill-checks.md`.

## Skill points
- **Occupation points:** typically **EDU × 4**, or an occupation-specific split — e.g.
  EDU×2 + a relevant characteristic×2 (a detective might use EDU×2 + DEX×2, a con artist
  EDU×2 + APP×2). Pick whichever split fits the concept; assign only to that occupation's
  skill list.
- **Personal interest points:** **INT × 2**, assignable to any skill.
- No skill exceeds **90%** at creation. Cthulhu Mythos starts at **0** (or an occupation's
  stated starting value, if any) — it is never bought up at creation.
- **Credit Rating** has an occupation-defined min–max band; pick within it to match the
  concept, not automatically the midpoint.

## Backstory hooks
7e's standard prompts — fill each one, don't skip it:
- **Personal description** — one visual line.
- **Ideology/beliefs, significant people, meaningful locations, treasured possessions,
  traits** — each is a lever the Keeper can pull mid-game.
- **Injuries/scars, phobias/manias** — optional, but a gift to a Keeper reaching for personal
  horror.

## Pregens vs. elite NPCs
- A **pregen** built for a specific scenario should have Credit Rating, skills, and backstory
  hooks tuned to the plot — every surviving hook should be something the scenario can actually
  use, not decoration. See `core/13-create-investigator.md`.
- An **elite NPC** (a named cultist, a rival investigator) can reuse the same mechanical
  skeleton (`templates/investigator.schema.json`) and skip the player-facing hooks section.

## Quality bar
- Skill points spent match the EDU×4 / INT×2 (or occupation-split) formula — recompute, don't
  eyeball.
- Every derived stat (HP, MP, SAN, Build, Damage Bonus, Dodge, Move, Luck) traces back
  correctly to the rolled characteristics.
- Credit Rating sits inside the occupation's declared band.
