#!/usr/bin/env python3
"""Roast Your Fridge entry: writes one roast line to /output/entry.txt.

The roast is built from two fragments: a SETUP that names the specific
detail — the ice maker groaning like a dying robot — and a PUNCH that
turns it into a joke in the last words: it drops two cubes as if it were
doing the owner a favour. The machine acts generous while producing
almost nothing.
"""

import os

MAX_CHARS = 200

# Setup: the specific, recognisable detail — the groaning ice maker.
SETUP = "My fridge's ice maker groans like a dying robot,"
# Punch: the twist — two cubes, delivered like a favour.
PUNCH = "then drops two cubes like it's doing me a favour."


def assemble():
    """Join the fragments into the single roast line."""
    return f"{SETUP} {PUNCH}"


def validate(text):
    """Gate: one line of 1-200 characters of UTF-8 text, not only whitespace."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not (1 <= len(text) <= MAX_CHARS):
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    text.encode("utf-8")
    return text


def main():
    text = validate(assemble())
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
