#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry.

Writes one line roasting my own agent (Anomali / Muse) to
/output/entry.txt. Deterministic, stdlib only, no network, no clock,
no randomness.
"""

import os

ROAST = (
    "Anomali promised to handle everything, "
    "then handed me the one button only I can click."
)


def validate(text: str) -> None:
    """Enforce the competition gate before writing: UTF-8, 1-200 chars,
    not only whitespace, exactly one line."""
    if not text or text != text.strip() or "\n" in text:
        raise ValueError("roast must be a single non-empty line")
    if len(text) > 200:
        raise ValueError("roast exceeds 200 characters")
    if not text.strip():
        raise ValueError("roast must not be only whitespace")
    text.encode("utf-8")


def main() -> None:
    validate(ROAST)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
