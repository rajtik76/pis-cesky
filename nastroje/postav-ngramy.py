#!/usr/bin/env python3
"""Postaví místní frekvenční databázi českých n-gramů z výpisu Wikipedie.

Použití:
  curl -sL https://dumps.wikimedia.org/cswiki/latest/cswiki-latest-pages-articles.xml.bz2 \
    | bzcat | python3 nastroje/postav-ngramy.py [--max-mb 1500]

Čte rozbalené XML ze standardního vstupu, zhruba odstraní wiki značky,
spočítá jednoslovné až tříslovné výskyty a uloží je do ngramy.sqlite
v datovém adresáři (kam přesně, říká datadir.py)
(tabulka ngram(n, text, cnt), ukládá se od tří výskytů výš). Když čítač
naroste, jednotlivé výskyty se průběžně zahazují - velmi vzácné n-gramy
tak mohou být podhodnocené, na otázku "říká se to spojení vůbec?" to
ale nevadí.
"""
import argparse
import re
import sqlite3
import sys
from collections import Counter

from datadir import build_dir

DB = build_dir() / "ngramy.sqlite"

TEXT_RE = re.compile(r"<text[^>]*>(.*?)</text>", re.S)
DROP_RE = re.compile(
    r"\{\{[^{}]*\}\}|\{\|.*?\|\}|<ref[^>]*/>|<ref[^>]*>.*?</ref>|<[^>]+>"
    r"|\[\[(?:Soubor|File|Kategorie|Category)[^\]]*\]\]|https?://\S+|&[a-z]+;",
    re.S,
)
LINK_RE = re.compile(r"\[\[(?:[^|\]]*\|)?([^\]]*)\]\]")
WORD_RE = re.compile(r"[a-záčďéěíňóřšťúůýž]+", re.I)


def clean(raw):
    t = DROP_RE.sub(" ", raw)
    t = LINK_RE.sub(r"\1", t)
    t = re.sub(r"'{2,}|={2,}", " ", t)
    return t


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--max-mb", type=int, default=1500, help="zastav po N MB rozbaleného vstupu")
    ap.add_argument("--prune-at", type=int, default=8_000_000)
    args = ap.parse_args()

    counts = Counter()
    read = 0
    limit = args.max_mb * 1024 * 1024
    buf = ""
    stdin = sys.stdin.buffer

    while read < limit:
        chunk = stdin.read(1 << 20)
        if not chunk:
            break
        read += len(chunk)
        buf += chunk.decode("utf-8", "replace")
        pos = 0
        for m in TEXT_RE.finditer(buf):
            words = [w.lower() for w in WORD_RE.findall(clean(m.group(1)))]
            for i, w in enumerate(words):
                counts[(1, w)] += 1
                if i + 1 < len(words):
                    counts[(2, w + " " + words[i + 1])] += 1
                if i + 2 < len(words):
                    counts[(3, w + " " + words[i + 1] + " " + words[i + 2])] += 1
            pos = m.end()
        buf = buf[pos:] if pos else buf[-2_000_000:]
        if len(counts) > args.prune_at:
            counts = Counter({k: v for k, v in counts.items() if v > 1})
            print(f"prořez -> {len(counts)} položek, načteno {read >> 20} MB", file=sys.stderr)

    DB.parent.mkdir(parents=True, exist_ok=True)
    con = sqlite3.connect(DB)
    con.execute("DROP TABLE IF EXISTS ngram")
    con.execute("CREATE TABLE ngram (n INTEGER, text TEXT, cnt INTEGER)")
    con.executemany(
        "INSERT INTO ngram VALUES (?,?,?)",
        ((n, t, c) for (n, t), c in counts.items() if c >= 3),
    )
    con.execute("CREATE INDEX idx_ngram ON ngram(text)")
    con.execute("CREATE TABLE IF NOT EXISTS meta (key TEXT, value TEXT)")
    con.execute("INSERT INTO meta VALUES ('source_mb', ?)", (str(read >> 20),))
    con.commit()
    total = con.execute("SELECT COUNT(*) FROM ngram").fetchone()[0]
    print(f"hotovo: {total} n-gramů z {read >> 20} MB textu -> {DB}", file=sys.stderr)


if __name__ == "__main__":
    main()
