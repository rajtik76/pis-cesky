# Metodika

Jak pravidla vznikla, z čeho jsou odvozená a co v nich zatím chybí.
Návod k instalaci a používání je v [README](../README.md).

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

**Technický styl** - tři zdroje, ~79 tisíc slov. Rozbory v `analyza/`:

| Zdroj          | Co odtud                                   | Čím se liší                   |
|----------------|--------------------------------------------|-------------------------------|
| blog.nette.org | 36 článků (2012-2022), 6 autorů            | profesionální blog s redakcí  |
| blog.root.cz   | 28 článků + diskuse (2020-2021), 10 autorů | komunita, syrové psaní        |
| nettech.cz     | 10 článků (2015-2021)                      | malá firma, návody bez redakce|

**Úřední styl** - čtyři zdroje, 68 dokumentů, ~180 tisíc slov. Rozbor
v `analyza/destilace-uredni.md`:

| Zdroj                          | Co odtud                                  | Čím se liší                    |
|--------------------------------|-------------------------------------------|--------------------------------|
| sbirka.nssoud.cz               | 17 rozhodnutí (2005-2021), 9 ročníků       | vrchol žánru, různé senáty     |
| nalus.usoud.cz                 | 8 nálezů (2009-2015), včetně disentu       | ústavní argumentace, já-pozice |
| weby úřadů (106/1999)          | 37 odpovědí od 16 institucí (2012-2021)    | běžný provoz, kolísavá kvalita |
| weby ministerstev              | 6 metodických pokynů od 6 resortů (2009-2018) | výklad úřadu pro úřady      |

Rozptyl kvality je v takto rozličném výběru textů záměrný: vedle precizního textu NSS stojí
odpověď úřadu městské části. Co se najde v obou, je vlastnost stylu; co
jen u slabších pisatelů, je kancelářský slang - a ten je v rozboru uveden jako
negativní vzor, doložený uvnitř stylu samotného.

Datum vydání je u úředních textů ověřitelné přímo v dokumentu (číslo
jednací, datum rozhodnutí), takže hranice před listopadem 2022 tu drží
spolehlivěji než u blogů. Část dokumentů, které úřady mezitím z webu
stáhly, pochází z Wayback Machine.

Stažené texty se do repa necommitují, `data/` je v `.gitignore` - z rozborů
v `analyza/` je u každého vzorce vidět zdroj i citace. Jazyková data pro
`nastroje/` stojí na jiných zdrojích: VALLEX 4.5 (ÚFAL UK, CC BY-NC-SA)
a česká Wikipedie (CC BY-SA), viz [jazyková data](jazykova-data.md).

## Jak to celé funguje

Univerzální "piš česky jako člověk" je zadání bez obsahu. Cestopis, technický
návod a úřední dokument se chovají jazykově jinak a pravidlo, které platí pro
všechny tři, tím pádem u AI nefunguje. Navíc má silné sklony k doslovným překladům
z angličtiny což vede k ještě horším výsledkům.

```
.claude-plugin/          manifest pluginu a marketplace
agents/korektor.md       jazykový korektor - definice subagenta
skills/pis-cesky/
  SKILL.md               obecná pravidla, načtou se vždy
  technicky.md           technický styl, postaveno na reálných textech
  uredni.md              úřední styl, postaveno na reálných textech
  vicefazove.md          draft → korektura bez záměru → přepis
skills/technicky/        zkratka /pis-cesky:technicky
skills/uredne/           zkratka /pis-cesky:uredne
skills/data/             /pis-cesky:data - postaví jazyková data
analyza/                 rozbory zdrojů, ze kterých pravidla vznikla
nastroje/                ověřování vazeb a spojení, kontrola mechaniky
priklady/                stejná zadání se skillem a bez něj
docs/                    tenhle adresář
```

Soubory se načítají, až když jsou potřeba - kořenový SKILL.md řekne, který
otevřít. Skill má zatím technický a úřední styl; osobní
a marketingový svůj teprve dostanou a do té doby jedou na obecných
pravidlech.

Protože skill není detektor, ale předpis, na doplnění dalšího žánru nepotřebuješ
dvojici AI text vs. lidský text. Stačí kvalitní texty psané lidmi v daném žánru.

## Stav

Rozpracované: obecná pravidla, technický styl, úřední styl a vícefázový
režim. Osobní text čeká na rozbor vzorků, marketing na vzorky samotné.

U úředního stylu vím o dvou mezerách. Korpus stojí na textech, které píší
úřady - žádost, odvolání ani stížnost z druhé strany v něm nejsou jako
samostatné dokumenty, jen citované uvnitř odpovědí (zato početně).
A metodika GFŘ je ve vzorku oříznutá na 12 tisíc slov, takže z ní stavba
delšího dokumentu vyčtená není.

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
