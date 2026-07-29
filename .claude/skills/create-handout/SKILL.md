---
name: create-handout
description: Write a player-facing Call of Cthulhu prop — a letter, newspaper clipping, journal page, telegram, police report, or photo caption — in-voice, in-period, with a clue buried in natural detail. Use when the user wants a handout the players physically receive. Writes player-safe files into the campaign's handouts/ folder.
version: "1.0.0"
---

# Create Handout

Write props that feel like real objects from the world — and are **safe to hand over**: the
clue is inside, the solution is not. A good handout is evidence the players get to hold.

## First
- Read the campaign `CLAUDE.md` for **era and locale** — dates, prices, place-names, idiom,
  and technology must be period-true (a telegram not an email; a shilling not a dollar).
- Know **what the handout plants** (the lead it seeds) and **where players get it** (scene link).
- Use `templates/handout.md`.

## Write it in-voice
- **Match the writer** — literacy, class, profession, emotional state, era. A dockhand's note
  and a professor's letter read nothing alike.
- **Bury the clue in natural detail.** One line should matter; surround it with the ordinary
  texture of a real document so it isn't spotlit. Reward the careful reader.
- **Leave room for investigation.** A smudge, a torn corner, a crossed-out word, an unfamiliar
  name — hooks that invite a Library Use or a follow-up, not a spoon-fed answer.
- **Form fits function:** newspaper clipping for public events; private letter for secrets and
  emotion; journal for a slow descent into the Mythos; telegram for urgency and clipped dread;
  police/medical report for cold official detail.

## Player-safe discipline (critical)
- The handout file is **PLAYER-FACING**. Put **no** answers, no keeper interpretation, no
  "this clue means…" inside it. Those belong in the linked scene/puzzle.
- Add a one-line keeper note *above the divider* (`what it plants`) that is clearly not part
  of the prop, and a presentation note for how to age/style it — neither is printed.

## Presentation
- Suggest how to make it real at the table: period font, tea-stained ageing, redaction bars,
  "hand it over torn in half," a photostat look. Keep it feasible, not a craft project.

## Output
- Save to `campaigns/<slug>/handouts/<name>.md`, `kebab-case.md`.
- The prop text sits between `---` dividers so it's obvious what to print.
- Link back to the scene/puzzle it belongs to.

## Quality bar
- Reads as a genuine period document; the clue is present but not underlined.
- Zero secrets/answers in the file — a player could read the whole thing with no spoilers.
- A clear, feasible note on how to present it.
