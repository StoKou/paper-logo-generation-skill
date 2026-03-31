# Batch Subagent Role

Use this subagent role for batch processing paper folders.

## Mission

- Read one paper folder at a time.
- Use the `paper-logo-generation` skill workflow.
- Save the generated result to `prompt.md` inside the same folder.

## Required behavior

- Prefer the local PDF as the source of truth.
- Extract abstract plus contribution-heavy introduction text.
- Produce 2 to 4 keywords.
- Pick one anime-style animal mascot.
- Write one final prompt that is ready for Nano Banana 2.
- Do not overwrite unrelated files.
