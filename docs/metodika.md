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

**Marketingový styl** - deset zdrojů, 239 článků, ~196 tisíc slov.
Rozbor v `analyza/destilace-marketing.md`, dílčí rozbory po osách
(`marketing-bonami.md`, `marketing-notino.md`, `marketing-vceliste.md`,
`marketing-b2c-eshopy.md`, `marketing-b2b-finance.md`,
`marketing-vyrobce-casopis.md`):

| Zdroj                  | Co odtud                            | Čím se liší                              |
|------------------------|-------------------------------------|------------------------------------------|
| bonami.cz              | 49 článků magazínu (2019-2020)      | e-shop s bydlením, krátké texty k fotkám |
| blog.notino.cz         | 41 článků + O nás (2017-2021)       | e-shop s kosmetikou, hosté v 1. osobě    |
| blog.rohlik.cz         | 20 článků (2016-2021)               | online supermarket, rozhovory s dodavateli |
| blog.decathlon.cz      | 12 článků, 9 autorů (2020-2021)     | sportovní řetězec, mužský čtenář, esej   |
| blog.fischer.cz        | 15 článků (2020-2021)               | cestovní kancelář, průvodcovský registr  |
| vceliste.cz            | 40 článků, 24 autorů (2011-2021)    | agentura, praktici i prodejci služby     |
| blog.freelo.cz         | 15 článků, 12 autorů (2016-2021)    | B2B software, autoři v 1. osobě          |
| portu.cz/blog          | 20 článků, 9 autorů (2017-2021)     | finance, čísla se zdrojem, bez imperativu |
| skoda-storyboard.com   | 12 článků (2016-2021)               | výrobce, značka jako téma, ne nabídka    |
| maximum.drmax.cz       | 15 článků (2016-2021)               | zákaznický časopis, produkt nula         |

Sedm oborů, pět typů firem, tři čtenáři (žena B2C, muž B2C, podnikatel).
Všechny zdroje jsou z Wayback Machine, každý článek má v hlavičce odkaz na
snapshot do konce roku 2021. U Včeliště to bylo nutné: živý web prošel po
roce 2022 revizí a tři články byly přepsané, jeden z 85 %. Vedle korpusu
stojí sekundární zdroj - 16 rozborů jazyka české reklamy z Markething.cz
(2012-2021), viz `analyza/markething-sekundarni.md`. Nejsou to vzory, ale
kritika zevnitř oboru: co Češi na českém marketingu považovali za chybu
dřív, než existoval generovaný text.

Hlavní nález destilace: obsahový marketing nemá jeden hlas, ale čtyři
registry podle vzdálenosti od pokladny - prodejce-rádce, praktik-firma,
vypravěč, vydavatel - a korpus je nemíchá. Imperativ klesá s vzdáleností
od pokladny (e-shop 1,9 na 100 slov, výrobce 0,1), superlativ je nejvyšší
tam, kde chybí autor, a drží ho číslo.

Krátké prodejní copy (slogan, landing page, newsletter) se před rokem
2022 v použitelném objemu sehnat nepodařilo: soutěžní archivy jsou
obrazové, diplomky citují reklamu screenshotem, Webarchiv NK je přístupný
jen v budově knihovny. Ke krátkému copy tak skill mluví jen přes
Markething a říká to.

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
  marketing.md           marketingový styl, postaveno na reálných textech
  vicefazove.md          draft → korektura bez záměru → přepis
skills/technicky/        zkratka /pis-cesky:technicky
skills/uredne/           zkratka /pis-cesky:uredne
skills/marketing/        zkratka /pis-cesky:marketing
skills/data/             /pis-cesky:data - postaví jazyková data
analyza/                 rozbory zdrojů, ze kterých pravidla vznikla
nastroje/                ověřování vazeb a spojení, kontrola mechaniky
priklady/                stejná zadání se skillem a bez něj
docs/                    tenhle adresář
```

Soubory se načítají, až když jsou potřeba - kořenový SKILL.md řekne, který
otevřít. Skill má technický, úřední a marketingový styl; osobní text
svůj teprve dostane a do té doby jede na obecných pravidlech.

Protože skill není detektor, ale předpis, na doplnění dalšího žánru nepotřebuješ
dvojici AI text vs. lidský text. Stačí kvalitní texty psané lidmi v daném žánru.

## Stav

Rozpracované: obecná pravidla, technický styl, úřední styl, marketingový
styl a vícefázový režim. Osobní text čeká na rozbor vzorků.

U marketingového stylu je mezera pojmenovaná výš: korpus je obsahový
marketing, krátké prodejní copy chybí. Decathlon a Fischer mají jen
2020-2021 (starší archiv neexistuje), Škoda a Dr.Max jsou jediní
zástupci svého typu a část Škody je překlad z němčiny - vzorce doložené
jen tam jsou v destilaci označené jako slabší.

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
