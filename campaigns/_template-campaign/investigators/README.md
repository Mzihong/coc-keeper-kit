# investigators/

Pregens and mechanically-full elite NPCs, built with the `create-investigator` skill from
`core/13-create-investigator.md`. One person per name: `<name>.json` (source of truth,
validated against `templates/investigator.schema.json`) plus `<name>.md` (rendered card, via
`scripts/render-investigator.py` or written directly from the JSON). Optional `roster.csv`
indexes name/occupation/status — always derived, never the source of truth.
