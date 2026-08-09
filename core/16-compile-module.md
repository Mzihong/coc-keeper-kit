# 16 — Compile a Module

Turn one arc's scattered material — world, cast, scenes, clues — into a single **linear,
readable module text** the Keeper can flip through at the table the way a published adventure
reads, following the shape of the rulebook's own Chapter 15. This is a **new artifact, not a
rebuild of the scene web**: `templates/scenario.md` stays the design document (a web, for an
author); `templates/module.md` is the reading document (a line, for a Keeper at the table).
Same facts, two different layouts — neither replaces the other.

## First

- **This is not `dist/bundle.md` come back.** That build step retired because it was zero-gain
  mechanical concatenation of the *whole repo*, for a model to read. This compiles **one arc**,
  for a **Keeper reading at the table**, and does real information reorganisation — the
  timeline is rewritten, not copied. Range, reader, method, and information gain all differ;
  don't let "no build products" veto this on the strength of a surface resemblance.
- **Compile after the arc is played, not before.** The module is a keepsake and a rereadable
  record, not session prep. Compiling early bakes in guesses about what will happen instead of
  what did; wait until the arc's events are in `canon-log.md`. What you build *before* running
  a session is `templates/session-prep.md`'s job, not this one — see "Boundary" below.
- **The compilation unit is one arc, never the whole campaign.** An open-ended chronicle
  compiles the way an official multi-part campaign book is bound: a shared primer plus one
  module per arc, not a single ever-growing linear text.
- Use `templates/module.md`. Read the campaign's `CLAUDE.md` first — output language, and any
  standing convention (a surface/secret narration split, a house rule) the compile must carry
  through rather than flatten.

## Step 1 — Gap report

Before compiling anything, list what this arc is missing:

- Which named NPCs the arc actually uses are still `stub` in `npcs/roster.md` rather than a
  full card (read the roster's status column — this is why the gap report can't run until
  `core/06-create-npc.md`'s two-tier system has something to read).
- Which scenes have no read-aloud prose written yet (a `<pending>` placeholder in `scenes/*.md`).
- Which clue-map entries have no scene actually landing them.

Tag each gap **blocks a readable compile** or **doesn't**. A stub NPC nobody in this arc ever
checks, fights, or talks to at length doesn't block anything — leave them a stub. A scene the
clue map depends on with no prose does. Hand the report to the Keeper and let them pick what to
fill in before compiling — this is `core/00-how-to-run.md`'s "preview, then confirm, then
expand" applied to this specific artifact. Compiling straight through the gaps produces a
module with holes in it, not a finished one.

## Step 2 — Transcription rules

Compiling is authorship, not concatenation. These four are mandatory, not stylistic choices:

- **Timeline.** `world/event-clock.md` tracks *stages*; the module's Timeline section tracks
  **Day N × what each faction is doing**. Rewrite the doom track into day-by-faction rows — this
  is the single largest piece of real work in a compile. A reviewer should not be able to match
  clock-stage prose against timeline rows 1:1; if they can, the rewrite didn't happen.
- **Stats inline.** An NPC or monster's stat block appears **the first time it's encountered**
  in the scene chapters — nobody wants to flip to an appendix mid-scene. Also gather every stat
  block into the module's consolidated Appendix section for a fast lookup later.
- **Handout numbers.** Every handout gets a stable `H1`, `H2`, … number for this module. The
  scene chapter text references it with a short blockquote where it comes up; the full handout
  text lives once, in the Appendix.
- **Surface / secret layering.** If the campaign's `CLAUDE.md` declares a two-layer narration
  convention (surface description vs. a hidden mechanism), keep it: the boxed text stays
  surface-only, and the mechanism goes in the `> **KEEPER ONLY**` blockquote immediately after
  it. The surface layer must never contain a word from the secret layer — compiling doesn't get
  an exception to a campaign's own rule just because it's reorganising text.

## Step 3 — Hard rule: compiling never invents a fact

If transcription turns up a gap the gap report missed — a scene references a clue that doesn't
exist anywhere, a timeline day has no corresponding scene — **stop and fix the source file**,
then recompile. Never patch the hole directly in the module text. The module is a derived
artifact: a fact that exists only in it is invisible to every other spec in this kit, and the
next compile silently drops it the moment someone regenerates from source. This rule mirrors
into `core/11-review.md`'s Blocking section — a reviewer finding a fact in a module text with no
source-file backing fails the review outright.

## Length & splitting

Cap a single module file at **~1200 lines**. Past that, split into `-part2.md`, `-part3.md`, …
— still one arc's material, just more than one file. A long arc's `world/` alone can already
run past 1000 lines uncompiled; an uncapped compile is unreadable by construction, not just
long.

## Output

```
campaigns/<slug>/module/
  00-campaign-primer.md    ← shared across every arc: worldview, translation glossary,
                               cast index, map index
  <arc>-<slug>.md          ← one file per arc, built from templates/module.md
  appendix-handouts.md     ← every handout in this arc, numbered H1/H2/…, gathered in one place
```

Cross-link back to the source files the module was compiled from — the source manifest at the
top of `templates/module.md` carries this — rather than duplicating anything not actually
rewritten. **The module text is entirely Keeper-facing.** Nothing in it is safe to hand a
player as-is; what players get is still the arc's own `handouts/` and any `--player` map
render, unchanged by this spec.

**Boundary with `templates/session-prep.md`:** the module is written *after* an arc closes, as
a rereadable record for the Keeper (or another Keeper); session prep is written *before* each
session, as a disposable working document for the next few hours of play. They cover similar
ground — cast, scenes, what happens — for different readers at different times. Don't let one
substitute for the other; `templates/session-prep.md` carries this same line pointing back
here.

## Quality bar

- The gap report ran and was shown to the Keeper before compiling; every gap it found is either
  filled or explicitly accepted as a known hole in the finished module.
- The Timeline section is genuinely rewritten from the event clock into day-by-faction rows,
  not copied.
- Every fact in the module text also exists in a source file — nothing was invented to paper
  over a gap (`core/11-review.md` audits this).
- Every stat block appears at its first in-scene mention and again in the consolidated
  Appendix.
- A campaign's declared surface/secret convention, if any, survives the compile unbroken.
- File stays under ~1200 lines, or is split into numbered parts that each do.
- The module text is entirely Keeper-facing; nothing in it could be handed to a player as-is.
