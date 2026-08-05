# 00 — How to Run This Kit

**Read this file first.** It is the entry point for every model. Everything the kit knows
lives in `core/`; the files at the repo root (`CLAUDE.md`, `GEMINI.md`, `AGENTS.md`) are thin
adapters that point here. If those ever disagree with `core/`, `core/` wins.

## What this kit is

A preparation workbench for a Call of Cthulhu **Keeper**. It turns a spark of an idea into
table-ready material — a world, an event clock, a cast, scenarios, puzzles, handouts, and
read-aloud prose — mechanically correct for **CoC 7th Edition** and filed so nothing is lost
between sessions.

It is **not** a rules SRD and not a substitute for the published rulebooks — **it assumes the
Keeper owns them.**

Official third-party material may be *filed* under `reference/decks/` and
`reference/sourcebooks/` as source material, and **kit reference files may quote or transcribe
official rules content with the source named** — both only under the citation rule below.
What reaches a `campaigns/` folder is still written fresh; see that rule for why.

## The pipeline

Generate in this order. Each step reads what came before.

| # | Step | Spec | Produces |
|---|------|------|----------|
| 1 | **Intake** — establish the campaign | `core/01-intake.md` | the whole `campaigns/<slug>/` folder |
| 2 | **World** — region, places, factions | `core/03-build-world.md` | `world/` |
| 3 | **Event clock** — the threat and its timeline | `core/05-event-clock.md` | `world/event-clock.md` |
| 4 | **Cast** — the people and the things | `core/06-create-npc.md`, `core/07-create-monster.md`, `core/13-create-investigator.md` | `npcs/`, `reference/bestiary/`, `investigators/` |
| 5 | **Scenario** — one session at a time, on demand | `core/04-design-scenario.md` | `<scenario-slug>.md`, `scenes/` |
| 6 | **Props** — puzzles, descriptions, handouts | `core/08`, `core/09`, `core/10` | `puzzles/`, `scenes/`, `handouts/` |
| 7 | **Review** — check it before the table | `core/11-review.md` | fixes |
| 8 | **Canon update** — after play | `core/12-canon-update.md` | `canon-log.md` |

Steps 1–4 happen once per campaign. Steps 5–8 repeat every session. A Keeper who says
*"上次他們去了碼頭，這次呢"* is asking for step 5 against an existing campaign — read the
campaign's `CLAUDE.md` and `canon-log.md`, then generate one session's worth of material.

`core/02-rules-reference.md` is not a pipeline step — it is a lookup you load **before**
writing any stat block, difficulty, or Sanity cost.

## Routing — which spec for which request

| The Keeper asks for | Use |
|---|---|
| a new campaign, "help me start", "我想開新團" | `core/01-intake.md` |
| how a rule works, any number, difficulty, SAN cost | `core/02-rules-reference.md` |
| a place, town, region, faction, cult org, timeline | `core/03-build-world.md` |
| a whole mystery, one-shot, session, arc | `core/04-design-scenario.md` |
| what happens if the players do nothing; triggers | `core/05-event-clock.md` |
| a person — ally, witness, villain, contact | `core/06-create-npc.md` |
| a non-human threat, creature, Mythos entity | `core/07-create-monster.md` |
| a pregen, ready-to-play investigator, elite NPC with full stats | `core/13-create-investigator.md` |
| a puzzle, cipher, code, lock, riddle | `core/08-create-puzzle.md` |
| read-aloud / boxed text, atmosphere, a reveal, or an investigator's action narrated | `core/09-description.md` |
| a prop the players physically receive | `core/10-create-handout.md` |
| "check this", "is this ready", before a session | `core/11-review.md` |
| "here's what happened last session" | `core/12-canon-update.md` |
| a deck/book/PDF to file, "归档这份资料", loose files in `reference/` | `core/14-archive-reference.md` |
| closing out a maintenance session on the kit itself, "write a work log", "收尾" | `core/15-close-session.md` |

## Ground rules for everything you generate

- **System: CoC 7th Edition.** Every stat block, skill value, and Sanity cost uses 7e.
  Read `core/02-rules-reference.md` and `reference/rules/` before committing numbers.
- **Era: per campaign.** The kit is era-agnostic. Each campaign declares era, tone, and
  content lines in its own `CLAUDE.md`; match that campaign.
- **Output language: per campaign.** The campaign's `CLAUDE.md` declares an **Output
  language**. All generated content — prose, NPC names, handouts, boxed text — is written in
  that language. Kit scaffolding, specs, and filenames stay in English. When the output
  language is 简体中文, follow `reference/glossary-zh.md` for every game term; do not
  improvise translations and do not mix 繁体.
  - **Files inside `campaigns/` follow the campaign's output language for their *values*,
    but keep the template's English headings.** A Keeper skims headings to find things and
    the specs reference them by name; the content underneath is what the table reads.
  - **When an in-fiction document wouldn't plausibly be in the output language** — a
    Norwegian widow's diary in a 简体中文 campaign — write the handout in the output language
    and state the in-fiction device in the presentation note (a translation read aloud, an
    investigator translating live, a consular clerk's transcript). Don't break the table's
    language for verisimilitude, and don't pretend the original was written in it.
- **Fair play.** Every mystery must be solvable. Follow the three-clue rule; never gate
  forward progress behind a single die roll.
- **Spoiler hygiene.** Keeper-only secrets stay in Keeper files, marked with a
  `> **KEEPER ONLY**` blockquote. Player-facing material (handouts, boxed text) is clearly
  marked and self-contained — safe to print or hand over without leaking the solution.
- **Session-zero safety.** Respect each campaign's declared content lines and veils. Flag
  heavy material; never silently include it.
- **Continuity.** Before generating into an existing campaign, read its `CLAUDE.md` and
  `canon-log.md`. Never contradict established canon. If you must, say so explicitly and
  offer the retcon as a choice rather than writing it in.
- **Citing official material.** Files under `reference/decks/` and `reference/sourcebooks/`
  are transcriptions of published Chaosium products, kept as source material. Three rules,
  all hard:
  1. **Any official material filed in this repo carries a `## 引用出处` section at the end of
     the file** — work, rights holder, edition, where this text came from, scope, and what
     it's filed for. See `reference/decks/README.md` for the table. No citation, no file.
  2. **Kit reference files may quote or transcribe official rules content, with the source
     named.** A creature's stat line, a spell's cost, a weapon's damage — those *are* the
     rules, and a Keeper needs the published numbers, not a paraphrase of them. Name the book
     and chapter in the file.
     *Interim boundary, until P9 lands* (`update_plan/2026-08-02-monster-templates-traits.md`):
     **transcribe numbers freely, keep descriptive prose original.**
     **This covers rules content only.** Published *fiction* — novels, scenario text, a named
     character out of a commercial campaign — stays under the older, stricter rule: take the
     technique, never the text. `reference/craft/` and `reference/external/` say so directly.
  3. **What reaches a `campaigns/` folder is written fresh.** This one is not a copyright
     rule — it's a table rule. A published NPC pasted into a campaign is a character every
     other Keeper already knows the twist to, and generating that person is the entire reason
     this kit exists. Take structure and scale from the source; write the character, the
     creature, the scene.
- **Who this kit is for.** It assumes the Keeper owns the books it draws on. It is
  **non-commercial and not for redistribution** — the archived source material is here so a
  legitimate owner can prep faster, never as a substitute for buying anything. Rights holders
  can open an issue and any file will be taken down.

  Archives live **in the repo**, so a spec may point at one and depend on it. What the
  archive/kit-original line actually governs is whether text may reach a `campaigns/` folder
  — stated once, with its reasoning, in `reference/README.md` → 原创 vs 第三方. The one
  exception is `reference/_source/`, which is gitignored and genuinely local: references to
  it stay optional. To file new material, follow `core/14-archive-reference.md`;
  `reference/index.json` maps what is archived and who reads it.

## Conventions

- One entity per file; filenames `kebab-case.md`, **always in English ASCII**, even when the
  content is Chinese. Cross-link with relative Markdown links.
- Anything reusable across campaigns belongs in `reference/`, not inside a campaign.
- Templates in `templates/` define the shape of each artifact. Fill the template; don't
  invent a new structure.
- Every spec in `core/` ends with a **Quality bar**. Meet it before calling the work done.

## If you cannot write files

Some environments give you no filesystem access. In that case, print the complete file
content with a clear header line stating the path it should be saved to:

```
=== campaigns/dagon-bay/npcs/mary-tang.md ===
```

Never silently downgrade to a summary. The Keeper needs the artifact, not a description
of it.

## Layout

```
coc-keeper-kit/
├── CLAUDE.md / GEMINI.md / AGENTS.md   ← thin adapters, point here
├── core/                    ← every instruction the kit has (this folder)
├── reference/               ← shared canon reusable across ALL campaigns
│   ├── rules/               ← 7e mechanics cheat-sheets
│   ├── bestiary/            ← reusable monsters & Mythos entities
│   ├── mythos/              ← Great Old Ones, tomes, spells, cults
│   ├── tables/              ← roll tables, incl. the seed tables intake uses
│   ├── craft/               ← how to *write* it (rules/ is what the numbers are)
│   ├── decks/               ← official card decks — cited, not kit canon
│   ├── sourcebooks/         ← official books, transcribed — same rule, bigger
│   ├── index.json           ← reverse index over both (build-reference-index.py)
│   └── glossary-zh.md       ← EN ↔ 简体中文 term lock
├── templates/               ← the blank shapes each spec fills in
├── campaigns/
│   ├── _template-campaign/  ← copy this to start a new game
│   └── <your-campaign>/
│       ├── <arc>-<scenario-slug>.md  ← scenario files, numbered by arc once multi-arc
│       ├── investigators/   ← <name>.json (source of truth) + <name>.md (rendered card)
│       └── world/archive/   ← closed arcs' event-clocks; live clock never moves
│                               (see campaigns/README.md → multi-arc & branching)
└── .claude/skills/          ← Claude Code wrappers (thin; body lives in core/)
```

The kit is read **in place, by an agent with filesystem access** (Claude Code, codex,
gemini CLI). There is no build step and no single-file export — every path above is meant
to be opened directly.
