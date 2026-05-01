# russia mobile internet whitelist

### 🍺🍺🍺 donations

<sup>BTC</sup>
`bc1q5cws5mx9x784kwn3zj6uz0q9cvdpj65lzenv6v`

<sup>SOL</sup>
`5iB8p3tMEtAQ1qaCJNHyd5Fm74DsT6qjud9Gg7TAMr5T`

<sup>ETH</sup>
`0x98e52948c78707b2003deb550a63a4705afccc1a`

<sup>USDT TON/just TON</sup>
`UQChsyq45Myo46fGh5kolTvtYW6Oye5IVkpd7Pp3MLEagssV`

<sup>USDT TRC20</sup>
`TLvej81gMURc2xXNJSZo4S3Dmmax6AtqHK`

<p align="center"><b>🇺🇸 please, star this repository so more people can see it.<br>🇷🇺 пожалуйста, поставьте звезду этому репозиторию, чтобы больше людей увидели его.<br>🇺🇦 будь ласка, поставте зірку цьому репозиторію, щоб більше людей побачили його.</b><br><br><em>🇺🇸 discord server: active help, community support, and huge amount of info that doesn't fit here.<br>🇷🇺 дискорд сервер: активная помощь, обсуждения и горы полезной инфы, которая не влезает в readme.<br>🇺🇦 діскорд сервер: активна допомога, обговорення та гори корисної інфи, яка не влізає в readme.</em><br><br><a href="https://discord.gg/QPBdMf8dxG"><img src="https://img.shields.io/discord/1282083082849091615?style=for-the-badge&logo=discord" alt="discord"></a></p>

🇺🇸 a list of domains and ips that stay live in russia when the mobile internet gets "restricted".
<br>
🇷🇺 список доменов и ip-адресов, которые остаются доступными в россии, когда мобильный интернет «ограничивают».
<br>
🇺🇦 список доменів та ip-адрес, які залишаються доступними в росії, коли мобільний інтернет «обмежують».

---

### **🇺🇸 english**

#### what's the problem?

in russia, mobile internet is heavily restricted, but "restricted" doesn't even begin to describe the chaos. there are no consistent rules. the situation varies not just by region, but by your specific mobile operator, the cell tower you're connected to, and even your virtual operator (mvno). for instance, yota, which is owned by and runs on megafon's network, can have a radically different (and often stricter) whitelist than megafon itself, even if you're standing in the same spot.

here's what you can expect:
*   **total blackout:** in some regions, especially villages and rural areas where the government assumes nobody is tech-savvy, the internet is simply turned off. sometimes, literally only two or three government websites work. nothing else.
*   **brutal throttling:** in other areas, any traffic to a non-whitelisted resource is throttled down to an unusable 14 kb/s (or even lower).
*   **whitelisting in action:** your connection attempts to unapproved servers might get a `connection reset` packet, or they might just disappear into a blackhole, resulting in a `timeout`. even icmp pings are blocked.
*   **sni whitelisting:** for some lucky people, the restrictions are still basic. the operator only checks the sni (domain name) you're trying to connect to. if it's on their list, you're good. your server's ip address doesn't matter.

#### the lists (and their new purpose)

the lists are a community effort, compiled by people who scan massive ip ranges during lockdowns to see what's still alive. **important:** this list is universal, a collection of what works across different operators and regions. it's not specific to just one provider.

*   `whitelist.txt`: a list of (sub)domains (sni) that are allowed. perfect for sni spoofing in vless/trojan.
*   `ipwhitelist.txt`: this is what `cidrwhitelist.txt` used to be. a list of individual whitelisted ip addresses, one per line.
*   `cidrwhitelist.txt`: the new format. this file contains whitelisted ip subnets in cidr notation (e.g., `0.0.0.0/0`).

#### ⚠️ the reality: sni vs ip/cidr and "the shield"

this is no longer a simple problem. operators are moving to a combined `ip + sni` model. this means even if you spoof a whitelisted domain perfectly, the connection will be blocked if your server's ip isn't also on their allowlist.

there's also a strange phenomenon we call **"the shield"** (personally verified by the repo owner, only on t2/tele2 so far).
*   **what is it?** a "shield" makes you immune to whitelisting. it's not a tariff or a service you can buy. there are no "static ip" services on mobile networks. it's a secret flag in the operator's system.
*   **how do people get it?** it's not given out randomly. it's either for "special" individuals (like a local politician) or for very persistent complainers. there was a real case where a user, during a whitelist, couldn't access government services. he threatened the operator with legal action, citing specific laws. they compensated him and silently enabled "the shield" on his account, likely to prevent future trouble.
*   **does it always work?** no. during the most severe, state-mandated shutdowns, even those with the shield lose connectivity like everyone else.

#### how to survive: tools and strategies

**1. how to tell if you're under a whitelist?**
it's simple. open a terminal or a browser.
*   can you access `yandex.ru` or `gosuslugi.ru`? if yes, you have some connection.
*   can you access `2ip.ru`, `yahoo.com`, or ping `1.1.1.1`? if they all time out or get blocked, while yandex works, you are under a whitelist.

**2. recommended clients & protocols**
your best bets are **vless** or **trojan**. always use encryption (reality/tls).
*   **ios:** streisand, happ.
*   **android:** husi, v2rayng.
*   **pc (windows / linux):** throne, or nekobox (specifically the fork by **qr243vbi**). **warning: the original nekobox is abandoned and outdated, do not use it!**
*   **ipv6?** forget it. russian mobile operators are greedy and haven't invested in ipv6 infrastructure. nobody has tested whitelisting on it.

**3. your options**
1.  **sni spoofing:** the easiest method. just use a domain from `whitelist.txt`. works only if your operator isn't checking ips.
2.  **find a whitelisted server:** search for a hosting provider (they exist both inside and outside of russia) whose ip subnets are in our `ipwhitelist.txt` or `cidrwhitelist.txt`. buy a server, get an ip from the list, and you're golden.
3.  **two-server setup:** the most reliable solution. the traffic flow is: `client -> russian server (with a whitelisted ip) -> foreign server -> internet`. this is more complex and costly, but it bypasses ip-based whitelisting.

**4. join the discord server!**
this readme is just the tip of the iceberg. the discord is a chaotic but incredibly valuable living knowledge base. people are constantly helping each other, sharing working configs, discussing which mvnos are working in which regions *right now*, and even talking about bypassing censorship on wired internet. if you're serious about this, you need to be there.

> **[view whitelist.txt](./whitelist.txt)**
>
> **[view ipwhitelist.txt](./ipwhitelist.txt)**
>
> **[view cidrwhitelist.txt](./cidrwhitelist.txt)**

---

### **🇷🇺 русский**

#### в чём проблема?

мобильный интернет в россии подвергается жёстким ограничениям, но слово «ограничения» не описывает всего хаоса. единых правил нет. ситуация меняется в зависимости от региона, вашего оператора, конкретной вышки, к которой вы подключены, и даже от того, виртуальный у вас оператор (mvno) или нет. например, yota, которая принадлежит мегафону и работает на его же сетях, может иметь радикально отличающийся (и обычно более жесткий) белый список, чем сам мегафон, даже если вы стоите в одной и той же точке.

вот, с чем вы можете столкнуться:
*   **полный блэкаут:** в некоторых регионах, особенно в селах и деревнях (где правительство считает, что технически грамотных людей нет), интернет просто выключают. иногда работают буквально два-три сайта госуслуг. и всё.
*   **жесточайший троттлинг:** в других местах любой трафик на адреса не из белого списка режется до непригодных 14 кбит/с (а то и ниже).
*   **вайтлистинг в действии:** ваши попытки подключиться к «запрещенным» серверам будут либо получать в ответ пакет `connection reset`, либо просто улетать в черную дыру с ошибкой `timeout`. блокируются даже icmp-пинги.
*   **вайтлистинг по sni:** некоторым везет. у них оператор проверяет только sni (имя домена), к которому идет подключение. если домен в списке — всё работает. ip-адрес вашего сервера в этом случае не важен.

#### списки (и их новое назначение)

эти списки — результат работы всего коммьюнити. во время блокировок люди сканируют огромные диапазоны ip-адресов, чтобы найти то, что еще живо. **важно:** список универсальный, он собран с нескольких операторов и из разных регионов, а не под кого-то одного.

*   `whitelist.txt`: список (саб)доменов (sni), которые входят в белый список. идеальны для sni-спуфинга в vless/trojan.
*   `ipwhitelist.txt`: то, чем раньше был `cidrwhitelist.txt`. список отдельных ip-адресов из белого списка, по одному на строку.
*   `cidrwhitelist.txt`: новый формат. в этом файле содержатся подсети из белого списка в cidr-нотации (например, `0.0.0.0/0`).

#### ⚠️ внимание: ip/cidr-вайтлистинг и феномен «щита»

проблема усложнилась. операторы переходят на комбинированную модель `ip + sni`. это значит, что даже если вы идеально подменили домен, соединение заблокируют, если ip вашего сервера не входит в разрешенный список.

а еще есть странный феномен, который мы называем **«щит»** (проверено лично владельцем репозитория, пока только на т2/теле2).
*   **что это такое?** «щит» дает вам иммунитет к вайтлистам. это не тариф и не услуга, которую можно купить. на мобильных сетях в принципе нет услуг типа «статический ip». это секретный флажок в системе оператора.
*   **как его получают?** его не выдают просто так. либо «особым» людям (какому-нибудь депутату), либо самым настойчивым жалобщикам. был реальный случай: у человека во время вайтлиста не работали госуслуги. он начал угрожать оператору, приводя реальные законы и доказательства. в итоге оператор сделал ему компенсацию и тихонько, в своей системе, подключил «щит», чтобы в будущем не «получить по попе».
*   **он работает всегда?** нет. во время самых жестких, принудительных государственных шатдаунов интернет пропадает даже у тех, у кого есть «щит».

#### как выжить: инструменты и стратегии

**1. как понять, что вас зацепило?**
очень просто.
*   открывается `yandex.ru` или `gosuslugi.ru`? если да, какое-то соединение есть.
*   открывается `2ip.ru`, `yahoo.com` или пингуется `1.1.1.1`? если всё висит, выдает тайм-аут или ошибку, а яндекс работает — поздравляю, вы под вайтлистом.

**2. рекомендуемые клиенты и протоколы**
лучший выбор — **vless** или **trojan**. всегда используйте шифрование (reality/tls).
*   **ios:** streisand, happ.
*   **android:** husi, v2rayng.
*   **пк (windows / linux):** throne или nekobox (а именно форк от **qr243vbi**). **внимание: оригинальный nekobox заброшен и устарел, не используйте его!**
*   **а что с ipv6?** забудьте. мобильные операторы в россии жадные и не вкладывались в ipv6. вайтлистинг на нём никто не проверял.

**3. ваши варианты**
1.  **sni-спуфинг:** самый простой метод. просто используйте домен из `whitelist.txt`. сработает, только если ваш оператор еще не проверяет ip.
2.  **найти сервер в белом списке:** ищите хостинг-провайдера (они есть и в рф, и за ее пределами), чьи ip-подсети есть в наших `ipwhitelist.txt` или `cidrwhitelist.txt`. покупаете сервер, выбиваете ip из списка — и вы в дамках.
3.  **схема с двумя серверами:** самое надежное решение. схема трафика: `клиент -> российский сервер (с «белым» ip) -> зарубежный сервер -> интернет`. сложнее и дороже, но обходит ip-вайтлистинг.

**4. зайдите в дискорд сервер!**
этот readme — лишь верхушка айсберга. дискорд — это хаотичная, но невероятно ценная и живая база знаний. люди постоянно помогают друг другу, делятся рабочими конфигами, обсуждают, какой mvno и в каком регионе *прямо сейчас* работает, и даже говорят про обход блокировок на проводном интернете. если вы тут всерьез, вам нужно быть там.

> **[посмотреть whitelist.txt](./whitelist.txt)**
>
> **[посмотреть ipwhitelist.txt](./ipwhitelist.txt)**
>
> **[посмотреть cidrwhitelist.txt](./cidrwhitelist.txt)**

---

### **🇺🇦 українська**

#### у чому проблема?

мобільний інтернет в росії обмежують, але слово «обмежують» не описує всього хаосу. єдиних правил немає. ситуація залежить від регіону, оператора, конкретної вежі, до якої ви підключені, і навіть від вашого віртуального оператора (mvno). наприклад, yota, яка належить мегафону і працює на його ж мережах, може мати радикально інший білий список, ніж сам мегафон.

ось, з чим ви можете зіткнутися:
*   **повний блекаут:** у деяких регіонах, особливо в селах (де уряд вважає, що технічно грамотних людей немає), інтернет просто вимикають. іноді працюють буквально два-три сайти держпослуг.
*   **жорстокий тротлінг:** в інших місцях будь-який трафік на адреси не з білого списку ріжеться до 14 кбіт/с.
*   **вайтлістинг в дії:** ваші спроби підключитися до «заборонених» серверів будуть або отримувати `connection reset`, або просто летіти в чорну діру з помилкою `timeout`.

#### списки (та їх нове призначення)

ці списки — результат роботи спільноти. під час блокувань люди сканують величезні діапазони ip-адрес, щоб знайти те, що ще живе. **важливо:** список є універсальним, зібраним з різних операторів та регіонів.

*   `whitelist.txt`: список (саб)доменів (sni), які дозволені.
*   `ipwhitelist.txt`: список окремих ip-адрес з білого списку.
*   `cidrwhitelist.txt`: підмережі з білого списку в cidr-нотації.

#### ⚠️ увага: ip/cidr-вайтлістинг та феномен «щита»

проблема ускладнилася. оператори переходять на комбіновану модель `ip + sni`. це означає, що навіть якщо ви ідеально підмінили домен, з'єднання заблокують, якщо ip вашого сервера не входить до дозволеного списку.

також існує дивний феномен, який ми називаємо **«щит»** (перевірено на т2/теле2).
*   **що це?** «щит» дає вам імунітет до вайтлістів. це не тариф і не послуга. це секретний прапорець в системі оператора.
*   **як його отримують?** його видають або «особливим» людям, або дуже наполегливим скаржникам (наприклад, після погроз судом через непрацюючі держпослуги).

#### як вижити: інструменти та стратегії

**1. як зрозуміти, що вас зачепило?**
*   `yandex.ru` працює? якщо тк, зв'язок є.
*   `2ip.ru` або `1.1.1.1` не працюють? якщо так — ви під вайтлістом.

**2. рекомендовані клієнти та протоколи**
найкращий вибір — **vless** або **trojan**. завжди використовуйте шифрування (reality/tls).
*   **ios:** streisand, happ.
*   **android:** husi, v2rayng.
*   **пк (windows / linux):** throne або nekobox (форк від **qr243vbi**). **увага: оригінальний nekobox застарів, не використовуйте його!**

**3. ваші варіанти**
1.  **sni-спуфінг:** найпростіший метод.
2.  **знайти сервер у білому списку:** шукайте хостинг-провайдера (є і в рф, і за її межами), чиї ip-підмережі є в наших списках.
3.  **схема з двома серверами:** найнадійніше рішення. `клієнт -> російський сервер (з «білим» ip) -> закордонний сервер -> інтернет`.

**4. зайдіть у діскорд сервер!**
цей readme — лише верхівка айсберга. діскорд — це хаотична, але неймовірно цінна жива база знань. там люди постійно допомагають одне одному.

> **[подивитися whitelist.txt](./whitelist.txt)**
>
> **[подивитися ipwhitelist.txt](./ipwhitelist.txt)**
>
> **[подивитися cidrwhitelist.txt](./cidrwhitelist.txt)**

---

### 🇺🇸 license | 🇷🇺 лицензия | 🇺🇦 ліцензія

mit

---

date&legend=top-left"><picture><source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=hxehex/russia-mobile-internet-whitelist&type=date&theme=dark&legend=top-left" /><source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=hxehex/russia-mobile-internet-whitelist&type=date&legend=top-left" /><img alt="Star History Chart" src="https://api.star-history.com/svg?repos=hxehex/russia-mobile-internet-whitelist&type=date&legend=top-left" /></picture></a>
