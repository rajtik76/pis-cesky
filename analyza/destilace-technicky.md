# Destilace: průnik nettech.cz × blog.nette.org × blog.root.cz

Tři korpusy, které nemají skoro nic společného - malý firemní blog bez
redakce, profesionální blog frameworku s šesti autory a komunitní blogy
deseti amatérů až poloprofesionálů včetně diskusí pod články. Patnáct let
rozpětí, různí lidé, různá úroveň psaní. Co se najde ve všech, není zvláštnost
jednoho autora, ale vlastnost českého technického psaní. Tohle je surovina
pro stylový soubor `technicky.md`.

## Patnáct vzorců a jejich doklady

**1. Já-pozice i v technickém textu.** Nettech: "Moje situace byla
následující. Doma nemáme televizi." Nette: "To, jak jsem omylem ve dvě
hodiny odpoledne rozeslal šest tisíc emailů, dál už rozebírat nebudu."
Technický text v češtině nese autora. Recenze, návod i release notes se
píší v první osobě jednotného čísla a autorský názor se neschovává za
neosobní vazby. Ověřitelný znak: text obsahuje aspoň jeden údaj, který autor
mohl znát jen z vlastní praxe (číslo, selhání, časový údaj, vlastní
konfigurace).

**2. Krátká věta jako pointa po dlouhém souvětí.** Nettech: "Nezoufejte.
Ovladače existují." Nette: "A to je vše. To je celé slavné DI." / "Krása."
Nejpřenositelnější rytmický vzorec: souvětí buduje, krátká věta uzavírá.
Generovaný text drží věty ve stejné střední délce; lidský text osciluje.

**3. Konec bez shrnutí - ve dvou původních korpusech bez jediné výjimky.**
Text končí
posledním krokem, otázkou do diskuse, odkazem, kusem kódu. Nadpis "Závěrem"
se smí objevit, ale pod ním je srovnání alternativ nebo přiznání slabin, ne
rekapitulace. "V tomto článku jsme si ukázali" nemá v korpusech jediný
výskyt.

**4. Čtenář je konkrétní člověk v konkrétní situaci.** Nettech: "Pokud také
marně a dlouze hledáte ovladače... nezoufejte." Nette: "Pamatujete si na
svůj první program?" / "šikovný programátor jako jste vy". Autor ví, proč
čtenář přišel, a mluví k němu. Otázky za čtenáře klade a hned zodpovídá
("Kam? Asi do databázové tabulky. Skutečně?") - to je dialog, ne prodejní
háček, který čeká na "ano".

**5. Délka podle obsahu, ne podle formátu.** Nettech: 63slovný post
problém-řešení-odkaz. Nette: 419slovný release note končící composer
příkazem. Mikroobsah zůstává mikro. A obráceně: autor smí odmítnout
vysvětlovat ("Kód komentovat nebudu, věřím, že je srozumitelný"). Nafouknutí
každého tématu na "článek" s úvodem a závěrem je znak generování.

**6. Nedokonalost zůstává, i s redakcí.** Překlepy, kolísání Vám/vám,
nevyhlazená mluvená řeč v rozhovoru, gramatické prohřešky slabších autorů.
Oba korpusy potvrzují: vyhlazení všech textů na jednotnou úroveň je samo
o sobě známka strojového psaní.

**7. Odrážky patří datům, próza argumentům.** V obou korpusech odrážky
nesou parametry, seznamy verzí, výčty kroků - věci souřadné a vyčíslitelné.
Úvaha běží v odstavcích. Odrážkovaný argument ("výhody: - rychlost
- bezpečnost - jednoduchost") se nevyskytuje.

**8. Ozdoba s rámcem.** Nettech značí hovorové výrazy uvozovkami
("brnkačka", "posmrtné produkty"), Nette rámuje nadsázku sebeironií nebo
emoji ("bezpečnostní experti nebudou mít co žrát 🙂"). Klišé a hříčka jsou
dovolené, když v okolí stojí značka, že autor ví, co dělá. Hustota: jedna
ozdoba na text funguje, tři na odstavec jsou vata.

**9. Míchání registrů.** Odborný výklad a v něm "Nojo, ale...", "je po tom
kulový" (Grudl), "fakt hustý nástroj", "cca dvě kafe" jako položka
hardwarových požadavků (Kajzar), "koronáč" (Raška), "Slunce je větší oser,
ale prakticky se to nedá pokazit" (Tauchman). Vysoký a nízký registr se
střídají uvnitř odstavce. Původně doloženo jen v nette, root korpus vzorec potvrdil u čtyř dalších
autorů - nejsilnější signál lidského českého hlasu. Nejtěžší na
nápodobu - špatně dávkovaný působí křečovitě. Dávka: jedna dvě hovorové
vsuvky na text, ne na odstavec.

**10. Zdrobněliny, domácí metafory a slovotvorná hra.** "Továrnička" pro
factory (Grudl), "utilitka", "věcička", "hejblátka", "zakopaná celá smečka
psů", "Maloměkká chyba" jako kalk Microsoftu (Novotný), "eRko" pro jazyk R.
Čeština zdrobňuje odborné termíny, bere metafory z domácnosti a tvoří
vlastní slova; překladová AI čeština nic z toho neudělá. Doloženo ve dvou
korpusech nezávisle.

**11. Přiznané slepé uličky až publikovaný neúspěch.** Nette: "z nějakého
důvodu jsem skončil u C" - autor smí nevědět proč. Root jde dál: neúspěch
je téma celého článku ("musím dopředu avizovat, že jsem se k dobrým
výsledkům nedopracoval" - Raška; "Byla to chyba, neopakujte ji po mě" -
Fiala). Cesta zůstává v textu, i když nikam nevedla - ušetří to čas někomu
dalšímu. Generovaný text neúspěch nepublikuje nikdy.

**12. Veřejná oprava a historie verzí.** "EDIT: Jakub Vrána v komentářích
připomněl..." (Hůla), sekce Aktualizace s časovými razítky vlastních oprav
(Kajzar), autor v diskusi: "To se přiznám, mne to nenapadlo… víc hlav víc
ví" (Tauchman). Změna názoru se dokumentuje, historie se nepřepisuje.
Doloženo ve dvou korpusech, potřetí v diskusích.

**13. Názor naplno, volba čtenáři.** "Volání error() mi přijde korektnější"
(Hůla) + "Neberte to jako to jediné správné řešení." "Wifi Extender je ta
nejhorší možnost." (Fiala). Tvrzení se nevyvažuje, rozhodnutí se nechává na čtenáři.
AI dělá přesný opak: rozředí tvrzení a rozhodne za čtenáře.

**14. Text jako zahájení konverzace.** (Nový, z root korpusu.) "Budu rád,
pokud mi to v diskuzi potvrdíte nebo vyvrátíte." "Napište je do diskuse,
rád je sem přidám." Autor počítá s opravou a doplněním dopředu; článek je
první tah, ne hotový produkt. Souvisí s 12: kdo zve k opravě, ten ji pak
veřejně přizná. AI text je vždy uzavřený artefakt.

**15. Sebeshazování jako budování důvěry.** (Nový.) "Nejsem epidemiolog",
"kuchařské pako jako já", "moje hloupost", Kajzar shodí i výsledek vlastního
článku ("prachbídné hrátky… grafy nám neřekly nic nového"). Autor se
shodí, aby tvrzení stálo na faktech, ne na autoritě. Opak AI textu, který
autoritu simuluje jistotou.

## Co korpusy vyvracejí (anti-blacklist)

"Pojďme se podívat" a "tento článek se zabývá" píší i nejlepší čeští
techničtí autoři - krátce, jednou, funkčně. Až šablona z toho dělá slop:
stejná formule na stejném místě každého textu. A obráceně, prodejní
řečnická otázka ("Ztrácíte se občas v záplavě oken?") je znak přepisu
marketingových podkladů, ne přítomnost otázky jako takové. Fráze nikdy
nerozhoduje sama; rozhoduje pozice, ze které je napsaná.

## Marketingový registr: třikrát totéž

Slop je starší než AI - je to marketingový přepisový registr. Nettech 2016
(Sierra, DJI: uniformní sekce, "nikdy to nebylo jednodušší"), root 2021
(Křiva o tonerech: benefitová stavba, řečnické otázky v mezititulcích).
Správná otázka pro skill není "zní to jako AI?", ale "je to psáno z vlastní
pozice, nebo přepsáno z cizích podkladů?". Křiva navíc ukázal, podle čeho se pozná marketing psaný člověkem: podle
přiznané pozice ("Tento článek jsem napsal jako majitel firmy… lze jej
považovat za propagaci"). Pro budoucí `marketing/`: povinné
přiznání, kdo mluví a co z toho má.

## Nuance k pravidlu o konci

Jediná rekapitulace v 74 textech všech tří korpusů: Tauchmanův "Závěr
projektu" na konci dvanáctidílného seriálu. Není informační - je to bilance s hodnocením,
sebekritikou vlastních článků a poděkováním manželce. Závěr smí existovat
na konci seriálu jako ohlédnutí; nikdy jako opakování řečeného.

## Diskusní registr (z root korpusu)

Komentáře pod články jsou samostatný registr: nulová zdvořilostní vata
("Pokud vim, tak pouziti cloudu neni povinne. Nemusite to pouzivat." -
konec), argumentuje se vlastní zkušeností ("Rozbity Arch som opravoval dva
dni"), běžné psaní bez diakritiky, slovenština v českých vláknech bez
překladu. Pro skill: když AI píše odpověď do diskuse nebo issue, platí
diskusní registr, ne článkový - žádný úvod, žádné shrnutí, žádné "doufám,
že to pomůže".

## Stav ověření

Vzorce 1-8 doložené nezávisle ve dvou korpusech, 9-13 původně jen z nette
ověřeny v root korpusu u dalších autorů - všech 15 vzorců teď stojí na
minimálně dvou nezávislých zdrojích. Podskill `technicky/` se z toho dá postavit celý. Slabší místa: 14 a 15 zatím jen z root korpusu (komunitní
prostředí je může zvýhodňovat); u profesionální firemní dokumentace bez
diskuse se uplatní omezeně.
