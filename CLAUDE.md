# CLAUDE.md — CoC Keeper Kit

## Vision
A preparation workbench for a Call of Cthulhu **Keeper**. Turn a spark of an idea into
table-ready material — worlds, NPCs, Mythos entities, investigation puzzles, player
handouts, and read-aloud scene text — all mechanically correct for **Call of Cthulhu
7th Edition** and organized so nothing is lost between sessions.

## What this is / isn't
- **IS** a private authoring kit. Reusable canon, templates, and skills live at the root;
  each game you run lives in its own folder under `campaigns/`.
- **ISN'T** a rules SRD or a substitute for the published rulebooks. It references
  mechanics so generated content is correct; it does not reproduce copyrighted text.

## Ground rules for generated content
- **System: CoC 7th Edition.** Every stat block, skill value, and Sanity cost uses 7e.
  Read `reference/rules/` — or load the `coc-rules-reference` skill — before writing any
  stat block or setting a difficulty.
- **Era: per-campaign.** Templates are era-agnostic. Each campaign declares its era, tone,
  and content lines in its own `CLAUDE.md`; match that campaign's era when generating for it.
- **Language: English** for all content and scaffolding.
- **Fair play.** Every mystery must be solvable. Follow the three-clue rule; never gate
  forward progress behind a single die roll.
- **Spoiler hygiene.** Keeper-only secrets stay in Keeper files. Player-facing material
  (handouts, boxed read-aloud text) is clearly marked and self-contained — safe to print
  or hand over without leaking the solution.
- **Session-zero safety.** Respect each campaign's declared content lines/veils. Flag,
  don't silently include, extreme content.

## Layout
```
coc-keeper-kit/
├── CLAUDE.md                 ← this file — vision + house rules
├── README.md                 ← human quick-start
├── .claude/skills/           ← the authoring skills (auto-discovered)
├── reference/                ← shared, reusable canon across ALL campaigns
│   ├── rules/                ← 7e mechanics cheat-sheets (checks, sanity, combat)
│   ├── bestiary/             ← reusable monsters & Mythos entities
│   ├── mythos/               ← Great Old Ones, tomes, spells, cults, factions
│   └── tables/               ← random roll tables (names, madness, rumours, loot)
├── templates/                ← blank fill-in templates the skills produce
└── campaigns/
    ├── _template-campaign/   ← copy this to start a new game
    └── <your-campaign>/      ← one folder per campaign
```

## Skills (load with the Skill tool)
| Skill | Use it to |
|-------|-----------|
| `coc-rules-reference` | Look up 7e mechanics — difficulty, Sanity, combat, skill bases. **Load first** whenever writing a stat block or setting a check. |
| `build-world`         | Generate a setting, region, town, faction, or timeline. |
| `create-npc`          | Produce a full 7e NPC — stat block, personality, secret, roleplaying notes. |
| `create-monster`      | Stat a Mythos entity or monster — attacks, Sanity loss, special abilities. |
| `scene-description`   | Write read-aloud "boxed" text and sensory scene/location detail. |
| `create-puzzle`       | Design investigation puzzles, clues, and ciphers with fair, multi-path solutions. |
| `design-scenario`     | Structure a whole mystery — hook, spine, act structure, clue map. |
| `create-handout`      | Write player-facing props — letters, clippings, journal pages, reports. |

## Starting a new campaign
1. Copy `campaigns/_template-campaign/` → `campaigns/<slug>/`.
2. Fill in that campaign's `CLAUDE.md` (era, tone, premise, content lines, canon).
3. Generate material into its subfolders. Skills read the campaign `CLAUDE.md` for tone,
   and `reference/` + `templates/` for correctness and shape.

## Typical workflow
`design-scenario` (skeleton) → `build-world` (places) → `create-npc` / `create-monster`
(cast) → `create-puzzle` (obstacles) → `scene-description` + `create-handout` (table-ready
prose) → save into the campaign folder → prep per session in `sessions/`.

## Conventions
- One entity per file; name files `kebab-case.md`. Cross-link with relative Markdown links.
- Anything reusable across campaigns belongs in `reference/`, not inside a campaign.
- Mark Keeper-only sections with a `> **KEEPER ONLY**` blockquote so they never get printed
  onto a handout by mistake.
