---
name: scene-description
description: Write atmospheric read-aloud "boxed text" and sensory scene/location detail for Call of Cthulhu — the flavour paragraphs the Keeper reads when players enter a place or meet a horror. Use when the user wants scene-setting prose, boxed text, a location's mood, or a monster/discovery reveal. Writes into the campaign's scenes/ folder.
version: "1.0.0"
---

# Scene Description

Write the prose a Keeper reads aloud — dread built from concrete, ordinary detail with one
thing quietly wrong. Evocative but *tight*: players stop listening after a few sentences.

## First
- Read the campaign `CLAUDE.md` for **era, tone, content lines** — period-true detail only.
- Know the scene's **purpose**: a clue, a choice, a shock, or a breather. Purpose sets length
  and where the paragraph "points."
- Use `templates/scene.md` (full scene) or just draft the boxed text if that's all that's asked.

## The craft of boxed text
- **3–6 sentences.** Long enough to immerse, short enough to keep the table's attention.
- **Multi-sensory:** always beyond sight — sound, smell, temperature, the feel of the air,
  the quality of the light. Two or three senses per box.
- **Concrete over abstract.** "The wallpaper is furred with damp" beats "it feels creepy."
  Let players draw the dread; don't tell them they're scared.
- **One wrong detail.** A single off-key note (a clock stopped at the same time in every room)
  does more than a pile of adjectives.
- **End on a hook, not a full stop** — something that invites action ("the cellar door stands
  open") rather than closing the moment down.
- **Say only what they perceive.** Keep interpretation, mechanics, and secrets *out* of the
  boxed text — those go in keeper notes below it.

## For a horror reveal
- Lead with the **image and motion**, then hand off the Sanity roll to `create-monster`'s
  entry. Describe wrongness through effect (what it does to the light, the smell it brings)
  rather than a full anatomy dump.

## Assemble the scene (if full)
Boxed text → what's here (clues, NPCs, features) → "if the players…" branches → the checks
that might come up (set difficulty, never gate the only path) → `> **KEEPER ONLY**` truth and
escalation.

## Output
- Save to `campaigns/<slug>/scenes/<name>.md`, `kebab-case.md`.
- Boxed text goes in a `>` blockquote so it's obvious what to read aloud.
- Cross-link NPCs, monsters, puzzles, and handouts present.

## Quality bar
- Reads aloud smoothly in ~20–30 seconds; no tongue-twisters or stage directions mid-prose.
- At least two senses and one "wrong" detail; ends on a hook.
- No secrets, mechanics, or player interpretation leaked into the read-aloud text.
