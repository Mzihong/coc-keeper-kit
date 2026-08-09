# Module — <Arc title>

*A rereadable record, compiled after this arc closed — not what you prep from before running a
session. For that, use `templates/session-prep.md`.*

**One-line premise:** <the hook, in one sentence — what a back-cover blurb would say>

> **Source manifest** — compiled <date> from the files below. **Facts live in the source
> files, not here.** If something in this document is wrong, fix the source and recompile;
> never hand-edit a fact into the module text itself.
>
> **These sources are not guaranteed to agree, and this compile never breaks a tie.** If two
> of them say different things about the same fact, the compile stops and reports it to the
> Keeper — where, what each side says, which is newer and why you think so — then the *source*
> is fixed and the module recompiled. Applying the campaign's own precedence rule on your own
> counts as breaking the tie: it may be the authoritative file that's wrong.
> See `core/16-compile-module.md` step 3.
> - `overview.md` — premise
> - `world/` (`timeline.md`, faction/location files, `event-clock.md`) — background, recent
>   events, timeline
> - `npcs/roster.md` + `npcs/<name>.md` — cast, stat blocks
> - `<scenario-slug>.md`, `scenes/*.md` — clue map, scene chapters
> - `puzzles/*.md` — puzzle chapters
> - `reference/bestiary/`, monster files — stat blocks
> - `handouts/*.md`, `world/*.svg` — appendix
>
> **Compiler map** — which section below is built from what, and how (see
> `core/16-compile-module.md` step 2 for the transcription rules this compile followed):
>
> | Section | Source | Transcription |
> |---|---|---|
> | Title + one-line premise | `overview.md` first line | copied |
> | Introduction | `CLAUDE.md` (era/tone/lethality/party/content lines) + this arc's clue map | which skills the clue map leans on hardest |
> | Background | scenario truth + `world/timeline.md` hidden track | reordered furthest-back to closest |
> | Recent events | `world/event-clock.md` stage 0 | rewritten as prose |
> | Cast at a glance | `npcs/roster.md` + card files' first line | condensed to one line each |
> | Timeline | `world/event-clock.md` doom track | **rewritten** — clock stages become day-by-faction rows, not copied |
> | Investigator hooks | scenario hooks + `investigators/` | as-is, handout-able |
> | How to run this arc | clue map + scene web | the network the linear read below can't show |
> | Scene chapters | `scenes/*.md` + `world/` locations + `puzzles/*.md` | linear, by day/location |
> | Endings & rewards | scenario's three endings + SAN rewards | as-is |
> | Appendix | `handouts/*.md`, `world/*.svg`, gathered stat blocks | stats consolidated; everything else linked |

## Introduction

*For the Keeper opening this file before the table sits down.*

- **Era & locale:** <as run — note here if a Keeper retheming this arc for another table would
  need to change anything load-bearing>
- **Weight:** <how much this arc leans on action vs. investigation>
- **Skills this arc leans on hardest:** <2–4 skills the clue map and scenes actually call for>
- **Read before running:** <which cheat-sheets or campaign files to have open — e.g. combat,
  chases, a specific NPC card>

## Background

*The truth, told from furthest back to most recent — what's actually going on, in the order it
happened, not the order the investigators will learn it.*

<the deep history>

## Recent events

*How the truth above arrived at the moment this arc opens on.*

<the immediate lead-in>

## Cast at a glance

| Name | Role | Wants | Secret (their tell) |
|---|---|---|---|
| <name> | <one line> | <one line> | <what gives them away, or what they're hiding> |

## Timeline

*Day 0 through the arc's close. One subsection per day, one line per faction — this is the
Keeper's reference for what's moving off-screen while the investigators do whatever they do.*

### Day 0 — <date>
- **<Faction / party A>:** <what they do>
- **<Faction / party B>:** <what they do>
- **Investigators:** <where they enter the timeline, if at all>

*(repeat one subsection per day of the arc)*

**If nothing stops it:** <what the antagonist achieves by the arc's last day>

## Investigator hooks

*Motives that can be handed to players as a pre-session handout, or discussed and adjusted to
fit their own concepts. Each is followed by a Keeper's note — how the hook pays off, and what
it's worth offering as a reward for playing it straight.*

### Hook A — <label>
<the handout-able paragraph, second person>

> **Keeper's note:** <how this hook connects to the plot, what triggers its payoff>

### Hook B — <label>
<...>

> **Keeper's note:** <...>

## How to run this arc

*The one section with no equivalent in a published module — everything the linear read above
had to leave out because the table won't experience it in order. This is where the web gets
put back.*

### Clue map

| Must realise | Clue | Where | Threshold type | Shelf life |
|---|---|---|---|---|
| <fact> | <source> | <scene link> | <roll / presence / relationship / timing / cost / handed-over> | <permanent, or decays by day N> |

### Scene map (entrances & exits)

| Scene | Reachable from | Leads to | Trigger to open it |
|---|---|---|---|---|
| <scene> | <scene(s), or "arc open"> | <scene(s)> | <what makes this scene available> |

## Scene chapters

*Linear, ordered by day then location — read top to bottom at the table.*

### 1. <Scene title> — Day <n>, <location>

**Read aloud:**
<boxed text>

**What's here / what can be learned:**
- <…>

**Checks & failure:**
- <check> — <what a failure costs, never a hard stop>

**NPC reactions:**
- <NPC> — <how they respond to being approached, pressed, or ignored>

**Stats (first appearance):**
<inline stat block, only if an NPC or monster appears here for the first time>

**Exits:**
- <condition> → <next scene>

*(repeat one subsection per scene)*

## Endings & rewards

- **Best:** <…> — *SAN reward:* <e.g. +1D6>
- **Muddled:** <…> — *SAN reward:* none
- **Grim:** <…> — *SAN reward:* none
- **Cthulhu Mythos / Luck / other changes:** <…>

## Appendix

### Stat blocks (consolidated)

*Everything that appeared inline above, gathered here for a quick lookup without flipping back
through the scene chapters.*

<NPC and monster stat blocks>

### Handouts

- **H1** — <name> → `handouts/<file>.md`
- **H2** — <name> → `handouts/<file>.md`

### Maps

- <link to `.svg`> — <which scene(s) it covers>
