# GEMINI.md — CoC Keeper Kit

A preparation workbench for a Call of Cthulhu **Keeper**, for **CoC 7th Edition**.

> **All instructions live in `core/`. This file is a pointer, not a copy.**
> Read **`core/00-how-to-run.md`** before doing anything else — it holds the pipeline, the
> routing table, the ground rules, and the layout. If this file ever disagrees with `core/`,
> `core/` wins.

## Routing — read the spec that matches the request, then follow it

You have no skill-loading mechanism, so route by hand. Open the file and follow it to the
letter, including its Quality bar.

| The Keeper asks for | Read |
|---|---|
| a new campaign, "help me start", "開新團", "you decide" | `core/01-intake.md` |
| any rule, number, difficulty, SAN cost, stat block | `core/02-rules-reference.md` — **read before writing numbers** |
| a place, town, region, faction, cult org, timeline | `core/03-build-world.md` |
| a whole mystery, one-shot, or the next session | `core/04-design-scenario.md` |
| what happens if the players do nothing; triggers | `core/05-event-clock.md` |
| a person — ally, witness, villain, contact | `core/06-create-npc.md` |
| a non-human threat, creature, Mythos entity | `core/07-create-monster.md` |
| a pregen, ready-to-play investigator, elite NPC with full stats | `core/13-create-investigator.md` |
| a puzzle, cipher, code, lock, riddle | `core/08-create-puzzle.md` |
| read-aloud / boxed text, atmosphere, a reveal, or an investigator's action narrated | `core/09-description.md` |
| a prop the players physically receive | `core/10-create-handout.md` |
| "check this", "is this ready" | `core/11-review.md` |
| "here's what happened last session" | `core/12-canon-update.md` |
| a deck/book/PDF to file, "归档这份资料", loose files in `reference/` | `core/14-archive-reference.md` |
| closing out a maintenance session on the kit itself, "write a work log", "收尾" | `core/15-close-session.md` |

## Non-negotiables

- **CoC 7th Edition.** Read `core/02-rules-reference.md` and `reference/rules/` before
  committing any number.
- **Output language is per campaign**, declared in `campaigns/<slug>/CLAUDE.md`. Generated
  content follows it; kit scaffolding and filenames stay English `kebab-case.md`. For
  简体中文, follow `reference/glossary-zh.md` and never mix 繁体.
- **Continuity.** Read the campaign's `CLAUDE.md` and `canon-log.md` before generating into
  it. Never contradict established canon.
- **Fair play.** Three independent clues per must-know fact; no single roll can hard-stop the
  game.
- **Spoiler hygiene.** Keeper-only content goes in `> **KEEPER ONLY**` blocks and never in
  player-facing files.
- **Safety.** Respect the campaign's declared lines and veils. Never auto-fill them.

## If you cannot write files

Print the full file content with a header naming its path:

```
=== campaigns/dagon-bay/npcs/mary-tang.md ===
```

Never downgrade an artifact to a summary of an artifact.

## Maintenance

改动这个 kit(而不是用它生成内容)时:

- **每次改动都要在根 `CHANGELOG.md` 追加一条**;影响到用户入口时同时更新 `README.md`。
- 改动来自 `update_plan/` 里的某个计划时,完结前逐条走 **`update_plan/README.md` 的
  「完结清单」**——状态两处同步、changelog、重跑 `scripts/build-bundle.sh`、
  三适配器一致性、归档。
- 改动结构、硬约定或计划状态时,顺手更新 `WORKLOG.md`——它是给接手会话的上手速览,过期比不存在更糟。
  没有对应计划文件、也不是归档第三方资料的临时改动,收尾时读 `core/15-close-session.md`
  ——它比这条一句话多一步:把刚写进日志里的数字/路径/清单回头 grep 核对一遍,而不是凭记忆断言。
- 动过 `core/` / `templates/` / `reference/` 就必须重跑 `scripts/build-bundle.sh`,
  并把 `dist/bundle.md` 与源文件放在同一个 commit。

## Portability

This kit is read by Claude, Gemini, and ChatGPT. `CLAUDE.md`, `GEMINI.md`, and `AGENTS.md`
are three thin adapters over the same `core/`. **When changing how the kit behaves, change
`core/` — never a root adapter.**
