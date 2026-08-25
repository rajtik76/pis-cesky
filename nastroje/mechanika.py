#!/usr/bin/env python3
"""Deterministická kontrola mechaniky českého textu.

Použití: mechanika.py <soubor> [další soubory...]
         mechanika.py -        (čte text ze stdin)

Chytá, co nepotřebuje jazykový úsudek: nespárované závorky a uvozovky,
pomlčky místo spojovníku s mezerami, dvojité mezery, mezery kolem
interpunkce a mezery na konci řádku. Pouští se před jazykovým
korektorem, aby drahý model neutrácel tokeny za triviality. Nález je
podnět k prověření, ne rozsudek.

Kód se nekontroluje: bloky ohraničené ``` nebo ~~~ i vsuvky v backticku
mají vlastní typografii, takže by hlásily chyby, které chybami nejsou.
Odsazení odrážek a zarovnání tabulek se z téhož důvodu za dvojitou
mezeru nepovažuje.
"""
import re
import sys
from pathlib import Path

PAIRS = {"(": ")", "[": "]", "{": "}"}
# Czech quotes: „ opens, " closes; ‚ opens, ' closes
QUOTE_PAIRS = [("„", "“"), ("‚", "‘")]

FENCE_RE = re.compile(r"^ {0,3}(?P<marker>`{3,}|~{3,})")
INLINE_CODE_RE = re.compile(r"(?P<ticks>`+).+?(?P=ticks)")


def check_line(line, lineno, findings):
    for dash, name in (("–", "en-pomlčka –"), ("—", "em-pomlčka —")):
        if dash in line:
            findings.append((lineno, f"{name}: styl žádá ' - ' (spojovník s mezerami)"))
    body = line.strip()
    # leading spaces indent list items, and table rows pad cells to align
    is_table_row = body.startswith("|") and body.endswith("|")
    if "  " in body and not is_table_row:
        findings.append((lineno, "dvojitá mezera"))
    trailing = len(line) - len(line.rstrip())
    if trailing and body:
        # two or more trailing spaces are a markdown line break, one is just leftover
        note = (" - v markdownu zalomení řádku, tedy možná záměr" if trailing >= 2
                else " - na zalomení nestačí, markdown chce dvě a víc")
        findings.append((lineno, f"mezera na konci řádku ({trailing}×){note}"))
    # a lone dot after space is a typo, three of them are an ellipsis
    for m in re.finditer(r"\s+(?:[,;:!?]|\.(?!\.))", line):
        findings.append((lineno, f"mezera před interpunkcí: '{m.group().strip()}' na pozici {m.start() + 1}"))
    # comma glued to a letter; digits excluded (1,5) as are quotes/brackets
    for m in re.finditer(r",(?=[^\W\d_])", line):
        findings.append((lineno, f"chybí mezera za čárkou na pozici {m.start() + 1}"))


def mask_code(text, findings):
    """Blank out code so its typography is not read as prose typography.

    Line count stays the same, so reported line numbers still match the
    original file; inline code keeps its width for the same reason.
    """
    masked = []
    fence = None
    opened_at = 0
    for lineno, line in enumerate(text.splitlines(), 1):
        m = FENCE_RE.match(line)
        if fence is not None:
            masked.append("")
            if m and m.group("marker")[0] == fence:
                fence = None
            continue
        if m:
            fence = m.group("marker")[0]
            opened_at = lineno
            masked.append("")
            continue
        masked.append(INLINE_CODE_RE.sub(lambda mm: "x" * len(mm.group()), line))
    if fence is not None:
        findings.append((opened_at, "neuzavřený blok kódu"))
    return "\n".join(masked)


def check_text(text, label):
    findings = []
    prose = mask_code(text, findings)
    for lineno, line in enumerate(prose.splitlines(), 1):
        check_line(line, lineno, findings)

    # pairing is checked over the whole text - brackets can span lines in prose
    for opener, closer in PAIRS.items():
        diff = prose.count(opener) - prose.count(closer)
        if diff:
            which = opener if diff > 0 else closer
            # enumerations ("Ad 1)", "a)") count too, so the surplus need not be an error
            note = ", číslované body se počítají taky" if which == ")" else ""
            findings.append((0, f"nespárovaná závorka: '{which}' přebývá {abs(diff)}×{note}"))
    for opener, closer in QUOTE_PAIRS:
        diff = prose.count(opener) - prose.count(closer)
        if diff:
            findings.append((0, f"nespárované uvozovky {opener}…{closer}: rozdíl {abs(diff)}"))
    straight = prose.count('"')
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
