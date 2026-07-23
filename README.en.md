<p align="center">
  <strong>English</strong> | <a href="README.md">Русский</a> | <a href="README.uk.md">Українська</a>
</p>

# russia mobile internet whitelist

### 🍺🍺🍺 donations

<sup>BTC</sup>
`bc1q5cws5mx9x784kwn3zj6uz0q9cvdpj65lzenv6v`

<sup>SOL</sup>
`3UTz412qPLAjNJSbRCzbs1CSMQRwXNnSXhct6twmhY6J`

<sup>ETH</sup>
`0x98e52948c78707b2003deb550a63a4705afccc1a`

<sup>USDT TON/just TON</sup>
`UQChsyq45Myo46fGh5kolTvtYW6Oye5IVkpd7Pp3MLEagssV`

<sup>USDT TRC20</sup>
`TLvej81gMURc2xXNJSZo4S3Dmmax6AtqHK`

<p align="center"><b> please, star this repository so more people can see it.</b><br><br><em> discord server: active help, community support, and huge amount of info that doesn't fit here.</em><br><br><a href="https://discord.gg/QPBdMf8dxG"><img src="https://img.shields.io/discord/1282083082849091615?style=for-the-badge&logo=discord" alt="discord"></a></p>

 a list of domains and ips that stay live in russia when the mobile internet gets "restricted".

---

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
*   **android:** husi, v2rayng, lxbox.
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

###  license

mit

---

no star history because of dogshit github 30jun update :joy:
