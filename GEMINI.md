# GEMINI.md — CoC Keeper Kit

A preparation workbench for a Call of Cthulhu **Keeper**, for **CoC 7th Edition**.

> **All instructions live in `core/`. This file is a pointer, not a copy.**
> Read **`core/00-how-to-run.md`** before doing anything else — it holds the pipeline, the
> routing table, the ground rules, and the layout. If this file ever disagrees with `core/`,
> `core/` wins.

## Routing — read the spec that matches the request, then follow it

You have no skill-loading mechanism, so route by hand. Open the file and follow it to the
letter, including its Quality bar.

| The Keeper asks for | Read |
|---|---|
| a new campaign, "help me start", "開新團", "you decide" | `core/01-intake.md` |
| any rule, number, difficulty, SAN cost, stat block | `core/02-rules-reference.md` — **read before writing numbers** |
| a place, town, region, faction, cult org, timeline | `core/03-build-world.md` |
| a whole mystery, one-shot, or the next session | `core/04-design-scenario.md` |
| what happens if the players do nothing; triggers | `core/05-event-clock.md` |
| a person — ally, witness, villain, contact | `core/06-create-npc.md` |
| a non-human threat, creature, Mythos entity | `core/07-create-monster.md` |
| a pregen, ready-to-play investigator, elite NPC with full stats | `core/13-create-investigator.md` |
| a puzzle, cipher, code, lock, riddle | `core/08-create-puzzle.md` |
| read-aloud / boxed text, atmosphere, a reveal, or an investigator's action narrated | `core/09-description.md` |
| a prop the players physically receive | `core/10-create-handout.md` |
| "check this", "is this ready" | `core/11-review.md` |
| "here's what happened last session" | `core/12-canon-update.md` |

## Non-negotiables

- **CoC 7th Edition.** Read `core/02-rules-reference.md` and `reference/rules/` before
  committing any number.
- **Output language is per campaign**, declared in `campaigns/<slug>/CLAUDE.md`. Generated
  content follows it; kit scaffolding and filenames stay English `kebab-case.md`. For
  简体中文, follow `reference/glossary-zh.md` and never mix 繁体.
- **Continuity.** Read the campaign's `CLAUDE.md` and `canon-log.md` before generating into
  it. Never contradict established canon.
- **Fair play.** Three independent clues per must-know fact; no single roll can hard-stop the
  game.
- **Spoiler hygiene.** Keeper-only content goes in `> **KEEPER ONLY**` blocks and never in
  player-facing files.
- **Safety.** Respect the campaign's declared lines and veils. Never auto-fill them.

## If you cannot write files

Print the full file content with a header naming its path:

```
=== campaigns/dagon-bay/npcs/mary-tang.md ===
```

Never downgrade an artifact to a summary of an artifact.

## Portability

This kit is read by Claude, Gemini, and ChatGPT. `CLAUDE.md`, `GEMINI.md`, and `AGENTS.md`
are three thin adapters over the same `core/`. **When changing how the kit behaves, change
`core/` — never a root adapter.**
