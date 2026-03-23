#!/usr/bin/env python3
import segno
import sys

if len(sys.argv) < 2:
    print("Usage: python make_qr.py \"text\" [output]")
    sys.exit(1)

text = sys.argv[1]
out = sys.argv[2] if len(sys.argv) > 2 else "qr.png"

qr = segno.make(text, error='H')
qr.save(out, scale=6, border=2)

print(f"QR created: {out}")
