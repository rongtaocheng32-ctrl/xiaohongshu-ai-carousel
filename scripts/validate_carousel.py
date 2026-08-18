#!/usr/bin/env python3
"""Validate ordered Xiaohongshu carousel raster files without third-party packages."""

from __future__ import annotations

import argparse
import re
import struct
import sys
from pathlib import Path


SUPPORTED = {".png", ".jpg", ".jpeg"}


def png_size(path: Path) -> tuple[int, int]:
    with path.open("rb") as handle:
        header = handle.read(24)
    if header[:8] != b"\x89PNG\r\n\x1a\n" or header[12:16] != b"IHDR":
        raise ValueError("invalid PNG header")
    return struct.unpack(">II", header[16:24])


def jpeg_size(path: Path) -> tuple[int, int]:
    with path.open("rb") as handle:
        if handle.read(2) != b"\xff\xd8":
            raise ValueError("invalid JPEG header")
        while True:
            marker_start = handle.read(1)
            if not marker_start:
                break
            if marker_start != b"\xff":
                continue
            marker = handle.read(1)
            while marker == b"\xff":
                marker = handle.read(1)
            if marker in {b"\xd8", b"\xd9"}:
                continue
            length_bytes = handle.read(2)
            if len(length_bytes) != 2:
                break
            length = struct.unpack(">H", length_bytes)[0]
            if marker and marker[0] in range(0xC0, 0xC4):
                payload = handle.read(5)
                if len(payload) != 5:
                    break
                height, width = struct.unpack(">HH", payload[1:5])
                return width, height
            handle.seek(length - 2, 1)
    raise ValueError("JPEG dimensions not found")


def image_size(path: Path) -> tuple[int, int]:
    if path.suffix.lower() == ".png":
        return png_size(path)
    return jpeg_size(path)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("folder", type=Path)
    parser.add_argument("--min-pages", type=int, default=4)
    parser.add_argument("--max-pages", type=int, default=8)
    parser.add_argument("--ratio-tolerance", type=float, default=0.01)
    parser.add_argument("--min-width", type=int, default=1000)
    parser.add_argument("--min-height", type=int, default=1333)
    args = parser.parse_args()

    if args.min_pages < 1:
        parser.error("--min-pages must be at least 1")
    if args.max_pages < args.min_pages:
        parser.error("--max-pages must be greater than or equal to --min-pages")

    if not args.folder.is_dir():
        print(f"ERROR: not a folder: {args.folder}")
        return 1

    files = sorted(p for p in args.folder.iterdir() if p.suffix.lower() in SUPPORTED)
    errors: list[str] = []
    if len(files) < args.min_pages:
        errors.append(f"expected at least {args.min_pages} images, found {len(files)}")
    if len(files) > args.max_pages:
        errors.append(f"expected at most {args.max_pages} images, found {len(files)}")

    expected_numbers = list(range(1, len(files) + 1))
    actual_numbers: list[int] = []

    for path in files:
        match = re.match(r"^(\d{2})[-_]", path.name)
        if not match:
            errors.append(f"{path.name}: filename must start with a zero-padded order such as 01-")
        else:
            actual_numbers.append(int(match.group(1)))
        try:
            width, height = image_size(path)
        except ValueError as exc:
            errors.append(f"{path.name}: {exc}")
            continue
        ratio = width / height
        if abs(ratio - 0.75) > args.ratio_tolerance:
            errors.append(f"{path.name}: ratio is {width}:{height}, expected 3:4")
        if width < args.min_width or height < args.min_height:
            errors.append(
                f"{path.name}: {width}x{height} is below {args.min_width}x{args.min_height}"
            )
        print(f"OK {path.name}: {width}x{height}")

    if actual_numbers and actual_numbers != expected_numbers:
        errors.append(f"page numbers are {actual_numbers}, expected {expected_numbers}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print(f"PASS: {len(files)} ordered 3:4 images")
    return 0


if __name__ == "__main__":
    sys.exit(main())
