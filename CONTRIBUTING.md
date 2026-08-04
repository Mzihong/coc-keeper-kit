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
- **Nothing you write into `campaigns/` is copied from a published product.** The characters,
  creatures, and scenes a campaign gets are generated — that is the whole point of the kit,
  and a pasted-in published NPC is one every other Keeper already knows the twist to.
- **Reference files under `reference/` may quote or transcribe official rules content**
  (a stat line, a spell cost, a damage value) **as long as the source is named in the file.**
  Those are the rules; a Keeper needs the published numbers, not a paraphrase. Interim
  boundary until P9 lands: transcribe numbers freely, keep descriptive prose original.
- **Official source material goes in `reference/decks/` or `reference/sourcebooks/`, and only
  with a citation.** Every such file ends with a `## 引用出处` block naming the work, rights
  holder, edition, where the text came from, its scope, and what it's filed for
  (`reference/decks/README.md` has the table). **No citation, no merge.**
- **This project is non-commercial and not for redistribution**, and it assumes its users own
  the books it draws on. Don't contribute material that would change that.
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
