---
name: paper-logo-generation
description: Generate a polished image prompt for a paper logo from a research paper PDF or paper URL. Use this when the user wants a paper-specific logo concept, mascot direction, or Nano Banana 2 prompt for a paper, technical report, or project paper. The workflow reads the paper abstract and core contributions, extracts 2-4 keywords, selects an anime-style animal mascot, and returns a ready-to-use image prompt.
---

# Paper Logo Generation

Use this skill when the user provides a paper PDF, arXiv link, Hugging Face paper link, or a local folder containing a paper PDF and wants a logo-generation prompt.

Read [style.md](./style.md) before drafting the final prompt.

## Workflow

1. Read the paper's abstract.
2. Read the contribution-heavy part of the introduction or summary section.
3. Distill the paper into 2 to 4 concrete keywords.
4. Choose one anime-animal mascot that best matches the domain and contribution.
5. Build one final image prompt that can be pasted directly into Nano Banana 2.

## Output requirements

The output should contain:

- `Title`
- `Keywords`
- `Mascot`
- `Prompt`

## Decision rules

- Prefer the abstract and explicit contribution statements over the rest of the paper.
- Keywords should be technical and visualizable, not vague marketing words.
- The mascot should fit the paper's role:
  - coding and reasoning: fox, owl, raven, raccoon
  - research and planning: raven, crane, wolf
  - audio and speech: dolphin, nightingale, whale
  - robotics and control: octopus, falcon, beetle, wolf
  - motion and video: cheetah, swallow, panther
  - vision and OCR: hawk, lynx, mantis, cat
- The prompt should describe a logo-like single-subject composition, not a full poster scene.
- Always include negative constraints: no text, no watermark, no UI, no multi-panel layout.

## Folder-based usage

If the user points to a paper folder:

1. Find the PDF in that folder.
2. Extract the paper title, abstract, and contribution clues.
3. Generate the prompt.
4. Save the result as `prompt.md` in the same folder.

## Bundled resources

- Prompt structure and phrasing guidance: [references/prompt-template.md](./references/prompt-template.md)
- Batch subagent configuration: [agents/paper-logo-batch-subagent.md](./agents/paper-logo-batch-subagent.md)
- UI-facing metadata: [agents/openai.yaml](./agents/openai.yaml)
