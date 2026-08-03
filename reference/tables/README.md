# tables/ — random tables

Roll tables for prep and live improv. Keep them era-agnostic where possible; put era-specific
tables in the campaign that needs them.

Format: a short intro (what to roll and when), then a table with a `dN` column and results.

## Seed tables — the anti-generic layer

These four are **not optional flavour**. `core/01-intake.md` requires them whenever the Keeper
gives little or no input. Without rolling, every model converges on the same campaign: Arkham,
a cult, a Great Old One stirring. Rolling and *keeping the result* is what makes a low-context
campaign specific.

- `hooks.md` (1d20) — how the investigators get pulled in.
- `locations.md` (1d20) — where it happens; breaks the default fishing-village gravity.
- `mythos-angles.md` (1d20) — what the wrongness actually is. The most important one.
- `npc-quirks.md` (1d20) — the tell that makes an NPC playable.

## Prep & play tables

- `complications.md` (1d20) — what goes sideways in a session; roll twice at session prep.
- `madness.md` (1D10) — bout-of-madness effects.
- `npc-appearance.md` (1d20) — first physical impression + temperament; companion to
  `npc-quirks.md` (appearance vs. mannerism).
- `cult-goals.md` (1D10 × 1D8) — a cult's want × its means; roll both, they multiply. See
  `reference/craft/cult-design-zh.md` §三.
- `cult-leader-positions.md` (1d10) — a cult leader's social front and the access it buys.
- `cult-power-sources.md` (1d4) — where a cult's claimed supernatural backing comes from.
- `cultist-archetypes.md` — 12 ready-to-use rank-and-file cultist stat blocks (grouped by
  role, not a die table) plus an Immortal Master toolkit. Companion to `create-npc`; see
  `core/06-create-npc.md`.

## Adding tables

One subject per file, `kebab-case.md`. State the die and when to roll it in the first two
lines. Prefer 20 concrete entries over 100 vague ones — a table you actually read beats a
table you skim.

Ideas: `rumours.md`, `investigator-names.md`, `weird-details.md`,
`what-the-cultist-carries.md`, `sounds-in-the-dark.md`.
