# 10 — Create Handout

Write props that feel like real objects from the world — and are **safe to hand over**: the
clue is inside, the solution is not. A good handout is evidence the players get to hold.

## First

- Read the campaign `CLAUDE.md` for **era, locale, and output language** — dates, prices,
  place-names, idiom, and technology must be period-true (a telegram not an email; a shilling
  not a dollar).
- Know **what the handout plants** (the lead it seeds) and **where players get it** (scene
  link).
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
  police/medical report for cold official detail. **An interactive scene map** (a floor plan
  the table looks at together, furniture and all) is also a handout by this same test — it's
  generated per `core/09-description.md`'s Output section, not this file, but it lands here and
  gets the same player-safe discipline and review below.

## In-period, in-language

A handout is the place where language and era are most visible, so get both right:

- Write the prop in the campaign's **output language**. A 1930s 上海 newspaper clipping should
  read like a period Chinese newspaper — 直排 conventions noted, 民国纪年 dates, period
  place-names — not like a translated English one.
- Match the writing system to the writer and the era: a 1920s letter uses 旧式书信 openings and
  closings; a modern text message does not.
- Where the fiction plausibly mixes languages (a colonial港英 police report, a foreign
  scholar's marginalia), mix them — it's texture and it can carry a clue.
- **When the writer wouldn't have written in the output language at all** — a Norwegian
  widow's 1919 diary in a 简体中文 campaign — write the prop in the **output language** and
  put the in-fiction device in the presentation note: a translation read aloud by the owner,
  an investigator translating live, a consular clerk's transcript, a mission-school copy.
  The table must be able to read the prop. Never hand over a page nobody present can read,
  and never quietly pretend the original was written in a language it wasn't.
- Keep proper nouns consistent with what's already in the campaign; check `canon-log.md`.

## Player-safe discipline (critical)

- The handout file is **PLAYER-FACING**. Put **no** answers, no keeper interpretation, no
  "this clue means…" inside it. Those belong in the linked scene/puzzle.
- Add a one-line keeper note *above the divider* (`what it plants`) that is clearly not part
  of the prop, and a presentation note for how to age/style it — neither is printed.

## Presentation

- Suggest how to make it real at the table: period font, tea-stained ageing, redaction bars,
  "hand it over torn in half," a photostat look. Keep it feasible, not a craft project.

## Output

- Save to `campaigns/<slug>/handouts/<name>.md`, `kebab-case.md` in English.
- The prop text sits between `---` dividers so it's obvious what to print.
- Link back to the scene/puzzle it belongs to.

## Quality bar

- Reads as a genuine period document in its own language; the clue is present but not
  underlined.
- Zero secrets/answers in the file — a player could read the whole thing with no spoilers.
- A clear, feasible note on how to present it.
