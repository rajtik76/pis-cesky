# Passkeys: přihlášení, na které phishing nestačí

20. července 2022 dostalo víc než sedmdesát zaměstnanců Cloudflare během
necelé minuty SMS s odkazem na falešnou přihlašovací stránku Okty -
vizuálně k nerozeznání od skutečné, jen na jiné doméně. Někteří lidé na
odkaz klikli a zadali heslo i jednorázový kód. Útočníci se přesto dovnitř
nedostali - k přístupu do interních aplikací totiž nestačilo heslo ani kód,
firma vyžadovala i fyzický bezpečnostní klíč podle standardu WebAuthn,
a ten na cizí doméně odmítl spolupracovat. Útočníci mířili souběžně i na
Twilio, jenže tam klíč chyběl a útok uspěl.

Rozdíl není v tom, že by klíč byl "bezpečnější heslo". Je to jiný
mechanismus a vyplatí se vědět, proč funguje - stojí na něm totiž i
passkeys, tedy softwarová varianta téhož, kterou dnes nabízí Apple, Google
i Microsoft.

## Proč phishing heslo ani kód nezastaví, ale WebAuthn ano

Heslo i kód z SMS jsou sdílená tajemství: obojí existuje jako řetězec
znaků, který zadáte do formuláře - a ten může patřit komukoli. Falešná
stránka ho prostě opíše a pošle dál na tu skutečnou. WebAuthn ho neřeší
tím, že by tajemství líp zašifroval, ale tím, že mezi vámi a serverem žádné
tajemství neputuje - to, co server dostane, je jen podpis, ne klíč, kterým
vznikl.

Při registraci prohlížeč zavolá `navigator.credentials.create()`.
Autentikátor - čip v telefonu, čtečka otisku v notebooku nebo fyzický klíč,
jaký používal Cloudflare - vygeneruje dvojici klíčů: privátní zůstane
uzamčený v zabezpečeném hardwaru a k serveru se nikdy nepřipojí, veřejný
putuje na server spolu s identifikátorem toho klíče (credential ID). Server
si veřejný klíč uloží k účtu.

Při přihlášení pošle server náhodnou výzvu (challenge). Autentikátor ji
podepíše privátním klíčem - ale jen tehdy, když se doména, pro kterou
podpis vzniká, shoduje s doménou, pro kterou byl klíč vytvořen. Právě
tohle svázání klíče s doménou Cloudflare zachránilo: falešná stránka Okty
běžela na jiné doméně, takže klíč odmítl cokoli podepsat, bez ohledu na to,
jak přesvědčivě stránka vypadala. Server na konci ověří podpis veřejným
klíčem, který má uložený - a hotovo, bez hesla, bez kódu, bez čehokoli, co
by šlo přeposlat dál.

## Co je na passkey nového

Bezpečnostní klíče, jaké má Cloudflare, stojí na WebAuthnu roky. Passkey je
stejný mechanismus, jen s jednou přidanou vlastností: dvojice klíčů se
nezamyká do jednoho kusu hardwaru. Právě tady passkey oproti hardwarovému
klíči ustupuje - privátní klíč pořád nejde poslat serveru ani cizí stránce,
ale mezi vlastními zařízeními smí putovat: zašifrovaný, přes cloudový účet
- iCloud Keychain, Google Password Manager, u Microsoftu obdobně. Ztratíte
telefon, koupíte nový, přihlásíte se ke svému účtu a passkey tam zase máte.
Synchronizace běží šifrovaná end-to-end, takže ani Apple, ani Google se
k privátnímu klíči nedostanou.

Za tohle pohodlí se platí: záruka je slabší než u fyzického klíče, který
z definice nejde zkopírovat na dálku - bezpečnost passkey stojí a padá
s účtem, přes který se synchronizuje. Pro firmu, jako je Cloudflare, proto
dává smysl trvat na hardwaru, ze kterého se klíč nedá dostat ven. Pro
běžného uživatele e-shopu je synchronizovaný passkey pořád o řád lepší než
heslo uložené v prohlížeči.

## Kde to dnes reálně je

Aktivních passkeys je dnes na standardu přes pět miliard. FIDO Alliance,
organizace, která za standardem stojí, k tomu v dubnu 2026 zadala agentuře
Sapio Research průzkum mezi 11 000 spotřebiteli a 1 400 firmami v deseti
zemích - jak lidé passkeys reálně používají. O passkeys ví 90 % dotázaných
spotřebitelů, založit si ho stihlo 75 % z nich, ale pravidelně ho používá
jen 49 %. Passkeys pro zaměstnance nasadilo 68 % dotázaných firem. Vedle
rozšíření stojí za pohled i úspěšnost přihlášení - 93 % u passkey proti
63 % u hesla, tedy ne bezpečnostní, ale čistě UX argument, protože passkey
si nemusíte pamatovat ani ho lovit ve správci hesel.

Samotný standard mezitím taky nestojí na místě. WebAuthn Level 3 postoupil
v lednu 2026 do fáze Candidate Recommendation a v červenci W3C navrhlo jeho
povýšení na plnou Recommendation - poslední krok, než se stane oficiální
webovou normou vedle HTML a CSS.

Mezera mezi těmi 75 % a 49 % - lidmi, kteří si passkey založili, a těmi,
kdo ho používají pravidelně - říká víc než samotný počet založených
passkeys. Něco cestou od "založil jsem si to" k "spoléhám na to" drhne -
a jestli je to návyk, nedůvěra, nebo to, že obnova po ztrátě telefonu
nefunguje, průzkum už neříká.
