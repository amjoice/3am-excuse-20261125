#!/usr/bin/env python3
"""The 3 AM Excuse - a hardware wallet's refusal, in one line.

The wallet will not sign at 3 AM: in the dark it cannot tell its owner
from a thief, a bot, or the owner on a third espresso. Pure stdlib,
deterministic, no network, no secrets; writes a single line under 200 chars.
"""
import os

# The excuse, assembled from its two halves so the wording stays in one place.
_OPENING = "At 3 AM I can't tell you from a thief, a bot, or you on your third espresso"
_CLOSING = "so I sign nothing until the sun can vouch for you."
_DASH = "\u2014"


def build_excuse():
    """Return the full one-line excuse, exactly 128 characters."""
    return " ".join((_OPENING, _DASH, _CLOSING))

def main():
    excuse = build_excuse()
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as out:
        out.write(excuse)

if __name__ == "__main__":
    main()
