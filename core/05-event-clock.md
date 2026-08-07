# 05 — Event Clock & Triggers

The world does not wait for the investigators. This spec builds the campaign's **standing
timeline of pressure** — what the threat achieves on its own, and what fires in response to
what the players do. It is the single artifact that keeps a campaign from becoming a
sequence of disconnected scenarios.

Build it once per campaign, right after the world. Update it after every session.

## The two halves

**1. The doom track — what happens if the investigators do nothing.**

A dated or staged countdown, from *now* to the threat's goal. Each stage names a **visible
sign** (what an ordinary person in the world would notice) and the **hidden progress** behind
it. The visible signs are the Keeper's free improvisation material — background dread that
costs no prep.

**2. The trigger table — what fires in response to the players.**

Each row is a condition the players might meet, and what changes when they do. Triggers are
not scenes; they are *changes to the world state* that any later scene must reflect.

## Build it

1. **Name the goal.** What is the threat trying to accomplish, concretely, and by when?
   Vague dread has no clock. "Open the gate at the spring tide, eleven days out" has one.
2. **Write 4–6 doom stages** from now to the goal. Each gets: a stage label, the in-fiction
   timing, the visible sign, and the keeper-only hidden progress.
3. **Write 6–10 triggers.** Cover, at minimum:
   - the players making the threat aware of them
   - the players killing, arresting, or exposing a key NPC
   - the players finding a core piece of evidence
   - the players doing nothing for a stretch
   - the players trying to leave, or to bring in outside authority
   - **the players stalling on a must-know fact for N sessions** — what the threat does in
     response is itself the next clue (see Principles below); this is the stall-recovery
     trigger `core/11-review.md`'s three-clue audit checks for
4. **Give every trigger both branches.** What if they succeed at it, and what if they fail
   or half-succeed? A trigger with one outcome is a railroad tie.
5. **Note reversibility.** Which stages can the players push *back*? A clock with no rewind
   is a losing timer, not a source of tension.

## Format

Use `templates/event-clock.md`. The trigger table's shape:

| # | Trigger condition | Fires | World-state change | Reversible? |
|---|---|---|---|---|

Keep "World-state change" concrete and checkable — *"the harbourmaster stops speaking to
outsiders; the night patrol doubles"*, not *"tension rises."* The Keeper must be able to read
one row and know what is different.

## Principles

- **Pressure, not punishment.** The clock exists to make choices cost something, not to
  defeat the players on schedule. The stall-recovery trigger above follows this same rule:
  when the players stall on a must-know fact, the threat acting on its own initiative is
  pressure, not a penalty — and the action itself doubles as a new clue, so a genuinely
  stalled table always has a way back in without the Keeper inventing a fourth clue on the
  spot (`core/04-design-scenario.md` step 5's six checks are what should have caught this
  before play; this trigger is the table-side backstop for when they didn't).
- **Signs before consequences.** Every stage should be foreshadowed by the previous stage's
  visible sign. Players who read the world get to act early; that's the reward.
- **The clock is public, the mechanism is secret.** Players should be able to feel time
  running out without being told the schedule.
- **Triggers respond, they don't dictate.** A trigger fires because of something the players
  did. If you're writing "the players go to the lighthouse" as a trigger, that's a scene —
  put it in the scenario.
- **Advance it honestly.** Once written, run the clock as written. Don't stall it to protect
  a plan or accelerate it to force a climax.

## Output

- Save to `campaigns/<slug>/world/event-clock.md`.
- Write in the campaign's declared **output language**; keep the table headers and structure
  intact.
- The doom track's hidden progress and the whole trigger table are `> **KEEPER ONLY**`.
- After each session, update the "current stage" line and mark fired triggers with the
  session number — see `core/12-canon-update.md`.

## Archiving (multi-arc campaigns)

When an arc's threat is fully resolved and a new arc opens in the same campaign folder
(`campaigns/README.md` → "Multi-arc & branching campaigns"), move the settled clock to
`world/archive/event-clock-<arc-slug>.md` and build a fresh clock at the live path for the new
arc's threat, following "Build it" above from scratch. **The live path never changes** — every
other spec always reads `world/event-clock.md` for "current," so nothing else needs to know an
archive happened. This step belongs to `core/12-canon-update.md`'s arc-close checklist.

## Quality bar

- The threat's goal is concrete and dated. Someone could ask "what day is it and what's
  happened?" and get an answer from this file alone.
- 4–6 doom stages, each with a visible sign *and* hidden progress.
- 6–10 triggers, each with a fires-branch, a fails-branch, and a concrete world-state change.
- At least two stages are marked reversible, with what it would take to push them back.
- Nothing here duplicates a scenario's scene list — this file is world state, not plot.
