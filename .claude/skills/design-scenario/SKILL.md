---
name: design-scenario
description: Structure a WHOLE Call of Cthulhu scenario or mystery end-to-end — the hook, the hidden truth, a clue map obeying the three-clue rule, a web of scenes, cast, threats, and branching endings. Use whenever the user wants to design or outline a one-shot, adventure, mystery, or campaign arc, or turn a loose idea into a runnable spine ("design a scenario about a missing lighthouse keeper", "plan a one-shot", "outline the mystery"). This is the top-level glue skill that calls the others (build-world, create-npc, create-monster, create-puzzle, scene-description, create-handout) for the pieces. Writes into the campaign folder and links everything together.
version: "1.0.0"
---

# Design Scenario

Turn an idea into a runnable investigation: a hidden truth, fair paths to uncover it, and a
web of scenes that survives players going off-script. This is the **glue skill** — it calls
the others (`build-world`, `create-npc`, `create-monster`, `create-puzzle`, `scene-description`,
`create-handout`) to fill in the pieces.

## First
- Read the campaign `CLAUDE.md` for **era, tone, content lines, length** — scope to fit.
- Use `templates/scenario.md`. Load `coc-rules-reference` before any stat or check.

## Build in this order
1. **The truth.** Write what's *really* happening — the situation the mystery conceals. Start
   from the horror and work backwards to how a normal person would first brush against it.
2. **The clock.** Decide what the antagonist achieves if the investigators do nothing, and
   when. Pressure, not railroad — the world moves whether they act or not.
3. **The hook.** Why *these* investigators get pulled in — personal, professional, or paid.
4. **The spine.** The 2–4 underlying facts, in the order the truth unfolds.
5. **The clue map (three-clue rule).** For **every** fact the players *must* realise, provide
   **three independent** clues from different sources. If any one is missed or a roll fails,
   two remain. Lay this out as a table — it's the anti-stall guarantee.
6. **The scenes as a web.** Key each node by *purpose* (clue / choice / shock / breather).
   Most scenes should be reachable in more than one order — avoid a single required sequence.
7. **Cast & threats.** Name the NPCs and creatures (hand to `create-npc` / `create-monster`);
   ensure each monster has its fair "out."
8. **Endings.** Sketch best / muddled / grim outcomes and the world-fallout each leaves.

## Principles
- **Investigation, not a corridor.** Give agency; let players skip, reorder, and surprise you.
- **Every lock has ≥2 keys** (clues, NPCs, and puzzles all obey this).
- **At least one non-combat resolution** to the central threat.
- **Sanity as pacing.** Space the big SAN hits; let dread build, then spike at the reveal.
- **Content care.** Honour the campaign's declared lines/veils; flag heavy material.

## Output
- Save the spine to `campaigns/<slug>/<scenario-slug>.md` (or `overview.md` for the campaign's
  main arc). Generate the referenced NPCs/scenes/etc. into their folders and cross-link.
- Fill the template's **prep checklist** before calling it done.

## Quality bar
- Every must-know fact has three routes; no roll or missed scene can hard-stop the game.
- Scenes form a web, not a line; at least one peaceful way through the climax exists.
- Opening read-aloud written; all stats 7e-correct; handouts player-safe.
