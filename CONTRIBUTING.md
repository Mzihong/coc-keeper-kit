# Contributing

Thanks for your interest! This is a Keeper's preparation kit for **Call of Cthulhu 7th
Edition** — a set of Claude Code skills, fill-in templates, and reference cheat-sheets. It is
unofficial fan tooling (see the disclaimer in the [README](README.md)).

## What's welcome
- New or improved **skills** under `.claude/skills/<name>/SKILL.md`.
- New **templates** under `templates/`.
- **Reference** entries: rules cheat-sheets, generic bestiary creatures, Mythos lore, or
  random tables under `reference/`.
- Fixes to mechanics accuracy, wording, or structure.

## Ground rules
- **Reproduce no copyrighted text.** Reference mechanics in your own words; never paste
  passages from Chaosium's rulebooks or published scenarios.
- **7th Edition mechanics** for anything with stats — see `reference/rules/`.
- **Keep content generic** in `reference/` (no one campaign's plot); campaign-specific
  material stays in `campaigns/`.
- **Player-safe discipline:** handout files carry no answers; keeper secrets live in
  `> **KEEPER ONLY**` blocks.
- **English**, Markdown, one entity per file, `kebab-case.md` filenames.

## How to propose a change
1. Fork and branch (`feature/<short-name>`).
2. Make the change; keep skills consistent with the existing format (frontmatter: `name`,
   `description`, `version`).
3. Open a pull request describing what it adds and why it's mechanically sound.

By contributing you agree your contributions are licensed under the repository's
[MIT License](LICENSE).
