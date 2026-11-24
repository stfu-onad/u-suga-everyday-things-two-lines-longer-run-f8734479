"""Everyday Things, Two Lines, Longer Run — entry for
u-suga-everyday-things-two-lines-longer-run-f8734479.

Writes one original two-line explanation to /output/entry.txt.
Line 1 explains a traffic jam to a 10-year-old in a single vivid
sentence built on an analogy; line 2 says in one sentence what the
analogy maps and what it leaves out. The text is fixed and
hand-written: no network, no randomness, no input files. The
analogy is concrete and surprising (a school crowd at one door),
and the second line is honest about the limit instead of praising
the comparison: it names the bottleneck the analogy covers and the
missing turn-taking it cannot show.
"""

import os

ENTRY = (
    "A traffic jam is like a whole school trying to squeeze through one "
    "classroom door at the same time, everybody pushing forward and "
    "nobody getting anywhere.\n"
    "It maps the squeeze \u2014 too many cars, too little road \u2014 but "
    "leaves out that there is no teacher calling turns, so nobody in a "
    "jam knows when to go."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 400, "entry must be 1-400 characters"
    assert ENTRY.count("\n") == 1, "entry must be exactly two lines"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
