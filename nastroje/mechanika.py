#!/usr/bin/env python3
"""Deterministická kontrola mechaniky českého textu.

Použití: mechanika.py <soubor> [další soubory...]
         mechanika.py -        (čte text ze stdin)

Chytá, co nepotřebuje jazykový úsudek: nespárované závorky a uvozovky,
pomlčky místo spojovníku s mezerami, dvojité mezery a mezery kolem
interpunkce. Pouští se před jazykovým korektorem, aby drahý model
neutrácel tokeny za triviality. Nález je podnět k prověření, ne rozsudek.
"""
import re
import sys
from pathlib import Path

PAIRS = {"(": ")", "[": "]", "{": "}"}
# Czech quotes: „ opens, " closes; ‚ opens, ' closes
QUOTE_PAIRS = [("„", "“"), ("‚", "‘")]


def check_line(line, lineno, findings):
    for dash, name in (("–", "en-pomlčka –"), ("—", "em-pomlčka —")):
        if dash in line:
            findings.append((lineno, f"{name}: styl žádá ' - ' (spojovník s mezerami)"))
    if "  " in line.rstrip("\n"):
        findings.append((lineno, "dvojitá mezera"))
    for m in re.finditer(r"\s+[,.;:!?]", line):
        findings.append((lineno, f"mezera před interpunkcí: '{m.group().strip()}' na pozici {m.start() + 1}"))
    # comma glued to a letter; digits excluded (1,5) as are quotes/brackets
    for m in re.finditer(r",(?=[^\W\d_])", line):
        findings.append((lineno, f"chybí mezera za čárkou na pozici {m.start() + 1}"))


def check_text(text, label):
    findings = []
    for lineno, line in enumerate(text.splitlines(), 1):
        check_line(line, lineno, findings)

    # pairing is checked over the whole text - brackets can span lines in prose
    for opener, closer in PAIRS.items():
        diff = text.count(opener) - text.count(closer)
        if diff:
            which = opener if diff > 0 else closer
            findings.append((0, f"nespárovaná závorka: '{which}' přebývá {abs(diff)}×"))
    for opener, closer in QUOTE_PAIRS:
        diff = text.count(opener) - text.count(closer)
        if diff:
            findings.append((0, f"nespárované uvozovky {opener}…{closer}: rozdíl {abs(diff)}"))
    straight = text.count('"')
    if straight % 2:
        findings.append((0, 'lichý počet rovných uvozovek (")'))

    if not findings:
        print(f"{label}: mechanika v pořádku")
        return
    for lineno, msg in sorted(findings):
        where = f"řádek {lineno}" if lineno else "celý text"
        print(f"{label}: {where}: {msg}")


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    for arg in sys.argv[1:]:
        if arg == "-":
            check_text(sys.stdin.read(), "stdin")
            continue
        path = Path(arg)
        if not path.exists():
            print(f"{arg}: soubor neexistuje")
            continue
        check_text(path.read_text(encoding="utf-8"), str(path))


if __name__ == "__main__":
    main()
