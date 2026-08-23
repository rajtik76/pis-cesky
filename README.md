# pis-cesky

[![Release](https://img.shields.io/github/v/release/rajtik76/pis-cesky?label=release)](https://github.com/rajtik76/pis-cesky/releases)
[![Claude Code](https://img.shields.io/badge/Claude_Code-skill-5A32FB)](https://github.com/rajtik76/pis-cesky)
[![Jazyk](https://img.shields.io/badge/jazyk-čeština-11457E)](README.md)
[![Licence](https://img.shields.io/badge/licence-MIT-green)](LICENSE)

Skill pro Claude Code, který mění způsob, jakým model generuje české texty. 
Ne tím, že by mu zakazoval jednotlivá slova nebo výrazy, ale tím, že mu určuje pozici, ze které text vzniká. 
Můj názor je ten, že rozdíl mezi lidským a AI textem v češtině není ve slovníku, ale 
v tom, kdo a jak obsah vypráví.

Samozřejmě jsem si vědom toho, že to není univerzální nástroj pro tvorbu dokonalých 
českých textů. Je to jen můj aktuální pohled na to, jak současné AI modely generují české texty, 
a pokus s tím něco udělat.
Cílem nebylo vytvořit skill, aby AI psala jako člověk ale aby generovala texty, které budou
pro člověka lépe čitelné a aby se odstranili ty doslovné překlady z AJ, které v češtině
zní strašně, např.:"Duck curve: profil dne, který slunce překreslilo", "proč cena v poledne padá, občas až do záporu" atd.

### Co skill je

Nástroj na **psaní nového českého textu**. Dostane téma nebo podklad
a napíše text, který na první pohled nevypadá jako přeložený z angličtiny.

- Podkladem může být cokoli - téma, tvoje poznámky, stažená stránka, cizí
  dokument. Skill si z něj vezme informace, ale formulace ani stavbu
  nepřebírá; výstup je nový text.
- **Žánrová pravidla má zatím jen technický sloh** - článek, návod,
  dokumentace, README. Postavená jsou na rozboru reálných textů psaných
  lidmi.
- Osobní text, marketing a úřední komunikaci napíše taky, ale řídí se u nich
  jen obecnou částí ale výsledek nemá o co opřít. Další styly budu přidávat
  postupně, vždycky až po rozboru vzorků.
- Umí si na sebe zavolat korekturu: nezávislý agent, který nezná zadání,
  projde draft a hledá chyby, které autor při vlastním čtení nevidí.

### Co skill není

**Není korektor tvého textu.** Když mu dáš hotový článek s tím, ať ho opraví,
pravidla sice použije, ale nemá pojmenované, kam až smí sáhnout - u textu,
který je celý vata, ho přepíše k nepoznání. Jestli chceš svůj text jen
opravit a pořád ho poznat, tenhle skill na to zatím není.

**Není překladač.** Překlad má vlastní zásady - hlavně že se z něj nesmí
ztratit žádné tvrzení, ani špatně napsané. Skill naopak vatu škrtá, což je
u překladu vada.

**Není detektor AI textu.** Nepozná jestli něco psal člověk, nebo model.

**Není seznam zakázaných slov.** Proč zrovna v češtině blacklist selže,
rozvádí následující kapitola.

## Proč ne seznam zakázaných frází?

Většinou se tu na GitHubu setkávám se strojovým překladem anti-slop skillů z angličtiny,
ale tyto skilly stojí na principu blacklistu: "delve into", "in today's
fast-paced world", "it's important to note". Funguje to, protože ty fráze
v lidském anglickém textu skoro nejsou. Model je používá nápadně častěji než
člověk takže je stačí odstranit.

V češtině to ale takhle nefunguje:
1. **Výrazy typu: "hraje klíčovou roli", "je důležité zdůraznit" nebo "v neposlední
řadě"** patří do českého oficiálního rejstříku dávno před ChatGPT. Např. ve výroční
zprávě jsou na místě. Signálem tady není přítomnost fráze, ale způsob jejího užití.
2. **klišé použité s odstupem není slop**. Když někdo napíše "lze směle
označit za game changer" a ví přitom, co dělá, je to styl. Blacklist to
neprávem označí za slop. Rozdíl není v tom, co je napsané, ale jak.
3. **frekvenční analýza v češtině neexistuje**. Pro angličtinu jsou data
(Buffer analyzoval 52 milionů příspěvků, Wikipedie vede přehled typických znaků AI
textů). A čeština? Nic! České repozitáře sice existují, ale opisují jeden od druhého.

## Zdroje dat

Pochází z českých textů psaných lidmi a publikovaných před listopadem 2022, tedy
předtím, než se generovaný text dostal do běžného provozu.

Podrobně analyzované rozbory jsou v adresáři `analyza/`:

| Zdroj          | Co odtud                                   | Žánr                             |
|----------------|--------------------------------------------|----------------------------------|
| blog.nette.org | 36 článků (2012-2022), 6 autorů            | profesionální technický blog     |
| blog.root.cz   | 27 článků + diskuse (2020-2021), 10 autorů | komunitní blogy, syrové psaní    |
| nettech.cz     | 10 článků (2015-2021)                      | technický návod, malá firma      |

Nástroje ve složce `nastroje/` navíc stavějí na veřejných datech: VALLEX
4.5 (valenční slovník sloves, ÚFAL UK, CC BY-NC-SA) a české Wikipedii
(frekvence spojení, CC BY-SA).

## Jak to celé funguje

Univerzální "piš česky jako člověk" je zadání bez obsahu. Cestopis, technický
návod a úřední dokument se chovají jazykově jinak a pravidlo, které platí pro
všechny tři, tím pádem u AI nefunguje. Navíc má silné sklony k doslovným překladům 
z angličtiny což vede k ještě horším výsledkům.

```
SKILL.md         obecná pravidla, načtou se vždy
technicky.md     technický žánr, postaveno na reálných textech
vicefazove.md    draft → korektura bez záměru → přepis
analyza/         rozbory korpusů, ze kterých pravidla vznikla
nastroje/        ověřování vazeb a spojení v datech
priklady/        stejná zadání se skillem a bez něj
```

Soubory se načítají, až když jsou potřeba - kořenový SKILL.md řekne, který
otevřít. Žánrový soubor má zatím jen technický text; osobní, marketingový
a úřední svůj teprve dostanou a do té doby jedou na obecných pravidlech.

Protože skill není detektor, ale předpis, na doplnění dalšího žánru nepotřebuješ
dvojici AI text vs. lidský text. Stačí dobré lidské psaní v tom žánru.

## Instalace

```bash
git clone https://github.com/rajtik76/pis-cesky.git ~/.claude/skills/pis-cesky
```
```bash
bash nastroje/stahni-data.sh
```

Hlášku o aktivaci skillu si vypisuje sám skill, takže záleží na tom, jestli ho
model poslechne. Kdo chce mít jistotu, přidá si do `~/.claude/settings.json`
hook, který tuto hlášku vypíše sám od sebe a jen u tohohle skillu:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Skill",
        "hooks": [
          {
            "type": "command",
            "command": "jq -e '.tool_input.skill == \"pis-cesky\"' >/dev/null 2>&1 && jq -nc '{systemMessage:\"🇨🇿 Píšu česky (skill aktivován)\"}' || true"
          }
        ]
      }
    ]
  }
}
```

Máš-li v `settings.json` hooky už zavedené, přidej ten blok do pole
`PreToolUse` vedle nich, ať si je nepřepíšeš. Aby se změna projevila, otevři
jednou `/hooks` nebo restartuj sezení. Potřebuje `jq`.

## Jak skill používat

Že se skill zapojil, poznáš podle prvního řádku odpovědi:

```
🇨🇿 Píšu česky (skill aktivován)
```

Skill se aktivuje sám, když píšeš delší český text.
O tom rozhoduje popis ve frontmatter. Když se na to spolehnout nechceš,
vynutíš ho příkazem `/pis-cesky`.

U textu, který někdo uvidí - článek, dokumentace, e-mail ven z firmy - se
skill ještě před psaním zeptá, jestli má pustit vícefázový režim: draft
podle žánrových pravidel, korektura nezávislým agentem, který nezná zadání
(a proto vidí chyby, které autor nevidí) a nakonec přepis a protokol oprav.   
Můžeš si o něj říct i sám ("piš vícefázově"). Vzniklo to
z poznatku, že text napoprvé není nikdy bez chyb a autorovo čtení vlastního
textu nechytí chyby významu.

Druhé kolo korektury se pouští podle rozsahu změn, a to i u jediného textu:
měnila se fakta nebo se přepisovaly celé odstavce, jde text na kontrolu
znovu. Když se opravovaly jen vazby a slova, stačí kolo jedno.

Pozor na cenu. Každý text dostane vlastního korektora a ten spotřebuje
zhruba 40 až 50 tisíc tokenů - u tří článků tedy počítej se sto padesáti
tisíci. Za tu cenu ale dostaneš i věcnou kontrolu - v testech korektor
zachytil rozpor mezi dvěma tvrzeními o passkeys, nesourodý základ dvou
procent z téhož průzkumu a model zařazený do nesprávné řady. Pro krátké
texty a poznámky vícefázový režim nepouštěj, běžný průchod skillem stačí.

Skill k tomu doporučuje nejsilnější dostupný model, dnes Opus, protože
slabší model neselže nahlas: nálezy vrátí, jen povrchní. Ohlídej si přitom
jednu past - korektor běží na modelu hlavní session, takže když sám jedeš
na Haiku, dostaneš i korekturu z Haiku. Skill si v takovém případě má
silnější model vyžádat explicitně.

Aby texty psané v jedné dávce neměli stejný styl a tudíž nevypadali stejně, řeší se to
plánováním před psaním, ne kontrolou po něm: skill si ke každému textu
předem vypíše osu, prvni větu, konec a autorskou pózu, porovná je a začne s generováním.
Ukázky obou sad najdeš v adresáři `priklady/`.

Korektura se navíc může opřít o lokální jazyková data - `nastroje/` umí
stáhnout VALLEX (valenční rámce 4 700 českých sloves, CC BY-NC-SA) a
postavit frekvenční databázi spojení z české Wikipedie:

Pak jde vazba slovesa ověřit příkazem `python3 nastroje/vazby.py přiznat`
a existence spojení příkazem `python3 nastroje/spojeni.py "hraje klíčovou
roli"`. Data se do repa necommitují, každý si je staví lokálně.

## Příklady promptů

Skill se pouští sám, tyhle prompty jsou na to, abys ho řídil. Všechny jsem
vyzkoušel na krátkých textech a výsledky odpovídají popisu.

**Jen draft, bez korektury**

```
napiš 3 věty pro vývojářský blog o tom, proč zapnout OPcache.
Korekturu nepouštěj, chci jen draft.
```

Skill se pak neptá a v předání sám uvede, že text korekturou neprošel.

**Rovnou vícefázově, bez ptaní**

```
napiš článek o X, piš vícefázově
```

Přeskočí dotaz a pustí draft, korekturu nezávislým agentem a přepis.

**Tykání**

```
napiš návod k X, čtenáři tykej
```

Vykání je výchozí, takže tohle je jediný způsob, jak dostat tykání
u dokumentace nebo firemního textu. U vývojářského blogu na to skill
přijde i sám ze zadání. Zvolené oslovení pak drží celým textem.

**Text psaný ženou**

```
napiš 3 věty o tom, jak jsem ladila cache v Redisu. Piš za mě v ženském rodě.
```

Funguje, ale drží to jen na instrukci v promptu. Skill pro rod pisatele
žádné pravidlo nemá a korektor ho nekontroluje, takže na delším textu se
může rod v půlce ztratit a nikdo to nechytí.

**Nový text z existujícího podkladu**

```
napiš článek podle @podklad.md
```

Podkladem může být cokoli - cizí dokument, poznámky, stažená stránka.
Výstup je nový text: skill si z podkladu vezme informace, ale formulace
ani stavbu z něj nepřebírá. Kdo chce naopak svůj text jen opravit a pořád
ho poznat, na to skill není, viz "Co skill není".

**Víc textů v jedné dávce**

```
napiš tři články na témata A, B, C
```

U dvou a víc textů si skill nejdřív vypíše plán ke každému z nich a dá jim
jinou kostru dřív, než napíše první větu. Pak teprve píše.

## Stav

Rozpracované: obecná pravidla, technický žánr a vícefázový režim.
Osobní text čeká na rozbor vzorků, marketing na vzorky samotné,
formální rejstřík na vlastní pravidla.

Pravidla ve skillu vznikají z chyb, které při psaní nachytám a ručně opravím.
Většina z nich patří do jedné rodiny: přeložím obsah slova, ale nepřenesu,
co si české sloveso žádá kolem sebe. Zobecněná chyba jde rovnou do
`SKILL.md`; dřív jsem k tomu vedl ještě deník jednotlivých záchytů, ale
měřením se ukázalo, že korektorovi nic nepřidává a jen žere tokeny, tak
šel pryč.

Otevřené je to, co zatím nemá řešení: jak formulovat pravidlo o klišé
s odstupem tak, aby ho model uměl použít a nejen odkývat. A jak výsledek
ověřit - detektorem AI textu to tady změřit nejde, cílem není projít jako
člověk.

## Závěr
Tento repozitář není, jako mnoho jiných, plně generovaný pomocí AI.
AI samozřejmě k jeho tvorbě používám (přece jenom je to AI skill)  
ale převážně k analýze a testování výsledků. Drtivou většinu obsahu manuálně 
reviduji a testuji.