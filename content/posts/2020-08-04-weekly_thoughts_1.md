---
title: Weekly Thoughts
slug: weekly_thoughts_1
date_published: 2020-08-04T21:31:12.000Z
date_updated: 2020-08-04T22:05:26.000Z
tags: 
    - Newsletter
excerpt: An Algorithm for Clouds, Thoughts on GitHub popularity, Cool Rust Tools, Sibling Plants
---

Hey! This is a new newsletter I am trialing. Basically, with previous newsletters I had to stick to a certain topic. Which sucks. I obsess over new things all the time. Soooo…. This newsletter is  just a mish-mash of things I think about, and things I learn. Enjoy! :)

# An Algorithm for clouds
![](https://cdn.substack.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fcd3fba70-20f2-4b07-866e-a25c7744ed57_1472x1963.jpeg)
I was looking up at the clouds one sunny day, and thought to myself “that’s an awfully lonely cloud.”

And I was right. The cloud was by itself. Higher up, you can see it has cloud-friends looking over it. But otherwise, the cloud is alone.

And it got me thinking. Why was the cloud alone? Why does the cloud have smaller sub-clouds, almost like a tail? How is the distance & spacing between clouds determined?

> Is there a mathematical algorithm to determine how clouds _work_?

I started to research the topic. It turns out, we know almost nothing. And most cloud simulations are about as good as my simulation of autonomous driving robots for my dissertation, which is to say, not very effective at real-world usage.

I read [The Cloud Book](https://www.amazon.co.uk/Cloud-Book-How-Understand-Skies/dp/0715328085/ref=sr_1_1?dchild=1&amp;keywords=the+cloud+book&amp;qid=1596563078&amp;sr=8-1&amp;tag=duckduckgo-ffab-uk-b-21), which only left me more confused about how clouds operate. The major players in cloud simulations are video games, but we don’t really know how they operate.

This [Scientific American](https://www.scientificamerican.com/article/why-do-clouds-always-appe/) article tries to explain how clouds form.

The premise is the same as how bubbles form in boiling water. A spot of the water gets hotter than others. When a bubble gets hot enough, the water’s surface tension can no longer hold it so it rises to the top where it bursts into steam.

The same can be said about clouds. Hot buildings can form bubbles of hot air, which bubbles to the top of the atmosphere (well, not always). There the cool air condenses the hot air into water droplets, which becomes a cloud.

This makes me wonder, if we develop a mathematical model for how heat works — could we theoretically & perfectly predict cloud formation over an area? Assuming heat is not totally random.

If this turns out to be the case, I would like to see at least once in my life “cloud art”, where the ground is heated, and the air cooled perfectly to form the cloud into the shape of some art. Assuming these are the only known variables, which most certainly isn’t the case this early on in this scientific regime.
![Cumulus radiatus (Cu ra) | International Cloud Atlas](https://cdn.substack.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F8980bcb6-1dc2-49ba-9de3-72299e9b11f7_4000x3000.jpeg)https://cloudatlas.wmo.int/en/varieties-cumulus-radiatus-cu-ra.html
# Thoughts on RustScan, Ciphey, and Popularity on GitHub

Recently I have found some success on GitHub. 2 of my tools have reached some level of fame. One of them is [Ciphey](https://github.com/Ciphey/Ciphey), an automated decryption tool using AI & NLP. Put in encrypted text, get back decrypted text.
![Ciphey demo](https://cdn.substack.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_lossy/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Ffbbe00d9-037b-410b-a54d-e85368fdb8aa_517x544.gif)
The other is RustScan, a fast port scanner. I built this tool to learn Rust, but it’s gained more popularity than I can imagine
![gif](https://cdn.substack.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_lossy/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F64965fe7-0aba-4ac0-85d2-2de857889611_1721x544.gif)
Okay, enough of the flexing. Let’s talk about *why* they gained popularity.

I believe this is down to 2 simple things:

1. Solve a problem people have (that you have had too, preferably).
2. Advertise clearly in the first few words they see, the problem being solved.

The first point is harder than it sounds. Solve a problem people have. If everyone could do this, we’d all be billionaires. The first step is to seeing a problem you have, and then seeing if other people have it.

For Ciphey, this was the fact that in capture the flag events (hacking competitions) many times we’d have some stupid encryption scheme. Encoded with Base64 then encrypted with Caesar Cipher. Good luck figuring that out by hand!

This meant that a very simple encryption scheme (base64 -> Caesar cipher) could easily take hours and hours of just manual, boring, brute force work. Ciphey solves this problem.
![](https://cdn.substack.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F8a8ed19d-8a49-4007-b4fd-d8cd9c09c9cf_1181x1636.png)
RustScan solves the problem of slow Nmap scans. In pentesting, the very first thing you’d do is Nmap. In fact, you wouldn’t pentest without a port scan. It’s essential. But Nmap frequently takes > 20 minutes to scan.

In a CTF where time is quite literally money (faster = more points = more chance to get money), Nmap just wasn’t cutting it. RustScan fixes this problem.
![](https://cdn.substack.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F33e2597c-1bf3-4b64-8d97-eb8309460a28_1167x512.png)
The second point, show it clearly as soon as the user sees it is the most important.

You can have the best tool in the world, but no one has time to read the source code to understand *why* your tool. You’ve got to advertise it front and centre.

Ciphey’s tagline is “automated decryption tool with AI & NLP”. This explains immediately that its a decryption tool like CyberChef, but *automated*. The automated part is what people want. They don’t want to think about doing it by hand.
![](https://cdn.substack.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F8e9a5d22-035c-4629-9f4a-abb3a23c5b1f_1133x914.png)
RustScan’s Tagline is “Faster Nmap scans” and right below it, it shows **clearly** how it makes Nmap faster.
![](https://cdn.substack.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F9b8d0387-1f26-46d9-8267-863952e778c7_1133x1536.png)
Notice how the logos both say exactly what it does. This is because when people share the GitHub repo on social media, the image appears.

And with the GitHub description too. Look at this social card from RustScan
![](https://cdn.substack.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F74ac2f47-0ac8-41d6-aa6b-667278dfca65_563x781.png)
You don’t even need to click on the repo to learn what it does, it says it right there. Once in the description, and once in the image.

Finally, a closing remark. Very early on in the README I clearly take the largest possible competitor, and I show exactly the need for the tool using Gifs and real time. CyberChef takes too long, too many steps to do what Ciphey can do in 2 seconds. Nmap’s manual scan takes too long.

Show your readers not only the purpose of your tool, but exactly why their current tool aren’t isn’t suitable for the job.

This is why I believe my tools are popular.

# Cool tools I found this week

Since I’ve been learning Rust lately, I decided to explore tools rewritten in Rust. Mostly based on [this](https://zaiste.net/posts/shell-commands-rust/) article.

### [Bat](https://github.com/sharkdp/bat)

A cat clone but better in almost every single way. Syntax highlighting, line numbers, and more.
![Git integration example](https://cdn.substack.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F4142e436-2a02-4eb4-8a3d-71a6d36fdae7_656x327.png)
### [Exa](https://github.com/ogham/exa)

Exa is LS rewritten.
![Screenshots of exa](https://cdn.substack.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fa8b9ca15-00a3-4a1a-9f5a-bdb99c35fe6c_2687x1460.png)
It uses colour by default, so automatically it’s awesome.

- [FD](https://github.com/sharkdp/fd) - Find clone that’s better and simpler. Also, in my opinion, faster.
- [Tokei](https://github.com/XAMPPRocky/tokei) - Code statistics calculator. Flex on your friends with useless metrics like lines of code or # of comments.
- [Grex](https://github.com/pemistahl/grex) - Given inputs, generate a Regex to match those inputs.
- [NuShell](https://github.com/nushell/nushell) - A new command line shell that looks gorgeous.

# Entropy & Compression ratios

I’ve been learning about entropy recently. Entropy is a measure of how “chaotic” a string is, how much “order” it has. This principle has uses in many applications, such as determining the difference between an attack and normal traffic on a network [see here](https://redteam.pl/en/threat-hunting-intelligence.html).

We use entropy in Ciphey to determine when we are “going in the right direction” of decryption. Here’s a cool example.
![](https://cdn.substack.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F0e1c211c-f3ef-4c0f-aa71-fcc5749583c3_1437x1195.png)
This is encrypted with Base64 -> Rot13 -> Vigenère (key: “key”).

The Shannen Entropy is 5.23.

Now if we “decode Base64” and get the entropy again:
![](https://cdn.substack.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2Fa9ceeddb-dece-4113-96c9-5a8c5776ce34_1441x1189.png)
It’s now 3.88. Even though we have no idea how many more decryptions there are, or if our Base64 decoding successfully resulted in the correct decoding (just because it decodes as Base64 does not mean it is Base64 - fun fact) we know we are going in the right direction because the Entropy is decreasing.

Ciphey is using this as part of a heuristic in A* search (we have many other things that go into the algorithm, more on it when I actually code it :P ).

But I thought this was a cool application of entropy. If you ever need to tell the difference between order & randomness, entropy is very useful.

# Co-existing plants
![Indoor Peace Lily Plants: Growing A Peace Lily Plant](https://cdn.substack.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F678c7248-40dc-4b97-a15f-0fa6dee3e075_400x533.jpeg)
Recently I had taken 2 cuttings of my Spider Plant, and created 2 new cute spider plant babies. 

I had actually taken 3 cuttings. 1 of them in its own pot, 2 of them in the same pot. And it got me thinking — do these plants fight each other to survive in the plant pot?

Well it turns out, [plants do know who their siblings are](https://www.google.com/search?hl=en&amp;sxsrf=ALeKk03G3Q5o4WtOWoOihTK42d2rZO3L3w%3A1596572288277&amp;ei=gMIpX9TIEJeQ8gKsypeYAg&amp;q=plants+know+siblings&amp;oq=plants+know+siblings&amp;gs_lcp=CgZwc3ktYWIQAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwAzIHCAAQRxCwA1C-QVjlRGCRRmgEcAB4AIABjwKIAYoEkgEDMi0ymAEAoAEBqgEHZ3dzLXdpesABAQ&amp;sclient=psy-ab&amp;ved=0ahUKEwjUiOegr4LrAhUXiFwKHSzlBSMQ4dUDCAs&amp;uact=5). And they don’t compete for the same space with siblings, they co-exist. But when thrown in with foreign plants, they do fight for root control and space.

This helped clarify that I am not a sadistic plant murderer, and in fact placing 2 sibling plants together wasn’t such a bad idea overall.

# Bye!

Anyway, this has been my first newsletter in this weird series of things I am interested in. Have a good week :D <3

    #myemail {
    background-color: #f0f0f0;
    color: black;
    padding: 15px;
    border-radius: 25px;
            width: 80%;
        margin: 0 auto;
    }
    #little {
    color: grey;
        font-size: 10px;
        }
    #email {
        width: 100%;
        padding: 10px;
        
        }
    #submit {
        width: 100%;
        background: rgb(36,255,204);
        }
        #gdpr { width: 15px; height: 15px; }
    

## At least this isn't a pop up! 😅

        Sign up now and get:
       
- A free 202 page book on algorithmic design paradigms
- A free 107 page book on employability skills
- And much more to help you become an awesome developer!

Email

GDPR: I consent to receive promotional emails about your products and services.
HP

One click unsubscribe anytime.
