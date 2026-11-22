#!/usr/bin/env python3
"""make.fun bounty: Sum up 22 November's world news in one image.

Entry program. It writes one image to /output/entry.png.
It copies the image this repository holds (entry.png), with no network
access, no randomness and no timestamps, so two runs write the same bytes.
"""
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png"
DST = Path("/output/entry.png")


def main() -> None:
    DST.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, DST)


if __name__ == "__main__":
    main()
