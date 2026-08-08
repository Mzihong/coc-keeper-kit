# npcs/

The people the investigators meet in this campaign. Built with the `create-npc` skill from
`templates/npc.md`. One NPC per file, `kebab-case.md`. Keep each character's secret in its
`> **KEEPER ONLY**` block.

**After each session, every NPC the party actually dealt with gets updated** — overwrite the
current attitude and append one line to the `> **KEEPER ONLY — Interaction history**` log
(facts and relationship changes only; the narration already lives in `canon-log.md`, so
cross-link the session number instead of repeating it). This is a required step of
`core/12-canon-update.md`, not an optional one — it's what keeps "does this NPC trust them?"
answerable from the NPC's own file.
