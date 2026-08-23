#!/usr/bin/env python3
"""Zjistí, jak časté je české spojení v místní n-gramové databázi.

Použití: spojeni.py "<fráze>" [další fráze...]

Vyhledá přesné spojení (1-3 slova) v ngramy.sqlite (kde se databáze
hledá, říká datadir.py) a vypíše jeho
výskyt i výskyty jednotlivých slov - podle toho poznáš, jestli je
spojení vzácné kvůli vzácným slovům, nebo proto, že se tak nemluví.
Verdikt je vodítko, ne rozsudek: databáze stojí na Wikipedii, takže
hovorová a vývojářská spojení mají nízký výskyt právem.
"""
import sqlite3
import sys
from pathlib import Path

from datadir import data_file

DB = data_file("ngramy.sqlite")


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    if not DB.exists():
        script = Path(__file__).resolve().parent / "stahni-data.sh"
        sys.exit(f"Chybí {DB} - postav ji příkazem: bash {script}")

    con = sqlite3.connect(DB)

    def count(text):
        row = con.execute("SELECT cnt FROM ngram WHERE text = ?", (text.lower(),)).fetchone()
        return row[0] if row else 0

    for phrase in sys.argv[1:]:
        words = phrase.lower().split()
        if not 1 <= len(words) <= 3:
            print(f"'{phrase}': podporuji 1-3 slova")
            continue
        c = count(" ".join(words))
        parts = ", ".join(f"{w}={count(w)}" for w in words)
        if len(words) == 1:
            print(f"'{phrase}': {c}×")
            continue
        min_word = min(count(w) for w in words)
        if c == 0 and min_word == 0:
            verdict = "slova mimo slovník DB - nic z toho neplyne"
        elif c == 0:
            verdict = "spojení v DB vůbec není - prověř, jestli se tak mluví"
        elif c < 5 and min_word > 1000:
            verdict = "slova běžná, spojení vzácné - podezřelá kolokace"
        else:
            verdict = "spojení doložené"
        print(f"'{phrase}': {c}× (slova: {parts}) -> {verdict}")


if __name__ == "__main__":
    main()
