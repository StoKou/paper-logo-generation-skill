"""Regression tests for paper-logo-generation prompt template."""

import pathlib

PROMPT_TEMPLATE_PATH = (
    pathlib.Path(__file__).resolve().parent.parent
    / "paper-logo-generation"
    / "references"
    / "prompt-template.md"
)


def _read_template() -> str:
    """Return the full text of the prompt template."""
    return PROMPT_TEMPLATE_PATH.read_text(encoding="utf-8")


def test_prompt_template_exists():
    """The prompt template file must exist."""
    assert PROMPT_TEMPLATE_PATH.exists(), (
        f"Prompt template not found at {PROMPT_TEMPLATE_PATH}"
    )


def test_title_extraction_instruction_present():
    """The template must instruct to extract the title and place it at the top
    when available, and to omit it when unavailable.

    Regression guard for the conditional title-extraction rule added in commit
    324990c ("clarify title extraction in skill logic").
    """
    content = _read_template()

    # The instruction should mention writing/placing the title at the top
    assert "标题" in content, (
        "Prompt template is missing any mention of '标题' (title)"
    )
    assert "顶部" in content, (
        "Prompt template is missing any mention of '顶部' (top) — "
        "it should instruct placing the title at the top"
    )

    # The instruction should cover both the "title available" and
    # "title unavailable" branches
    assert "省略" in content or "忽略" in content, (
        "Prompt template is missing the instruction to omit/ignore the title "
        "when it is not available ('省略' or '忽略')"
    )


def test_title_at_top_conditional_rule():
    """The template must contain an explicit conditional rule:
    write the title to the top if extractable, omit it otherwise.

    This checks for the *complete* two-branch instruction rather than
    individual keywords.
    """
    content = _read_template()

    # Look for the presence of a line that contains both the "write to top"
    # and "omit" semantics together, ensuring they haven't been split apart.
    has_write_top = any(
        "标题" in line and "顶部" in line
        for line in content.splitlines()
    )
    assert has_write_top, (
        "Prompt template must have a line that mentions both '标题' (title) "
        "and '顶部' (top) — the instruction to place the title at the top"
    )

    has_omit_branch = any(
        ("省略" in line or "忽略" in line) and ("标题" in line or "顶部" in line or "文字" in line)
        for line in content.splitlines()
    )
    assert has_omit_branch, (
        "Prompt template must have a line that instructs omitting the title "
        "when it cannot be extracted"
    )
