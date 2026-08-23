# Jak přispět

Skill stojí na pravidlech odvozených z reálných textů, ne na názoru, jak by
čeština měla znít. Proto má i příspěvek vždycky dvě části: tvrzení a důkaz.
Bez důkazu se pravidlo nepřijímá, ať zní sebepřesvědčivěji.

## Nahlásit špatně znějící text

Nejjednodušší příspěvek. Otevři issue a napiš:

- **co skill vygeneroval** - doslovná citace věty nebo pasáže
- **co na tom zní špatně** - konkrétně, ne "zní to jako AI"
- **jak by to řekl člověk** - tvůj návrh, i kdyby nebyl definitivní

Nejcennější jsou nálezy, kde umíš pojmenovat mechanismus - že jde o
kalk, špatnou valenci, rozbité odkazování a podobně. Nemusíš znát
lingvistický termín, stačí popsat, co konkrétně nesedí. Zbytek se dá
dohledat.

## Navrhnout nové pravidlo do SKILL.md

Obecná pravidla v `SKILL.md` platí pro každý český text bez ohledu na
žánr, takže mají vysokou laťku. Návrh potřebuje:

1. **Alespoň tři důkazy** ze skutečných textů - ne z jednoho generovaného
   vzorku, ale z různých zdrojů, kde se stejný jev opakuje.
2. **Mechanismus, ne jen výsledek.** Nestačí "tohle zní špatně", potřeba
   je vysvětlit proč - jaký anglický vzorec se propsal, jakou vazbu čeština
   žádá místo něj.
3. **Zkoušku, kterou jde pravidlo ověřit.** Podívej se na formu ostatních
   pravidel v souboru - každé jde aplikovat jako test na konkrétní větu,
   ne jen jako obecná rada.

Pravidlo, které platí jen pro jeden text nebo jeden obor, nepatří do
`SKILL.md` - buď je moc úzké na obecnou vrstvu, nebo patří do žánrového
souboru.

## Navrhnout nový žánr

Dnes existuje jen `technicky.md`. Marketing, osobní text a úřední
komunikace na vlastní pravidla čekají. Nový žánrový soubor nevzniká
z blacklistu ani z intuice, ale ze stejného postupu jako `technicky.md`:

1. **Nasbírej vzorek.** Aspoň 15-20 textů daného žánru, psaných lidmi,
   ideálně z více zdrojů a autorů. Přednost mají texty publikované před
   listopadem 2022 - z pozdějších nejde spolehlivě poznat, jestli je psal
   člověk nebo model.
2. **Rozbor patří do `analyza/`.** Podívej se na existující soubory v tom
   adresáři jako na vzor formátu a hloubky.
3. **Destilace patří do žánrového souboru.** Z rozboru vzniknou pravidla
   ve stejném duchu jako v `technicky.md` - popis pozice pisatele
   a stavby textu, ne seznam frází.
4. **Přiznej, co vzorek neukázal.** Sekce `Stav` v `README.md` a případně
   poznámka přímo v žánrovém souboru - lepší přiznaná mezera než pravidlo
   vymyšlené nad rámec dokladů.

Zdroj, který sám omezuje šíření (přísné copyright podmínky, placený
obsah), do `analyza/` nepatří - ověř licenci dřív, než začneš rozbor psát.

## Co do repa nepatří

- **Stažená jazyková data.** `data/` je v `.gitignore` schválně - VALLEX
  (CC BY-NC-SA) a n-gramy z Wikipedie (CC BY-SA) se stahují a staví
  lokálně skriptem `nastroje/stahni-data.sh`, ne commitují.
- **Blacklist frází.** Návrh ve formátu "zakaž slovo X" se zamítá bez
  ohledu na to, jak otravné to slovo je - důvod je v README, sekce
  "Proč ne seznam zakázaných frází?".
- **Pravidlo bez mechanismu.** "Tohle zní líp" nestačí; potřeba je říct,
  proč to zní líp a jak to poznat příště.

## Kód v `nastroje/`

Komentáře a chybové hlášky v kódu jsou anglicky, i když je zbytek repa
česky - drž se toho. Skripty (`vazby.py`, `spojeni.py`) ověřují jazyková
data, negenerují je - pokud navrhuješ nový nástroj, měl by sloužit ke
kontrole, ne k tvorbě pravidel.

## Pull requesty

Menší oprava (formulace, překlep, jeden doklad k existujícímu pravidlu)
může jít rovnou jako PR. Cokoli většího - nový žánr, změna obecného
pravidla, nový nástroj - napřed jako issue k diskusi, ať se rozbor nebo
kód nedělá nadarmo.
