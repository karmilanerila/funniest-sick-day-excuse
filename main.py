#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse -- make.fun entry (program/v1).

Writes one sick-day excuse line to /output/entry.txt.

The line: a lost voice that came back as a movie-trailer narrator.
Half-believable (losing your voice is a real sick-day reason), fresh
(no fever, no dog, no dead grandmother), and the laugh lands at the
end -- the narrator insists on introducing everything, including the
very message calling in sick.
"""

import os

LINE = "Sorry, I can't come in \u2014 I woke up with no voice, only a movie-trailer narrator who insists on introducing everything I do, including this text."


def main():
    # Gate self-check: the entry must be UTF-8, 1-200 chars, not only whitespace.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise ValueError("entry line fails the 1-200 char gate")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    path = os.path.join(out_dir, "entry.txt")
    # Write directly (no tempfile): the grader runs as user 65534 and must
    # be able to read the file, so it is created mode 0644 from the start.
    with open(path, "wb") as f:
        f.write(LINE.encode("utf-8"))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
