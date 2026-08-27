# Jazyková data

Skill má vlastní jazykovou vrstvu: valenční rámce sloves z VALLEXu
a frekvence spojení z české Wikipedie, obojí lokálně. Korektor si do nich
sáhne, když si není jistý vazbou. Instalace je v [README](../README.md).

## Model si o češtině nerozhodne sám

Generovaná čeština má jednu zákeřnou vlastnost: spojení bývá gramaticky
možné i významově srozumitelné, jenže ho žádný český mluvčí takto nepoužije.
A model vlastní práci posoudit neumí - když se ho zeptáš, jestli spojení
zní česky, většinou si svou volbu obhájí.

Proto korektor u sporné vazby nehádá od oka. Ve složce `nastroje/` jsou
dva skripty, které sahají do lokální databáze:

- `vazby.py přiznat` - valenční rámce slovesa z VALLEXu 4.5 (2 772
  českých sloves, ÚFAL UK): jaké pády, předložky a spojky si sloveso
  žádá a jaký má vid
- `spojeni.py "hraje klíčovou roli"` - frekvence spojení v n-gramech
  z české Wikipedie

## Kontrolní kolokace

Frekvenční kontrola má slabinu: nerozliší "tohle se neříká" od "tohle
korpus nepokrývá". Korektor to řeší kontrolní kolokací - k podezřelému
spojení přibalí do téže dávky spojení, o kterém ví, že je správné. Nula
jen u podezřelého ukazuje, že vada je ve vazbě; nula u obou znamená, že
data na doménu nestačí a rozhoduje úsudek.

## Kudy to prochází

```
zadání -> skill (pravidla stylu) -> draft
                                      |
                           korektor (nezná zadání)
                                      |  max 3 dotazy
                            +---------+---------+
                            |                   |
                        vazby.py            spojeni.py
                        VALLEX 4.5          n-gramy z Wikipedie
                            |                   |
                            +-- lokální data ---+
                                      |
                               nálezy -> přepis
```

A poctivě k rozsahu, ať to nevypadá robustněji, než to je: nejde
o kontrolu každé věty. Do dat si smí sáhnout i skill při psaní, ale
pravidelně je používá až korektor ve vícefázovém režimu - a i ten smí na
text položit nejvýš tři dotazy. Zbytek pořád rozhoduje úsudkem. Dokud
data nepostavíš, běží skill i korektor dál, jen bez téhle opory.

## Licence a proč se data nedistribuují

VALLEX je pod licencí CC BY-NC-SA, tedy jen pro nekomerční užití. Proto
a kvůli velikosti se data nedistribuují s pluginem - každý si je postaví
na svém stroji příkazem `/pis-cesky:data` (250 MB na disku). Data
z české Wikipedie jsou pod CC BY-SA.

Kam se uloží, rozhoduje `nastroje/datadir.py`: přepíše to proměnná
`PIS_CESKY_DATA`, jinak padnou do sdíleného adresáře uživatele mimo
instalaci pluginu. Aktualizace pluginu je proto nezahodí a stavějí se
jen jednou.

## Cesty ke skriptům

Skripty si skill volá plnou cestou přes `${CLAUDE_PLUGIN_ROOT}`, protože
relativní cesta by mířila do adresáře, kde zrovna pracuješ, ne do
pluginu. Data si hledají podle svého vlastního umístění, takže je můžeš
spustit odkudkoli:

```bash
python3 ${CLAUDE_PLUGIN_ROOT}/nastroje/vazby.py přiznat
python3 ${CLAUDE_PLUGIN_ROOT}/nastroje/spojeni.py "hraje klíčovou roli"
```
