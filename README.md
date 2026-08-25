# pis-cesky

[![Release](https://img.shields.io/github/v/release/rajtik76/pis-cesky?label=release)](https://github.com/rajtik76/pis-cesky/releases)
[![Claude Code](https://img.shields.io/badge/Claude_Code-plugin-5A32FB)](https://github.com/rajtik76/pis-cesky)
[![Jazyk](https://img.shields.io/badge/jazyk-čeština-11457E)](README.md)
[![Licence](https://img.shields.io/badge/licence-MIT-green)](LICENSE)

Plugin pro Claude Code, který mění způsob, jakým model generuje české texty.
Ne tím, že by mu zakazoval jednotlivá slova nebo výrazy, ale tím, že mu určuje pozici, ze které text vzniká.
Můj názor je ten, že rozdíl mezi lidským a AI textem v češtině není ve slovníku, ale
v tom, kdo a jak obsah vypráví.

Samozřejmě jsem si vědom toho, že to není univerzální nástroj pro tvorbu dokonalých
českých textů. Je to jen můj aktuální pohled na to, jak současné AI modely generují české texty,
a pokus s tím něco udělat.
Cílem nebylo vytvořit skill, aby AI psala jako člověk ale aby generovala texty, které budou
pro člověka lépe čitelné a aby se odstranily ty doslovné překlady z AJ, které v češtině
zní strašně, např.:"Duck curve: profil dne, který slunce překreslilo", "proč cena v poledne padá, občas až do záporu" atd.

### Co skill je

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

## Model si o češtině nerozhodne sám

Frekvenční data o generované češtině tedy nemám. Data o češtině samotné
ale ano - a ta odpovídají na jinou, praktičtější otázku.

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

Frekvenční kontrola má slabinu: nerozliší "tohle se neříká" od "tohle
korpus nepokrývá". Korektor to řeší kontrolní kolokací - k podezřelému
spojení přibalí do téže dávky spojení, o kterém ví, že je správné. Nula
jen u podezřelého ukazuje, že vada je ve vazbě; nula u obou znamená, že
data na doménu nestačí a rozhoduje úsudek.

A poctivě k rozsahu, ať to nevypadá robustněji, než to je: nejde
o kontrolu každé věty. Do dat si smí sáhnout i skill při psaní, ale
pravidelně je používá až korektor ve vícefázovém režimu - a i ten smí na
text položit nejvýš tři dotazy. Zbytek pořád rozhoduje úsudkem. Dokud
data nepostavíš, běží skill i korektor dál, jen bez téhle opory.

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

VALLEX je pod licencí CC BY-NC-SA, tedy jen pro nekomerční užití. Proto
a kvůli velikosti se data nedistribuují s pluginem - každý si je postaví
na svém stroji příkazem `/pis-cesky:data` (250 MB na disku, podrobnosti
v sekci Instalace).

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
a česká Wikipedie (CC BY-SA), viz kap. výše.

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
```

Soubory se načítají, až když jsou potřeba - kořenový SKILL.md řekne, který
otevřít. Skill má zatím technický a úřední styl; osobní
a marketingový svůj teprve dostanou a do té doby jedou na obecných
pravidlech.

Protože skill není detektor, ale předpis, na doplnění dalšího žánru nepotřebuješ
dvojici AI text vs. lidský text. Stačí kvalitní texty psané lidmi v daném žánru.

## Instalace

Je to plugin pro Claude Code:

```
/plugin marketplace add rajtik76/pis-cesky
/plugin install pis-cesky@pis-cesky
```

Volitelně si postav jazyková data pro ověřování vazeb a spojení (VALLEX
a n-gramy z Wikipedie, viz Zdroje dat). Do repa se necommitují kvůli
licenci a velikosti, takže je plugin v sobě nemá - stáhnou se až na lokálu.
Na to je vlastní příkaz:

```
/pis-cesky:data
```

Ten ví, kam se data ukládají, a skript spustí sám. Data zabírají na disku
zhruba 250 MB a leží ve sdíleném adresáři uživatele mimo instalaci
pluginu (vypíše ho `nastroje/datadir.py`, přepíše proměnná
`PIS_CESKY_DATA`), takže je aktualizace pluginu nezahodí - stavějí se
jen jednou. Bez nich skill funguje dál, ale s tím, že korektor nemůže
ověřovat vazby a kolokace v datech.

Kdo si repo klonuje ručně, může ho stále dát rovnou do adresáře skillů -
`~/.claude/skills/pis-cesky` - a Claude Code ho podle manifestu načte jako
plugin sám, bez registrace marketplace:

```bash
git clone https://github.com/rajtik76/pis-cesky.git ~/.claude/skills/pis-cesky
```

Na vývoj a zkoušení bez instalace je `claude --plugin-dir ./pis-cesky`;
po úpravách stačí `/reload-plugins`.

## Jak skill používat

Že se skill zapojil, poznáš podle prvního řádku odpovědi - a zároveň z něj
vyčteš, podle kterého stylu text vzniká:

```
🇨🇿 Píšu česky (styl: technický)
🇨🇿 Píšu česky (styl: úřední)
🇨🇿 Píšu česky (styl: obecný)
```

Skill se aktivuje sám, když píšeš delší český text.
O tom rozhoduje popis ve frontmatter. Když se na to spolehnout nechceš,
vynutíš ho příkazem `/pis-cesky:pis-cesky` a styl si necháš určit skillu.

Styl vynutíš dvěma způsoby. Buď zkratkou:

```
/pis-cesky:uredne napiš odvolání proti platebnímu výměru
/pis-cesky:technicky popiš, jak zapnout OPcache
```

nebo argumentem hlavního příkazu (`/pis-cesky:pis-cesky uredne ...`),
případně prostou větou ("piš to úředně"). Na tvaru argumentu nezáleží,
projde `uredne`, `úředně` i `uredni`, u technického stylu `technicky`
i `tech`.

Zkratky nekopírují pravidla, jen přeskočí určování žánru. Hodí se, když
zadání samo o sobě žánr neprozradí - třeba u úředního dopisu
o technické věci.

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
zhruba 30 tisíc tokenů - u tří článků tedy počítej se zhruba sto tisíci.
Korektor běží jako samostatný agent (`agents/korektor.md`) s ořezanou
výbavou, mechanické kontroly (párové znaky, pomlčky, mezery) převzal
skript `nastroje/mechanika.py` a dotazy do jazykových dat mají strop tří
volání; krátké texty do zhruba 300 slov se navíc slučují po dvou až
třech na jednoho korektora. Za tu cenu dostaneš i věcnou kontrolu -
v testech korektor zachytil rozpor mezi dvěma tvrzeními o passkeys,
nesourodý základ dvou procent z téhož průzkumu a model zařazený do
nesprávné řady. Pro krátké texty a poznámky vícefázový režim nepouštěj,
běžný průchod skillem stačí.

Skill k tomu doporučuje nejsilnější dostupný model, dnes Opus, protože
slabší model neselže nahlas: nálezy vrátí, jen povrchní. Korektor má
proto `model: opus` přímo v definici agenta - nehrozí, že by korekturu
tiše převzal slabší model hlavní session. Druhé kolo, zúžené na kontrolu
přepsaných pasáží, jede úsporněji na Sonnetu.

Aby texty psané v jedné dávce neměly stejný styl a tudíž nevypadaly stejně, řeší se to
plánováním před psaním, ne kontrolou po něm: skill si ke každému textu
předem vypíše osu, první větu, konec a autorskou pózu, porovná je a začne s generováním.
Ukázky obou sad najdeš v adresáři `priklady/`.

Skripty na ověřování vazeb a spojení (viz kap. "Model si o češtině
nerozhodne sám") si skill volá plnou cestou přes `${CLAUDE_PLUGIN_ROOT}`,
protože relativní cesta by mířila do adresáře, kde zrovna pracuješ, ne do
pluginu. Data si hledají podle svého vlastního umístění, takže je můžeš
spustit odkudkoli.

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

## Závěr
Tento repozitář není, jako mnoho jiných, plně generovaný pomocí AI.
AI samozřejmě k jeho tvorbě používám (přece jenom je to AI skill)  
ale převážně k analýze a testování výsledků. Drtivou většinu obsahu manuálně
reviduji a testuji.