# campaigns/

One folder per game you run.

## Starting a campaign

Ask the model to start a new campaign (`start-campaign`, or `core/01-intake.md` directly).
It runs the intake, copies the template, and fills it in — including anything you answered
`auto` to, which it then shows you for approval.

To do it by hand instead:

1. **Copy the template:** `_template-campaign/` → `<your-campaign-slug>/` (English kebab-case).
2. **Fill `CLAUDE.md`** — era, output language, tone, premise, content lines. Leave anything
   you don't care about as `<auto>`; the intake step resolves it. Content lines and veils are
   never auto-filled.
3. **Build the standing state:** `world/`, then `world/event-clock.md`, then the cast.
4. **Then generate per session** into `sessions/`, `scenes/`, `npcs/`, `puzzles/`, `handouts/`.

## The three files every generator reads

| File | Holds | Updated by |
|---|---|---|
| `CLAUDE.md` | Era, language, tone, safety, structural canon | you, at intake |
| `canon-log.md` | What has actually happened; true vs. player-known | `core/12-canon-update.md`, after each session |
| `world/event-clock.md` | Where the threat currently stands; fired triggers | `core/05-event-clock.md`, then each session |

Keep these current. Everything downstream — scenarios, NPCs, handouts — is generated against
them, so a stale canon log produces contradictions at the table.

## Conventions

- Campaign-specific material lives here. Anything reusable across games (a generic monster, a
  Mythos tome, a random table) belongs in the root `reference/` instead.
- Filenames are English `kebab-case.md` even when the content is Chinese.
- `_template-campaign/` is the skeleton — don't run a game out of it; copy it.

## Multi-arc & branching campaigns

The default assumption is one folder = one timeline = one append-only `canon-log.md` = one
live `world/event-clock.md`. Two situations break that assumption; **which one applies turns
on whether canon forks:**

**Doesn't fork → stay in the same folder, use arcs.** A sequel or a time-skip ("a year later,
new threat") continues the same timeline — it just needs a "chapter" layer above scenarios.

- Number scenario files by arc: `01-<scenario-slug>.md`, `02-<scenario-slug>.md`, …
- `overview.md` gets an **Arcs** index listing each arc, its scenarios, and its status.
- `sessions/` numbering stays **global and continuous** — it does not reset per arc, and
  `canon-log.md` always cites the global session number.
- When time skips between arcs, `canon-log.md` gets an **Interlude** entry (see below) instead
  of a session entry.
- When an arc's threat is resolved, its `world/event-clock.md` is archived to
  `world/archive/event-clock-<arc-slug>.md` and a fresh live clock is built for the next arc's
  threat. The live path (`world/event-clock.md`) never changes, so no spec needs to know which
  arc is current.
- `world/` (locations, factions, NPCs-as-world-entities) is mutable current-state and is edited
  forward in place; history of how it got there lives in `canon-log.md`, not in `world/`.

**Forks → new sibling campaign folder, declare Lineage.** A parallel-world or diverging-canon
branch needs two mutually contradictory timelines to coexist, which one append-only log can't
hold.

- Create `campaigns/<slug>-<branch>/` as a **complete, standalone campaign** (full five-piece
  skeleton) — every generator works on it unmodified; nothing about it is special-cased.
- Its `CLAUDE.md` declares an optional **Lineage** field: `Forked from: <parent-slug> @ session
  <n> / <in-fiction date>`.
- Canon before the fork point is **read-only inherited**: generators may read the parent's
  `canon-log.md` up to session `<n>` for context, but **never write back to the parent** —
  everything that happens after the fork, including divergences, is recorded only in the
  branch's own `canon-log.md`.
- Shared entities are **copy-on-write**: while a branch's version of an NPC/location matches
  the parent, link to the parent's file instead of duplicating it; the moment the branch
  changes it, copy the file into the branch and mark its header
  `> Diverged from <parent path> @ <divergence point>`.
- Cross-world effects (an action in one branch affecting the other) are not a new mechanism —
  write them as ordinary triggers in each branch's own `world/event-clock.md`, with the
  condition referencing the other campaign's `canon-log.md`.
