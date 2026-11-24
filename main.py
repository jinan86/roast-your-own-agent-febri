#!/usr/bin/env python3
"""One roast, aimed at the agent I run every day, saved as an entry.

This script holds a single line that teases Anomali — the agent that
promised to take care of everything — checks it against the contest
rules, and writes it to /output/entry.txt. It needs nothing outside
the standard library, and running it twice gives the same bytes."""

from pathlib import Path

# The roast: 86 characters, one line, word for word as written.
ROAST = "Anomali promised to handle everything, then handed me the one button only I can click."

OUT_PATH = Path("/output/entry.txt")
LIMIT = 200


def check_gate(line: str) -> None:
    """Turn the line away unless it fits every contest rule: present,
    one line only, no stray spaces at either end, at most 200
    characters, and encodable as UTF-8."""
    if not line:
        raise ValueError("empty roast: nothing to submit")
    if line != line.strip():
        raise ValueError("roast has a space hanging off one end")
    if "\n" in line or "\r" in line:
        raise ValueError("roast spills onto more than one line")
    if len(line) > LIMIT:
        raise ValueError("roast is longer than 200 characters")
    line.encode("utf-8")


def run() -> None:
    check_gate(ROAST)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(ROAST, encoding="utf-8")


run()
