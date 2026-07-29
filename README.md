# CoC Keeper Kit

A preparation workbench for running **Call of Cthulhu 7th Edition** as the Keeper.
Ask Claude Code (from inside this folder) to build worlds, NPCs, monsters, puzzles,
handouts, and read-aloud scene text — mechanically correct and filed where you can find it.

## Quick start

1. **Start a campaign**
   ```
   Copy campaigns/_template-campaign/  →  campaigns/my-campaign/
   ```
   Then fill in `campaigns/my-campaign/CLAUDE.md` (era, tone, premise, content lines).

2. **Ask for material.** Examples:
   - "Design a one-shot scenario about a missing lighthouse keeper for `my-campaign`."
   - "Create an NPC: the town doctor who secretly feeds the cult. Full 7e stats."
   - "Stat a shambling drowned-sailor monster, moderate threat."
   - "Write read-aloud boxed text for the players entering the flooded crypt."
   - "Build a cipher puzzle the investigators solve from a torn ledger."
   - "Make a 1923 newspaper-clipping handout hinting at the disappearances."

3. **Where it lands.** Generated files go into the campaign's subfolders
   (`npcs/`, `scenes/`, `puzzles/`, `handouts/`, `world/`, `sessions/`).
   Reusable monsters/lore/tables go in the root `reference/`.

## What's in here

- **`CLAUDE.md`** — project vision and the house rules Claude follows.
- **`.claude/skills/`** — the authoring skills (rules lookup, NPC/monster/scene/puzzle/
  handout/world/scenario generators). Loaded automatically when relevant.
- **`reference/`** — shared canon: 7e rules cheat-sheets, a growing bestiary, Mythos lore,
  and random tables — usable by every campaign.
- **`templates/`** — the blank shapes each skill fills in.
- **`campaigns/`** — one folder per game, plus `_template-campaign/` to copy from.

## Notes
- Keeper-only secrets are marked `> **KEEPER ONLY**` and kept out of player-facing files.

## License
Released under the [MIT License](LICENSE) © 2026 Mzihong. Contributions are welcome — see
[CONTRIBUTING.md](CONTRIBUTING.md) and the [Code of Conduct](CODE_OF_CONDUCT.md).

## Disclaimer
This is an **unofficial, fan-made** preparation kit. *Call of Cthulhu* is a trademark of
**Chaosium Inc.**; this project is **not affiliated with, endorsed, or sponsored by
Chaosium**. It **references** 7th Edition mechanics so generated material is correct but
**reproduces no copyrighted text** from any rulebook or published scenario — you need the
official *Call of Cthulhu Keeper Rulebook* to actually play. The Cthulhu Mythos was created
by H. P. Lovecraft. All original content generated with this kit is yours.
