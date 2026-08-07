# 04 — Design Scenario

Turn an idea into a runnable investigation: a hidden truth, fair paths to uncover it, and a
web of scenes that survives players going off-script. This is the **glue spec** — it calls
the others (`core/03`, `core/05`, `core/06`, `core/07`, `core/08`, `core/09`, `core/10`) to
fill in the pieces.

## First

- Read the campaign `CLAUDE.md` for **era, tone, output language, content lines, length** —
  scope to fit. Read `canon-log.md` and never contradict what has already happened at the
  table.
- Use `templates/scenario.md`. Read `core/02-rules-reference.md` before any stat or check.

## Build in this order

1. **The truth.** Write what's *really* happening — the situation the mystery conceals. Start
   from the horror and work backwards to how a normal person would first brush against it.
   If the campaign `CLAUDE.md` declares a **Threat** (category, and for a cult/organisation
   or named antagonist, a link to its `world/` file), the truth must be built consistent with
   it — read that field first; this spec doesn't re-ask what the threat is. If the truth
   traces back to a **named Great Old One or Outer God**, read its page in
   `reference/mythos/great-old-ones/` before inventing awakening conditions or signs — it's
   pre-written there.
2. **The clock.** Decide what the antagonist achieves if the investigators do nothing, and
   when. Pressure, not railroad — the world moves whether they act or not. For a campaign
   this is a standing artifact: build or update `world/event-clock.md` per
   `core/05-event-clock.md` rather than re-inventing a timeline per scenario.
3. **The hook.** Why *these* investigators get pulled in — personal, professional, or paid.
4. **The spine.** The 2–4 underlying facts, in the order the truth unfolds.
5. **The clue map (three-clue rule).** For **every** fact the players *must* realise, provide
   **three independent** clues from different sources. If any one is missed or a roll fails,
   two remain. Lay this out as a table — it's the anti-stall guarantee.
   - **Sourcing:** roll `reference/tables/clue-engines.md` (2–3 engines "live," never all
     ten) instead of inventing from habit. Cult threats: `cult-design-zh.md` §四 is engine 1
     (funding) expanded; others read the engine table directly. Three clues for one fact
     should come from **three different engines**.
   - **Draw it as a scene web** — `reference/craft/diagram-conventions-zh.md` §三. Nodes are
     scenes, edges labelled with the clue that gets you there. A must-reach scene with fewer
     than three inbound edges is a stall point.
   - **Six checks** (check 1 is also "independent"'s working definition;
     `core/11-review.md`'s audit reads off these six):

     | # | Check | Test |
     |---|---|---|
     | 1 | Tonight-discovery | If the threat learns tonight it's made, how many of the three can it kill by morning? **≥2 killable = not independent.** |
     | 2 | Threshold types differ | roll / presence / relationship / timing / cost / handed-over — the three land in three different types. |
     | 3 | ≥1 roll-free | Lands just from showing up, no check gates it. |
     | 4 | ≥1 permanent | Filed or fixed in the landscape — doesn't decay with the clock (engines 7, 10 fit naturally). |
     | 5 | ≥1 points somewhere | Names the next place/person; "this is wrong" ×3 still stalls — the clue-map side of the web's inbound-edge count. |
     | 6 | From three engines | Not three branches of one `clue-engines.md` roll. |
6. **The scenes as a web.** Key each node by *purpose* (clue / choice / shock / breather). This
   step is about the rest of the web, not the must-reach scenes step 5 already constrains
   (≥3 inbound edges each) — of the remaining scenes, most should be reachable in more than one
   order, avoiding a single required sequence. If a scene is a pursuit or an escape, read
   `reference/rules/chases.md` before writing it. **Once the web is drawn, count inbound edges
   on every must-reach node** (`diagram-conventions-zh.md` §三 already requires this on the
   diagram itself; this is the reminder to actually do it before moving on) — a clue with
   nowhere to point at is a ghost clue, and it doesn't show up just from counting to three.
7. **Cast & threats.** Name the NPCs and creatures (hand to `core/06` / `core/07`); ensure
   each monster has its fair "out." **Choosing which Mythos creature fits a given role**
   (especially "the boss is deity X — what's a fitting elite/servitor?") — check
   `reference/tables/monster-index.md` before inventing one from scratch; it indexes all 223
   `malleus-monstrorum-zh.md` entries by tier and `Serves` (who they answer to), so the search
   is "who serves X" instead of reading the full transcript.
8. **Endings.** Sketch best / muddled / grim outcomes and the world-fallout each leaves. Tag
   each ending with a **suggested SAN reward** per `reference/rules/sanity.md`'s scenario-end
   table — a starting number for `core/12-canon-update.md` to propose, adjust, and confirm with
   the Keeper after play. A muddled/grim ending gets no award.

## Generating one session against an existing campaign

The common request is not "design a campaign" but *"last time they went to the docks — what
now?"* In that case:

- Read `CLAUDE.md`, `canon-log.md`, and `world/event-clock.md`.
- Advance the clock by the elapsed in-fiction time and check which triggers have fired.
- Build **one session's worth**: an opening beat that answers where they left off, 3–5 scenes,
  the clues reachable this session, two complications
  (`python scripts/roll.py complications --times 2 --campaign <slug>`), and likely stopping
  points.
- Do **not** resolve the campaign's central truth early because the session needs a climax.
  A session can end on a partial revelation.
- Save to `campaigns/<slug>/sessions/<n>-<slug>.md` using `templates/session-prep.md`.

## Opening a new arc in an existing campaign

A sequel or time-skip ("a year later, new threat") that stays in the same campaign folder —
see `campaigns/README.md` → "Multi-arc & branching campaigns" for when this applies rather
than forking to a new campaign.

- Read `CLAUDE.md`, the **full** `canon-log.md` (all prior arcs and any Interlude entries),
  and every archived clock in `world/archive/` — not just the live one, which now tracks the
  *new* arc's threat.
- Number the new arc's scenario files `<arc>-<scenario-slug>.md`; add the arc to `overview.md`'s
  Arcs index.
- **Don't rebuild the world.** `world/` is standing state that carries forward; extend it (new
  locations, evolved factions) rather than re-generating what already exists.
- Otherwise follow "Build in this order" above as normal — the new arc gets its own truth,
  clock, hook, and clue map; it just inherits everything upstream instead of starting cold.

## Principles

- **Investigation, not a corridor.** Give agency; let players skip, reorder, and surprise you.
- **Every lock has ≥2 keys** (clues, NPCs, and puzzles all obey this).
- **At least one non-combat resolution** to the central threat.
- **Sanity as pacing.** Space the big SAN hits; let dread build, then spike at the reveal.
- **Content care.** Honour the campaign's declared lines/veils; flag heavy material.
- **Scale to the table.** If the actual party size differs from the campaign's declared party
  size (`CLAUDE.md`), add a **Scaling** sidebar: how opposition numbers, clue redundancy, and
  total SAN pressure shift up or down. A 3-investigator table needs fewer simultaneous threats
  and *more* clue redundancy (fewer skill points spread across more must-know facts), not less.

## Output

- Save the spine to `campaigns/<slug>/<scenario-slug>.md` (or `overview.md` for the campaign's
  main arc). Generate the referenced NPCs/scenes/etc. into their folders and cross-link.
- Write in the campaign's declared **output language**; keep filenames English kebab-case.
- Fill the template's **prep checklist** before calling it done.

## Quality bar

- Every must-know fact has three routes; no roll or missed scene can hard-stop the game.
- Scenes form a web, not a line; at least one peaceful way through the climax exists.
- Opening read-aloud written; all stats 7e-correct; handouts player-safe.
- Nothing contradicts `canon-log.md`.
