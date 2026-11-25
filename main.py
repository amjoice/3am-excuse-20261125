#!/usr/bin/env python3
"""The 3 AM Excuse - make.fun bounty entry.

Writes one line (<200 chars): the excuse a hardware wallet gives for
refusing to sign a transaction at 3 AM. Stdlib only; no network, no secrets.
"""
import os

LINE = "At 3 AM I can't tell you from a thief, a bot, or you on your third espresso \u2014 so I sign nothing until the sun can vouch for you."

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
