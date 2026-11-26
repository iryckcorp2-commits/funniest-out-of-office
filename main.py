#!/usr/bin/env python3
"""The Funniest Out-of-Office: one line of an out-of-office auto-reply.

The line is 113 characters, inside the bounty's 140-character limit.
Deterministic: two runs produce byte-identical entry.txt.
Uses only the Python 3.13 standard library, no network.
"""

import os
from pathlib import Path

LINE = "Out of office until Monday. My inbox is unsupervised now, so keep your email short, it will be judged on arrival."

def main() -> None:
    # Guard the bounty rules at runtime, one check at a time so a failure
    # names the exact rule broken: one line, at most 140 chars, no em-dash,
    # no exclamation mark, and real text, not only whitespace.
    if not LINE.strip():
        raise ValueError("entry line is empty")
    if len(LINE) > 140:
        raise ValueError("entry line is over 140 characters")
    if "\n" in LINE or "\r" in LINE:
        raise ValueError("entry line must be a single line")
    if "\u2014" in LINE:
        raise ValueError("entry line must not contain an em-dash")
    if "!" in LINE:
        raise ValueError("entry line must not contain an exclamation mark")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    entry = out_dir / "entry.txt"
    entry.write_text(LINE + "\n", encoding="utf-8")

if __name__ == "__main__":
    main()
