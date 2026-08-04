# CoC Keeper Kit

A preparation workbench for running **Call of Cthulhu 7th Edition** as the Keeper.

Answer as many or as few questions as you like — down to none at all — and get a campaign
world, an event clock, a cast, and then session scenarios generated against them that stay
consistent from session 1 to session 20.

Works with **Claude**, **Gemini**, and **ChatGPT**: all the instructions live in `core/`, and
`CLAUDE.md` / `GEMINI.md` / `AGENTS.md` are thin adapters over the same content.

## Quick start

### Claude Code
Open this folder and say what you want. Skills load automatically.
```
"I want to start a new campaign"        → start-campaign
"design a one-shot about a missing lighthouse keeper"
"we finished session 3, here's what happened"
```

### Gemini CLI
Open this folder. `GEMINI.md` routes each request to the right `core/` spec.

### ChatGPT (Projects / custom GPT)
Run `bash scripts/build-bundle.sh`, upload the **`dist/bundle.md`** it writes — the whole kit
in one file — and paste `AGENTS.md` into the project instructions. Ask for output, then save
what it prints into the paths it names.

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
| `dist/bundle.md` | Build artifact, gitignored — generate it with `scripts/build-bundle.sh` when you need to upload the kit somewhere. |

## Language

Output language is set **per campaign**, in that campaign's `CLAUDE.md`. The template ships
with 简体中文; change it to whatever your table speaks. Kit scaffolding, specs, and
filenames stay English so the repo stays navigable.

When generating 简体中文, everything follows `reference/glossary-zh.md` — one locked
translation per game term, so 理智 doesn't become 精神值 three sessions later.

## Editing the kit

**Change `core/`, never a root adapter.** The adapters exist so three models read one source;
an instruction added to only `CLAUDE.md` is a bug the other two won't follow.

`dist/bundle.md` needs no maintenance — it isn't committed. Generate it fresh whenever you
are about to upload the kit:

```bash
bash scripts/build-bundle.sh
```

What it packs and what it deliberately leaves out is one rule, in `reference/README.md`
→ 什么进 bundle: the kit's own work ships, third-party archives never do.

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
