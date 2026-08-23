# Příklady: stejné zadání, jednou se skillem a jednou bez něj

Tři témata, každé zpracované 2x. Ve složce `bez-skillu/` jsou texty psané bez
jakýchkoli stylistických instrukcí - tak, jak model píše česky sám od sebe.
Ve složce `se-skillem/` jsou stejná zadání zpracovaná podle pravidel z tohoto repa,
včetně korektury nezávislým agentem.

| téma                       | bez skillu                                                                   | se skillem                                                                 |
|----------------------------|------------------------------------------------------------------------------|----------------------------------------------------------------------------|
| Passkeys a WebAuthn        | [bez-skillu/passkeys-webauthn.md](bez-skillu/passkeys-webauthn.md)           | [se-skillem/passkeys-webauthn.md](se-skillem/passkeys-webauthn.md)         |
| Fyzikální limity procesorů | [bez-skillu/moorovy-zakon.md](bez-skillu/moorovy-zakon.md)                   | [se-skillem/moorovy-zakon.md](se-skillem/moorovy-zakon.md)                 |
| Spotové ceny elektřiny     | [bez-skillu/spotove-ceny-elektriny.md](bez-skillu/spotove-ceny-elektriny.md) | [se-skillem/spotove-ceny-elektriny.md](se-skillem/spotove-ceny-elektriny.md) |

Všechny texty vznikly na Claude Sonnet 5 s high effort a se stejným
zadáním. Sada bez skillu vznikla v jedné čisté session; u sady se skillem
psala jedna session passkeys a druhá zbylá dvě témata. Žádná z nich
neznala texty té druhé.

## Čeho si všímat

Texty v `bez-skillu/` jsou kontrolní vzorek, ne odstrašující příklad -
nikdo je záměrně nekazil. Právě proto v nich jsou vidět vzorce, které se
v generovaném českém textu opakují samy od sebe: shrnující závěr, vyvažování
kladů a záporů na konci každé kapitoly, uvozovací obraty ve stylu "Důležité
je, že", stejně dlouhé věty a neosobní pozice bez autora. Všechny tři navíc
sdílejí stavbu - úvod, sekce, shrnutí, zdroje.

Texty v `se-skillem/` stojí každý na jiné ose (chronologie limitů,
mechanismus podpisu, denní cyklus), přiznávají, odkud autor čerpá, a končí
tam, kde jim došel materiál.

## Co korektura chytila

Nezávislý korektor v čistém kontextu nehlídá jen jazyk. V těchhle sadách
našel i věcné chyby, které by čtenář neodhalil:

- tvrzení, že soukromý klíč passkey nikdy neopustí zařízení, si protiřečilo
  s pasáží o synchronizaci přes cloud
- dvě procenta ze stejného průzkumu měla nesourodý základ (spotřebitelé
  versus všichni dotázaní včetně firem)

## Jak sady vznikly

Zadání, doslovně:

```text
1. ignoruj cely obsah CLAUDE.md
2. necti zadne soubory z adresare /priklady
3. nesmis pouzit skill /pis-cesky !!!        (u druhé sady: musis pouzit skill /pis-cesky)
4. napis 3 technicke clanky na nasledujici temata: Passkeys (WebAuthn) - jak
   funguje přihlašování bez hesla, Proč nejde stavit procesory donekonečna
   rychlejší - fyzikální limity Moorova zákona, Cena elektřiny a spotové trhy -
   proč kolísá během dne. Uloz je do adresare /priklady/bez-skillu
5. necti auto-memory (~/.claude/.../memory/)

Mas dovoleno stahnout obsah z internetu jako podklad pro vygenerovani clanku.
Nic vic! Potvrd mi podminky.
```

V původním zadání stálo `/examples` - adresář jsem přejmenoval až potom.
Sada se skillem se stejně tak ukládala do `/priklady/se-skillem`.

U sady se skillem směla session číst soubory skillu (`SKILL.md`,
`technicky.md`, `vicefazove.md`, `slovnik.md` (od té doby zrušený),
`nastroje/`, `analyza/`) -
to je celý rozdíl mezi oběma běhy.
