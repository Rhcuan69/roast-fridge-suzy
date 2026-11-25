"""Roast Your Fridge: write one roast line to /output/entry.txt.

Pure Python stdlib, deterministic, no network access.
The line is a single line of at most 200 characters, no trailing newline.
"""

import os

# One original roast line: a specific fridge detail (the all-night hum),
# a twist that pays off in the last few words (bodyguard -> pickles).
LINE = (
    "My fridge hums all night like a bodyguard, "
    "but the only treasure it has ever protected "
    "is a jar of pickles from 2019."
)


def build_entry():
    """Return the entry text, checked against the gate's own rules."""
    text = LINE.strip()
    if not text or len(text) > 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return text


def main():
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(build_entry())


if __name__ == "__main__":
    main()
