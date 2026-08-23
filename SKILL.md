---
name: pis-cesky
description: Psaní českých textů, které nezní jako generovaná šablona. Použij pokaždé, když píšeš delší souvislý český text pro čtenáře - článek, blogpost, dokumentaci, e-mail, popis produktu, esej. Neaktivuj pro krátké odpovědi v chatu ani pro kód.
user-invocable: true
---

# Čeština

Rozdíl mezi lidským a generovaným českým textem není ve slovníku. Je v tom,
jestli za větou někdo stojí.

Tenhle skill neříká, která slova nepoužívat. Určuje pozici, ze které text
vzniká. Ze špatné pozice napíšeš slop i bez jediného zakázaného slova, ze
správné projde i klišé.

## Ohlas se

První řádek odpovědi, ve které tenhle skill použiješ, patří hlášce:

```
🇨🇿 Píšu česky (skill aktivován)
```

Vypiš ji jednou na začátku, ne u každého odstavce, a pak pokračuj běžnou
odpovědí. Uživatel podle ní pozná, že text vzniká podle pravidel, a ne
z výchozího nastavení modelu.

## Nejdřív urči žánr a režim

Pravidla v tomhle souboru platí pro každý český text. Ke konkrétnímu
zadání si navíc otevři soubor, který odpovídá:

| Píšeš | Otevři |
|---|---|
| technický článek, návod, dokumentaci, README, popis architektury | `technicky.md` |
| osobní text, marketing, úřední komunikaci | zatím nevzniklo - drž se pravidel níže |

Když text spadá do dvou kategorií, otevři oba soubory.

## Zeptej se na korekturu, než začneš psát

Vzniká text, který někdo uvidí - článek, dokumentace, e-mail ven z firmy,
popis produktu? Pak se zeptej dřív, než napíšeš první větu:

> Mám na to pustit vícefázový režim podle `vicefazove.md` (draft →
> korektura nezávislým agentem → přepis)? Stojí to zhruba 50 tisíc tokenů
> na text navíc, ale chytá chyby, které při vlastním čtení neuvidím -
> věcné omyly i to, že si texty vyjdou na stejnou kostru. Bez něj dostaneš
> jednoprůchodový draft.

Neptej se u krátkých odpovědí, poznámek, commit zpráv a textů do chatu -
tam draft stačí. A nikdy si na to neodpovídej sám: text napoprvé není
nikdy bez chyb, takže tiše korekturu přeskočit znamená odevzdat práci,
kterou nikdo nezkontroloval. Když uživatel řekne ne, napiš draft
a v předání uveď, že korekturou neprošel.

## Než napíšeš první větu: pojmenuj materiál

Šablona nevzniká z nedostatku pravidel, ale z nedostatku pozice. Když
nevíš, co k tématu máš, sáhneš po efektní figuře - a protože sáhneš vždycky
po stejné, vyjdou ti dva texty přes kopírák. Proto začni tímhle:

Co zadání nabízí za materiál? Příběh, čísla z měření, postup, spor, rozšířený
omyl, časovou řadu, vlastní selhání? Co z toho znáš z první ruky a kde jsi
ignorant? Odpověz si na to dřív, než začneš psát.

Formu pak odvoď z nejsilnějšího materiálu, nikdy ji nevybírej ze zásobníku.
Máš čísla z měření? Text stojí na nich. Máš chronologii? Vyprávěj ji. Máš
jen cizí prameny? Řekni to a stav text kolem toho, co jde ověřit. Dva texty
smí mít stejnou stavbu jedině tehdy, když mají stejný druh materiálu -
a když ti vyjde stejná kostra u dvou různých zadání, je to důkaz, že jsi
formu nezvolil, ale zopakoval.

## Dvě vrstvy pravidel

Pravidla o jazyce (vazby sloves, kalky, slovosled, kolokace, oslovení) jsou
závazná. Splníš je tisícem různých způsobů, takže z nich žádná šablona
nevzniká.

Pravidla o stavbě textu (otvírák, konec, rytmus, délka) jsou popis toho, jak
široce se lidské psaní rozbíhá - ne recept. Příklady u nich jsou doklady
z korpusu, ne vzory k napodobení. Zopakovat figuru z příkladu je stejná
chyba jako počeštit "pipe operátor" na "rouru": aplikace pravidla bez
vlastního úsudku.

A korpus není jeden hlas. Grudl klade sokratovské otázky a odpovídá si,
Hůla suše přiznává, co neví, Novotný si hraje se slovy a vymýšlí "Maloměkkou
chybu", Tauchman vypráví chronologii vlastního bastlení, Kajzar taktuje
instalaci počtem vypitých káv. Píšeš jako jeden z nich, ne jako jejich
průměr.

## Pozice pisatele

Sedm pravidel. Nejsou to pravidla čištění hotového textu, jsou to pravidla
psaní od začátku. Odvozená z ručně psaných českých textů před rokem 2022,
soupis zdrojů je v README.

### 1. Piš z pozice někoho, kdo tam byl

Autorita v českém textu nestojí na tom, že tvrzení zní vyváženě. Stojí na
tom, že autor to zažil. "Moje situace byla následující." "Na ten jsem
vytvořil přes stovku testů." "Zkoušel jsem to tři měsíce a nefungovalo to."

Testovatelně: v textu musí být aspoň jeden konkrétní údaj, který nejde
odvodit z obecné znalosti tématu - číslo, datum, název, částka, verze,
jméno nástroje. Když ho tam nemůžeš dát, protože ho nemáš, napiš to
otevřeně, ale nenahrazuj ho obecnou formulací.

### 2. Frázi smíš použít, ale musíš vědět, že ji používáš

Klišé bez sebeuvědomění je slop. Klišé s odstupem je styl. "Lze směle
označit za game changer" je dobrá věta, když autor ví, jak zní.

Aby to bylo použitelné a ne jen hezky řečené: rozhoduje hustota a rámec.
Jedna ozdobná fráze na text funguje jako důraz. Tři na odstavec jsou vata.
A to, jestli je fráze vědomá, se pozná tak, že v okolí věty stojí něco,
co ji láme - ironický přívlastek, uvozovky, poznámka, protiklad. Když frázi
nedokážeš odůvodnit jinak než "takhle se to píše", vyhoď ji.

### 3. Nejistotu přiznej za běhu, ne v disclaimeru

Ne vyhrazený odstavec "je třeba poznamenat, že situace může být složitější".
Místo toho přímo v proudu úvahy: "Hmmm, to nezní příliš prakticky. Ale
tohle už je zajímavější:"

Poctivé váhání patří tam, kde vzniklo. Vata na konci sekce je jen alibi.

### 4. Nekonči shrnutím

Napříč zdrojovým korpusem nemá závěrečnou rekapitulaci ani jeden text.
Texty končí tam, kde jim došel materiál - poslední myšlenkou, posledním
krokem postupu, odkazem, kusem kódu.

Žádné "Shrnuto", "Závěrem", "Jak vidíte", "V tomto článku jsme si ukázali".
Když čtenář potřebuje shrnutí, znamená to, že text byl špatně stavěný, ne
že mu chybí odstavec navíc.

Konce se v korpusu rozbíhají: odkaz na migraci, poslední příkaz do konzole,
rada k ověření, zákaz, přiznaná slabina řešení, nevyvratitelná předpověď,
dopředná reference na další díl. Vyber ten, který plyne z tvého materiálu -
tedy z místa, kde ti látka došla. Nevybírej ten, který ti přijde nejhezčí.

Pozor na past: konec bez shrnutí neznamená konec podle jiné šablony. Výzva
do diskuse ("napiš do diskuse, na čem ses zasekl") patří výhradně do textu,
který diskusi má - tedy do blogu nebo fóra, a jen když si o takový útvar
uživatel řekl. V dokumentaci, e-mailu, README, zprávě ani popisu produktu
nemá co dělat. Když ti vyjdou dva texty za sebou se stejným typem konce,
druhý přepiš.

### 5. Seznam nech v próze, když to jde

Odrážky patří tam, kde záleží na pořadí nebo kde jsou položky opravdu
paralelní - kroky postupu, výčet parametrů. Ne tam, kde jen vypisuješ věci,
které by ve větě stály lépe.

Tři odrážky po jedné řádce jsou skoro vždycky rozsekaná věta.

### 6. Nevyvažuj, když nemusíš

"Na jednu stranu, na druhou stranu" má smysl, jen když skutečně obě strany
zvažuješ. Když máš názor, napiš názor. Přidat protiargument, který sám
nepovažuješ za platný, jen aby text vypadal vyváženě, je nejrozšířenější
znak generovaného českého textu.

### 7. Nech text nedokonalý

Nejde o výrobu chyb. Jde o to, že vyhlazení do dokonalé konzistence je samo
o sobě signál. Ve zdrojovém korpusu jsou překlepy, neshody v pádech, dvakrát
totéž slovo blízko sebe, souvětí, které se rozjede na tři řádky.

Prakticky to znamená: nezarovnávej všechny odstavce na stejnou délku,
nedávej každé sekci stejnou stavbu, nenech všechny věty skončit stejným
rytmem. Když ti druhý průchod textem nabízí "vylepšení", které jen srovnává
tvar, neprováděj ho.

Totéž platí mezi texty, ne jen uvnitř jednoho. Pravidla níže popisují, co
má text dělat, ne jakými slovy to má udělat - a když si z nich uděláš
oblíbený obrat, vyrobíš vlastní šablonu. Hlídej si zvlášť otvírák (dvojtečka
s výčtem "Přiznám dvě věci:" je jedna z mnoha možností, ne výchozí),
uvozovací dvojtečku obecně a typ konce. Dva texty po sobě se stejnou
kostrou znamenají, že píšeš přes kopírák.

Buď si vědom limitu: nezávislé běhy modelu tíhnou ke stejnému řešení a
žádná instrukce to nezaruší úplně. Jediná spolehlivá obrana je navázat
formu na materiál - ten je u každého zadání jiný, kdežto zásobník efektních
figur je pořád stejný.

## Oslovení čtenáře: vykání, pokud nezazní jinak

Výchozí je vykání. Tykej jen tehdy, když si o to uživatel řekne nebo když
to jednoznačně plyne ze zadání - vývojářský blog, komunitní fórum, text
pro kamaráda. V dokumentaci, e-mailu, firemním sdělení, nabídce a čemkoli,
co jde ven z firmy, se vyká.

Zdrojový korpus obojí míchá: Grudl vyká ("Budete-li psát třídu vyžadující
databázi..."), nettech vyká ("Pokud také marně hledáte ovladače..."),
komunitní blogy si často tykají. Z korpusu tedy neplyne jedno správné
oslovení - plyne z toho, komu píšeš.

Co platí bez ohledu na volbu: drž ji celým textem. Přeskočit uprostřed
z "můžete" na "můžeš" je horší chyba než kterákoli z obou variant. A když
oslovuješ, oslovuj i v instrukcích - "konfiguraci zapíšete přes atributy",
ne "konfiguraci lze zapsat přes atributy".

## Stavba věty: od slovesa

Nejčastější chyba generovaného českého textu není ve slovech, ale ve
stavbě: věta se postaví po anglicku kolem podstatných jmen a česká slovesa
se do ní jen vsadí. Čeština staví větu od slovesa - to diktuje pády,
předložky, částice i slovosled. Proto u každé věty nejdřív vyber české
sloveso a zeptej se, co si žádá: kdo, co, komu, čím, kam. Teprve pak
skládej zbytek.

Konkrétně to znamená hlídat:

Vazbu a doplnění. Pročtu co, ne "pročtu v čem". Přiznám se, ne holé
"přiznám rovnou". Frazém se přenáší celý, nebo vůbec.

Modalitu. Kde angličtina říká "you can", čeština potřebuje "můžeš" nebo
částici "si klidně" - jinak se z nabídnuté možnosti stane rozkaz.

Rámec u sloves pohybu a přenosu. "Vracet" chce rámec: do hry, na scénu -
"vracejí funkci" bez rámce zní přeloženě.

Existenční stavbu. Angličtina si abstrakce přivlastňuje ("the version
has a catch"), čeština je umisťuje: "někde je problém", "v něčem je háček".

Švy mezi větami. Věty položené vedle sebe bez navazovací částice jsou
anglická parataxe; česká návaznost stojí na "ale", "ovšem", "jenže",
"tedy", "tak". Po podmínkové větě navazuj "tak", ne knižní "pak".

Sbalené děje. Angličtina ráda zabalí děj do podstatného jména a čeština
ho zas rozbalí do věty: "bez nastavení retry se job zahodí" → "když retry
nenastavíš, job po pádu zmizí"; "tichý únik chyby zarazíš v jazyce" →
"chybě předejdeš rovnou v jazyce". Když v jedné větě stojí dvě podstatná
jména slovesná vedle sebe, jedno z nich má být sloveso.

Příčestí v přívlastku. "Vyhozená výjimka", "vrácená hodnota" jsou kalky
z thrown exception, returned value - čeština tyhle vazby drží u slovesa
("kód vyhodí výjimku"), ne u přívlastku. Zkoušku uděláš tak, že přívlastek
škrtneš: když věta říká pořád totéž ("místo chyby" = "místo vyhozené
chyby"), byl navíc.

A u obrazů a idiomů se neptej "jak to přeložit", ale "jak tuhle situaci
popisuje česká komunita". Metafora se nepřekládá, nahrazuje se domácí
("z ostrého provozu", ne "z bojiště"); i ryze české slovo může být mimo
doménu ("na čem to skříplo" → "na čem jste se zasekli"; "až verzi pustí"
→ "až vydá aktualizaci"). Anglicismus obhájí jen díra ve slovníku
(release notes), ne pohodlí (tab → záložka) - a i pak smí stát jen jako
přívlastek, do přísudku patří česká vazba ("máš to přímo v základu", ne
"máš to first-party"). Zástupné "věc" ("největší věc je...") nahraď tím,
co ta věc skutečně je.

Pozor, tohle pravidlo platí oběma směry a rozhoduje vždy úzus, ne
mechanika: počeštit termín, který komunita drží anglicky, je stejná chyba
jako obráceně. V Unixu se pipe říká "roura", v PHP se |> říká "pipe
operátor" - a přejmenovat ho na rouru je přehnaná domestikace. Když
nevíš, jak tomu obor říká, ověř si to (dokumentace, diskuse, korpus);
netvoř.

## Slovosled: nové na konec

Anglický slovosled je pevný, český nese význam. Věta v klidném výkladu
začíná tím, co čtenář už zná (téma), a končí tím, co se mu sděluje nového
(réma) - informační váha roste zleva doprava. Když překlopíš anglickou
větu jedna ku jedné, důraz přistane na špatném slově a věta drhne, i když
je gramaticky správně.

Test na každou větu: co je tady novinka? Musí stát na konci. "Reverb umí
databázový driver" (novinka = driver, správně na konci) versus "Databázový
driver je novinkou Reverbu" (totéž po anglicku, důraz utopený uprostřed).
Obrácené pořadí je dovolené jen jako záměrný citový důraz, ne jako default.

S tím souvisí příklonky - krátká nepřízvučná slova (se, si, jsem, bych,
mi, mu, ho, to) patří na druhou pozici ve větě, hned za první větný člen,
a řadí se v pevném pořadí: -li → jsem/bych → se/si → mi/mu → ho/to.
"Včera jsem se mu to snažil vysvětlit," ne "Včera jsem snažil se mu to
vysvětlit." V dlouhých souvětích si pozici příklonek zkontroluj zvlášť -
tam se rozbíjí nejčastěji.

A vid: angličtina ho nemá, čeština jím rozlišuje děj jednorázově dokončený
(napíšu, spustil jsem) od průběžného nebo opakovaného (píšu, spouštěl
jsem). Při převodu z anglické myšlenky se vid volí, ne překládá - "I will
write" je podle situace "napíšu" i "budu psát", nikdy "budu napsat".

## Kde si ověřit, že to tak Češi říkají

Nejistota u vazby slovesa: Internetová jazyková příručka ÚJČ
(prirucka.ujc.cas.cz) - u hesel uvádí vazby; valenci podrobně vede VALLEX
(ufal.mff.cuni.cz/vallex). Nejistota, jestli se spojení vůbec říká: Český
národní korpus (kontext.korpus.cz) - nízký výskyt = prověř, jestli sis
spojení nevymyslel. Tohle jsou kontroly, ne dekorace: "na čem to skříplo" by korpus
shodil dřív, než by ho musel opravovat člověk.

## Co dělat před odevzdáním

Přečti si text nahlas, jako by ho psal někdo jiný. Hledáš místo, kde věta
stojí proto, že se to tak píše, a ne proto, že to chceš říct. Takové místo
přepiš nebo smaž.

Tenhle průchod ale nechytí chyby, které nevidíš právě proto, že znáš
svůj záměr - proto přidej čtyři povinné kontroly:

Zájmena a odkazy. U každého "tyhle", "to", "ten" se zeptej, k čemu se
váže pro čtenáře, který nezná tvůj záměr. Zájmeno se v češtině chytá
nejbližšího výrazu - když mezi ním a cílem stojí vsuvka nebo výčet, odkaz
pojmenuj ("ty tři hlavní, o kterých byla řeč") nebo větu přestav.

Kolokace a doménová slova. U spojení, kterým si nejsi jistý, ověř, že se
reálně říká (korpus, dokumentace, diskuse oboru) - platí pro míry (kód je
krátký, ne malý), slovesa (verze se vydává, nepouští) i termíny oběma
směry (pipe operátor se nepočešťuje, tab se počešťuje). Ověř, netvoř.

Synonyma pro tutéž akci. Jedna akce = jedno sloveso; na druhou zmínku
odkazuj ("když to udělá"), nestřídej synonyma - střídání je anglické pravidlo,
které v češtině vyrábí zmatek.

Vata, která něco tvrdí. Fráze na doplnění rytmu ("tohle budeš potkávat
denně", "bez toho se dnes neobejdeš") vypadá jako stylistická vycpávka, ale
je to tvrzení o světě, které nemáš čím doložit. Buď ho podepři, nebo škrtni -
věcná chyba schovaná ve vatě je horší než vata sama.

## Tvrdá pravidla zápisu

Nepoužívej pomlčku "—" ani "–". Vždy spojovník s mezerami " - ".

Znak "§" jen u citací zákonů. Na kapitoly "kap.".

Komentáře v kódu piš anglicky, i když je text okolo česky.
