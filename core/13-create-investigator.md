# 13 — Create Investigator

Build a player investigator — usually a **pregen** for a one-shot or a new player, sometimes an
**elite NPC** (a named cultist, a rival investigator) reusing the same mechanical skeleton.
The JSON record is the source of truth; the Markdown card is a rendered view for the table.

## First

- **Read `reference/rules/character-creation.md`** before rolling anything.
- Read the campaign `CLAUDE.md` for era, tone, and premise — every surviving backstory hook
  must tie into it; a hook that connects to nothing in the campaign is decoration, not prep.
- Use `templates/investigator.schema.json` (data) and `templates/investigator.md` (view).

## Build in this order

1. **Concept.** One line: who they are, what they want out of this case.
2. **Occupation.** Pick or invent one; it sets the occupation skill list, the point split, and
   the Credit Rating band.
3. **Numbers.** Roll or assign characteristics; derive HP/MP/SAN/Luck/Move/Build/Damage
   Bonus/Dodge; spend occupation and personal-interest skill points. Recompute — don't eyeball.
4. **Backstory hooks.** Fill every 7e backstory prompt (ideology, significant people,
   locations, possessions, traits), then keep only the ones that could plausibly matter to
   this campaign — cut the rest rather than pad the file. Each surviving hook should point at
   something the Keeper can actually pull on: an NPC, a faction, a location, or the central
   mystery.

## Storage

- **Source of truth:** `campaigns/<slug>/investigators/<name>.json`, validated against
  `templates/investigator.schema.json`.
- **Rendered view:** `campaigns/<slug>/investigators/<name>.md` — generate it with
  `scripts/render-investigator.py`, or write it directly from the JSON. The two must never
  disagree; regenerate the `.md` whenever the `.json` changes.
- An optional `campaigns/<slug>/investigators/roster.csv` can index name/occupation/status for
  a quick glance at the table; it is always derived, never the source of truth.

## Pregens vs. elite NPCs

Elite cultists or other mechanically-full villains (`core/06-create-npc.md` NPCs who need
complete stats) may use this schema instead of a lighter NPC stat block — set
`"type": "elite-npc"` in the JSON and skip the player-facing backstory-hooks section.

## Output

- Write prose fields in the campaign's declared **output language**. Stat notation (`STR 60`,
  skill percentages) stays English per `core/02-rules-reference.md`.

## Quality bar

- The JSON validates against `templates/investigator.schema.json`.
- Every derived stat traces back correctly to the rolled characteristics
  (`reference/rules/character-creation.md`) — recompute, don't eyeball.
- Skill points spent match the EDU×4 / INT×2 (or occupation-split) formula.
- Every surviving backstory hook ties into something the campaign can actually use.
- The `.md` view and the `.json` source agree; no stat appears in one but not the other.
