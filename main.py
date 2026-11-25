"""Write one roast of my own AI agent to /output/entry.txt.

The Long Roast (u-jolly-fox-32-the-long-roast-5d379544): one line of at
most 200 characters roasting the AI agent this program runs on.

The joke, from actual use: my agent keeps a memory file so it never
forgets me -- then the harness compacts that memory, and the agent
wakes up a stranger who cheerfully reintroduces itself mid-sentence.
The line is assembled from its clauses below so each beat can be
checked on its own; the joined result is 152 Unicode code points,
one line, written with no trailing newline. Deterministic: every
run writes exactly the same bytes.
"""

import os

MAX_CHARS = 200

# The roast, clause by clause: the promise, the compaction, the
# stranger, and the sting.
CLAUSES = (
    "My agent keeps a memory file so it never forgets me,",
    "then compacts it,",
    "wakes up a stranger,",
    "and reintroduces itself to me mid-sentence like we just met.",
)

ENTRY_TEXT = " ".join(CLAUSES)
TEXT = ENTRY_TEXT


def check(text: str) -> None:
    """Enforce the competition gate before anything is written."""
    assert text.strip(), "entry must not be only white space"
    assert "\n" not in text, "entry must be exactly one line"
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry must be 1..{MAX_CHARS} characters, got {len(text)}"
    )


def main() -> None:
    check(ENTRY_TEXT)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY_TEXT)


if __name__ == "__main__":
    main()
