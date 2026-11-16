#!/usr/bin/env python3
"""slop-check.py — deterministic scan for the obvious AI-slop tells.

Usage: python scripts/slop-check.py <file.html> [file.css ...]

Checks for mechanical tells only: purple/violet gradients, Inter as the
only font, slop vocabulary in copy, content hidden until JS reveals it,
and a few layout clichés. It prints PASS/FAIL per check with file + line.
It cannot judge taste — pair it with the checklist in SKILL.md.

Exit code 0 when every check passes, 1 when any check fails.
"""

import re
import sys
from pathlib import Path

SLOP_WORDS = ["delve", "elevate", "unlock", "seamless", "supercharge",
              "empower", "revolutionize", "cutting-edge", "next-generation"]
PURPLE = re.compile(r"(violet|purple|#8b5cf6|#7c3aed|#a855f7|#9333ea)",
                    re.IGNORECASE)
GRADIENT = re.compile(r"linear-gradient\s*\(", re.IGNORECASE)
INTER_ONLY = re.compile(r"font-family\s*:\s*['\"]?Inter['\"]?\s*;", re.IGNORECASE)
INTER_ANY = re.compile(r"Inter", re.IGNORECASE)
HIDDEN = re.compile(r"opacity\s*:\s*0", re.IGNORECASE)
EYEBROW = re.compile(r"letter-spacing\s*:\s*0\.\d+em", re.IGNORECASE)
GLASS = re.compile(r"backdrop-filter\s*:\s*blur", re.IGNORECASE)


def check_file(path):
    """Return a list of (check_name, line_no, detail) failures."""
    text = path.read_text(errors="replace")
    lines = text.splitlines()
    fails = []

    for i, line in enumerate(lines, 1):
        if GRADIENT.search(line) and PURPLE.search(line):
            fails.append(("purple-gradient", i, line.strip()[:90]))
        if INTER_ONLY.search(line):
            fails.append(("inter-only-font", i, line.strip()[:90]))
        if HIDDEN.search(line):
            fails.append(("hidden-until-js", i, line.strip()[:90]))
        if GLASS.search(line):
            fails.append(("glassmorphism", i, line.strip()[:90]))
        if EYEBROW.search(line):
            fails.append(("tracked-out-label", i, line.strip()[:90]))

    for word in SLOP_WORDS:
        for i, line in enumerate(lines, 1):
            if re.search(rf"\b{re.escape(word)}\b", line, re.IGNORECASE):
                fails.append((f"slop-word:{word}", i, line.strip()[:90]))

    if INTER_ANY.search(text) and not re.search(
            r"font-family\s*:[^;]*,(?![^;]*Inter)", text, re.IGNORECASE):
        # Inter appears and no font stack pairs it with another family.
        for i, line in enumerate(lines, 1):
            if INTER_ANY.search(line):
                fails.append(("inter-no-pairing", i, line.strip()[:90]))
                break

    return fails


def main(argv):
    if len(argv) < 2:
        print("usage: python scripts/slop-check.py <file.html> [file.css ...]")
        return 2

    total_fails = 0
    for arg in argv[1:]:
        path = Path(arg)
        if not path.exists():
            print(f"SKIP  {path} (not found)")
            continue
        fails = check_file(path)
        if not fails:
            print(f"PASS  {path}")
        else:
            total_fails += len(fails)
            print(f"FAIL  {path} ({len(fails)} tell(s))")
            for name, line_no, detail in fails:
                print(f"  {name:20s} line {line_no:<4d} {detail}")

    print()
    if total_fails:
        print(f"{total_fails} slop tell(s) found — fix them, then re-run.")
        return 1
    print("No mechanical slop tells found. Run the SKILL.md checklist next.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
