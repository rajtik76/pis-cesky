---
name: data
description: Postaví jazyková data pro pis-cesky - VALLEX (valenční rámce sloves) a frekvenční databázi spojení z české Wikipedie. Data se nedistribuují s pluginem, staví se lokálně.
user-invocable: true
disable-model-invocation: true
---

# Postavit jazyková data

Spusť skript a počkej, až doběhne:

```
bash ${CLAUDE_PLUGIN_ROOT}/nastroje/stahni-data.sh
```

Cestu ke skriptu piš vždy přes `${CLAUDE_PLUGIN_ROOT}` - relativní cesta
míří do adresáře, kde uživatel zrovna pracuje, a selže. Kam se data
postaví, rozhoduje `nastroje/datadir.py`: proměnná `PIS_CESKY_DATA`,
jinak sdílený adresář uživatele mimo instalaci pluginu (vypíšeš ho
příkazem `python3 ${CLAUDE_PLUGIN_ROOT}/nastroje/datadir.py`). Skripty
`vazby.py` a `spojeni.py` hledají tamtéž, navíc vidí i lokálně
postavená data v klonu repa.

Co k tomu vědět a říct uživateli dopředu:

- VALLEX je stažení na 13 MB. N-gramy se staví z dumpu české
  Wikipedie: proteče přes gigabajt dat a trvá to desítky minut.
  Výsledek zabere na disku asi 250 MB (n-gramy 240 MB, VALLEX 13 MB). Pusť to na pozadí, ne
  v popředí.
- Když už data existují, skript je znovu nestahuje. Není třeba to
  kontrolovat předem.
- Data leží mimo instalaci pluginu, takže aktualizace pluginu je
  nezahodí - stavějí se jen jednou.

Až to doběhne, ověř, že obojí funguje:

```
python3 ${CLAUDE_PLUGIN_ROOT}/nastroje/vazby.py přiznat
python3 ${CLAUDE_PLUGIN_ROOT}/nastroje/spojeni.py "hraje klíčovou roli"
```
