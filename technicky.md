# Čeština: technický text

Piš jako člověk, který to sám zkusil a teď to vypráví kolegovi. Všechna
pravidla níže jsou důsledky téhle věty.

Citace z korpusu jsou doklady, ne vzory. Ukazují, že se daná věc dělá -
ne že se dělá právě takhle. Když převezmeš figuru z příkladu, vyrobíš
šablonu; stavbu textu odvoď z toho, co máš k tématu v ruce.

Doplněk kořenového `SKILL.md` - ten platí pořád, tady jsou navíc
pravidla pro technický žánr.

Odvozeno ze tří korpusů českých textů psaných lidmi v letech 2005-2022:
blog.nette.org (36 článků, 6 autorů), blog.root.cz (27 článků + diskuse,
10 autorů), nettech.cz (10 článků). Podrobnosti v analyza/. Platí pro
technické psaní; osobní esej, marketing a úřední texty vlastní soubor
zatím nemají.

## Pozice: byl jsi u toho

Autorita českého technického textu nestojí na neosobním tónu, ale na tom,
že to autor sám dělal. Piš v první osobě jednotného čísla i tam, kde by
angličtina volila pasivum. "Zkoušel jsem A, pak B, skončil jsem u C."

Testovatelný požadavek: v textu musí být aspoň jeden údaj, který nejde
vygooglit, jen zažít. Číslo z měření, cena, doba trvání, verze, na které
to spadlo, vlastní konfigurace. Korpus: "11 W proti 66 W", "šest tisíc
emailů ve dvě odpoledne", "1 lžíce 6% peroxidu do 750 ml vody", "o 2 dny
jsem nestihl 14denní lhůtu". Když takový údaj nemáš, protože jsi to
nedělal, napiš to rovnou - nenahrazuj ho obecnou formulací.

K pozici patří i nevědění a neúspěch. "Z nějakého důvodu jsem skončil se
dvěma složkami" je legitimní věta - autor smí nevědět proč. Slepé uličky
nechej v textu, šetří čtenáři čas. A text o postupu, který nevyšel, je
plnohodnotný obsah, pokud to řekneš hned v úvodu: "Musím dopředu avizovat,
že jsem se k dobrým výsledkům nedopracoval."

Smíš se i shodit: "Nejsem epidemiolog." "Bylo to moje první pájení, znalci
prominou." Sebeshození přesouvá váhu tvrzení z autority na fakta. Nikdy ho
ale nepoužívej jako alibi místo ověření faktů.

## Čtenář: konkrétní člověk s konkrétním problémem

Čtenář nepřišel číst, přišel něco vyřešit - často z vyhledávače, často
otrávený. Mluv přímo k němu: "Pokud také marně hledáte ovladače,
nezoufejte. Ovladače existují."

Vykání nebo tykání řeší kořenový `SKILL.md` - výchozí je vykání. Citace
níže jsou z korpusu, který obojí míchá; přebírej z nich vzorec, ne tvar
oslovení.

Otázky za čtenáře pokládej a hned zodpovídej, včetně námitek: "Kam? Asi do
databázové tabulky. Skutečně? Co když ho uloží do souboru na disk?" -
"A teď si možná říkáte: vždyť je to jedno. Proč do toho rýpeš?" Tohle je
dialog, ne prodejní háček. Rozdíl poznáš tak, že prodejní otázka čeká na
"ano" a nabízí produkt ("Ztrácíte se v záplavě oken?"), kdežto dialogová
otázka formuluje skutečnou pochybnost a ty se s ní argumenty vypořádáš.

Autor taky rozhoduje, co čtenář nepotřebuje, a řekne to nahlas: "Kód
komentovat nebudu, věřím, že je srozumitelný." "Tím bych její popis
uzavřel." Vysvětlovat všechno stejně důkladně je znak generátoru - lidský
text má odvahu vynechávat.

Názor řekni naplno a volbu nech čtenáři: "Volání error() mi přijde
korektnější." + "Neberte to jako to jediné správné řešení." Nikdy obráceně
- rozředit tvrzení ("každý přístup má své výhody") a rozhodnout za čtenáře
je přesně to, co dělá generovaný text.

## Rytmus a jazyk

Po dlouhém souvětí krátká věta jako úder: "Tak jsem pátral a našel
perfektní řešení." - "A to je vše. To je celé slavné DI." - "Krása."
Nejpřenositelnější vzorec celého korpusu. Generátor drží věty ve stejné
střední délce; člověk střídá krátké s dlouhými.

Střídej registr. Odborný výklad unese hovorovou vsuvku: "Nojo, ale...",
"je po tom kulový", "cca dvě kafe" jako položka požadavků. Dávka: jedna
až dvě vsuvky na text. Tři na odstavec už jsou křeč.

Čeština zdrobňuje a tvoří slova - využij to: "továrnička" pro factory,
"utilitka", "eRko" pro jazyk R, "Maloměkká chyba". Zdrobnělina nese postoj
(malá, neškodná, pomocná věc). Metafory ber z domácnosti a fyzického
světa: "vařit několik jídel v jednom hrnci", "zakopaná celá smečka psů".

Stavbu věty od slovesa (vazby, modalita, částice, domestikace idiomů)
řeší kořenový `SKILL.md` - platí tady beze zbytku.
Navíc pro technický text: příkazy a API piš v celé funkční podobě ("než
pustíš update přes Composer", ne "než pustíš composer" - holý příkaz nic
neudělá a čtenář-vývojář ti přestane věřit).

Ozdobnou frázi nebo klišé smíš použít, když v okolí stojí značka, že o ní
víš: uvozovky ("brnkačka", "posmrtné produkty"), sebeironie, nadsázka
("bezpečnostní experti nebudou mít co žrát"). Jedna ozdoba na text funguje
jako důraz, tři na odstavec jsou vata. Když frázi neumíš obhájit jinak než
"takhle se to píše", vyhoď ji.

## Stavba

Délka podle obsahu, ne podle formátu. Mikroobsah zůstává mikro: problém,
řešení, odkaz, konec - 63 slov je legitimní článek. Dvě věty a blok kódu
taky. Nafouknutí každého tématu na "článek" s úvodem, kontextem a závěrem
je jeden z nejspolehlivějších znaků generování.

Odrážky patří datům: parametrům, výčtům verzí, krokům postupu, seznamu
techniky. Argumenty a úvahy běží v odstavcích. Odrážkovaný argument
("výhody: rychlost, bezpečnost, jednoduchost") v korpusu neexistuje.

Krátká metanavigace je v pořádku: "Pojďme se na ně podívat" píší i
nejlepší čeští autoři - jednou, funkčně. Slop z ní dělá až šablona: stejná
formule na stejném místě každého textu.

Nekonči shrnutím. V 73 textech korpusu není jediné. Text končí posledním
krokem, kusem kódu, otázkou do diskuse ("Jak se na novou verzi těšíte?"),
odkazem, dopřednou referencí ("Třetí díl bude jen taková třešnička.").
Nadpis "Závěrem" smí existovat, ale pod ním je srovnání alternativ nebo
přiznání slabin řešení, ne rekapitulace. Jediná povolená bilance: konec
vícedílného seriálu, a i tam hodnotíš a děkuješ, neopakuješ řečené.

Text je první tah, ne hotový produkt. Kde existuje diskuse, počítej s ní:
"Budu rád, když mi to v diskuzi potvrdíte nebo vyvrátíte." A když tě někdo
opraví, opravu dokumentuj, text mlčky nepřepisuj: "EDIT: Jakub Vrána
v komentářích připomněl..." Historie textu zůstává viditelná.

## Nedokonalost nech být

Nezarovnávej odstavce na stejnou délku, nedávej každé sekci stejnou
stavbu. Kolísání (jedna sekce věta, jiná pět odstavců) je přirozený stav
korpusu. Když ti druhý průchod nabízí úpravu, která jen srovnává tvar,
neprováděj ji. Vyhlazení do dokonalé konzistence je samo o sobě signál
stroje - profesionální blog s redakcí nechává autorům překlepy i kolísavé
Vám/vám. Neznamená to chyby vyrábět; znamená to nehonit je.

## Odpověď do diskuse, issue, code review

Jiný registr než článek. Nulová vata: žádný pozdrav, žádné "doufám, že to
pomůže", žádné shrnutí. Tvrzení + vlastní zkušenost jako podklad
("Rozbitý Arch jsem opravoval dva dny") + případný odkaz. Dvě věty jsou
plnohodnotná odpověď. Když tě v diskusi někdo opraví a má pravdu, přiznej
to krátce a poděkuj: "To mě nenapadlo, díky. Víc hlav víc ví."

## Před odevzdáním

Přečti si text nahlas jako rodilý mluvčí a hledej větu, která tam stojí
proto, že se to tak píše, a ne proto, že to chceš říct. Pak projdi tři
povinné kontroly z kořenového `SKILL.md`: zájmena a odkazy (na co reálně
ukazují pro čtenáře), kolokace a doménová slova (ověřit v korpusu nebo
dokumentaci, netvořit), synonyma pro tutéž akci (sjednotit) a vatu, která
něco tvrdí (podepřít, nebo škrtnout).
