#!/bin/bash
# Downloads the language data used by the tools in this directory.
# Data is NOT committed - VALLEX is CC BY-NC-SA (redistribution would
# bind the whole repo to NC), the n-gram DB is derived from a Wikipedia
# dump (CC BY-SA) and is cheaper to rebuild than to ship.
#
# The target directory comes from datadir.py: $PIS_CESKY_DATA if set,
# otherwise a per-user cache dir that survives plugin updates. Set
# PIS_CESKY_DATA=data to build into a repo clone instead.
set -euo pipefail
cd "$(dirname "$0")/.."
DATA_DIR="$(python3 nastroje/datadir.py)"
mkdir -p "$DATA_DIR"
echo "Datový adresář: $DATA_DIR"

# VALLEX 4.5 - valency lexicon of Czech verbs (UFAL, CC BY-NC-SA 4.0)
# https://lindat.mff.cuni.cz/repository/handle/11234/1-4756
if [ ! -s "$DATA_DIR/vallex-verbs-4.5.xml" ]; then
  echo "Stahuji VALLEX 4.5..."
  curl -sSL "https://lindat.mff.cuni.cz/repository/server/api/core/bitstreams/3053847c-95c7-43fe-b5c3-3fe4451d1eb8/content" \
    -o "$DATA_DIR/vallex-verbs-4.5.xml"
fi
head -c 100 "$DATA_DIR/vallex-verbs-4.5.xml" | grep -q '<?xml' || { echo "VALLEX se nestáhl správně"; exit 1; }
echo "VALLEX ok: $(du -h "$DATA_DIR/vallex-verbs-4.5.xml" | cut -f1)"

# N-gram DB from Czech Wikipedia (CC BY-SA). --max-mb caps how much of
# the decompressed dump is processed. 300 MB catches only very common
# collocations; 1500 MB gives usable coverage of rarer ones. Absence of
# a phrase is always just a hint to verify, presence is real evidence.
MAX_MB="${1:-1500}"
if [ ! -s "$DATA_DIR/ngramy.sqlite" ]; then
  echo "Stavím n-gramovou DB z české Wikipedie (--max-mb $MAX_MB, potrvá minuty až desítky minut)..."
  # postav-ngramy.py stops reading once --max-mb is reached, which sends
  # SIGPIPE up the pipeline: curl and bzcat then exit 141 and pipefail
  # would report a finished build as a failure. Judge the build by the
  # exit status of the writer at the end of the pipe, not by the feeders.
  set +e +o pipefail
  curl -sL "https://dumps.wikimedia.org/cswiki/latest/cswiki-latest-pages-articles.xml.bz2" \
    | bzcat | python3 nastroje/postav-ngramy.py --max-mb "$MAX_MB"
  ngram_status=${PIPESTATUS[2]}
  set -e -o pipefail

  if [ "$ngram_status" -ne 0 ]; then
    echo "Stavba n-gramové DB selhala (návratový kód $ngram_status)" >&2
    exit 1
  fi
fi
[ -s "$DATA_DIR/ngramy.sqlite" ] || { echo "N-gramová DB se nepostavila" >&2; exit 1; }
echo "N-gramy ok: $(du -h "$DATA_DIR/ngramy.sqlite" | cut -f1)"
echo "hotovo"
