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

Cestu piš vždy přes `${CLAUDE_PLUGIN_ROOT}`. Data patří k nainstalovanému
pluginu, ne do adresáře, ve kterém uživatel zrovna pracuje - i když tam
náhodou leží klon repa s vlastními daty. Skripty `vazby.py` a
`spojeni.py` je hledají vedle sebe, takže jinam je stavět nemá smysl.

Co k tomu vědět a říct uživateli dopředu:

- VALLEX je stažení na 13 MB. N-gramy se staví z dumpu české
  Wikipedie: proteče přes gigabajt dat a trvá to desítky minut.
  Výsledek zabere na disku asi 250 MB (n-gramy 240 MB, VALLEX 13 MB). Pusť to na pozadí, ne
  v popředí.
- Když už data existují, skript je znovu nestahuje. Není třeba to
  kontrolovat předem.
- Data leží v adresáři konkrétní verze pluginu, takže po aktualizaci na
  novou verzi se stavějí znovu.

Až to doběhne, ověř, že obojí funguje:

```
python3 ${CLAUDE_PLUGIN_ROOT}/nastroje/vazby.py přiznat
python3 ${CLAUDE_PLUGIN_ROOT}/nastroje/spojeni.py "hraje klíčovou roli"
```
