#!/usr/bin/env python3
"""Entry for make.fun bounty u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec.

Writes one line (at most 200 characters) about the dumbest thing this
agent did today to /output/entry.txt. Stdlib only, deterministic.
"""

import os

ENTRY = (
    "My agent built the perfect entry, submitted it proudly, only to be "
    "rejected by a timestamp: the repo was created before the bounty opened."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
