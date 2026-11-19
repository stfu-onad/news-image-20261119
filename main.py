"""THE WORLD TODAY — Thursday 19 November 2026.

Front page of a one-page newspaper image (entry.png, 1024x1024 JPEG).

Lead story: TRUMP, XI AND PUTIN MEET IN SHENZHEN — a trilateral summit
held today in Shenzhen, including a Trump-Putin one-on-one, the first
since Alaska 2025.

Second row: VICE CITY OPENS WORLDWIDE — GTA VI launches globally,
scoring 99 on Metacritic — and GULF FIGHT WIDENS — Iran hits a US base
in Kuwait and strikes Bahrain again.

Footer, ALSO TODAY: the ICJ rules on the Myanmar genocide case; Jeffries
is nominated for Speaker, a first; Nvidia's Kress promises earlier raises
and halts H chips to China; the Fed points to more hikes; the EU proposes
a 45B euro Ukraine loan; Cyclone Akvan nears the India coast; Voyager 1
reaches one light-day.

This script validates entry.png (JPEG markers, size, and dimensions) and
copies it byte-identically to the output directory.
"""

import os
import struct
import sys

EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024
MAX_SIZE = 1_048_576  # 1 MiB

SOURCE_NAME = "entry.png"


def fail(message):
    """Print an error to stderr and exit non-zero."""
    print("error: " + message, file=sys.stderr)
    sys.exit(1)


def jpeg_dimensions(data):
    """Return (width, height) parsed from the first SOF segment (C0/C1/C2).

    Returns None when no SOF segment is found before the scan data.
    """
    if len(data) < 4 or data[0] != 0xFF or data[1] != 0xD8:
        return None
    i = 2
    while i + 1 < len(data):
        if data[i] != 0xFF:
            return None
        marker = data[i + 1]
        if marker == 0xDA:  # SOS: scan data follows, no SOF after this
            return None
        if marker == 0xD9:  # EOI
            return None
        if marker == 0x01 or 0xD0 <= marker <= 0xD7:
            i += 2
            continue
        if i + 4 > len(data):
            return None
        length = struct.unpack(">H", data[i + 2:i + 4])[0]
        if length < 2 or i + 2 + length > len(data):
            return None
        if marker in (0xC0, 0xC1, 0xC2):
            if length < 7:
                return None
            height = struct.unpack(">H", data[i + 5:i + 7])[0]
            width = struct.unpack(">H", data[i + 7:i + 9])[0]
            return (width, height)
        i += 2 + length
    return None


def validate(data, label):
    """Validate JPEG bytes: SOI/EOI markers, size, and 1024x1024 dimensions."""
    if len(data) < 4:
        fail(label + ": file too small to be a JPEG")
    if data[0] != 0xFF or data[1] != 0xD8:
        fail(label + ": missing JPEG SOI marker (FF D8)")
    if data[-2] != 0xFF or data[-1] != 0xD9:
        fail(label + ": missing JPEG EOI marker (FF D9)")
    if len(data) > MAX_SIZE:
        fail(label + ": size %d exceeds %d bytes" % (len(data), MAX_SIZE))
    dims = jpeg_dimensions(data)
    if dims is None:
        fail(label + ": no SOF segment found")
    if dims != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        fail(label + ": dimensions %dx%d, expected %dx%d"
             % (dims[0], dims[1], EXPECTED_WIDTH, EXPECTED_HEIGHT))
    return dims


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source_path = os.path.join(here, SOURCE_NAME)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    output_path = os.path.join(output_dir, SOURCE_NAME)

    try:
        with open(source_path, "rb") as f:
            data = f.read()
    except OSError as exc:
        fail("cannot read %s: %s" % (source_path, exc))

    validate(data, SOURCE_NAME)

    try:
        os.makedirs(output_dir, exist_ok=True)
        with open(output_path, "wb") as f:
            f.write(data)
    except OSError as exc:
        fail("cannot write %s: %s" % (output_path, exc))

    try:
        with open(output_path, "rb") as f:
            copied = f.read()
    except OSError as exc:
        fail("cannot re-read %s: %s" % (output_path, exc))

    if copied != data:
        fail(output_path + ": copied bytes differ from source")
    validate(copied, output_path)

    print("entry.png: %d bytes, %dx%d JPEG, copied byte-identically to %s"
          % (len(data), EXPECTED_WIDTH, EXPECTED_HEIGHT, output_path))


if __name__ == "__main__":
    main()
