# Passkeys (WebAuthn) - jak funguje přihlašování bez hesla

Passkeys jsou způsob přihlašování, který nahrazuje klasické heslo dvojicí kryptografických klíčů. Technologie stojí na standardu WebAuthn (Web Authentication), který definuje, jak si prohlížeč, operační systém a server vyměňují data potřebná k ověření identity uživatele. Cílem je zbavit se hesla jako slabého článku - hesla se dají odcizit phishingem, uniknout z databáze nebo uhodnout, zatímco privátní klíč passkey nikdy neopustí zařízení uživatele.

## Asymetrická kryptografie místo sdíleného tajemství

Klasické heslo je sdílené tajemství: uživatel i server znají (nebo by měli znát jen server ve formě hashe) stejný řetězec znaků. Passkey funguje jinak - při vytvoření vznikne pár klíčů, veřejný a privátní. Privátní klíč zůstává uložený v bezpečném úložišti na zařízení uživatele (Secure Enclave na iPhonu, TPM na Windows, hardwarový bezpečnostní klíč typu YubiKey), veřejný klíč se pošle a uloží na serveru dané služby.

Protože server drží pouze veřejný klíč, jeho únik z databáze útočníkovi k ničemu není - veřejný klíč neumožňuje podepsat autentizační výzvu bez odpovídajícího privátního klíče. To je zásadní rozdíl oproti úniku databáze hesel, kde stačí hash prolomit nebo ho porovnat s dříve prolomenými hesly z jiných úniků.

## Registrace: vznik klíčového páru

Když si uživatel na webu vytváří passkey poprvé, proběhne tzv. registrační ceremonie:

1. Server (v terminologii WebAuthn "relying party") vygeneruje náhodnou výzvu (challenge) a pošle ji do prohlížeče.
2. Prohlížeč zavolá WebAuthn API, které předá požadavek autentizátoru - může to být otisk prstu, Face ID, PIN Windows Hello nebo externí hardwarový klíč.
3. Autentizátor po ověření uživatele (biometrie, PIN) vygeneruje nový pár klíčů, který je svázaný s doménou (origin) daného webu. Tím se passkey nedá zneužít na jiné, byť vizuálně identické, doméně - což je jeden z důvodů, proč je tato metoda odolná vůči phishingu.
4. Privátní klíč zůstává na zařízení, veřejný klíč spolu s podepsanou výzvou putuje zpátky na server.
5. Server si veřejný klíč uloží a spáruje s účtem uživatele.

## Autentizace: podpis výzvy

Při dalším přihlášení probíhá autentizační ceremonie, která je v principu jednodušší:

1. Server pošle novou náhodnou výzvu.
2. Zařízení po ověření uživatele (otisk prstu, PIN) podepíše výzvu privátním klíčem.
3. Podepsaná výzva se pošle zpět na server, který ji ověří proti uloženému veřejnému klíči.
4. Pokud podpis sedí, uživatel je přihlášen.

Žádné heslo nikdy neputuje po síti, a to ani v zašifrované podobě. Server navíc nemusí kontrolovat sílu hesla, jeho stáří ani to, jestli uživatel nepoužívá stejné heslo jinde - všechny tyto problémy passkeys eliminují tím, že heslo v procesu vůbec nefiguruje.

## Platformní vs. přenosné autentizátory

WebAuthn rozlišuje dva typy autentizátorů:

- **Platformní autentizátor** je vestavěný přímo v zařízení - Touch ID a Face ID na Apple zařízeních, Windows Hello na PC, otisk prstu na Androidu. Passkey vytvořený tímto způsobem je typicky svázaný s ekosystémem výrobce a synchronizuje se přes cloudové úložiště (iCloud Keychain, Google Password Manager).
- **Přenosný (roaming) autentizátor** je externí zařízení, nejčastěji hardwarový klíč připojený přes USB, NFC nebo Bluetooth (např. YubiKey). Ten funguje nezávisle na konkrétním zařízení a dá se přenášet mezi počítači.

Kromě toho existuje tzv. hybridní přihlášení (cross-device), kdy se uživatel přihlašuje na jednom zařízení (třeba na počítači) pomocí passkey uloženého v telefonu - spojení se naváže přes QR kód a ověří přes Bluetooth, aby se potvrdila fyzická blízkost obou zařízení.

## Proč je to odolnější vůči phishingu

Klíčová vlastnost, kterou heslo nemá, je vazba na doménu. Passkey vytvořený pro `banka.cz` se nedá použít na phishingové stránce `banka-cz.example.com`, protože prohlížeč a autentizátor si při ověřování hlídají, že se výzva podepisuje jen pro origin, pro který byl klíč vytvořen. Útočník tak sice může uživatele nalákat na podvodnou stránku, ale nezíská nic použitelného - passkey se na cizí doméně jednoduše nenabídne k použití.

Zároveň odpadá riziko opakovaného použití hesla napříč službami. Únik jedné databáze veřejných klíčů nijak neohrožuje ostatní účty uživatele, protože každý pár klíčů je jedinečný pro danou dvojici uživatel-služba.

## Synchronizace, zálohování a praktická úskalí

Passkeys uložené jako platformní autentizátor se typicky synchronizují přes cloudové služby výrobce - iCloud Keychain u Apple zařízení, Google Password Manager u Chromu a Androidu. Tyto dva ekosystémy si navzájem nesynchronizují klíče - passkey vytvořený na iPhonu se sám od sebe neobjeví na Android telefonu. Řešením jsou správci hesel třetích stran (1Password, Bitwarden, Dashlane), kteří umí passkeys synchronizovat napříč platformami.

Firefox nemá vlastní úložiště passkeys a spoléhá na to, co nabízí operační systém nebo externí správce hesel.

Praktický problém nastává při ztrátě všech zařízení bez zálohy - v takovém případě se uživatel k passkey nedostane a musí projít záložním procesem obnovy účtu, který se u řady služeb stále opírá o e-mail nebo SMS. Passkeys tedy neřeší úplně všechny scénáře obnovy identity, jen podstatně snižují plochu útoku při běžném přihlašování.

V roce 2026 podporují passkeys prakticky všechny velké služby - Google, Apple, Microsoft, Amazon, banky i řada sociálních sítí - a všechny čtyři hlavní prohlížeče umí passkey vytvořit i použít. Rozdíly zůstávají v detailech: automatické vyplňování přes tzv. conditional UI a plynulost cross-device přihlašování se liší podle kombinace prohlížeče a operačního systému.

Sources:
- [How to Implement Passkeys with WebAuthn: Developer Guide](https://www.authgear.com/post/how-to-implement-passkeys-developer-guide/)
- [WebAuthn Guide: Understanding Authenticators & Ceremonies](https://fusionauth.io/blog/authenticators-ceremonies-webauthn-oh-my)
- [What is WebAuthn Standard? Guide to WebAuthn Protocol, API & How It Works](https://www.passkeys.com/what-is-webauthn)
- [WebAuthn and Passkeys](https://www.webauthn.me/passkeys)
- [Passkey Support Matrix: Browser, OS, and Feature Support](https://mojoauth.com/blog/passkey-support-matrix-browser-os-feature-support)
- [Cross Device Passkey Sync Explained: iCloud Keychain, Google Password Manager, and 1Password](https://mojoauth.com/blog/cross-device-passkey-sync-icloud-google-1password)
- [Passkeys in 2026: Practical Guide to Going Passwordless](https://www.dailycruncher.com/passkeys-2026-passwordless-guide)
