# Používání

Podrobnosti k ovládání skillu, vícefázovému režimu a ceně. Instalace
a rychlý start jsou v [README](../README.md).

## Jak poznáš, že se skill zapojil

Podle prvního řádku odpovědi - a zároveň z něj vyčteš, podle kterého
stylu text vzniká:

```
🇨🇿 Píšu česky (styl: technický)
🇨🇿 Píšu česky (styl: úřední)
🇨🇿 Píšu česky (styl: obecný)
```

Skill se aktivuje sám, když píšeš delší český text.
O tom rozhoduje popis ve frontmatter. Když se na to spolehnout nechceš,
vynutíš ho příkazem `/pis-cesky:pis-cesky` a styl si necháš určit skillu.

## Vynucení stylu

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

## Vícefázový režim

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

Aby texty psané v jedné dávce neměly stejný styl a tudíž nevypadaly stejně, řeší se to
plánováním před psaním, ne kontrolou po něm: skill si ke každému textu
předem vypíše osu, první větu, konec a autorskou pózu, porovná je a začne s generováním.
Ukázky obou sad najdeš v adresáři `priklady/`.

## Cena

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
ho poznat, na to skill není, viz "Co skill není" v README.

**Víc textů v jedné dávce**

```
napiš tři články na témata A, B, C
```

U dvou a víc textů si skill nejdřív vypíše plán ke každému z nich a dá jim
jinou kostru dřív, než napíše první větu. Pak teprve píše.
