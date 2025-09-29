# russia mobile internet whitelist

[![Discord](https://img.shields.io/discord/1282083082849091615?style=flat-square)](https://discord.gg/QPBdMf8dxG)

🇺🇸 a list of domains that stay live in russia when the mobile internet gets "restricted".
<br>
🇷🇺 список доменов, которые остаются доступными в россии, когда мобильный интернет «ограничивают».

---

### **🇺🇸 english**

#### what's the problem?

russia's mobile internet sometimes just gets "turned off" — a fancy way of saying "heavily restricted for security reasons" because of the war in ukraine. this leaves only a few services online, like major banks (sberbank, t-bank), maps (yandex, 2gis), government portals (gosuslugi), and the usual big names like yandex, rutube, avito, etc.

#### the whitelist

the full list of (sub)domains is in `whitelist.txt`, which I update regularly.

#### ⚠️ CAUTION
the "beeline" provider seems to enforce its own aggressive whitelist, so the domains listed here may not work for their users. if you're on beeline, your best bet is to switch to another provider like "t2" (tele2, the best), "mts" (mid), or even "megafon" (the worst of the bunch).

> heads up: according to reports from some regions, providers are using a combined **ip + sni whitelist**, not just a simple sni (server name indication) whitelist. this means even if you spoof a valid sni for your vless/trojan + reality server, the connection will get "refused" if your server's ip address isn't in their whitelist. the only options left are to test russian hosting services, change your provider, or simply move. if you ran into this and solved the problem, help others by [opening an issue](https://github.com/hxehex/russia-mobile-internet-whitelist/issues).

> **[view the whitelist](./whitelist.txt)**

#### use case: vless/trojan + reality sni spoofing

these domains are perfect for sni (server name indication) spoofing in vless/trojan + reality. the idea is simple: mask your traffic to look like it's going to a boring, whitelisted service. by spoofing a common, "allowed" (sub)domain (e.g., a random yandex cdn like `cdnrhkgfkkpupuotntfj.svc.cdn.yandex.net`, which stays online during shutdowns), you can bypass their stupid restrictions.

#### how to help

found a domain that works? or one on the list that's dead? [open an issue](https://github.com/hxehex/russia-mobile-internet-whitelist/issues).

---

### **🇷🇺 русский**

#### в чём проблема?

мобильный интернет в россии иногда просто «выключают» (подвергают серьёзным ограничениям по «соображениям безопасности» из-за текущей ситуации с войной в Украине). работать остаются только некоторые сервисы: банки (сбербанк, газпромбанк, т-банк), карты (яндекс карты, 2гис), государственные порталы (госуслуги, мчс, прокуратура рф и т.д.), и некоторые сторонние сервисы по типу яндекса, авито, рутуб, и всякая прочая русская дрянь.

#### "белый" список

полный список (саб)доменов находится в файле `whitelist.txt`. так же он регулярно пополняется лично мной.

#### ⚠️ ПРЕДУПРЕЖДЕНИЕ
провайдер под названием «билайн» составляет свой личный вайтлист, и список моих (саб)доменов может не работать у вас ни при каких обстоятельствах. решением будет просто сменить провайдера, например на «т2» (теле2, самый лучший), мтс (такое себе), или даже мегафон (залупа полная).

> по некоторой информации в некоторых регионах (и с некоторыми провайдерами) используют тип вайтлиста по **ip сервера & sni** вместо простого вайтлиста по sni (server name indication). то есть вы условно настроили сервер с vless/trojan + reality, условно поставили sni spoofing на какой-нибудь вайтлистнутый (саб)домен, но оно не будет работать, так как айпи вашего сервера не находится в вайтлисте вашего провайдера. тут остаётся только рассматривать русских хост-провайдеров и поштучно проверять каждого. либо менять провайдера, либо просто переезжать. так же вы можете помочь другим с такой же проблемой, [открыв «issue»](https://github.com/hxehex/russia-mobile-internet-whitelist/issues).

> **[посмотреть "белый" список](./whitelist.txt)**

#### продвинутое использование: sni-спуфинг в vless/trojan + reality

(саб)домены из этого списка идеально подходят для sni-спуфинга (подмены server name indication) в vless/trojan + reality. идея простая: маскируете свой трафик под подключение к обычному, разрешённому сервису. подставив «правильный» (саб)домен (например, рандомный cdn яндекса типа `cdnrhkgfkkpupuotntfj.svc.cdn.yandex.net`, который оставляют рабочим во время «ограничений мобильного интернета»), можно спокойно и без всякой хуйни обойти всю эту путинскую парашу.

#### как помочь проекту

нашли рабочий домен? или какой-то из списка больше не работает? [создайте «issue»](https://github.com/hxehex/russia-mobile-internet-whitelist/issues).

---

### 🇺🇸 license | 🇷🇺 лицензия

mit
