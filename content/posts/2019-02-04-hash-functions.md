---
title: Hash functions explained for non cryptographers
slug: hash-functions
date_published: 2019-02-04T13:15:26.000Z
date: 2019-11-19T01:47:38.000Z
tags: 
    - University
    - Computer Science
    - Infosec
excerpt: Hash functions are one of the most important concepts in cryptography and cryptocurrencies. This article explains how they work, simply.
---

A hash function takes a message, m, and returns a pseudo-random string of letters/numbers which should be unique to that message. Let's say the hash function returns "aBc67D" for the message "I love dogs". This function should not return the same "aBc67D" for "Donuts are cool". 

Hashing algorithms have 3 requirements:

1. A hashing algorithm needs to be reasonably fast to compute and reasonably fast to verify.
2. If you change one single bit anywhere in the message, the outputted string must look completely different.
3. You must avoid collisions.

For the first point, the algorithms have to be fast. Hashing algorithms are often used by much slower algorithms (such as RSA) to speed up the algorithm. As a side note, most hashing algorithms are designed to be one-way functions.

The algorithm has to be fast, but it does not have to be *efficient*. Efficient hashing algorithms make causing collisions easier for attacks. Hashing algorithms need to be resistant towards "*pre-image attacks*". That is, given a hash, it should be extremely difficult to calculate  retrace the deterministic steps taken to reproduce the value that  created the hash (i.e. the pre-image).

For the second point, if using *[SHA-5](https://www.ibm.com/support/knowledgecenter/en/SSYKE2_7.1.0/com.ibm.java.security.api.doc/jcefips/com/ibm/crypto/fips/provider/SHA5.html)* and we input:

    abc = a9993e364706816aba3e25717850c26c9cd0d89d

An important feature we want is that if we were to change the original string even slightly by say one letter the entire outputted hash has to change. If we input "*abd"* we get:

    abd = cb4cc28df0fdbe0ecf9d9662e294b118092a5735

So the idea of randomness here is that the first hash does not look  anything like the second hash despite us only changing 1 letter. In fact, with some code:

We find out that a and b are 0% similar (using the [Hamming Distance](https://www.wikiwand.com/en/Hamming_distance)). This is called the [Avalanche effect](https://www.wikiwand.com/en/Avalanche_effect). When the input changes slightly, the output changes significantly.

For the third point, this is the donut/dogs example above. Sometimes, it's okay to not avoid collisions because there are billions of different messages and a fixed length hash message. But, by not avoiding collisions other people can artificially make a message with the same hash as another file and this is an issue - because it's a fake message.

Let's walk through how SHA-1, an old hashing algorithm, works in detail. Although all hashing algorithms work differently and SHA-1 isn't used in the real world anymore, seeing how SHA-1 works in detail will enable us to generalise how hashing algorithms work.

---

## SHA-1

SHA-1 takes a bit string of length less than 264 bits and produces a 160-bit hash value known as the message digest. Note: I will be using hexadecimal numbering for brevity. Hashing algorithms never take a message of size X, and return a message of size X. They always 'compress' and create a digest of the message. Remember rule 1 for hashing algorithms from earlier? We want hashing algorithms to be fast. Producing large messages is not fast.

SHA-1 was published in 1993 by NIST, but was developed by the NSA (yes, that NSA). Not much is known about the history of SHA-1, so I apologise for not including history here.

Suppose we want to encode the message 'abc' using SHA-1. We start off by converting it into binary:

$$ abc = 01100001 01100010 01100011$$

SHA-1 starts with an internal state. Let's say our internal state of SHA-1 is:

$$ h_0, h_1, h_2, h_3, h_4$$

The internal state size is exactly the same as the length it produces  (160). So each internal state H has 160/5 = 32-bit words which is 4 bytes each. We split it into chunks because it's easier to calculate. We start by initializing these internal states with five random strings of hex characters:

$$H_0 = 67DE2A01$$

$$H_1 = BB03E28C$$

$$H_2 = 011EF1DC$$

$$H_3 = 9293E9E2$$

$$H_4 = CDEF23A9$$

The message is then padded by appending a 1, followed by enough 0s until the message is 448 bits. The length of the message represented by 64 bits is then added to the end, producing a message that is 512 bits long.
![](/content/images/2019/01/image-538.png)https://brilliant.org/wiki/secure-hashing-algorithms/
The padded input obtained above, $M$, is then divided into 512-bit chunks and each chunk is further divided into sixteen 32-bit words, $W_0, ..., W_15$. In the case of '*abc*' there is only one chunk, as the message is less than 512-bits total.

For each chunk, begin the 80 iterations, $i$, necessary for hashing (80 is the determined number for SHA-1), and execute the following steps on each chunk, $M_n$:

For iterations 16 through to 79, where $16 \le i \le 79$, perform the following operation:

$$W(i) = S^1(W(i-3) \oplus W(i-8) \oplus W(i-14) \oplus W(i-16))$$

The symbol $\oplus $ is [XOR ](https://www.wikiwand.com/en/Exclusive_or)which is exclusive or. The resultant is True (1) if and only if either the left hand side or right hand side is 1, but not both.
![](/content/images/2019/02/image-23.png)Truth table for XOR
As an example, when $i$ is 16, the words chosen are W(13), W(8), W(2), W(0) and the output is a new word, W(16), so performing the XOR operation on these words gives us:
![](/content/images/2019/01/image-539.png)
Now, the circular shift operation on the word by bits, being an integer between and, is defined by

$$S^n(X) = (X << n) OR (X>> 32 - n)$$

where $X << n$ is the **left-shift** operation, obtained by discarding the leftmost $n$ bits of  $X$ and padding the result with zeroes on the right. If you don't know what the logic symbols mean, I've written an article explaining them [here](/mathematical-logic/).

$X >> 32 - n$ is the **right-shift** operation obtained by discarding the $n$ rightmost bits of $x$ and padding the result with $n$ zeroes on the left. Thus $S^n(X)$ is equivalent to a circular shift of by positions, and in this case, the circular left-shift is used. 
![](/content/images/2019/01/image-540.png)
A left shift $S^n(W(i))$, where $W(i)$ is $10010$ would produce $01001$ as the rightmost bit, 0, is shifted to the left side of the string. Therefore $W(16)$ would end up being:

$$ W(16) = 11000010 11000100 11000111 00000000$$ 

Now store the hash values defined in step 1 in the following variables:

$$A = H_0$$

$$B = H_1$$

$$C = H_2$$

$$D = H_3$$

$$E = H_4$$

For 80 iterations, where $0 \le i \geq 79$ compute:

$$TEMP = S^5 * (A) + f(i; B, C, D) + E + W(i) + K(i)$$

We have to use a which takes in our data and a bit of the message and turns it into another set of h values.

A sequence of functions are used in SHA-1 depending on the value of $i$ and on three 32-bit words, B, C, and D, in order to produce a 32-bit output.

The following equations describe these logical functions.

$f(i; B, C, D) = (B \land C) \vee ((\not B) \land D)$ for $0 \geq i \geq 19$

$ f(i; B, C, D) = B \oplus C \oplus D$ for $20 \geq i \geq 39$

$ f(i; B, C, D) = (B \land C) \vee (B \land D) \vee (C \land D)$ for $40 \geq i \geq 59$

$f(i; B, C, D)  = B \oplus C \oplus D$ for $60 \geq i \geq 79$

A sequence of constant words $K(0), K(1), ... , K(79)$ is used in the SHA-1. In hex, these are given:

      $K(i) = 5A827999$ for $0 <= i <= 19)$

      $K(i) = 6ED9EBA1$ for $20 <= i <= 39$

      $K(i) = 8F1BBCDC$ for $40 <= i <= 59$

      $K(i) = CA62C1D6$ for $60 <= i <= 79$

Reassign the following values:

$$ E = D$$

$$D = C$$

$$ C = S^30 (B)$$

$$B = A$$

$$ A = TEMP$$

Store the result of the chunk's hash to the overall hash value of all chunks as shown below, and proceed to execute the next chunk:

$$H_0 = H_0 + A$$

$$H_1 = H_1 + B$$

$$H_2 = H_2 + C$$

$$H_3 = H_3 + D$$

$$H_4 = H_4 + E$$

As a final step, when all chunks have been processed, the message digest is represented as the 160-bit string comprised of the OR logical operator and the 5 hashed values:

$$H = S^128 (H_0) \vee S^96 (H_2) \vee S^32(H_3) \vee H_4$$

---

# Sha-1 sucks

SHA-1 was broken quite a few years ago. By broken, I mean that it's possible to artificially create collisions. That is, given a document with an SHA-1 hash of "cb4cc28df0fdbe0ecf9d9662e294b118092a5735" it is possible to produce a different document that has the **same **hash.

This article used SHA-1 because it's relatively easy to explain when compared to non-broken hash functions such as SHA-5. If you want to learn more about why you shouldn't use SHA-1, read this [article](https://www.schneier.com/blog/archives/2005/02/cryptanalysis_o.html).

As a side note, do not try to implement SHA-1 yourself. Remember [Scheiner's rule](https://www.schneier.com/blog/archives/2011/04/schneiers_law.html):

> "Anyone, from the most clueless amateur to the best cryptographer, can create an algorithm that he himself can't break."

While your implementation SHA-1 may appear to work to you, it may have some underlying issue that you didn't spot. It's always best to use implementations created and monitored by the community (open source).

---

## Breaking hashes

MD5 was a pretty popular hashing algorithm which produced 128-bit outputs. It is suspectible to a birthday attack. 

[Birthday attacks ](https://www.wikiwand.com/en/Birthday_attack)are formulated on the [birthday problem](https://www.wikiwand.com/en/Birthday_problem). If there are 23 people in a room, there is a 50% chance two of them will share the same birthday. If there are 70 people in a room, this is a 99.9% chance 2 people share the same birthday.

This comes from what is called the *[pigeonhole principle](https://www.wikiwand.com/en/Pigeonhole_principle)*. If you have 9 pigeonholes (boxes to put pigeons in) and 10 pigeons, 2 pigeons will have to share the same hole.
![](/content/images/2019/02/image-15.png)
In fact, MD5 is so weak to collision resistance that a simple, household  2.4GHz Pentium Processor can compute artificial hash collisions within  seconds. Moreover, its extensive usage in the earlier days of the  current web has created tons of leaked MD5 pre-images online that can be  found with a simple Google search of their hash.

---

## Conclusion

The 3 rules to hashing algorithms are:

1. A hashing algorithm needs to be reasonably fast to compute and reasonably fast to verify.
2. If you change one single bit anywhere in the message, the outputted string must look completely different.
3. You must avoid collisions.

As we saw with SHA-1, it uses a compressor function to take a message and turn that message into a much smaller, hashed version. SHA-1 isn't used in the real world anymore, and it's not secure in the sense that collisions can be created. Although it's a nice historical example of how hashing algorithms work.

For more on SHA-1, check out the official document describing it [here](https://www.ipa.go.jp/security/rfc/RFC3174EN.html). If you're interested in what hash functions are used now (especially in cryptocurrencies, as well as the attacks on them and the differences this [article ](https://medium.com/zkcapital/the-state-of-hashing-algorithms-the-why-the-how-and-the-future-b21d5c0440de)is very good.

Hey 👋 Want to subscribe to my blog and stay up to date with posts similar to this one? Subscribe to my email list below. I won't spam you. I will only send you posts similar to this one 😊✨

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
    

## At least this isn't a full screen pop up! 😅

        Sign up now and get:
       
- A free 202 page book on algorithmic design paradigms
- A free 107 page book on employability skills
- And much more to help you become an awesome developer!

Email

GDPR: I consent to receive promotional emails about your products and services.
HP

One click unsubscribe anytime.

If you're feeling extra generous, I have a [PayPal ](https://www.paypal.me/BrandonSkerritt) and even a [Patreon](https://www.patreon.com/user?u=15993188). I'm  a university student who writes these blogs in their spare time. This blog is my full time job, so any and all donations are appreciated!
