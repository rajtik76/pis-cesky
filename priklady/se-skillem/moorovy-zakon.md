# Proč se procesory přestaly zrychlovat

V roce 2004 Intel potichu pohřbil vlastní projekt s kódovým označením
Tejas - čtyřgigahertzový nástupce Pentia 4. Ne proto, že by inženýři
neuměli tranzistory dost zmenšit. Problém byl v teple: čip by se
zahříval rychleji, než by teplo stihlo odvést jakékoli chlazení. O pár
měsíců dřív přitom přišla na trh varianta Pentia 4 s jádrem Prescott,
která topila tak, že recenzenti museli nad testovacím strojem otevírat
okno.

Za tou historkou stojí fyzika, ne manažerské rozhodnutí. V roce 1974
popsal Robert Dennard z IBM pravidlo, které pak přes třicet let drželo
Moorův zákon při životě: když tranzistor zmenšíte, klesne s ním i napětí
a proud, takže hustota výkonu na čipu zůstane zhruba stejná. Můžete tedy
nacpat víc tranzistorů na stejnou plochu a ještě je spínat rychleji,
aniž by se čip uvařil. Jenže od poloviny nultých let přestalo pravidlo
platit - prahové napětí při zmenšování neklesá tak ochotně jako zbytek
tranzistoru, svodové proudy naopak rostou, a s nimi i hustota výkonu
s každou generací. Odtud "power wall" - zeď, na kterou narazil i zmíněný
Tejas. Od Tejasu uběhlo přes dvacet let. Taktovací frekvence sice dnes
v krátkém boostu jednoho jádra vyšplhá až k 6,2 gigahertzům (rekord drží
Intel Core i9-14900KS), ale trvalý chod celého čipu se drží pořád
v řádu jednotek gigahertzů, stejně jako tehdy. Procesory se nezrychlily,
jen se rozrostly do šířky - jader přibylo, gigahertzů ne.

Dnešní hranice leží jinde, ale je to pořád stejný druh problému.
Tranzistory na nejnovějším výrobním procesu TSMC (označovaném jako N2)
mají hradlo, jehož oxidová vrstva má tloušťku pár atomů - to N2 v názvu
je ale jméno uzlu, ne skutečný rozměr na křemíku. Při takhle tenké
vrstvě začnou elektrony bariérou procházet kvantovým tunelováním, i když
na to podle klasické fyziky nemají dost energie. Vznikne svodový proud,
kterého se konstrukcí nezbavíte; čip prostě žere energii i tam, kde má
být tranzistor podle schématu zavřený.

A k tomu teplo. Z povrchu křemíkového čipu dnešního výkonného GPU odchází
(podle dostupných zdrojů, vlastní teploměr na to nemám) sto až sto
padesát wattů tepla na centimetr čtvereční - zhruba stejný řád, jaký musí
zvládat chlazení trysky raketového motoru v jejích méně namáhaných
místech. Motor to dokáže jen díky kryogennímu palivu, které
stěnou trysky protéká, a pár minutám provozu. Čip žádné chladicí palivo
nemá - a pod devadesáti stupni musí vydržet roky.

Průmysl proto sází na jinou geometrii tranzistoru. U gate-all-around,
zkráceně GAA, hradlo obepíná kanál ze všech stran, ne jen shora - hradlo
tak kanál ovládá líp a svodový proud je nižší. Za tohle zlepšení se ale
platí: přechod na GAA je hlavní důvod, proč wafer na TSMC procesu N2 stojí
kolem 30 tisíc dolarů, o polovinu víc než na předchozím N3. Levnější
tranzistory to zatím nejsou, jen o něco méně děravé.
