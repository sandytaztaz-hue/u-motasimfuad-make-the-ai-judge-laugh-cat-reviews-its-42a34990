#!/usr/bin/env python3
"""Cat Reviews Its Human: a one-line, one-star review by a house cat.

The entry is a single fixed line: a deadpan one-star review in which
the cat's complaint (a shut bathroom door) escalates, on cat logic,
to a toothbrush in the toilet — and the cat files it as housekeeping.
The program writes it to /output/entry.txt (the competition's gate
reads that file) and prints exactly the same line to stdout, so the
entry is identical whichever channel the harness reads. No input, no
randomness, no network.
"""

import os

ENTRY = "One star. He shut the bathroom door in my face, so I waited nine minutes and knocked his toothbrush into the toilet. I call it housekeeping."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
