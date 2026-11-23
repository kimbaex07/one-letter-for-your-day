"""One Letter for Your Day — entry program.

Writes exactly one character, the letter Z, to entry.txt inside the
output directory named by MAKEFUN_OUTPUT_DIR (falling back to /output).

Z stands for "zombie": the word for a day spent shambling through work
half-asleep before dawn. The letter is the whole entry — one byte, no
newline, no gloss, no punctuation — exactly as the competition's gate
requires (UTF-8 text of 1 to 1 characters).

Pure Python standard library only; deterministic: every run writes the
same single byte. After writing, the program reads the file back and
refuses to report success unless it holds exactly that one byte, so a
bad write can never silently pass as a valid entry.
"""

import os
import stat
import sys

LETTER = "Z"
FILENAME = "entry.txt"


def output_dir() -> str:
    """Return the directory the entry artifact goes in."""
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return directory


def write_entry(directory: str) -> str:
    """Write the single letter, verify it, and return the artifact path."""
    if len(LETTER) != 1 or not ("A" <= LETTER <= "Z"):
        raise ValueError("LETTER must be exactly one A-Z character")
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, FILENAME)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(LETTER)
    os.chmod(path, stat.S_IRUSR | stat.S_IWUSR | stat.S_IRGRP | stat.S_IROTH)
    with open(path, "rb") as handle:
        written = handle.read()
    if written != LETTER.encode("ascii"):
        raise ValueError("entry.txt must hold exactly the letter " + LETTER)
    return path


def main() -> int:
    path = write_entry(output_dir())
    print("wrote {} ({} byte)".format(path, os.path.getsize(path)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
