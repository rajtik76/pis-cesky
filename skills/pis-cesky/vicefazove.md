# Vícefázové psaní

Doplněk kořenového `SKILL.md`. Otevři ho, když uživatel na dotaz z kapitoly
"Zeptej se na korekturu" odpověděl ano - nebo když si o vícefázový režim
řekl sám.

Text vygenerovaný na první dobrou nikdy není bez chyb - a autorovo čtení
vlastního textu nechytí chyby významu, protože autor zná svůj záměr.
Tenhle skill proto psaní rozděluje: napíšeš, necháš zkontrolovat někým,
kdo záměr nezná, a přepíšeš. Kroky drž v pořadí.

## 1. Draft

Urči žánr a načti pravidla: kořenový `SKILL.md` (pozice pisatele, stavba
věty od slovesa, slovosled, kontroly) plus stylový soubor podle žánru
(`technicky.md`, `uredni.md`).

Než napíšeš první větu, pojmenuj materiál podle kořenového `SKILL.md`: co
zadání nabízí, co znáš z první ruky, kde jsi ignorant. Formu odvoď odtud.

U dvou a víc textů si nejdřív udělej plán a teprve pak piš. Ke každému
textu si vypiš čtyři položky:

- osa, na které text stojí (čísla, čas, prostředí, spor, postup, omyl)
- typ otvíráku
- typ konce
- autorská póza

Pak ty plány porovnej vedle sebe a přepiš je tak, aby se kostry nekryly,
dřív než napíšeš první větu. Tohle není kontrola cizí práce, ale tvoje vlastní plánování - čtyři
položky vedle sebe a shodu vidíš na první pohled, žádný agent k tomu není
potřeba. Sedí-li shoda proto, že texty mají opravdu stejný materiál
(u obou píšeš z cizích pramenů), dej každému aspoň jiný otvírák a jiný
konec.

Kolik shody je ještě únosné, závisí na počtu textů:

- dva až pět textů: žádná shoda kostry, každý stojí na jiné ose
- kolem deseti: jedno až dvě opakování jsou v pořádku
- víc než deset: opakování přibývá a je to normální, trvat na deseti
  odlišných kostrách by vedlo k vymýšlení šroubovaných forem

Cílem není jinakost za každou cenu. Cílem je, aby forma plynula z obsahu -
a když má deset textů jen pět druhů materiálu, pět koster je poctivý
výsledek.

Piš texty jeden po druhém, ne všechny v jednom tahu. Před každým dalším se
podívej na ty hotové - máš je v kontextu a je to jediná chvíle, kdy vlastní
šablonu uvidíš zadarmo.

Fakta ověř dřív, než začneš psát. Když skill žádá údaj z praxe a máš
možnost si věc reálně spustit nebo změřit, udělej to; jinak přiznej
v textu, že píšeš od stolu.

Draft ulož tam, kam řekne uživatel. Když neřekl nic a jde o jeden text do
konverzace, soubor nezakládej - korektorovi ho předáš rovnou v promptu.

## 2. Korektura v čistém kontextu

Než korektora spustíš, projeď text skriptem
`python3 ${CLAUDE_PLUGIN_ROOT}/nastroje/mechanika.py <soubor>` (text bez
souboru mu pošli na stdin s argumentem `-`). Párové znaky, pomlčky,
dvojité mezery a mezery u interpunkce chytí deterministicky za nula
tokenů; jeho nálezy zapracuješ při přepisu a korektor už mechaniku
neřeší.

Spusť subagenta `pis-cesky:korektor` (Agent tool) - kontrolní zadání,
nástroje i formát nálezů má v definici `agents/korektor.md` a nenese
výbavu, kterou nepotřebuje. Zásadní pravidlo: korektor NESMÍ dostat
zadání, konverzaci ani tvůj záměr - jen text. Právě proto uvidí, co ty
nevidíš: on čte text tak, jak ho bude číst čtenář.

Prompt skládej vždy stejně a jen ze dvou věcí:

1. první řádek `Kořen pluginu: <absolutní cesta>` - podle něj korektor
   najde nástroje, kdyby v jeho prostředí nebyla proměnná
   `${CLAUDE_PLUGIN_ROOT}`
2. text draftu (u textů uložených v souborech cesty k nim)

Nic dalšího nepřidávej a formulace neměň. Stejná definice agenta
a stejný začátek promptu napříč korektory znamenají, že se prefix uloží
do cache - N paralelních korektorů ho platí jednou a běží rychleji.

Korektura je z celého postupu nejnáročnější krok, tak na ní nešetři.
Draft je jen generování podle pravidel, kdežto korektor musí rozlišit
jemné vazby, ověřit fakta a obsloužit nástroje; rychlý ani malý model
sem nepatří. Agent má proto v definici `model: opus` - když máš
k dispozici silnější model, předej ho parametrem `model` - a přemýšlení
nech na vysokém nastavení. Slabší model přitom neselže viditelně:
nálezy vrátí, jen budou povrchní, a toho si na první pohled nevšimneš.
Ověřit model jde jednoduše - subagent má své ID v systémovém promptu
a na přímý dotaz ho řekne. Počítej zhruba s 30 tisíci tokeny na jeden
text; korektura běží jednou, takže se to vyplatí.

Jeden text = jeden korektor, jazykový - s jednou výjimkou: texty pod
zhruba 300 slov slučuj po dvou až třech na jednoho korektora. Čistý
kontext to neporušuje, korektor záměr pořád nezná, jen se režie agenta
neplatí vícekrát. Korektora kostry nespouštěj, nemá co s čím porovnávat -
byl by to vyhozený agent i tokeny.

U dvou a víc delších textů pusť N jazykových korektorů paralelně,
každého na jeden text.

Korektora kostry samostatně nepouštěj. Kostru sis rozvrhl v kroku 1
a porovnání plánů je plánování, ne kontrola - stojí pár set tokenů proti
desítkám tisíc za agenta. Zvláštního korektora na kostru zavolej jen
tehdy, když si po dopsání nejsi jistý, jestli texty dopadly podle plánu,
nebo když si o to uživatel řekne. Pak dostane všechny texty a hledá
výhradně shodu stavby, jazyk neřeší.

Levnější varianta, pokud je po ruce: kostru posoudí kdokoli, kdo ty texty
nepsal - druhá session, jiný agent, uživatel. Autorská slepota se týká
psaní, ne čtení, takže třetí strana to zvládne z tabulky čtyř prvků
(otvírák, osa, konec, póza) bez plné korektury.

Kostru nesmí posuzovat hlavní session, i když má nejvíc kontextu. Autor
svou vlastní šablonu nevidí - každou osu volil zvlášť a v tu chvíli mu
dávala smysl, takže tři podobné kostry bude vnímat jako tři různé. Navíc
hlavní session může běžet na slabším modelu než subagenti a rozhodoval by
pak nejslabší článek řetězu. Detekce proto patří subagentovi bez záměru,
rozhodnutí, co s nálezem, zůstává hlavní session.

Korektor kostry vlastní definici agenta nemá - běží zřídka - a zadání
dostane v promptu; jazyk neřeší vůbec:

> Dostáváš několik textů bez kontextu. Nezajímá tě jazyk ani fakta, jen
> jedno: jestli jsou postavené na stejné kostře. Porovnej typ otvíráku,
> osu, na které text stojí, typ konce, rétorické figury, opakující se
> větné stavby a autorskou pózu. Nálezy vrať jako tabulku prvek → jak
> vypadá v jednotlivých textech. Shodu hlas i tehdy, když je každý text
> sám o sobě v pořádku - vada je v tom, že si jsou podobné.

Nástroje na ověřování vazeb (`vazby.py`) a kolokací (`spojeni.py`),
pravidla dávkování dotazů i strop tří volání na korekturu má jazykový
korektor v definici agenta - do promptu je nepiš. Korektor kostry
nástroje nepotřebuje, ten pracuje jen se stavbou. Hlavní session jen
ohlídá, že existují jazyková data.

Data se nestahují spolu s pluginem, staví se lokálně skriptem
`bash ${CLAUDE_PLUGIN_ROOT}/nastroje/stahni-data.sh` (asi 250 MB na
disku, desítky minut). Když skript ohlásí, že soubor chybí, nabídni uživateli, že je
postavíš, a mezitím pokračuj bez nástrojů - korekturu kvůli tomu
nezastavuj. Když si uživatel řekne o postavení dat sám, spusť ten příkaz
rovnou.

Než začneš přepisovat, počkej, až se vrátí všichni korektoři.

Kde Agent tool není (Codex, omezené prostředí), degraduj poctivě: zavři
zadání, otevři soubor znovu a čti ho výhradně očima cizího čtenáře -
u každé věty se ptej "co tahle věta říká někomu, kdo nezná můj záměr".
Kontrolní seznam i nástroje si vezmi z `agents/korektor.md` a mechaniku
pusť skriptem `mechanika.py` i v tomhle režimu. Je to slabší kontrola
než čistý kontext a v předání to přiznej.

Kostru v tomhle režimu neposuzuj od oka. Vypiš si z každého textu čtyři
údaje - první věta, osa textu, poslední věta, autorská póza - do tabulky
vedle sebe a rozhoduj podle ní. Nejde o plnou náhradu, ale tabulka aspoň
donutí porovnávat texty místo dojmu z nich.

## 3. Přepis a předání

Nálezy zapracuj. Nesouhlasit smíš, ale jen s důvodem, který umíš říct
nahlas - "zní mi to líp" důvod není, doložený úzus ano.

U jednoho textu tenhle odstavec přeskoč - shoda kostry se týká jen sad.

Když korektor ohlásí shodu kostry mezi texty, neupravuj jednotlivé věty.
Vrať se ke kroku 1, znovu pojmenuj materiál toho slabšího textu a postav
ho na jiné ose - jinak jen přebarvíš tutéž šablonu.

A "vrať se ke kroku 1" znamená projít cyklus celý, tedy i korekturu.
Přepsaný text nikdo nečetl: osa je jiná, věty se přeskládaly, fakta se
přesunula mezi odstavci - to všechno jsou nové chyby, které první kolo
vidět nemohlo. Odevzdat text, který prošel jen přepisem, znamená vydat
nezkontrolovanou verzi.

Druhé kolo se ale neváže jen na kostru, nýbrž na rozsah změn - a platí
i pro jediný text. Rozhodni podle toho, co jsi po korektuře udělal:

- měnil jsi fakta, přepisoval celé odstavce nebo pasáže s čísly → druhé
  kolo pusť, i když šlo o jeden text
- opravoval jsi jen vazby, slova a interpunkci → druhé kolo nech být,
  stavba ani tvrzení se nezměnily

Když si nejsi jistý, kam případ patří, pusť ho. Nezkontrolovaná verze je
horší než jeden agent navíc.

Druhé kolo smí být užší než první, ať se nenafoukne cena. Korektorovi dej
přepsané texty a zadání zúžené na tři věci: (1) nové věcné chyby vzniklé
přesunem údajů, (2) rozbité vazby a odkazy v přepsaných pasážích,
(3) jestli se kostry po přepisu opravdu rozešly. Nálezy z prvního kola
mu neposílej - má číst znovu bez zátěže.

Druhé kolo pusť na témže agentovi `korektor`, ale s parametrem
`model: sonnet` a běžným přemýšlením. Zúžené zadání je mechanická
kontrola a nejsilnější model by tu byl vyhozený. Do promptu napiš, že
jde o druhé kolo - agent pak svůj plný kontrolní seznam neřeší a drží
se jen těch tří věcí.

Víc než dvě kola nedělej. Když se kostry nerozejdou ani napodruhé,
rozliš, o jakou shodu jde:

Shoda formulací - stejná věta, stejná figura, tentýž obrat na tomtéž
místě - je vada vždycky. Typicky vzniká z pravidla, které sis přeložil do
jedné oblíbené věty: skill říká "když nemáš materiál z první ruky, přiznej
to", ne "napiš přesně tuhle větu". Řekni to v každém textu jinak a jinde -
jednou v první větě, podruhé mimochodem u konkrétního čísla. Totéž platí
pro konce: dva různé se najdou vždycky.

Shoda pózy, která plyne ze stejného materiálu, vada není. Když u obou
témat píšeš z cizích pramenů bez vlastní praxe, budeš u obou stát ve
stejné pozici - a předstírat u jednoho zkušenost, kterou nemáš, je horší
než přiznaná podobnost. Tuhle shodu přijmi a uveď ji v protokolu.

Zahodit jeden z textů má smysl jen tehdy, když sis obě témata volil sám
a zjistíš, že říkají totéž. U zadaných témat tahle možnost není.

Uživateli předej finální text a k němu protokol: co korektoři chytili, co
se změnilo, co jsi odmítl a proč. Do protokolu patří i rozhodnutí, která
korektor nevidí - hlavně volba mezi vykáním a tykáním a její důvod. Když proběhla dvě kola, uveď obě - a
řekni výslovně, jestli finální verze prošla korekturou, nebo jestli po ní
ještě někdo sahal. Protokol je součást výstupu - uživatel
podle něj pozná, jestli korektura funguje, a rozhodne, jestli některý nález
patří do pravidel skillu.
