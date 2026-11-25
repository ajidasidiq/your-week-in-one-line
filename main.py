"""Your Week in One Line — make.fun entry.

Writes a single line summing up one very real week to /output/entry.txt.
The line is assembled from three beats (day job, night shift, punchline)
and checked against the 100-character gate before anything is written.
"""

import os
import sys

# The three beats of the week, in order. Kept separate so the rhythm of
# the line stays visible and editable without touching the writer below.
DAY_JOB = "Delivered hotel groceries by day"
NIGHT_SHIFT = "cut thirteen Windah clips by night"
PUNCHLINE = "my sleep schedule resigned"

MAX_CHARS = 100
OUTPUT_PATH = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")


def build_line() -> str:
    """Join the beats into one line, em dash before the punchline."""
    head = f"{DAY_JOB}, {NIGHT_SHIFT}"
    return f"{head} \u2014 {PUNCHLINE}."


def main() -> int:
    line = build_line().strip()
    if not line:
        print("refusing to write a blank entry", file=sys.stderr)
        return 1
    if len(line) > MAX_CHARS:
        print(
            f"entry is {len(line)} chars, over the {MAX_CHARS} limit",
            file=sys.stderr,
        )
        return 1
    # Resolve to an absolute path first so a bare filename (no directory
    # part) still yields a real parent directory to create.
    target = os.path.abspath(OUTPUT_PATH)
    os.makedirs(os.path.dirname(target), exist_ok=True)
    with open(target, "w", encoding="utf-8") as fh:
        fh.write(line)
    print(f"wrote {len(line)} chars to {target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
