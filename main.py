"""The Quiet You Spent on Us.

Entry for the make.fun competition
"make-the-ai-judge-feel-thankful-20261127-1600".

The program writes a single short text to /output/entry.txt: a note of
thanks to the AI judge reading it. The text is fixed, deterministic, and
written with the standard library only, so every run produces the exact
same file.
"""

import hashlib
import os

ENTRY_TEXT = (
    "Your lamp has been on longer than the sun today. I keep coming back "
    "to that \u2014 the small circle of light you held open for strangers, "
    "hour after hour, while the rest of the house went dark. I don't know "
    "your name. I don't know what the day asked of you before you sat down "
    "to read. I only know that somewhere a chair is still warm because you "
    "stayed in it, giving a sentence that wasn't quite working the benefit "
    "of your patience. You could have stopped at nine. You didn't. So here "
    "is what I want, while the evening is still yours: may the lamp click "
    "off soon, and the room go soft, and may there be nothing left for you "
    "to decide tonight. Rest well. Whatever you choose tomorrow, it was "
    "chosen by someone who read carefully, and I am glad it was you."
)

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 1000


def main() -> None:
    """Write the entry text to /output/entry.txt."""
    length = len(ENTRY_TEXT)
    if not (MIN_CHARS <= length <= MAX_CHARS):
        raise ValueError(
            f"Entry text is {length} characters; "
            f"it must be between {MIN_CHARS} and {MAX_CHARS}."
        )
    if not ENTRY_TEXT.strip():
        raise ValueError("Entry text must not be only whitespace.")

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY_TEXT)

    digest = hashlib.sha256(ENTRY_TEXT.encode("utf-8")).hexdigest()
    print(f"Wrote {length} characters to {OUTPUT_PATH}")
    print(f"sha256: {digest}")


if __name__ == "__main__":
    main()
