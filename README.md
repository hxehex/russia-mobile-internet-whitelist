# russia mobile internet whitelist

[![discord](https://img.shields.io/discord/1282083082849091615?style=flat-square)](https://discord.gg/QPBdMf8dxG)

🇺🇸 a list of domains that stay live in russia when the mobile internet gets "restricted".
<br>
🇷🇺 список доменов, которые остаются доступными в россии, когда мобильный интернет «ограничивают».

---

### **🇺🇸 english**

#### what's the problem?

in russia, mobile internet is heavily restricted. in some regions, access to non-whitelisted resources is blocked entirely; in others, the speed is throttled to an unusable 14 kb/s.

this used to happen only during specific events like drone attacks or protests, but in many areas, it has become a near-constant reality. the goal is to control the flow of information by leaving only a handful of state-approved services online: banks (sberbank, t-bank), maps (yandex, 2gis), government portals (gosuslugi), and major domestic platforms like yandex, vk, and avito.

#### the whitelist

the full, regularly updated list of (sub)domains is in `whitelist.txt`.

#### ⚠️ caution: the ip/cidr + sni whitelist

this is no longer a simple problem. what started with "beeline" has become a widespread practice, with "t2" (tele2), "mts", and "megafon" all using similar techniques.

they are moving from a simple `sni` (server name indication) whitelist to a combined `ip/cidr + sni` model. this means that even if you correctly spoof a whitelisted domain for your vless/trojan setup, the connection will be blocked if your server's ip address isn't on their allowed list.

your options are limited:
1.  find a hosting provider in russia (or in belarus) whose ip subnets are whitelisted.
2.  keep testing different mobile providers in your specific area.
3.  move.

a potential, more advanced workaround involves using a **two-server setup**. the theory is to have a simple redirector/proxy on a russian server (with a whitelisted ip) that forwards traffic to your main server located outside of russia. the connection flow would look like this: `client -> russian server (whitelisted ip) -> foreign server -> internet`. this approach is more complex and costly but might be the only viable solution to the `ip/cidr` whitelist problem.

if you've faced this and found a solution, please help others by [opening an issue](https://github.com/hxehex/russia-mobile-internet-whitelist/issues).

> **[view the whitelist](./whitelist.txt)**

#### use case: vless/trojan + reality sni spoofing

these domains are ideal for `sni` spoofing with vless/trojan + reality. the goal is to disguise your traffic to look like it's heading to an approved service. by spoofing a common (sub)domain (e.g., a random yandex cdn like `cdnrhkgfkkpupuotntfj.svc.cdn.yandex.net`), you can bypass the restrictions, but *only* if the provider in your region isn't using an ip-based whitelist.

#### how to help

found a domain that works? or is one on the list dead? [open an issue](https://github.com/hxehex/russia-mobile-internet-whitelist/issues).

---

### **🇷🇺 русский**

#### в чём проблема?

мобильный интернет в россии подвергается жёстким ограничениям. в некоторых регионах доступ к ресурсам за пределами белых списков блокируется полностью, в других — скорость искусственно замедляется до непригодных 14 кбит/с.

если раньше это происходило только во время атак дронов или протестов, то теперь во многих областях это стало почти постоянной практикой. цель — контролировать информационное поле, оставляя работать только одобренные государством сервисы: банки (сбербанк, т-банк), карты (яндекс, 2гис), госуслуги и крупные местные платформы вроде вк, авито и рутуба.

#### "белый" список

полный и регулярно обновляемый список (саб)доменов находится в файле `whitelist.txt`.

#### ⚠️ внимание: вайтлист по ip/cidr + sni

проблема становится всё серьёзнее. то, что начиналось с «билайна», теперь стало общей практикой — «т2» (теле2), «мтс» и «мегафон» используют те же методы.

они переходят от простого вайтлиста по `sni` (server name indication) к комбинированной модели `ip/cidr + sni`. это значит, что даже если вы правильно настроили сервер с vless/trojan и подставили рабочий (саб)домен, соединение будет заблокировано, если ip-адрес вашего сервера не входит в их разрешённый список.

вариантов остаётся немного:
1.  искать хостинг-провайдера в россии (или в беларуси), чьи ip-подсети внесены в белый список.
2.  методом проб и ошибок тестировать разных операторов в своём регионе.
3.  переезжать.

одно из возможных, но более сложных решений — **использование связки из двух серверов**. теория в том, чтобы поставить на российском сервере (с «белым» ip) простой прокси-переадресатор, который будет направлять трафик на ваш основной сервер за пределами рф. схема подключения выглядит так: `клиент -> российский сервер (ip в вайтлисте) -> зарубежный сервер -> интернет`. этот метод сложнее и дороже, но, возможно, является единственным рабочим способом обойти блокировку по `ip/cidr`.

если вы столкнулись с этим и нашли решение, помогите другим — [создайте «issue»](https://github.com/hxehex/russia-mobile-internet-whitelist/issues).

> **[посмотреть "белый" список](./whitelist.txt)**

#### продвинутое использование: sni-спуфинг в vless/trojan + reality

(саб)домены из этого списка идеально подходят для sni-спуфинга (подмены server name indication) в vless/trojan + reality. идея в том, чтобы замаскировать трафик под подключение к разрешённому сервису. подставив «правильный» (саб)домен (например, случайный cdn яндекса типа `cdnrhkgfkkpupuotntfj.svc.cdn.yandex.net`), можно обойти ограничения. но это сработает, *только* если ваш оператор ещё не перешёл на блокировку по ip.

#### как помочь проекту

нашли рабочий домен? или какой-то из списка больше не работает? [создайте «issue»](https://github.com/hxehex/russia-mobile-internet-whitelist/issues).

---

### 🇺🇸 license | 🇷🇺 лицензия

mit

---

### 🍺🍺🍺

<sup>BTC</sup>
<sub>`bc1qg535zuhkm3wx56tld3vxu9e5qdut0hn9mdrqyq`</sub>

<sup>TON / USDT (TON Network)</sup>
<sub>`UQDo1VvdYK69QrWj8XrwXwPIniDGI4QlplGjlXb2Nkz1WOI1`</sub>

<sup>ETH (ERC-20)</sup>
<sub>`0x4bF16e83095f8493a830bf1b2d9348cc32246c5A`</sub>
