# Project Meta

## Goal

Build a reusable `paper-logo-generation` skill that reads a paper and produces a Nano Banana 2-ready logo prompt.

## Core workflow

1. Read the paper abstract.
2. Read contribution-heavy text from the introduction.
3. Extract 2 to 4 keywords.
4. Map the paper to an anime-style animal mascot.
5. Output a direct image prompt.

## Important files

- `SKILL.md`: skill definition and workflow
- `style.md`: prompt styling rules
- `references/prompt-template.md`: output format reference
- `agents/openai.yaml`: default subagent-facing metadata
- `agents/paper-logo-batch-subagent.md`: batch subagent role instructions

## Batch target

- Source folders: `/root/sk/code/collect-paper-logo/papers-logo/*`
- Output file per folder: `prompt.md`

## Git target

- Repository: `https://github.com/StoKou/paper-logo-generation-skill.git`
- Default branch: `main`

## Safety note

GitHub access credentials were supplied in the task context, but they are intentionally not persisted into repository files. Use them only at push time.

## Future improvements

- Improve keyword extraction with section-aware parsing for papers that use nonstandard headings.
- Add a richer domain-to-mascot map for biotech, security, math, and systems papers.
- Add prompt variants for minimalist logo, emblem badge, and launch-poster mascot.
- Add optional support for reading title and abstract from paper URLs directly.
- Add regression examples to validate prompt quality across paper domains.
