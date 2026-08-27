# pis-cesky

[![Release](https://img.shields.io/github/v/release/rajtik76/pis-cesky?label=release)](https://github.com/rajtik76/pis-cesky/releases)
[![Claude Code](https://img.shields.io/badge/Claude_Code-plugin-5A32FB)](https://github.com/rajtik76/pis-cesky)
[![Jazyk](https://img.shields.io/badge/jazyk-čeština-11457E)](README.md)
[![Licence](https://img.shields.io/badge/licence-MIT-green)](LICENSE)

Plugin pro Claude Code, který mění způsob, jakým model generuje české texty.
Ne tím, že by mu zakazoval jednotlivá slova nebo výrazy, ale tím, že mu určuje pozici, ze které text vzniká.
Můj názor je ten, že rozdíl mezi lidským a AI textem v češtině není ve slovníku, ale
v tom, kdo a jak obsah vypráví.

Cílem nebylo vytvořit skill, aby AI psala jako člověk ale aby generovala texty, které budou
pro člověka lépe čitelné a aby se odstranily ty doslovné překlady z AJ, které v češtině
zní strašně, např.:"Duck curve: profil dne, který slunce překreslilo", "proč cena v poledne padá, občas až do záporu" atd.

## Instalace

Je to plugin pro Claude Code:

```
/plugin marketplace add rajtik76/pis-cesky
/plugin install pis-cesky@pis-cesky
```

Volitelně si postav jazyková data pro ověřování vazeb a spojení:

```
/pis-cesky:data
```

Příkaz ví, kam se data ukládají, a skript spustí sám. Zaberou na disku
zhruba 250 MB a leží ve sdíleném adresáři uživatele mimo instalaci
pluginu, takže je aktualizace pluginu nezahodí - stavějí se jen jednou.
Bez nich skill funguje dál, jen si korektor nemůže ověřovat vazby
a kolokace v datech. Podrobnosti v [docs/jazykova-data.md](docs/jazykova-data.md).

Kdo si repo klonuje ručně, může ho stále dát rovnou do adresáře skillů -
`~/.claude/skills/pis-cesky` - a Claude Code ho podle manifestu načte jako
plugin sám, bez registrace marketplace:

```bash
git clone https://github.com/rajtik76/pis-cesky.git ~/.claude/skills/pis-cesky
```

Na vývoj a zkoušení bez instalace je `claude --plugin-dir ./pis-cesky`;
po úpravách stačí `/reload-plugins`.

## Rychlý start

Skill se aktivuje sám, když píšeš delší český text. Že se zapojil, poznáš
podle prvního řádku odpovědi, kde je i styl, podle kterého text vzniká:

```
🇨🇿 Píšu česky (styl: technický)
```

Styl si můžeš vynutit zkratkou:

```
/pis-cesky:technicky popiš, jak zapnout OPcache
/pis-cesky:uredne napiš odvolání proti platebnímu výměru
```

U textu, který uvidí i někdo jiný než ty, se skill před psaním zeptá na vícefázový
režim: draft, korektura nezávislým agentem bez znalosti zadání a přepis.
Chytá to chyby, které při vlastním čtení neuvidíš, ale stojí to navíc
zhruba 30 tisíc tokenů na text.

Zbytek ovládání, další prompty a rozbor ceny jsou
v [docs/pouzivani.md](docs/pouzivani.md).

## Co skill je

Nástroj na **psaní nového českého textu**. Dostane téma nebo podklad
a napíše text, který na první pohled nevypadá jako přeložený z angličtiny.

- Podkladem může být cokoli - téma, tvoje poznámky, stažená stránka, cizí
  dokument. Skill si z něj vezme informace, ale formulace ani stavbu
  nepřebírá; výstup je nový text.
- **Vlastní žánrová pravidla mají zatím dva styly** - technický (článek,
  návod, dokumentace, README) a úřední (žádost, odvolání, stížnost,
  odpověď úřadu, metodika). Obojí je postavené na rozboru reálných textů
  psaných lidmi.
- Osobní text a marketing napíše taky, ale řídí se u nich jen obecnou
  částí, takže výsledek nemá o co opřít. Další styly budu přidávat
  postupně, vždycky až po rozboru vzorků.
- Umí si na sebe zavolat korekturu: nezávislý agent, který nezná zadání,
  projde draft a hledá chyby, které autor při vlastním čtení nevidí.

## Co skill není

**Není korektor tvého textu.** Když mu dáš hotový článek s tím, ať ho opraví,
pravidla sice použije, ale nemá pojmenované, kam až smí sáhnout - u textu,
který je celý vata, ho přepíše k nepoznání. Jestli chceš svůj text jen
opravit a pořád ho poznat, tenhle skill na to zatím není.

**Není překladač.** Překlad má vlastní zásady - hlavně že se z něj nesmí
ztratit žádné tvrzení, ani špatně napsané. Skill naopak vatu škrtá, což je
u překladu vada.

**Není detektor AI textu.** Nepozná jestli něco psal člověk, nebo model.

**Není seznam zakázaných slov.** Blacklist typu "delve into" funguje
v angličtině, protože ty fráze v lidském textu skoro nejsou. V češtině
selže: "hraje klíčovou roli" patří do úředního rejstříku dávno před
ChatGPT a ve výroční zprávě je na místě. Signálem není přítomnost fráze,
ale způsob jejího užití - a to blacklist nepozná. Podrobněji
v [docs/metodika.md](docs/metodika.md).

## Model si o češtině nerozhodne sám

Model vlastní práci posoudit neumí - když se ho zeptáš, jestli spojení zní
česky, většinou si svou volbu obhájí. Korektor proto vazbu neodhaduje od
oka, ale ověří si ji v lokálních jazykových datech:

- `vazby.py přiznat` - valenční rámce slovesa z VALLEXu 4.5 (2 772
  českých sloves, ÚFAL UK)
- `spojeni.py "hraje klíčovou roli"` - frekvence spojení v n-gramech
  z české Wikipedie

Abych nepřeháněl: nejde o kontrolu každé věty. Pravidelně data používá až
korektor ve vícefázovém režimu a i ten smí položit nejvýš tři dotazy na
text. Jak korektor odliší "tohle se neříká" od "tohle korpus nepokrývá",
je v [docs/jazykova-data.md](docs/jazykova-data.md).

## Kde je co

- [docs/metodika.md](docs/metodika.md) - proč ne blacklist, zdroje dat, stavba repa, stav a mezery
- [docs/jazykova-data.md](docs/jazykova-data.md) - VALLEX a n-gramy, kontrolní kolokace, licence
- [docs/pouzivani.md](docs/pouzivani.md) - ovládání, vícefázový režim, cena, příklady promptů
- `analyza/` - rozbory zdrojů, ze kterých pravidla vznikla
- `priklady/` - stejná zadání se skillem a bez něj

Samozřejmě jsem si vědom toho, že to není univerzální nástroj pro tvorbu dokonalých
českých textů. Je to jen můj aktuální pohled na to, jak současné AI modely generují české texty,
a pokus s tím něco udělat.

## Závěr
Tento repozitář není, jako mnoho jiných, plně generovaný pomocí AI.
AI samozřejmě k jeho tvorbě používám (přece jenom je to AI skill)
ale převážně k analýze a testování výsledků. Drtivou většinu obsahu manuálně
reviduji a testuji.
