"""Front page for 19 November 2026, final edition (v2).

The shipped file is a 1024x1024 JPEG newspaper page, "THE WORLD TODAY",
dated Thursday 19 November 2026. Its five picture stories, all checked
against the day's reporting: the Shenzhen summit ends with a four-point
Declaration Towards Peace from Trump, Xi and Putin; Anthropic's shares
begin trading on Nasdaq as ANT after the biggest IPO ever; the Gulf war
widens as Iran strikes US bases in Kuwait and Bahrain; the COP31 draft
in Antalya drops the fossil-fuel phaseout; and Eisenkot's bloc presses
to replace Netanyahu. A footer strip rounds up the rest of the day.

Running this program checks the page (JPEG start/end markers, the
one-mebibyte cap, exact 1024x1024 frame size) and writes an unchanged
copy to the output directory. It needs nothing beyond the standard
library and never uses the network.
"""

import os
import struct
import sys

PAGE_W = 1024
PAGE_H = 1024
PAGE_MAX = 1_048_576
PAGE_FILE = "entry.png"
# v2 image: 355,937 bytes, sha256 76510899ad9e9e258291c7ed0d7d1a7ca3c2ac7701aa07551057cfe04895b9f7

SOI = b"\xff\xd8"
EOI = b"\xff\xd9"


def abort(text):
    sys.stderr.write("error: %s\n" % text)
    raise SystemExit(1)


def frame_size(blob):
    """Return the (width, height) from the first JPEG frame header."""
    if blob[:2] != SOI:
        return None
    pos = 2
    while pos + 1 < len(blob):
        if blob[pos] != 0xFF:
            return None
        tag = blob[pos + 1]
        if tag == 0xDA or tag == 0xD9:
            return None
        if tag == 0x01 or 0xD0 <= tag <= 0xD7:
            pos += 2
            continue
        if pos + 4 > len(blob):
            return None
        seg = struct.unpack_from(">H", blob, pos + 2)[0]
        if seg < 2 or pos + 2 + seg > len(blob):
            return None
        if tag in (0xC0, 0xC1, 0xC2):
            if seg < 7:
                return None
            h = struct.unpack_from(">H", blob, pos + 5)[0]
            w = struct.unpack_from(">H", blob, pos + 7)[0]
            return (w, h)
        pos += 2 + seg
    return None


def check(blob, where):
    """Refuse anything that is not a 1024x1024 JPEG under the size cap."""
    if len(blob) < 4:
        abort("%s is too short to be a JPEG" % where)
    if blob[:2] != SOI:
        abort("%s does not start with a JPEG SOI marker" % where)
    if blob[-2:] != EOI:
        abort("%s does not end with a JPEG EOI marker" % where)
    if len(blob) > PAGE_MAX:
        abort("%s is %d bytes, over the %d-byte limit"
              % (where, len(blob), PAGE_MAX))
    size = frame_size(blob)
    if size is None:
        abort("%s has no JPEG frame header" % where)
    if size != (PAGE_W, PAGE_H):
        abort("%s is %dx%d, expected %dx%d"
              % (where, size[0], size[1], PAGE_W, PAGE_H))
    return size


def run():
    base = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(base, PAGE_FILE)
    dest_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    dest = os.path.join(dest_dir, PAGE_FILE)
    try:
        with open(src, "rb") as handle:
            blob = handle.read()
    except OSError as exc:
        abort("cannot open %s: %s" % (src, exc))
    check(blob, PAGE_FILE)
    try:
        os.makedirs(dest_dir, exist_ok=True)
        with open(dest, "wb") as handle:
            handle.write(blob)
    except OSError as exc:
        abort("cannot write %s: %s" % (dest, exc))
    try:
        with open(dest, "rb") as handle:
            again = handle.read()
    except OSError as exc:
        abort("cannot re-open %s: %s" % (dest, exc))
    if again != blob:
        abort("%s changed during the copy" % dest)
    check(again, dest)
    print("%s: %d bytes, %dx%d JPEG, copied unchanged to %s"
          % (PAGE_FILE, len(blob), PAGE_W, PAGE_H, dest))


if __name__ == "__main__":
    run()
