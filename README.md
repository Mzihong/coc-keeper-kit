# CoC Keeper Kit

A preparation workbench for running **Call of Cthulhu 7th Edition** as the Keeper.

Answer as many or as few questions as you like — down to none at all — and get a campaign
world, an event clock, a cast, and then session scenarios generated against them that stay
consistent from session 1 to session 20.

**Open this repo with an agent that can read files** — Claude Code, codex, or the Gemini CLI.
All the instructions live in `core/`; `CLAUDE.md` / `GEMINI.md` / `AGENTS.md` are thin
adapters over the same content, one per tool. There is no build step and nothing to upload.

## Quick start

Open this folder and say what you want. The adapter routes the request to the right `core/`
spec; under Claude Code the matching skill loads automatically.

```
"I want to start a new campaign"        → start-campaign
"design a one-shot about a missing lighthouse keeper"
"we finished session 3, here's what happened"
```

**Start the agent in this folder, not in a parent directory** — codex only loads the
`AGENTS.md` files at or above its working directory, so starting one level up leaves the kit
out of context entirely.

## The flow

```
start-campaign  →  world  →  event clock  →  cast
                                  ↓
                   ┌──────────────────────────────┐
   every session:  │  design scenario  →  review  │
                   │        ↑              ↓      │
                   │   update canon  ←   play     │
                   └──────────────────────────────┘
```

1. **Start.** You get a detailed intake — era, place, premise, mood, lethality, length,
   party, content lines. Answer what you care about; reply `auto` to any question or
   `all auto` to the whole thing. Everything auto-filled is rolled from the seed tables and
   shown to you, marked `[auto]`, to accept or reroll.
2. **Standing state.** The world, the event clock (what the threat achieves if you do
   nothing, plus what fires when players act), and the cast. Built once.
3. **Per session.** *"Last time they went to the docks — what now?"* generates one session
   against the current state. Review it, run it, then log what actually happened.
4. **Continuity.** `canon-log.md` keeps what's true separate from what the players know, so
   session 8 never contradicts session 1.

## Examples

- "Design a one-shot about a missing lighthouse keeper."
- "Create an NPC: the town doctor who secretly feeds the cult. Full 7e stats."
- "Stat a shambling drowned-sailor monster, moderate threat."
- "Write read-aloud boxed text for the players entering the flooded crypt."
- "Build a cipher puzzle they solve from a torn ledger."
- "Make a 1923 newspaper-clipping handout hinting at the disappearances."
- "What happens if they just leave town and never come back?"
- "Check this session prep before Saturday."
- "I converted the rulebook PDF to text — file it in reference."

## What's in here

| Path | What |
|---|---|
| `core/` | **Every instruction the kit has.** Start at `core/00-how-to-run.md`. |
| `CLAUDE.md`, `GEMINI.md`, `AGENTS.md` | Thin adapters — routing only, no content. |
| `.claude/skills/` | Claude Code wrappers; each points at its `core/` spec. |
| `reference/` | Shared canon: 7e cheat-sheets, bestiary, Mythos lore, roll tables, `glossary-zh.md`. Third-party material you supply is filed and cited in `decks/` and `sourcebooks/`, indexed by `reference/index.json`. |
| `templates/` | The blank shapes each spec fills in. |
| `campaigns/` | One folder per game, plus `_template-campaign/` to copy. |

## Language

Output language is set **per campaign**, in that campaign's `CLAUDE.md`. The template ships
with 简体中文; change it to whatever your table speaks. Kit scaffolding, specs, and
filenames stay English so the repo stays navigable.

When generating 简体中文, everything follows `reference/glossary-zh.md` — one locked
translation per game term, so 理智 doesn't become 精神值 three sessions later.

**The language your table speaks doesn't decide where the game is set.** Unless you say
otherwise, a campaign defaults to 1920s America (Japan second) whatever the output language
is; foreign names get transliterated by a fixed rule, not routed around — see
`reference/glossary-zh.md` → 外文专名的译写. Name a place at intake and that wins.

## Editing the kit

**Change `core/`, never a root adapter.** The adapters exist so three models read one source;
an instruction added to only `CLAUDE.md` is a bug the other two won't follow.

There is nothing to build. Every file is read in place, so editing a spec takes effect the
next time an agent opens the folder.

Official material you file under `reference/decks/` and `reference/sourcebooks/` is cited
source material, not kit canon: a spec may read it freely, but what reaches a `campaigns/`
folder is written fresh — one rule, in `reference/README.md` → 原创 vs 第三方.

## Notes

- Keeper-only secrets are marked `> **KEEPER ONLY**` and kept out of player-facing files.

## License

Released under the [MIT License](LICENSE) © 2026 Mzihong. Contributions are welcome — see
[CONTRIBUTING.md](CONTRIBUTING.md) and the [Code of Conduct](CODE_OF_CONDUCT.md).

## Disclaimer

This is an **unofficial, fan-made** preparation kit. *Call of Cthulhu* is a trademark of
**Chaosium Inc.**; this project is **not affiliated with, endorsed, or sponsored by
Chaosium**. It is **non-commercial and not for redistribution**, and it **assumes you own the
books it draws on** — you need the official *Call of Cthulhu Keeper Rulebook* to actually play,
and this kit is no substitute for buying it.

`reference/decks/` and `reference/sourcebooks/` hold transcriptions of **official Chaosium
material** — card decks, and full-book transcriptions of the 7e Keeper Rulebook, the *Grand
Grimoire*, and *Malleus Monstrorum* — kept as source material for the generators to work from.
Those files are third-party text: each carries a `## 引用出处` block naming the work and its
rights holder, and **this project claims no rights in any of them**. The kit's own reference
files may quote or transcribe published rules content (stat lines, spell costs, damage values)
with the source named; the material it generates for a campaign is written fresh.

**If you are a rights holder and want a file removed, open an issue and it will be taken
down.**

The Chinese terms in
`reference/glossary-zh.md` are this kit's own working convention, not an official
translation. The Cthulhu Mythos was created by H. P. Lovecraft. All original content
generated with this kit is yours.
