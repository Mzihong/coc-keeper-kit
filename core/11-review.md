# 11 — Review

Run this on generated material **before it reaches the table**. It is a verification pass,
not a rewrite: read what exists, check it against the list, report what fails, then fix what
the Keeper asks you to fix.

This spec exists because the quality bars in the other specs are written for the model that
*generates*. This one is written for a model that *audits* — including auditing another
model's output. Assume the material is wrong until each line checks out.

## How to run it

1. Ask what to review, or infer it (a scenario, a session, the whole campaign folder).
2. Read the campaign `CLAUDE.md`, `canon-log.md`, and `world/event-clock.md` for the
   standards this material must meet.
3. Walk the checklist below. For each item: **pass**, **fail**, or **n/a**.
4. Report failures **most-severe first**, each with the file, the specific problem, and a
   concrete fix. Don't report passes individually — one line confirming the rest passed.
5. Fix only what the Keeper approves. A review that silently rewrites is not a review.

## The checklist

### Blocking — the session breaks without these

- [ ] **Three clues per must-know fact.** Every fact the players *must* realise has three
      independent sources. Count them; don't trust the clue map's own claim.
- [ ] **No single-roll gates.** No failed check anywhere can end the investigation. Trace each
      required clue back: if the only route is one roll, it fails.
- [ ] **Every lock has ≥2 keys.** Puzzles, locked doors, and uncooperative NPCs all have an
      alternate route plus a mercy path.
- [ ] **Every monster has a fair out**, and it is discoverable in play — not only in the
      Keeper's notes.
- [ ] **At least one non-combat resolution** to the central threat exists.
- [ ] **No unwinnable state.** Is there any sequence of reasonable player choices that leaves
      the scenario with no path forward? Name it if so.

### Continuity

- [ ] Nothing contradicts `canon-log.md` — dead NPCs stay dead, revealed facts stay revealed.
- [ ] Nothing contradicts `world/event-clock.md`'s current stage or fired triggers.
- [ ] Names, dates, and place-names match their earlier spellings exactly.
- [ ] Cross-links resolve — every relative link points at a file that exists.
- [ ] **Rolled content traces back to `campaigns/<slug>/rolls.log`.** If the material rolled
      anything (a seed table, an NPC quirk, a complication), the campaign has a `rolls.log`
      and its entries match what the material claims was rolled — a fail here usually means a
      result was reported from memory instead of `python scripts/roll.py`.

### Craft

- [ ] Every NPC has a **want**, a **secret**, and a **prepared lie**.
- [ ] Every scene is keyed by purpose (clue / choice / shock / breather).
- [ ] Scenes form a web — at least one scene is reachable in more than one order.
- [ ] Boxed text: 3–6 sentences, ≥2 senses, one wrong detail, ends on a hook.
- [ ] SAN hits are spaced, not stacked; the biggest lands at the reveal.
- [ ] Scenario-level material: each ending carries a suggested SAN reward (or explicitly none
      for muddled/grim), and a Scaling sidebar exists if the table's size differs from baseline.

### Mechanics

- [ ] Stat blocks internally consistent: HP = (CON+SIZ)/10, Dodge = ½ DEX, Build and Damage
      Bonus derived from STR+SIZ. **Recompute them; don't eyeball.**
- [ ] **Human antagonists: skill height is lethality-derived, not background-derived.**
      Background picks *which* skills a villain has; it never justifies *how high* one goes.
      If a skill value would land a single successful roll as an unrecoverable outcome on an
      investigator, that's the ceiling regardless of the character's backstory
      (`reference/rules/character-creation.md` §11). Cross-check against the campaign
      `CLAUDE.md`'s declared **lethality** field.
- [ ] Difficulties (Regular/Hard/Extreme) are set deliberately and only where failure is
      interesting.
- [ ] Sanity costs are proportionate to the horror, not to the gore.
- [ ] Any `investigators/*.json` validates against `templates/investigator.schema.json`; its
      derived stats are internally consistent and its `.md` view agrees with the JSON.
- [ ] **Non-human monsters: every numeric trait has a discoverable counter-play.** For each
      trait listed under "Special abilities (traits)", confirm the entry (or a linked file)
      states how a player could find or use that trait's 破解口 — a counter-play that exists
      only in `reference/tables/monster-traits.md` and never reaches the table doesn't count.
      N traits demand N *findable* answers; one missing is a broken fair-out, not a nitpick.
- [ ] **Non-human monsters: trait load is at or under the tier ceiling.** Sum the loads on
      "Trait load total" against `reference/rules/monster-scale.md`'s ceiling for that tier
      (L2/L3 = 2, L4 = 3, L5 = 4). Over budget means the entry reads as the wrong tier wearing
      a costume, not a legitimately scarier version of its actual tier.

### Safety & spoilers

- [ ] Declared **lines** appear nowhere. Declared **veils** are off-screen.
- [ ] Heavy material is flagged for the Keeper, not silently included.
- [ ] Every player-facing file (`handouts/`, boxed text) is spoiler-clean — read it as a
      player would and confirm it gives away nothing.
- [ ] Keeper-only content is inside `> **KEEPER ONLY**` blocks, never in player files.

### Language

- [ ] Everything is in the campaign's declared **output language** — no drifted-back-to-English
      paragraphs.
- [ ] 简体中文 material uses `reference/glossary-zh.md` terms consistently; no 繁体 characters;
      no two translations of the same game term.
- [ ] **Proper nouns follow the setting, not the output language.** A 简体中文 campaign set
      abroad (the default is American — `core/01-intake.md`) transliterates people, places,
      and institutions per `reference/glossary-zh.md` → 外文专名的译写: one spelling per name
      campaign-wide, original in parentheses on first appearance, Japanese names in 汉字
      rather than re-transliterated through English.
- [ ] Filenames are English `kebab-case.md`.
- [ ] Any cipher or wordplay actually works in the script it's written in.

## Report format

```
BLOCKING
1. campaigns/dagon-bay/the-red-tide.md — "the ledger" is the only route to Fact 2.
   Fix: add a second source (the harbourmaster's slip) and a third (the dredging photos).

CRAFT
2. npcs/mary-tang.md — has a secret but no prepared lie; the Keeper will have to invent
   her answer mid-scene. Fix: add what she says when asked directly about the boat.

Everything else on the checklist passes.
```

## Quality bar

- Every blocking item was actually traced, not assumed. Say how you verified the three-clue
  count and the stat arithmetic.
- Findings are specific enough to act on without re-reading the whole file.
- Nothing was rewritten without approval.
- If the material passes, say so plainly rather than inventing findings.
