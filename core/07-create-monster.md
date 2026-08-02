# 07 — Create Monster

Stat a threat that is frightening *and* fair — the players can learn what it is and how to
live through it. In CoC the monster is usually an obstacle to survive, not a boss to beat.

## First

- **Read `core/02-rules-reference.md`** — especially `reference/rules/combat.md` (Build,
  Damage Bonus, HP) and `reference/rules/sanity.md` (X/Y loss). Numbers must be 7e-correct.
- Decide **type** (human / beast / undead / mythos servitor / independent race / great old
  one) and **threat** (trivial / moderate / deadly / mythic). Threat sets stat scale and SAN.
- Use `templates/monster.md`.

## Design the horror

- **The reveal first.** Write 2–4 sensory sentences of *wrongness* (motion, sound, smell) —
  the Keeper reads this, THEN calls the Sanity roll. Lead with the image, not the stat line.
- **Sanity cost proportionate** to what it is: minor servitor ~0/1D6, major entity ~1D6/2D10,
  a god ~1D10/1D100. Don't inflate for gore alone.
- **Attacks with texture** — not just damage. A grab that drags, a touch that drains POW, a
  gaze that ages. Give per-round attack count, skill %, damage (with db where physical).
- **Armour / immunities** — many Mythos things shrug off bullets or knives. Say what *does*
  work (fire, cold iron, a ward, a name).
- **The fair out.** Every creature needs a discoverable way to be **fled, warded, tricked,
  burned, or endured**. Combat is the failure branch; give a better one.
- **Weakness = a clue.** The out should be findable through investigation (a tome, a survivor,
  an experiment) — hand that thread to `core/08-create-puzzle.md` / `core/04-design-scenario.md`.

## Stat guidance (7e)

- Give **average characteristics** (note "roll/scale per individual" if many appear).
- Derive **HP = (CON+SIZ)/10**, **Build & Damage Bonus** from STR+SIZ, **Move** to fit the body.
- Big entities have high SIZ → high Build → hard to grapple and heavy Damage Bonus; reflect it.
- Spellcasters: list spells and their MP/SAN costs; cross-link `reference/mythos/`.

## Output

- **Reusable, campaign-neutral** → `reference/bestiary/<name>.md` (no plot). Write these in
  **English** — they are shared across campaigns with different output languages.
- **Plot-bound** (its origin *is* the mystery) → `campaigns/<slug>/world/` or `scenes/`, in
  that campaign's output language, with secrets in a `> **KEEPER ONLY**` block.
- One creature per file, `kebab-case.md`.

## Quality bar

- Stats internally consistent; SAN cost proportionate; attacks and armour concrete.
- There is at least one **non-combat way to survive** the encounter, and it's discoverable.
- Keeper-only lore is quarantined; the reveal text is ready to read aloud.
