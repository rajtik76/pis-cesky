# Proč nejde stavět procesory donekonečna rychlejší - fyzikální limity Moorova zákona

Moorův zákon je jeden z nejčastěji citovaných a zároveň nejčastěji nepochopených principů v počítačovém průmyslu. Gordon Moore, spoluzakladatel Intelu, v roce 1965 pozoroval, že počet tranzistorů na čipu se při konstantních nákladech přibližně každý rok zdvojnásobuje (později upraveno na přibližně 18-24 měsíců). Důležité je, že Moore nikdy nemluvil o taktovací frekvenci procesorů - to je hustota tranzistorů, ne rychlost hodin. Přesto se v populárním povědomí Moorův zákon zjednodušil na "počítače budou pořád rychlejší", což vede k mylné představě, že procesory mohou zrychlovat bez omezení.

## Kde se zastavily hodiny

Na přelomu tisíciletí platilo i tzv. Dennardovo škálování - pravidlo, podle kterého se se zmenšujícím se tranzistorem úměrně snižovalo i napětí, takže spotřeba na jednotku plochy zůstávala přibližně konstantní a výrobci mohli zvyšovat frekvenci bez enormního nárůstu spotřeby. Kolem roku 2005-2006, když se délka hradla tranzistoru dostala pod 90 nm, se toto škálování zhroutilo. Napětí už nešlo dál snižovat, aniž by tranzistory ztrácely spolehlivost, takže se snižování spotřeby zastavilo, zatímco hustota tranzistorů dál rostla. Výsledkem byl prudký nárůst hustoty výkonu (wattů na milimetr čtvereční), a od té doby se běžné procesory pohybují v pásmu zhruba 3-5 GHz - vyšší frekvence sice jde vyrobit, ale za cenu spotřeby a tepla, které už nejde v běžném pouzdře odvést.

## Kvantové efekty a atomová hranice

Druhý strop je čistě fyzikální. Moderní tranzistory mají klíčové rozměry v jednotkách nanometrů - tedy v řádu několika desítek atomů křemíku. Když se izolační vrstva hradla ztenčí na několik atomových vrstev, elektrony ji začnou "tunelovat" skrz, i když by podle klasické fyziky neměly mít dost energie na překonání bariéry. Tento tzv. tunelový jev způsobuje únikové proudy (leakage current) - tranzistor propouští proud, i když je vypnutý, a čip tak žere energii a hřeje se i v klidu. Čím menší tranzistor, tím výraznější efekt. Výrobci na to reagovali novými geometriemi (FinFET, později gate-all-around neboli GAAFET), které obalí kanál tranzistoru izolací z více stran a tunelování částečně potlačí, ale i tahle řešení mají svůj fyzikální strop - blíží se hranici, kdy tranzistor tvoří jen několik desítek atomů a další zmenšování ztrácí smysl, protože už není co zmenšovat.

Třetí problém je teplo. Hustota výkonu na moderních čipech dosahuje stovek wattů na plochu velikosti poštovní známky. Odvod tepla z tak malé plochy je čistě termodynamický problém - nejde o to, jak rychle procesor "umí" počítat, ale o to, jak rychle se z něj dá teplo dostat pryč, aniž by se křemík poškodil nebo tranzistory neztratily spolehlivost. K tomu se přidává zpoždění na propojkách (interconnect delay) - se zmenšujícími se rozměry rostou paradoxně relativní odpory a kapacity vodičů mezi tranzistory, takže signál se v čipu šíří relativně pomaleji, což dál limituje, jak vysoko lze frekvenci reálně dostat.

## Odpověď: nejít do šířky namísto do výšky frekvence

Protože se nedalo dál zvyšovat frekvenci, výrobci procesorů obrátili strategii - místo jednoho stále rychlejšího jádra začali dávat na čip víc jader. Vícejádrové procesory umožňují zvyšovat celkový výkon paralelním zpracováním, aniž by rostla spotřeba na jádro. Tenhle přístup má ale limity taky - ne každý úkol se dá efektivně rozdělit na paralelní vlákna (Amdahlův zákon).

Dalším směrem je 3D stohování a chipletová architektura - místo jednoho velkého monolitického čipu se skládá procesor z několika menších čiplů propojených přes pokročilé pouzdření, případně se čipy staví doslova na sebe jako patra budovy. To umožňuje zvyšovat hustotu tranzistorů v celém "balíčku", i když se jednotlivý tranzistor už dál nezmenšuje. AMD tímhle přístupem (Ryzen/EPYC s chiplety) i Intel a TSMC se svými pokročilými 2.5D/3D pouzdřeními dnes běžně kompenzují zpomalující se zmenšování tranzistorů.

Třetí cestou je specializovaný křemík - grafické karty, AI akcelerátory, signálové procesory a podobné čipy, které jsou navržené jen pro úzkou třídu výpočtů, ale v ní jsou o řády efektivnější než univerzální CPU. Místo obecného "rychlejšího procesoru pro cokoliv" jde vývoj směrem k "specializovanému křemíku pro konkrétní úlohu".

## Kde jsme teď

Podle plánů TSMC, Samsungu a Intelu se výroba v roce 2026 pohybuje kolem uzlů 2nm, s výhledem na cca 1,4 nm ke konci dekády. Podle plánu výzkumného konsorcia imec by uzly kolem 0,3 nm (v novém značení, kde už název uzlu nekopíruje reálný fyzický rozměr) mohly přijít kolem roku 2038, s tranzistory typu CFET (complementary FET, kde se n-typové a p-typové tranzistory staví jeden na druhý) jako dalším krokem k vyšší hustotě bez dalšího zmenšování jednotlivého tranzistoru. Sub-1nm technologie se podle aktuálních odhadů neočekává dřív než kolem roku 2034.

Většina odborníků se shoduje, že Moorův zákon v původním smyslu - tedy pravidelné zdvojnásobování hustoty tranzistorů při stejné ceně - už neplatí tak, jak platil v 70. a 80. letech. Pokrok ale nekončí, jen mění podobu: místo honby za menším tranzistorem jde o chytřejší skládání čipů, specializaci křemíku a lepší využití každého cyklu procesoru softwarem.

Sources:
- [Are We Reaching the Physical Limits of Transistor Scaling?](https://medium.com/@sayedathar242/are-we-reaching-the-physical-limits-of-transistor-scaling-74b3e231766a)
- [Dennard Scaling - an overview | ScienceDirect Topics](https://www.sciencedirect.com/topics/computer-science/dennard-scaling)
- [Moore's Law: History, Data & the Slowdown](https://processorhistory.com/moores-law/)
- [Imec's 2026 roadmap details 0.3nm nodes by 2038 | Tom's Hardware](https://www.tomshardware.com/tech-industry/semiconductors/imecs-2026-roadmap-details-0-3nm-nodes-by-2038-cfet-transistors-become-viable-at-0-7nm-company-redefines-moores-law-as-cell-sizes-gain-importance-for-density)
- [TSMC's Chip Scaling Efforts Reach Crossroads at 2nm - EE Times](https://www.eetimes.com/tsmcs-chip-scaling-efforts-reach-crossroads-at-2nm/)
- [Sub-1nm Process Technology Won't Arrive Till 2034 - wccftech](https://wccftech.com/sub-1nm-process-node-technology-wont-arrive-till-2034-logic-roadmap-2dfets-sub-0-2nm-2046/)
