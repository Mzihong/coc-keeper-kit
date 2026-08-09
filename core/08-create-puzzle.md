# 08 — Create Puzzle

Design obstacles that reward thinking without ever hard-stopping the story. In an
investigation game a stuck puzzle is a dead session — build in redundancy and mercy.

## First

- **Preview before you expand** — `core/00-how-to-run.md` → ground rules: a ≤15-line list of
  what you're about to write, confirmed by the Keeper, before any file goes to disk.
- Read the campaign `CLAUDE.md` for era/tone/output language (a cipher's form should fit the
  period *and* the language it's written in).
- Decide the **type**: cipher/code, logic, physical mechanism, social deduction, or ritual
  reconstruction. Know **what solving it grants** (access, a clue, a warning, an item).
- Use `templates/puzzle.md`.

## Fair-play rules (non-negotiable)

- **Solvable from what's present.** Players must have, or be able to find, every piece needed.
  No leaps that require the Keeper's private knowledge.
- **At least two routes through**: the intended clean solution *plus* an alternate (a skill
  roll, an NPC who knows, brute force at a cost). Add a **bypass/mercy** for true dead-ends.
- **Never gate the sole path forward on one roll.** A failed roll costs time, attention, or
  safety — not the solution. (This is the three-clue rule at puzzle scale.)
- **A hint ladder**, so you can un-stick the table gracefully:
  1. **Nudge** — draw attention to a detail already in front of them.
  2. **Lead** — point at the method.
  3. **Gift** — hand them a solved piece so the story moves.

## Make it good

- **The answer should feel earned**, not arbitrary — clues cohere into an "aha," not a guess.
- **Player-facing material self-contained.** If there's a cipher/riddle/diagram, write it so
  it works from the handout alone; put it here or hand off to `core/10-create-handout.md`.
- **Keep the solution keeper-only** — answer and method go in a `> **KEEPER ONLY**` block.
- **Fit the fiction.** The lock reflects who built it: a sailor's knots, a scholar's Latin, a
  cultist's star-signs. Form carries flavour and a half-clue.

## Ciphers specifically

- Match difficulty to the table, not to you. Simple, satisfying codes (Caesar shift,
  substitution with a keyword, book cipher, Pigpen, reversed/mirror text) beat unbreakable
  ones. **Always include the worked solution and the intended crack** in the keeper block.
- **In Chinese-language campaigns, letter-substitution ciphers don't work.** Use forms that
  survive the language: 拆字 (character decomposition), 藏頭 (acrostic by first character),
  部首 keys, stroke-count numbering, 反切 phonetic spelling, a book cipher keyed to page and
  character index, or a period-plausible telegraph code (中文電碼). Verify the puzzle actually
  works in the script it's written in before shipping it.

## Output

- Save to `campaigns/<slug>/puzzles/<name>.md`, `kebab-case.md` in English.
- Write the content in the campaign's declared **output language**.
- Link the scene it appears in and any handout that carries it.

## Quality bar

- ≥ 2 solution routes + a mercy path; a 3-rung hint ladder written out.
- Player material is solvable on its own; the worked answer is present but keeper-only.
- The puzzle mechanically works in the language it is written in.
- No single die roll can end the investigation.
