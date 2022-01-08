---
title: In Response to My first impressions of web3
slug: response-to-moxie
date_published: 2021-01-1T13:17:32.000Z
date: 2021-01-1T13:17:32.000Z
draft: false
---

> Both gave me a feeling for how the space works. To be clear, there is nothing particularly “distributed” about the apps themselves: they’re just normal react websites. The “distributedness” refers to where the state and the logic/permissions for updating the state lives: on the blockchain instead of in a “centralized” database.

Just to clarify, this is what the author wanted to do. You can create distributed apps easily using [Fleek](https://fleek.co/) or by manually uploading to IPFS, Arweave or Filecoin.

> A server! But, as we know, people don’t want to run their own servers. As it happens, companies have emerged that sell API access to an ethereum node they run as a service, along with providing analytics, enhanced APIs they’ve built on top of the default ethereum APIs, and access to historical transactions. Which sounds… familiar. At this point, there are basically two companies. Almost all dApps use either Infura or Alchemy in order to interact with the blockchain. In fact, even when you connect a wallet like MetaMask to a dApp, and the dApp interacts with the blockchain via your wallet, MetaMask is just making calls to Infura!

This is true at the moment, but there is work being done on [Light Clients](https://eth.wiki/concepts/light-client-protocol) which:

> The purpose of the light client protocol is to allow users in low-capacity environments (embedded smart property environments, smartphones, browser extensions, some desktops, etc) to maintain a high-security assurance about the current state of some particular part of the Ethereum state or verify the execution of a transaction.

And also alternatives to Infura such as [Pockt Network](https://www.pokt.network/) which is a decentralised Web3 infrastructure company. Per Pockt Network's website:

> Instead of deploying to a single service provider, paying absurd fees for random outages and leaked data, tap into Pocket’s trustless API protocol and route your requests to 1000’s of independent full nodes. Available for all major blockchain networks.

Moxie then goes on to say....

> These client APIs are not using anything to verify blockchain state or the authenticity of responses. The results aren’t even signed.

Both of the proposed solutions (Pockt, Light Clients) solve this.

Moxie then talks about:

> Partisans of the blockchain might say that it’s okay if these types of centralized platforms emerge, because the state itself is available on the blockchain, so if these platforms misbehave clients can simply move elsewhere. However, I would suggest that this is a very simplistic view of the dynamics that make platforms what they are.
> I also wanted to create a more traditional NFT. Most people think of images and digital art when they think of NFTs, but NFTs generally do not store that data on-chain.

This is true, most NFTs do not store data on-chain. But this is not always true, you can store the data on the chain. You can also use alternative layer-1s such as [Tezos](https://tezos.com/), [https://www.avax.network/](Avalanche) which makes it much more cost efficient to store on-chain data. However, I am not a fan of this. One of the big rebuttals we don't have an answer for is "what if we store illegal images on the chain?" currently it is too expensive to do so, but genuinely there is no work being done on this that I can see and it is a concern for everyone.

You also have to consider sending NFTs to other people that are prohibitively expensive to sell. You can easily make an NFT that costs say, $4000 to sell (just make it contain a lot of data) and this person will be stuck with it attached to their identity forever. Opensea lets you "hide" them, but this only works on their frontend.

>  Looking at many of the NFTs on popular marketplaces being sold for tens, hundreds, or millions of dollars, that URL often just points to some VPS running Apache somewhere.

This is a lie. Most NFTs which sell for millions use IPFS, Arweave, Filecoin or others for decentralised storage of data. A lot of NFTs do use Google Drive or Imgur or whatever. However, I can promise you that one of the first things people do when making sure they are not rugged (crypto-term for scammed) is to make sure it's not possible for the author to suddenly delete or change the image.

> So as an experiment, I made an NFT that changes based on who is looking at it, since the web server that serves the image can choose to serve different images based on the IP or User Agent of the requester.

I just wanted to point out that this was hilarious and I saw it was taken down by Opensea. My belief is that image changing is often related to scams, so Opensea took it down thinking it was a scam.

> What I found most interesting, though, is that after OpenSea removed my NFT, it also no longer appeared in any crypto wallet on my device.
> A wallet like MetaMask needs to do basic things like display your balance, your recent transactions, and your NFTs, as well as more complex things like constructing transactions, interacting with smart contracts, etc. In short, MetaMask needs to interact with the blockchain, but the blockchain has been built such that clients like MetaMask can’t interact with it. So like my dApp, MetaMask accomplishes this by making API calls to three companies that have consolidated in this space.
> All this means that if your NFT is removed from OpenSea, it also disappears from your wallet. It doesn’t functionally matter that my NFT is indelibly on the blockchain somewhere, because the wallet (and increasingly everything else in the ecosystem) is just using the OpenSea API to display NFTs, which began returning 304 No Content for the query of NFTs owned by my address!

This is true, wallets suck so much it's funny. I was sent a £2k NFT the other day which I can't sell because Opensea has glitched and my wallet won't show me the NFT, which means I can't send it or sell it! (they are working on this, and I have told them that relying on centralised Opensea is a very bad idea).

Almost everyone in Web3 hates Opensea and their centralised mess. There are alternatives being worked on such as [OpenDao](https://www.theopendao.com/), [NFTX](https://nftx.io/) and more. The sooner Opensea dies, the better.

I think this is a very fair comment from Moxie and we should dunk on wallets and Opensea for this mess they've created. However, I wanted to point out that people in Web3 don't sit idly by and enjoy this centralised mess. We are actively building alternatives!

> Likewise, the web3 protocols are slow to evolve. When building First Derivative, it would have been great to price minting derivatives as a percentage of the underlying’s value. That data isn’t on chain, but it’s in an API that OpenSea will give you. 

This is how markets work, and why arbitrage exists. See [Flash Boys](https://en.wikipedia.org/wiki/Flash_Boys) for how this works in the stock market. Your NFT is only worth what someone wants to pay. Someone on Opensea may pay 5 eth for it, but someone on Discord may pay 10 eth.

You chose to use Opensea to get the value of what people on Opensea will pay you for. That data isn't on chain because that's not how markets work, although it'd be cool if every market place used the same market-order book on-chain.

> People are excited about NFT royalties for the way that can benefit creators, but royalties aren’t specified in ERC-721

You're right, royalties are specified in [ERC-2981](https://eips.ethereum.org/EIPS/eip-2981). I would also like to point out that ERC-721 is not the only NFT standard, take a look at [ERC-1155](https://eips.ethereum.org/EIPS/eip-1155) if you wanted to dive deeper :-) 

> so OpenSea has its own way of configuring royalties that exists in web2 space. Iterating quickly on centralized platforms is already outpacing the distributed protocols and consolidating control into platforms.

This is true, but also, fuck Opensea.

> “It’s early days still” is the most common refrain I see from people in the web3 space when discussing matters like these. In some ways, cryptocurrency’s failure to scale beyond relatively nascent engineering is what makes it possible to consider the days “early,” since objectively it has already been a decade or more.

This is because it is early days, still. As you could read from my article there is so much work being done. NFTs are only 3 years old. Layer 1's and 2's are arguably only around a year old. 

> When you think about it, OpenSea would actually be much “better” in the immediate sense if all the web3 parts were gone. It would be faster, cheaper for everyone, and easier to use. 
> For example, to accept a bid on my NFT, I would have had to pay over $80-$150+ just in ethereum transaction fees.


This sounds like you're describing a [layer-2 solution](https://www.youtube.com/watch?v=BgCgauWVTs0), thankfully Opensea supports polygon which does make it cheaper, faster, and easier to use. I am personally hoping for [zk-rollups](https://docs.ethhub.io/ethereum-roadmap/layer-2-scaling/zk-rollups/) to really make it cheaper, easier to use.

I will say we shouldn't strive for "cheaper", we should strive for "so cheap its free". Opensea lets you mint NFTs for free using Polygon. The benefits of fully decentralised technologies without the downside of a microtransaction at every aspect of it. I talk more about this later.

> So the money draws people into OpenSea, they improve the experience by building a platform that iterates on the underlying web3 protocols in web2 space, they eventually offer the ability to “mint” NFTs through OpenSea itself instead of through your own smart contract, and eventually this all opens the door for Coinbase to offer access to the validated NFT market with their own platform via your debit card. That opens the door to Coinbase managing the tokens themselves through dark pools that Coinbase holds, which helpfully eliminates the transaction fees and makes it possible to avoid having to interact with smart contracts at all. Eventually, all the web3 parts are gone, and you have a website for buying and selling JPEGS with your debit card. The project can’t start as a web2 platform because of the market dynamics, but the same market dynamics and the fundamental forces of centralization will likely drive it to end up there.

Moxie is right about this currently. It is harder to use true web3 stuff than it is to use a centralised platform. The user experience of Web3 is its biggest problem, and something we are all working very hard on. Things like [Argent Wallet](https://www.argent.xyz/) are working hard to improve this, but we still have a long way to go because we are in the early days.

# Conclusion

I think was this a fair article that accurately portrays some parts of web3 at this given moment in time. Moxie mentions:

> I have only dipped my toe in the waters of web3.

Which is fair. I just thought I'd write this and explain what's being done to fix this and go further. My personal pet hates for crypto are:

* Illegal images being sent to your wallet, forcing you to go to prison in some places.
* Fuck Opensea.
* Every user will have to pay for everything. I am actually working on this myself, I think staking and using the proceeds from staking to pay for non-web3 users would work. I'm interested to hear how others are letting web2 users use web3 without paying. [DM me](https://twitter.com/bee_sec_san)!

There is some genuinely cool tech being worked on here, but due to the monetrary aspect there are scams up to my eyeballs. And those scams make the whole industry look bad. 

For some of the cool uses, please check out:
* [Axie Infinity and how it's bringing entire nations out of poverty](https://www.notboring.co/p/infinity-revenue-infinity-possibilities)
* [Terra Luna and the mission to create the perfect stablecoin](https://www.readthegeneralist.com/briefing/terra)
* [Decentralised Finance and being your own bank](https://www.youtube.com/watch?v=17QRFlml4pA)

Note: Not everyone should be their own bank, but it's helpful for some who want to be.

WAGMI (ps: love you Moxie. Big big fan!)