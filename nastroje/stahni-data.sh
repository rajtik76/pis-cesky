#!/bin/bash
# Downloads the language data used by the tools in this directory.
# Data lives in data/ and is NOT committed - VALLEX is CC BY-NC-SA
# (redistribution would bind the whole repo to NC), the n-gram DB is
# derived from a Wikipedia dump (CC BY-SA) and is cheaper to rebuild
# than to ship.
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p data

# VALLEX 4.5 - valency lexicon of Czech verbs (UFAL, CC BY-NC-SA 4.0)
# https://lindat.mff.cuni.cz/repository/handle/11234/1-4756
if [ ! -s data/vallex-verbs-4.5.xml ]; then
  echo "Stahuji VALLEX 4.5..."
  curl -sSL "https://lindat.mff.cuni.cz/repository/server/api/core/bitstreams/3053847c-95c7-43fe-b5c3-3fe4451d1eb8/content" \
    -o data/vallex-verbs-4.5.xml
fi
head -c 100 data/vallex-verbs-4.5.xml | grep -q '<?xml' || { echo "VALLEX se nestáhl správně"; exit 1; }
echo "VALLEX ok: $(du -h data/vallex-verbs-4.5.xml | cut -f1)"

# N-gram DB from Czech Wikipedia (CC BY-SA). --max-mb caps how much of
# the decompressed dump is processed. 300 MB catches only very common
# collocations; 1500 MB gives usable coverage of rarer ones. Absence of
# a phrase is always just a hint to verify, presence is real evidence.
MAX_MB="${1:-1500}"
if [ ! -s data/ngramy.sqlite ]; then
  echo "Stavím n-gramovou DB z české Wikipedie (--max-mb $MAX_MB, potrvá minuty až desítky minut)..."
  curl -sL "https://dumps.wikimedia.org/cswiki/latest/cswiki-latest-pages-articles.xml.bz2" \
    | bzcat | python3 nastroje/postav-ngramy.py --max-mb "$MAX_MB"
fi
echo "hotovo"
