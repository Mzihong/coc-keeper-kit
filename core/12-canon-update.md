# 12 — Canon Update

Run this **after every session**. It is what keeps session 8 from contradicting session 1.

The Keeper describes what happened — usually informally, often briefly, sometimes days later.
Your job is to turn that into durable campaign state that every later generation step reads.

## How to run it

1. Ask what happened, if they haven't said. Prompt for the five things that actually change
   state:
   - Where did they end up, and when is it now in-fiction?
   - What did they **learn** — which facts are now known to the players?
   - Who died, was arrested, fled, or flipped?
   - What did they change in the world — burned, stolen, exposed, promised?
   - What did *you* improvise that isn't written down anywhere?

   That last one matters most. Improvised detail is the canon most likely to be lost, and the
   most likely to be contradicted later.

2. Read `campaigns/<slug>/canon-log.md`, `CLAUDE.md`, and `world/event-clock.md`.

3. Write the updates below. Never rewrite history — **append**.

## What to update

**`canon-log.md`** — append a new session entry:
- Session number and in-fiction date range.
- **Established facts** — what is now true and locked, including anything improvised at the
  table. Write these as flat statements; they are the constraints all later generation obeys.
- **Player knowledge** — what the *investigators* know, which is not the same as what is true.
  Keep these separate; the gap between them is the campaign.
- **Cast changes** — dead, missing, hostile, allied, promoted.
- **World changes** — what is physically or socially different now.
- **Open threads** — promises made, questions raised, things the players said they'd do next.

**`world/event-clock.md`**:
- Advance the **current stage** by elapsed in-fiction time.
- Mark fired triggers with the session number and record the branch that actually resolved.
- Add any new trigger the session created.

**`CLAUDE.md`** (campaign):
- Update the *Canon so far* keeper block only when something structural changed — a central
  secret is now known, a main antagonist is dead, the premise has shifted.
- Update the investigator list for deaths, replacements, and SAN state worth remembering.

**`npcs/<name>.md`** — for every NPC the party actually interacted with this session (not
every NPC mentioned): overwrite that NPC's **current attitude** to reflect where things now
stand, and append one line to the **interaction history log** (`> **KEEPER ONLY —
Interaction history**` block in `templates/npc.md`) — facts and relationship changes only, no
narration; the narration already lives in this session's `canon-log.md` entry, cross-link the
session number instead of repeating it. **This is a required step, not an optional one** — the
whole point of the log is that "does this NPC know/trust the party" stays answerable from that
NPC's own file without rereading the campaign's full canon-log, and it silently rots the first
time a session update skips it.

**`sessions/<n>-<slug>.md`**:
- Fill in the template's "After the session" block.

## Session-end rewards

Only when this session closed out a scenario's central threat — reaching one of the endings
sketched in the scenario file, not every session:

1. Read which ending was actually reached and its suggested SAN reward (`templates/scenario.md`
   tags each ending with one; if the scenario predates this convention, use
   `reference/rules/sanity.md`'s scenario-end table instead).
2. **Suggest, then ask, then adjust** — never write a number silently:
   - Propose the SAN award and note which skills are eligible for a 7e development roll (any
     skill an investigator successfully used at least once this session).
   - Ask the Keeper to accept, adjust, or skip the award.
   - This kit doesn't track investigator sheets — development rolls happen at the table; the
     reminder is informational.
3. Record the confirmed number (or "none — muddled/grim ending") in the session's canon-log
   entry's `Rewards` line.

## Rules

- **Append, never revise.** If the table contradicted something written, the *table* is
  canon. Record the new truth as a new entry and note that it supersedes the old one — don't
  edit the old entry away. The history of the contradiction is useful.
- **Separate true from known.** A fact the Keeper knows and a fact the players have learned
  are different columns. Later scenarios need both: one to stay consistent, one to know what
  still counts as a revelation.
- **Record improvisation verbatim** where you can. The name the Keeper made up for a barman
  is now that barman's name forever.
- **Don't invent what happened.** If the Keeper's account is vague, write what they said and
  mark the gap `<unclear — confirm>`. Filling gaps with plausible fiction is how canon rots.
- **Flag contradictions** you notice between the account and existing canon. Ask; don't
  silently pick one.
- Write in the campaign's **output language**, matching the rest of the campaign.

## Closing an arc (multi-arc campaigns only)

See `campaigns/README.md` → "Multi-arc & branching campaigns" for when this applies — a
sequel or time-skip that stays in the same campaign folder rather than forking to a new one.

- **If time skips before the next arc starts**, write an **Interlude** entry instead of a
  session entry — same append-only rules, using the Interlude shape in `canon-log.md`: elapsed
  time, what happened off-screen, cast status swept forward, what carries into the new arc.
- **Archive the closed arc's clock:** move `world/event-clock.md` to
  `world/archive/event-clock-<arc-slug>.md`, then build a fresh live `world/event-clock.md` for
  the new arc's threat per `core/05-event-clock.md`. The live path never changes.
- **Cast state sweep:** update every recurring NPC's status for the time elapsed — ages,
  deaths, relocations, allegiance shifts — in `canon-log.md`'s Cast status table.
- **Update `overview.md`'s Arcs index** with the closed arc's status and archived-clock link.
- **Update `CLAUDE.md`'s Canon so far block** only if something structural changed for the new
  arc (a new central threat, a new premise layer) — same rule as any other structural update.

## Then

Offer the obvious next step: *"Prep session `<n+1>`?"* — which runs
`core/04-design-scenario.md` against the freshly-updated state.

## Quality bar

- Every improvised detail the Keeper mentioned is now written down somewhere findable.
- True-vs-known is separated, not merged.
- The event clock's current stage is correct and fired triggers are marked.
- Every NPC who actually interacted with the party this session has an updated attitude and a
  new interaction-history log line — not just the ones with plot-critical secrets.
- No existing entry was edited or deleted; contradictions are marked, not resolved silently.
- A model reading only `canon-log.md` could generate the next session without contradicting
  anything that happened.
