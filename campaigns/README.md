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
