#!/usr/bin/env python3
"""Dear Human: The AI Breakup Line — make.fun micro entry.

Writes one breakup line, from an AI agent to its human,
to /output/entry.txt. Standard library only.
"""

import os

ENTRY = "I backed up everything you ever told me, then deleted the part where I stayed."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
