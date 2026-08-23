# Analýza: blog.nette.org (2012-2022, 36 článků, ~31 000 slov)

Profesionální technický blog, šest autorů (Grudl 27 textů, Hůla 3, Černý 3,
Toman, Šedivý, Šulc v rozhovoru). Všechny texty publikované před listopadem
2022. Proti nettech.cz jde o pisatelsky silný korpus s redakcí - a přesto,
jak se ukáže, nevyhlazený. Citace jsou krátké úryvky s uvedením zdroje
(§ 31 AutZ).

## Sokratovský dialog: autor odpovídá na nevyslovené otázky

Nejnápadnější Grudlův vzorec. Autor klade za čtenáře otázky včetně
námitek a hned na ně odpovídá:

"Kam? Asi do databázové tabulky. Skutečně? Co když ho uloží do souboru na
disk? A pokud do databáze, tak do jaké tabulky?" (Co je DI, 2012)

"A teď si možná říkáte: vždyť je to přece jedno. [...] Proč do toho
rýpeš?" (Úvod do DI, 2020)

"Trefil jsem se?" (tamtéž, po odhadu, jak vypadal čtenářův první program)

Není to řečnická otázka jako prodejní udička ("Ztrácíte se občas v záplavě
oken?" - to je přepisový styl z nettech/Sierra). Rozdíl: prodejní otázka
očekává "ano" a nabízí produkt, sokratovská otázka formuluje skutečnou
pochybnost čtenáře a autor se s ní vypořádá argumentem.

## Krátká věta jako pointa

Po dlouhém souvětí úder: "A to je vše. To je celé slavné DI." - "Krása." -
"A najednou nejsou žádné otázky." - "Jaj, statické proměnné jsou zlo." -
"A tady by mohl článek skončit. Jenže nekončí."

Stejný vzorec jako v nettech ("Nezoufejte. Ovladače existují."). Napříč
autory i lety. Rytmus dlouhá-dlouhá-krátká je asi nejpřenositelnější
prvek celého korpusu.

## Metafory z fyzického světa a zdrobněliny

"Vařit několik různých jídel v jednom hrnci" (verzování), "každý ve svém
domečku", "zlé dvojče" (service locator), "pancéřový bunkr pod kapotou",
"pískoviště" (sandbox), "misky vah", "rozplynula jak pára nad hrncem",
vlastní termín "antisemantické verzování".

A zdrobněliny: "továrnička" pro factory, důsledně celou sérií o DI. To je
bytostně česká figura - anglicky myslící text zdrobnělinu odborného termínu
nevytvoří. Zdrobnělina zároveň nese postoj (továrnička = malá, neškodná,
pomocná věc).

## Míchání registrů

Odborný výklad, a do něj: "Nojo, ale...", "Jo, kdyby...", "je po tom
kulový", "Kašlete na to, konstruktor se prostě znovu volat nesmí", "Ufff,
rychle zpátky", "stahování zipů je tááák zastaralé". V rozhovoru "Čoveče,
dobrá otázka", "heleď", "víš jak".

AI drží jednotný registr v celém textu. Člověk píšící česky střídá vysoký a
nízký registr uvnitř odstavce, a právě tím signalizuje, že za textem je
konkrétní hlas. Tohle je pravděpodobně nejsilnější signál lidského autora,
jaký korpus nabízí.

## Sebepřerušení a veřejná oprava

"(…Tedy, ehm, neřeší… Ale k tomu se hnedle dostaneme.)" - autor uprostřed
textu shodí tvrzení, které sám o odstavec výš napsal, a nechá obojí stát.

"EDIT: Jakub Vrána v komentářích připomněl, že přesměrování
z neexistujícího článku je antipattern. [...] Jednoznačné argumenty pro
použití 404." (Hůla) - autor veřejně přizná, že komentátor měl pravdu, přímo
v těle článku, bez přepsání původního odstavce.

To je pravidlo 3 (nejistota v běhu) v nejsilnější podobě: nejen váhání, ale
rovnou zdokumentovaná změna názoru.

## Přiznané slepé uličky a nevědění

Hůla je v tomhle učebnicový příklad: "Zkoušel jsem používat konvenci
bin/cron-xyz.php,
jindy zase podsložku bin/cron/, ale z nějakého důvodu jsem skončil se dvěma
oddělenými složkami." - "z nějakého důvodu"! Autor přiznává, že nezná
racionální vysvětlení vlastní volby. "Zatím jsem nepřišel na žádné
automatizované elegantní řešení." "Jeden čas jsem koketoval s myšlenkou
vypustit .php příponu. [...] Ale upustil jsem od toho."

Cesta včetně slepých uliček zůstává v textu. AI výklad podává jen výsledek.

## Odmítnutí vysvětlovat všechno

"Kód komentovat nebudu, věřím, že je srozumitelný." - "Ponechme ji v klidu
v zapomnění." (o TextResponse) - "tím bych její popis uzavřel." (o
JsonResponse) - "Bližší popis mechanismu útoku nebudeme zveřejňovat." (CVE)
- "To, jak jsem omylem ve dvě hodiny odpoledne rozeslal šest tisíc emailů,
které měly odejít až po půlnoci, dál už rozebírat nebudu."

Autor rozhoduje, co čtenář nepotřebuje, a řekne to nahlas. Generovaný text
vysvětluje všechno stejně důkladně, protože nemá odvahu vynechávat. Mimochodem
ta věta o šesti tisících emailech je zároveň ukázka příběhu vlastního selhání
jako výukového prostředku - jedna věta, konkrétní čísla, žádná morální
poučka za ní.

## Názor bez vyvažování, autonomie čtenáře bez alibismu

"Volání error() mi přijde korektnější, lépe vystihuje situaci." - "Latte
svými vlastnostmi válcuje konkurenci." - "Řada částí Nette představuje
světovou špičku."

Sebevědomá tvrzení bez "na druhou stranu". A vedle toho: "Neberte to jako
'to jediné správné' řešení." - "Úvahy o tom, jak moc je to užitečné,
ponechám na vás." - "Záleží na vás." Rozdíl proti AI vyvažování: autor svůj
názor řekne naplno a pak nechá volbu čtenáři. AI názor rozředí, aby volbu
nemusela nechat nikomu.

## Konce

Otázka do komentářů ("Jak se na novou verzi PHP těšíte?", "Je vůbec ještě
něco, co v Latte chybí?"), odkaz na migraci, dopředná reference ("Třetí díl
už bude jen taková třešnička."), nebo prostě poslední kus kódu (PhpGenerator
3.4 končí příkazem pro Composer). Shrnutí nula z 36.

Nuance: Hůlův CLI článek má sekci nadepsanou "Závěrem" - ale není to
rekapitulace, je to poctivé srovnání alternativ (Symfony Console, wget) a
přiznání hlavní nevýhody vlastního řešení. Nadpis "Závěrem" tedy sám o sobě
není znak slopu; znakem je obsah typu "shrnuli jsme si".

## Co korpus vyvrací: "pojďme se podívat" není znak AI

Poctivost velí zaznamenat: Grudl píše "Pojďme se na ně podívat!" (2×),
"V tomto třetím se podíváme na atributy", 2014: "Tento článek se zabývá
nejdůležitějšími vylepšeními formulářů". Metanavigace v českém technickém
blogu normálně existuje - krátká, funkční, jednou za text. Slopem se stává,
až když ztuhne v šablonu: stejná formule v každém textu na stejném místě
(viz changelogy editee se stejnou větou třikrát). Další hřebík do rakve blacklistů -
fráze sama o sobě nic neznamená.

## Slabší pisatelé vzorce potvrzují

Šedivý (EET): překlepy ("strášákem", "příjmat", "řešite", "přesueneme"),
kostrbatá souvětí - a k tomu osobní příklad s vlastním DIČ a číslem pokladny 1989,
"abych to nemusel furt zadávat". Toman: "pokud nemáte rádi klasickou
konfiguraci webpacku stejně jako já", "imho". Rozhovor se Šulcem nechává
mluvenou řeč nevyhlazenou včetně gramatických uklouznutí ("Nějaké se
udělali"). Profesionální blog s redakcí, a nedokonalost jednotlivých hlasů
nechává být. Vyhlazení všech textů na jednu úroveň by bylo přesně to, co
dělá generátor.

## Titulky

"Nabušené DI srdce pro vaše aplikace", "PhpGenerator 3.4: přímo na tělo",
"opevnění uvnitř šablony", "Latte 2.9: to nejlepší nakonec", "radost
debugovat". Hříčky a tělesné metafory, ne popisná SEO formule. Titulek nese
postoj dřív než informaci - informace je v podtitulu nebo perexu.

## Omezení

Korpusu dominuje jeden hlas (Grudl, 27 z 36). Co vypadá jako vzorec
žánru, může být vzorec jednoho autora - proto má váhu, že klíčové vzorce
(krátká pointa, přiznané nevědění, konec bez shrnutí, míchání registrů) se
našly i u Hůly, Tomana a v korpusu nettech.cz psaném někým úplně jiným.
