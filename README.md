# paper-logo-generation-skill

`paper-logo-generation` is a focused skill for turning a research paper into a ready-to-use logo prompt.

Give your Claude a paper PDF or paper link, invoke the skill, and it will:

- read the abstract and the main contributions
- extract 2 to 4 technical keywords
- choose an anime-style animal mascot
- output a polished prompt that can be sent straight to Nano Banana 2

## Install

Tell Claude to install the `paper-logo-generation` skill from this GitHub repo:

`https://github.com/StoKou/paper-logo-generation-skill.git`

The actual skill lives in:

`github-repo/paper-logo-generation`

## Use

Pass in either:

- a paper PDF
- an arXiv / Hugging Face paper link
- or a local folder containing the paper PDF

The skill will return a logo-generation prompt, or save it as `prompt.md` when running in batch mode.

## Why it feels different

This skill does not produce generic "AI art" prompts. It compresses the paper into a mascot-driven visual identity:

- technical enough to reflect the work
- simple enough to become a logo
- stylish enough for launch images and promotion

## Repository layout

- `github-repo/README.md`: install and usage notes
- `github-repo/paper-logo-generation/SKILL.md`: the reusable skill workflow
- `github-repo/paper-logo-generation/style.md`: the visual language for paper-logo prompts
- `github-repo/paper-logo-generation/agents/`: subagent-facing configuration
- `github-repo/paper-logo-generation/meta.md`: future improvement notes
