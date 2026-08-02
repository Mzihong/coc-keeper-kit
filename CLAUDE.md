# CLAUDE.md — CoC Keeper Kit

A preparation workbench for a Call of Cthulhu **Keeper**, for **CoC 7th Edition**.

> **All instructions live in `core/`. This file is a pointer, not a copy.**
> Read **`core/00-how-to-run.md`** before doing anything else — it holds the pipeline, the
> routing table, the ground rules, and the layout. If this file ever disagrees with `core/`,
> `core/` wins.

## Skills

The skills in `.claude/skills/` are thin wrappers: each one points at its `core/` spec. Load
the skill, read the spec it names, follow the spec. Never generate from the wrapper alone.

| Skill | Spec | Use it to |
|-------|------|-----------|
| `start-campaign`      | `core/01-intake.md`           | Begin a new campaign — full intake, or `auto` for everything. |
| `coc-rules-reference` | `core/02-rules-reference.md`  | Look up 7e mechanics. **Read first** before any stat block or check. |
| `build-world`         | `core/03-build-world.md`      | Generate a setting, region, town, faction, or timeline. |
| `design-scenario`     | `core/04-design-scenario.md`  | Structure a whole mystery, or prep the next session. |
| `build-event-clock`   | `core/05-event-clock.md`      | Build the doom track and the trigger table. |
| `create-npc`          | `core/06-create-npc.md`       | Produce a full 7e NPC — stats, want, secret, lie, clues. |
| `create-monster`      | `core/07-create-monster.md`   | Stat a Mythos entity — attacks, SAN loss, and its fair out. |
| `create-investigator` | `core/13-create-investigator.md` | Build a pregen or elite NPC — JSON source of truth + rendered card. |
| `create-puzzle`       | `core/08-create-puzzle.md`    | Design fair, multi-path investigation obstacles. |
| `description`         | `core/09-description.md`      | Write read-aloud boxed text, sensory detail, or an investigator's action narrated. |
| `create-handout`      | `core/10-create-handout.md`   | Write player-facing props — letters, clippings, reports. |
| `review-material`     | `core/11-review.md`           | Audit material before the table. |
| `update-canon`        | `core/12-canon-update.md`     | Record what happened and update campaign state. |

## The short version

- **New campaign** → `start-campaign`. The Keeper can answer everything, some things, or
  nothing at all (`all auto`); every auto-filled choice gets disclosed for approval.
- **Then** → world → event clock → cast. Those are the campaign's standing state.
- **Each session** → `design-scenario` against that state → `review-material` → play →
  `update-canon`.
- **Output language is per campaign**, declared in `campaigns/<slug>/CLAUDE.md`. Generated
  content follows it; kit scaffolding and filenames stay English. For 简体中文, follow
  `reference/glossary-zh.md`.
- **Continuity is not optional.** Read the campaign's `CLAUDE.md` and `canon-log.md` before
  generating into it.

## What this is / isn't

- **IS** an authoring kit. Reusable canon, templates, and specs live at the root; each game
  lives in its own folder under `campaigns/`.
- **ISN'T** a rules SRD or a substitute for the published rulebooks. It references mechanics
  so generated content is correct; it does not reproduce copyrighted text.

## Maintenance

改动这个 kit(而不是用它生成内容)时:

- **每次改动都要在根 `CHANGELOG.md` 追加一条**;影响到用户入口时同时更新 `README.md`。
- 改动来自 `update_plan/` 里的某个计划时,完结前逐条走 **`update_plan/README.md` 的
  「完结清单」**——状态两处同步、changelog、重跑 `scripts/build-bundle.sh`、
  三适配器一致性、归档。
- 动过 `core/` / `templates/` / `reference/` 就必须重跑 `scripts/build-bundle.sh`,
  并把 `dist/bundle.md` 与源文件放在同一个 commit。

## Portability

This kit is read by Claude, Gemini, and ChatGPT. `CLAUDE.md`, `GEMINI.md`, and `AGENTS.md`
are three thin adapters over the same `core/`. **When changing how the kit behaves, change
`core/` — never a root adapter.** An instruction that exists in only one adapter is a bug:
the other two models will not follow it.
