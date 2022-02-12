---
title: Wallet Security for New Witches
slug: wallet-security
date: 2022-02-11T23:42:12.596Z
draft: false
toc: true
socialImage: "/media/p2p.jpg"
cover:
    image: "/media/p2p.jpg"
---


The problem with being your own bank is that you are your own bank. Often when people are phished / scammed they cry out for centralisation, for some sort of regulatory body to protect them. Sadly this is not how cryptocurrencies work.

<figure>
	<img src="/media/wallets/hacked_apes.png" alt="">
	<figcaption></figcaption>
</figure>

When you are your bank, you are responsible for your security. No one else is. It is your fault if you get hacked.

Most people never bother investing in security, until it is too late. Once you are hacked, no matter how much you invest in security you can never go back to where you were before. This is why it's important to invest in security now.

Most wallet security articles are written by people who work on wallets, they stand to directly gain from advertising their wallet. Them saying "use this wallet" makes them more money. Sometimes this is at the detriment to your security. I do not work at a wallet company, so I stand to gain nothing from this article. I am not biased.

# Understanding your threat model

As part of your threat model, you need to understand how much you're willing to lose. I prefer following this adage:

> If you're having trouble sleeping at night, reassess your risk based on your tolerance

If I have trouble sleeping at night thinking "what if my NFTs got hacked?" or "what if they go to 0?" I reassess. 

For this article, we'll take someone with an imaginary salary of £10,000. This is just an example, but you should reassess your threat model based on how well you can sleep, and remember -- **you forget you need security until you wish you had it**, therefore it's better to be overly cautious.

# £0 - £1000

**10% of yearly salary**

To be honest, just use an exchange. No one cares. They are pretty safe, and for such a small amount you do not need to worry about it.

# 1k - 5k

**10 - 50% of yearly salary**

Now we're getting to the part about sleeping bad at night. If 50% of my yearly salary (6 months!) was tied up in an exchange, I would start losing sleep.

Don't get me wrong, exchanges are secure but:

> Not your keys, not your crypto!

Lets explain this. **Your crypto coins are not stored in the wallet**. When you buy some on Coinbase, Rainbow, Argent or whatever your coins do not exist on that wallet.

There are 3 parts to a wallet:
1. Your address, such as `0xa7051d46a3C27C7E86aFAbf183DF51B73674AdFA`. This is the last 20 bytes of your public key.
2. Your [public key](https://skerritt.blog/how-does-public-key-cryptography-work/).
3. Your [private key](https://skerritt.blog/how-does-public-key-cryptography-work/).

Let's say you have a number (6), and when you sign the number with your private key it turns into a different number. (6 * private key = 9) If someone signed that new number with your public key, they'd get the original number (9 * public key = 6).

When you want to prove ownership over the wallet, an app will give you a random message and ask you to sign it with your private key. Once you've done that, the app can decrypt it using your public key. If the message it decrypts to is the same message they asked you to encrypt, they know you own the wallet.

Your wallet does not contain the coins or NFTs you own. Instead, because the blockchain is a public ledger your public key is listed as the owner of them. Essentially each token you buy keeps a lil internal database of who owns what. And that lil internal database just happens to be the blockchain.

Now, when you use Coinbase or Kraken they have both the private key and public key. They own your wallet, you do not own it.

If 50% of your salary is owned by a corporation, that should scare you. There have been many times when these companies were hacked , or they just didn't like someone and stole their money:
* [Crypto.com hacked, loses $30 million](https://www.wired.com/story/crypto-hack-nso-group-security-news/)
* [Liquid hacked, loses $90 million](https://www.cnbc.com/2021/08/19/liquid-cryptocurrency-exchange-hack.html)
* [BitMart hacked, loses $196 million](https://www.coindesk.com/business/2021/12/05/crypto-exchange-bitmart-hacked-with-losses-estimated-at-196-million/#:~:text=The%20hackers%20were%20able%20to,of%20approximately%20USD%20150%20millions.&text=The%20%24196%20million%20in%20losses,centralized%20exchange%20hacks%20to%20date.)


In cryptocurrencies we say:

> Not your keys, not your wallet

If you do not own the private key, it is not your money -- you do not have custody over it.

For this reason, the biggest step-up of security we can do at this point is to move our money to a wallet that we control. There are quite a few we can use, in order of my favourites:
1. Metamask
2. Argent
3. Rainbow

Adding more security increases the complexity of using things. In this case, it's _seed phrases_. Seed phrases are encodings of your private key. **Anyone who has your key phrase has access to your money**.

No one will **ever** need to know it other than you. Not Metamask, not Rainbow or otherwise. If you give this out, you are giving away all your money to someone else.

This is the first & only requirement of our security at this level. Do not, under any circumstances -- **EVER** give away your seed phrase.

For what it's worth, I hold my metamask seed phrase in my password manager. At this level of security trusting a password manager is good, as their whole job is to protect your private information and a loss of this level won't cause much pain.

# 5k - 10k

For 50 - 100% of your yearly salary, you'll want to take things a bit more serious. This kind of loss is enough to upset you significantly. 

As we advance up the security ladder, 2 things are often true:
1. We need to learn more.
2. We slightly complicate our current process.

For this part, let's learn! 🤓

## Hot vs Cold wallets

Here's the main differences:

| Hot Wallet | Cold Wallet |
| --- | --- |
Easy to access | Harder to perform transactions with
Connected to the internet 24/7 | not connected 24/7
Exists on your device, vulenrable to Windows, IOS hacks etc | Uses custom hardware & firmware, not as vulnerable

There's some common misconceptions, so lets look at the bad parts of hot wallets:

### Connected to the internet 24/7

Whenever you use Metamask or Rainbow, it is connected to the internet. Streaming data such as prices of coins, your assets or otherwise.

By being connected 24/7 it makes it more likely for an attacker to hack it, as it's always online.

Hardware wallets are sometimes stated as being "offline". This is not true. When you connect a hardware wallet to your PC, it becomes online. You can test this by trying to submit a transaction with your internet turned off. Instead, they are offline most of the time.

**Exists on your device**
When you use Metamask, it can be hacked in a bunch of ways:
1. Via Windows / Mac OS itself.
2. [Via an NFT sent to metamask](https://medium.com/@alxlpsc/critical-privacy-vulnerability-getting-exposed-by-metamask-693c63c2ce94)
3. Someone uses your computer.
4. Private key is loaded into RAM, a virus reads it and takes your money.
5. Your browser is hacked.
6. Screensharing for a movie night in Discord, you accidentally show the seed phrase trying to flex your money (this is a true story from someone I know 😢)

Hardware wallets solve this _because_ they use custom-made hardware & software. It's a lot harder to write a virus for new hardware with new firmware than it is for Windows / Mac.

This doesn't mean it's impossible, just unlikely enough that we can take that risk at this level of investment.

In short: hardware wallets are good because they reduce your attack vector, but they are not the be-all-end-all to security like most people say.

**PS:** write your seed phrase down on the paper the hardware wallets give you.

# 10k - 30k

Now we're at 1x to 3x annual salary. If we lost a year of annual salary, I'd be very upset! 3 years would set me back 3 whole years from my financial goals!

We need to take things seriously. If you read a lot of other security of wallets articles (I do) you'll know they very often end around hardware wallets. If they don't they often end up with "use multiple wallets".

## Multiple Wallets

A common misconception is that more wallets = more security because if one wallet is hacked the others are safe. This is not true. 

If you had 5 safes with keys, and all those keys were on the same keyring you do not have more security because there are more safes. In the same way, you do not have more security by having more wallets.

It is not the diversification of your assets amongst wallets that make them safer, it is the diversification of the security of those wallets. Making sure each wallet has unique and their security matches their operational use is complex. For example, one wallet might contain £500k and another £1k. How do you ensure the £500k wallet and £1k wallet have good security for their uses but are separate entities? 

Despite what crypto people think, banks are the best at this. They have been storing money for thousands of years. Banks have multiple levels of security like so:
* Vault, maximum security - 99% of the money
* ATMs, medium-security - 0.9% of money
* Teller machines, lowest security - 0.1% of the money

Banks reduce the amount of money at each level of security, but they also reduce availability. It is a lot harder to get money from the vault than it is from the teller machine. This is a common problem in security. You can't have an incredibly secure system against all possible attacks which maintain easy access to the people that need to access it.

It is also not feasible to have multiple maximum security vaults, especially for an individual. Just know you can have 1 super-strong vault and multiple wallets with lesser security for your use case.

## CIA Triad
The CIA Triad is a popular model designed to guide policies on information security.

<figure>
	<img src="/media/wallets/cia.png" alt="">
	<figcaption></figcaption>
</figure>

There are 3 parts to it:
* Confidentiality - Limits access to information unless necessary.
* Integrity - Protects data from deletion/modification by an unauthorised party.
* Availability - Information is available to users when they need it.
  
As we flow through this article we will see more concrete examples of these. 

Understanding the triad helps us make better decisions. Security is all about tradeoffs, we need to learn what our tradeoffs arre.

## Single points of failure

Every time we've gone up a level in this article I ask myself the question:

> What are the single points of failure?

Then I rank them all from most likely to least likely. And then I calculate what wouldn't reduce availability the most.

For example, upgrading from a hot wallet (metamask). The single points of failure are:
1. Metamask actively runs code on the wallet to display NFTs, prices and others. These require API calls to external parties which may be poisoned.
2. Metamask runs on my computer and thus my computer needs better security.
3. Vladimir Putin could come to my home with the KGB and waterboard me until I give him my password.
4. Quantum computers are invented and my seed phrase is useless as public-key cryptography is broken.
5. My house burns down, including all of my computers and paper and I no longer have a copy of my seed phrase.

Now I rank them from most likely to least
1. My house burns down, including all of my computers and paper and I no longer have a copy of my seed phrase.
2. Metamask actively runs code on the wallet to display NFTs, prices and others. These require API calls to external parties which may be poisoned.
3. Metamask runs on my computer and thus my computer needs better security.
4. Quantum computers are invented and my seed phrase is useless as public-key cryptography is broken.
5. Vladimir Putin could come to my home with the KGB and waterboard me until I give him my password.

Now I look at each one and ask "will the solution reduce my availability so much it is not worth it at this level of security?"

**House burns down**
Solution: off-site backup or seed phrase on a fireproof container.
Availability score (10 affects us a lot, 0 is not a lot): 6, because whenever we need to restore our wallet we need to travel to the off-site backup or open/read a fireproof container instead of using a password manager.

**Metamask runs on my computer**
Solution: a hardware wallet.
Availability score: 3, because it works exactly like a hot wallet except you need to plug it in.

**Metamask actively runs code**
Solution: Use GETH to create a wallet as it has no real interface like Metamask.
Availability score: 9, as it makes using DAPPS and others almost unusable unless we manually sign transactions using the CLI.

**Quantum Computers exist**
Solution: create quantum-resistant crypto
Availability score: 10, as we'd need to invent this and that could take 100+ years.

**Vladimir Putin comes over**
Solution: Make it so I do not know the seed phrase, require multi-signature or Sharmir Sharing
Availability score: 8, as it requires a key ceremony which can take up to a month to plan. And if we ever need to use our wallet it will likely take 5 whole days just to buy an NFT on Opensea!

The thing we can do at this level to increase our security without decreasing our availability is to solve "Metamask runs on my computer", which is to get a hardware wallet!

Everything we do in security is a tradeoff, we need to make sure the tradeoffs are the best option for what we want. It's easy to make a wallet no one can access (throw away the seed phrase and never use it), security is about making a secure wallet that we can also access & use.

Now we're at the next level, 1x  - 3x our salary. Our next security upgrade is to protect our seed phrase from our house burning down.

###  Better Seed Protection

If you remember from our CIA triad:
* Confidentiality - Limits access to information unless necessary.
* Integrity - Protects data from deletion/modification by an unauthorised party.
* Availability - Information is available to users when they need it.

We've been focused on Availability and Integrity so far. How do we ensure our wallet is both highly available to us, and also no unauthorised transactions occur? Let's introduce some Confidentiality.

We, the owners of the wallet -- do not need constant access to the seed phrase unless it is necessary. We do not need it in a password manager or on a bit of paper in a draw. We only need it in case of emergencies, when our hardware wallet dies and we need to restore it or we get a new one. So let's keep this in mind and increase the confidentiality here, reducing availability of the seed phrase and in turn protecting the seed phrase from fires and other natural disasters!

<figure>
	<img src="/media/wallets/seasaw.png" alt="">
	<figcaption></figcaption>
</figure>

We can do that using something like a [Cryptosteel capsule](https://cryptosteel.com/product/cryptosteel-capsule/). They cost a pretty penny but they are our next best security upgrade. If our house burns down or gets flooded at least our seed phrase will be okay!

It'll take longer for us to recover the seed phrase (increasing confidentiality) but not too long that it burdens us.


# 30k - £1 million

Now we're at this stage, lets evaluate some of the problems we have:

* Ledger is not open source so a government may force a backdoor into the code.
* Vladimir Putin may hit you until you give up your seed phrase.
* Since your seed phrase is now in a pretty capsule, someone might come over and steal it.
* Quantum computing is invented and renders crypto useless.
* You lose your seed phrase and can no longer recover your wallet.

Now, what if I told you that there is a technology that solves most of these problems? A multi-signature wallet! These types of wallets require multiple **other** wallets to approve transactions. Think of it like those nuclear keyholders in movies!

<figure>
	<img src="/media/wallets/americans.jpg" alt="">
	<figcaption></figcaption>
</figure>

Let's take a look at Argent as a wallet since it's the most friendly multi-sig I can find, and go through each of our points.

* Ledger is not open source so a government may force a backdoor into the code.

Argent is fully open-source and you can view the contract yourself. The threat goes from "full hardware/software backdoor" to just "backdoors might exist in the app".

* Vladimir Putin may hit you until you give up your seed phrase.
Argent does not have a seed phrase as it is a multi-signature wallet, Vladimir Putin will need access to all the other wallets to get access to yours!

We can further increase this security by allowing our friends to become keyholders of our wallets, so Putin will have to visit all of them to get the seed.

* Since your seed phrase is now in a pretty capsule, someone might come over and steal it.

No seed!

* You lose your seed phrase and can no longer recover your wallet.

No seed! You just need the majority of keyholders to restore a wallet.

The number 1 problem with hardware wallets is their single point of failure is their seed. Using multi-sig fixes this. There is no alternative at this level or higher, we **need** multi-sig wallets.

Now, here is where it gets cool. Because Argent is a mobile app with a nice UI, its availability isn't as bad as what we'd normally expect at this level. We have the same level of integrity (Argent's integrity matches your phones) & availability as a ledger, but much more security. 

<figure>
	<img src="/media/wallets/argent.png" alt="">
	<figcaption></figcaption>
</figure>

I recommend Argent for everyone who needs the security of a Ledger. Since we've gone through this process you should come to the same conclusion. Eventually, we need multi-signature based wallets for the storage of expensive assets. If Argent is just as easy to use as a mobile wallet like Rainbow or Metamask, why not skip all the fuss and just use it?

# 1 million - 10 million

At this level, it would be life-ruining on our £10k yearly salary! Now we're using Argent, what could go wrong? 

The main complaint by people (those same people who promote the wallets they work on) is if Argent dies, what happens? More specifically:

* Argent the company may shut down, meaning we can't use Argent for phone/email multi-sig
* Argent the company may shut down so the app becomes unusable.
* Apple may remove the app from the AppStore.
* Our iPhone gets hacked and is no longer secure.
* Our email/phone for the Argent guardian exists on our phone

Essentially the 2 biggest problems we have are:
* Argent the company
* Our mobile phone

We can solve both of these with 1 solution. So far we've been using Argent as our multi-signer, we can instead use different wallets to sign our transactions! 

Let's dig out our Ledger (see my section on Ledger security) and find a Metamask wallet or two, they will become signers of our wallet and we can disable the Argent guardian. By disabling the Argent wallet and using our wallets as signers:
* If Argent the company dies, we can recover and use our wallet as we own the signers and the smart contract is open source & cannot be removed. See https://www.argent.xyz/blog/the-ultimate-non-custodial-test/
* If our iPhone gets hacked, the hackers would need access to our Ledger / Metamask to sign transactions.
* If the app is  removed from the App store and Argent dies, we can still sign the transaction using this https://www.argent.xyz/blog/the-ultimate-non-custodial-test/

This reduces our availability slightly as it's now harder to sign transactions, Argent fixes this by using trusted addresses which means we can choose to not require verification for sending to other wallets. it increases our confidentiality a lot as the confidentiality no longer matches our phone, and our integrity is increased a lot because if Argent dies / the government wants to shut it down we can still use it.

Alternatively, recruit some friends to be your [guardians](https://support.argent.xyz/hc/en-us/articles/360022631992-About-guardians).

# 10m+ 

At this point not only do we have to protect out wallet, but we have to protect ourselves. £10 million is generational changing money. It's so much money we should expect to have enemies

<figure>
	<img src="/media/wallets/enemies.jpg" alt="">
	<figcaption></figcaption>
</figure>

Throughout this article, we have looked at the weak points and fixed them. At this level of money, there is 1 big weak point -- you.

<figure>
	<img src="/media/wallets/xkcd.png" alt="">
	<figcaption></figcaption>
</figure>

No matter how good our security is, whether we put our keys into a safety deposit box or not we are now the weakest link. How do we solve this?

## Sharmir's Secrets

On our measly £10k salary, £10 million will completely change our family lineage. This may be £100 million to you, or £1 billion. But to us, £10 million is **a lot**.

We want to have maximum security, which means availability tanks so integrity & confidentiality skyrockets. We want a system that takes us 3 - 7 days to complete a transaction on, and to do that requires coordination and monumental work that an attacker would have a very hard time doing.

Firstly, we need an [airgapped laptop](https://www.thesslstore.com/blog/air-gapped-computer/) without any storage, just RAM, running a copy of [Coen](https://github.com/iana-org/coen). Coen is a live (not stored on a hard drive) operating system. Coen is used for root key ceremonies, but its most important feature is that it's reproducible. This means with the same inputs we get the same output, so anyone can verify in the future the operating system was not modified before the ceremony.

All materials (the operating system, the passwords) are stored on CD-R disks because they can only be written once, meaning that they cannot be modified. Each disk is then copied 3 times and stored in tamper-proof bags.

Then we want to generate a wallet using Geth. 

```
geth account new --password /mnt/password
```

Geth lets us make new wallets entirely offline (Argent is online only), the `--password` argument reads the password from CD-R without placing it into standard input. The password is multiple CDs split using [Shamir's Secret Sharing Scheme](https://en.wikipedia.org/wiki/Shamir%27s_Secret_Sharing) and we combine them on-the-fly on the laptop at the time of need.

Once we've done this, we can mail the copies of the CDs to our key ceremony holders. These people should not know each other and be trustworthy, and their identities are to be kept secret. They are also required to live in other parts of the world. We will have 7 keyholders and require 3 to reconstruct the password to the account. I prefer mailing the CDs because unless we are a business, this allows the keyholders to remain anonymous to each other. We can even split the private key using the same schema.

When we want to create a transaction to move money out of our new vault, we should fly 3 of the 7 keyholders out to a secret location where they will use their CDs to reconstruct the password & private key. The transaction we want to make should be done entirely offline, and then once the transaction is signed offline we can bring it out of the room and upload it to the Ethereum network.

In an emergency, with unlimited money and resources, it should take around 1 week to fully coordinate this. I would give it 6 months in a non-emergency to make sure everyone's schedules line up. We have tanked our availability, but if it takes us this long to gain access to our wallet imagine how long it'd take attackers.

Ideally, we buy assets on a lower security wallet and send them to our vault.

For more on [key ceremonies, click here for how a bank does it](https://monzo.com/blog/2021/11/18/protecting-our-most-sensitive-secrets). This was just a taster in how complex & advance our security can become 😉 I am available for consultations for a fee too 😜

# Conclusion

Not only should you be coming away with the ideal security setup for you, but also how to derive better security setups in the future. I hope you liked this article :)

A very short summary is:
* under £1k - Use Coinbase or whatever.
* Under £5k - Use Metamask if you like, so long as you own the keys.
* £5k and higher - use Argent

Then you just increase the security of the signing keys as you get more advanced.

Alternatively, follow the hardware wallet route if you like -- but eventually you'll need multi-signature security so why not start there.