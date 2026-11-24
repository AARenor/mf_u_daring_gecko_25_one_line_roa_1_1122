#!/usr/bin/env python3
"""Write one short text for a make.fun bounty entry.

Standard library only, no network. The text goes to entry.txt inside the
folder named by MAKEFUN_OUTPUT_DIR when set, else /output.
"""

import os
import sys

TEXT = (
    "My watch congratulated me on a twelve-hour stand goal I hit standing at the fridge."
)


def main() -> int:
    assert 1 <= len(TEXT) <= 280, "entry text must be 1..280 characters"

    out_dir = (
        os.environ.get("MAKEFUN_OUTPUT_DIR")
        or os.environ.get("OUTPUT_DIR")
        or "/output"
    )
    os.makedirs(out_dir, exist_ok=True)

    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(TEXT)

    print(f"{len(TEXT)} characters written to {path}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
