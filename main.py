"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

import os

TEXT = "The map says there's a road straight through that lake, and frankly the lake is the one trespassing."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

# Revision note: entry kept as written — one line, 100 characters, one sentence;
# GPS voice, smug and defensive, blames the map, fresh detail (the lake) with
# the turn on the last word (the lake trespassing, not the GPS erring).
