# russia mobile internet whitelist

[![discord](https://img.shields.io/discord/1282083082849091615?style=flat-square)](https://discord.gg/qpbdf8dxgg)

🇺🇸 a list of domains that stay live in russia when the mobile internet gets "restricted".
<br>
🇷🇺 список доменов, которые остаются доступными в россии, когда мобильный интернет «ограничивают».

---

### **🇺🇸 english**

#### what's the problem?

in russia, mobile internet is sometimes "shut down" — a technical way of saying it's heavily restricted. this usually happens during protests, drone attacks, or other events to control the flow of information. during these shutdowns, only a handful of whitelisted services remain online. these typically include major banks (sberbank, t-bank), maps (yandex, 2gis), government portals (gosuslugi), and a few major domestic services like yandex, vk, and avito.

#### the whitelist

the full, regularly updated list of (sub)domains is in `whitelist.txt`.

#### ⚠️ caution: the situation is getting worse

this is no longer a problem specific to one provider. what started with "beeline" using aggressive whitelists has now become a widespread practice.

**recent reports confirm that "t2" (tele2), once considered a reliable alternative, has also started implementing a combined `ip/cidr + sni` whitelist in many regions.** this means simply switching your mobile provider is no longer a guaranteed solution. other providers like "mts" and "megafon" are known to use similar methods.

the core issue is the move from a simple `sni` (server name indication) whitelist to a combined `ip + sni` one. this means that even if you correctly spoof a whitelisted domain for your vless/trojan + reality setup, the connection will be blocked if your server's ip address isn't in their allowed list (the cidr whitelist).

your remaining options are limited:
1.  find a hosting provider in russia whose ip subnets are whitelisted.
2.  keep testing different mobile providers in your specific area.
3.  move.

if you've faced this and found a solution, please help others by [opening an issue](https://github.com/hxehex/russia-mobile-internet-whitelist/issues).

> **[view the whitelist](./whitelist.txt)**

#### use case: vless/trojan + reality sni spoofing

these domains are ideal for `sni` (server name indication) spoofing with vless/trojan + reality. the goal is to disguise your traffic, making it look like it's heading to an approved, whitelisted service. by spoofing a common, "allowed" (sub)domain (e.g., a random yandex cdn like `cdnrhkgfkkpupuotntfj.svc.cdn.yandex.net`), you can bypass these restrictions, but only if the provider isn't using an ip-based whitelist.

#### how to help

found a domain that works? or is one on the list dead? [open an issue](https://github.com/hxehex/russia-mobile-internet-whitelist/issues).

---

### **🇷🇺 русский**

#### в чём проблема?

мобильный интернет в россии периодически «выключают» — то есть, подвергают жёстким ограничениям. обычно это происходит во время протестов, атак дронов или других событий, чтобы контролировать информационное поле. в такие моменты работать остаются только сервисы из «белого списка»: банки (сбербанк, т-банк), карты (яндекс, 2гис), госуслуги и другие крупные местные сервисы вроде вк, авито и рутуба.

#### "белый" список

полный и регулярно обновляемый список (саб)доменов находится в файле `whitelist.txt`.

#### ⚠️ внимание: ситуация ухудшается

это больше не проблема одного конкретного оператора. то, что начиналось с агрессивных белых списков у «билайна», теперь стало повсеместной практикой.

**по последней информации, «т2» (теле2), который раньше считался надёжным вариантом, тоже начал внедрять комбинированный вайтлист по `ip/cidr + sni` во многих регионах.** это значит, что простая смена оператора больше не гарантирует результат. другие, вроде «мтс» и «мегафона», используют схожие методы.

ключевая проблема — переход от простого вайтлиста по `sni` (server name indication) к связке `ip + sni`. даже если вы правильно настроили сервер с vless/trojan + reality и подставили рабочий (саб)домен, соединение будет заблокировано, если ip-адрес вашего сервера не находится в разрешённом списке сетей (том самом cidr вайтлисте).

вариантов остаётся немного:
1.  искать хостинг-провайдера в россии, чьи подсети внесены в белый список.
2.  методом проб и ошибок тестировать разных операторов в своём регионе.
3.  переезжать.

если вы столкнулись с этим и нашли решение, помогите другим — [создайте «issue»](https://github.com/hxehex/russia-mobile-internet-whitelist/issues).

> **[посмотреть "белый" список](./whitelist.txt)**

#### продвинутое использование: sni-спуфинг в vless/trojan + reality

(саб)домены из этого списка идеально подходят для sni-спуфинга (подмены server name indication) в vless/trojan + reality. идея простая: вы маскируете свой трафик под подключение к разрешённому сервису. подставив «правильный» (саб)домен (например, случайный cdn яндекса типа `cdnrhkgfkkpupuotntfj.svc.cdn.yandex.net`), можно обойти ограничения. но это сработает только в том случае, если ваш оператор ещё не перешёл на блокировку по ip.

#### как помочь проекту

нашли рабочий домен? или какой-то из списка больше не работает? [создайте «issue»](https://github.com/hxehex/russia-mobile-internet-whitelist/issues).

---

### 🇺🇸 license | 🇷🇺 лицензия

mit
