#!/usr/bin/env python3
"""One Line, One Chill — make.fun entry.

Writes a single horror sentence (1-200 characters) to entry.txt.
Standard library only.
"""

import os

LINE = "The doctor smiled and said the tumor was wearing my face."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
