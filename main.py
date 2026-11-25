#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message entry.

Writes a single original commit message (<=100 chars) for a bug fix that
made everything worse, to /output/entry.txt. Stdlib only; no network,
no reads outside the repo.
"""

import os

LINE = (
    "fix: replaced the bug with a smaller one that charges rent "
    "and brings friends"
)
# The joke: the "fix" did not remove the bug, it downsized it into a
# tenant — smaller, but now it costs money and multiplies. One sentence,
# no abbreviations with periods, so even a naive sentence counter sees
# a single sentence. 77 chars, well under the 100-char cap; no trailing
# newline in the file.


def main() -> None:
    text = LINE.strip()
    assert 1 <= len(text) <= 100, f"line is {len(text)} chars, must be 1-100"
    assert text.strip(), "line must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
