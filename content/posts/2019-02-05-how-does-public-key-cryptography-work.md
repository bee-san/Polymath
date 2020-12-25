---
title: Public Key Cryptography Simply Explained
slug: how-does-public-key-cryptography-work
date_published: 2019-02-05T10:31:00.000Z
date: 2019-11-19T01:47:08.000Z
tags: 
    - University
    - Computer Science
    - Datastructures and Algorithms
    - Infosec
excerpt: Public key cryptography seems magical to everyone, even those who understand it. In this post, I'm going to explain public key cryptography. Public Key Cryptography is based on asymmetric cryptography, so first let us talk about symmetric cryptography.
math: true
---

Public key cryptography seems magical to everyone, even those who understand it. In this post, I'm going to explain public key cryptography. Public Key Cryptography is based on asymmetric cryptography, so first let us talk about symmetric cryptography.

---

## Symmetric Cryptography

Your front door is usually locked by a key. This key unlocks & locks your front door. With symmetric cryptography, you have one key which you use to unlock and lock things.

Only people with the key or a copy of the key can unlock the door. Now, imagine you're on holiday in Bali. You want to invite your friend around to look after your cat 😺 while you're on the beautiful beaches 🏖️.

Before the holiday, you give your friend the key to your door. Your friend is then robbed, so someone else has your front door key now. Or your friend leaves it laying around and someone clones it. The problem with symmetric key cryptography is that this one key is easy to clone, it's easy to attack your house in many different ways.

Let's take this from an analogy to a real-life example of symmetric cryptography.

### Caeser's Cipher

Julius Caeser used a cipher to send messages that no one else could read other than the intended recipient. Mainly because no one could read back in 100 BC, and those that could wouldn't understand a random string of letters. That's the whole point of cryptography. To create ways to communicate without third parties listening in. This cipher is *Caeser's Cipher*. Given an alphabet and a key (the key is an integer between 1 and 25), shift all of the alphabet letters by key. 

<figure>
    <img src="/media/rsa/1.png">
    <figcaption><a href="https://www.geeksforgeeks.org/caesar-cipher/">Caeser's Cipher shift of 3</a><figcaption>
</figure>

With a shift of 3, as seen in the image above, A becomes D, B becomes E and so on until it wraps around with X = A. The original message is called the *plaintext *and the encrypted message is called the *ciphertext*.

The easiest way to perform Caesar's Cipher is to turn all of the letters into numbers, a = 1, b = 2, c = 3 and so on.

To encrypt, E, you calculate this for every letter (where s is the shift):

$$ E_{s}(letter) = (letter + shift)   mod \;  26$$

This is called a *function. *You put an input into it, and an output comes out. A lot of functions are known as two-way functions. You can encrypt by using the function above, and it makes sense that to decrypt you just do the opposite. Given a function that doubles a number, if you have a doubled number and you want to reverse the function do the opposite of multiplying by 2, divide the number by 2.

*mod *is the modulus operator. It's the remainder of dividing. We do modulous because there isn't a 27th letter in the alphabet, you just wrap around from "z" back to "a". We'll talk more about modular arithmeticlater on in this article. Look at this small example below:

$$ 4  \; mod \; 3 = 1 $$

Because 4 divided by 3 has a remainder of 1.

To decrypt Caesar's cipher, D, you calculate this for every letter:

$$ D_{s}(letter) = (letter - shift) \; mod \; 26$$  

As you can tell, it's not very secure. With 25 total shifts you just have to shift the text 25 times until you find the decrypted code, this is called a brute force attack. You take the encrypted text and shift it all 25 times until you find the decrypted text. But let's imagine for a second that this was a hard cipher - that brute force isn't feasible.

How do you tell your friend you're using a shift of 9, for example? You have to communicate it to them somehow. Any and all forms of communication can be listened in on - whether that's writing a letter or going to a hidden forest in Switzerland 30 miles from the nearest town and telling your friend.

The latter isn't very feasible, but it is a lot more secure than telling your friend in Times Square, New York 🗽 what the shift is.

Now, imagine you brought your lunch to work in a special lunchbox - the same you've had since nursery school. Someone steals your food and your lunchbox. You don't mind losing the food, but you do want the lunchbox back. You want a way for them to securely return your lunchbox without you knowing who took it - because that takes the pressure off of them.

You place a box in the staff room with a lock & key. You give copies of keys to everyone in the office and hope for the best - that someone will return the lunchbox by placing it in the box.

<figure>
    <img src="/media/rsa/2.png">
    <figcaption><a href="https://www.amazon.co.uk/Metal-File-Box-Storage-Suspension/dp/B06Y3CD5G5/ref=sr_1_16?ie=UTF8&amp;qid=1549211348&amp;sr=8-16&amp;keywords=lock+box">Image of a lock box from</a><figcaption>
</figure>

Unfortunately, the keys everyone has also unlocks the box as well as locks it. This means that someone could unlock the box and re-steal your lunchbox.

We need to find a way to get rid of this idea of sharing keys, get rid of the idea of 'any key can lock and unlock', and this is where asymmetric cryptography comes in.

---

## Asymmetric cryptography
<figure>
    <img src="/media/rsa/3.png">caption>
</figure>

You install an extraordinary lock on this box, one that has two separate keys. The first key 🔑 can only turn clockwise, from **A** (locked) to **B** (unlocked) to **C** (locked).

The second key 🗝️ can only turn anti-clockwise, from **C** to **B** to **A**. You pick the first key and keep it to yourself. This is called a private key. The second key is called the public key. This key is given out to everyone in the office. You want everyone to have this key.

When someone returns your prized lunchbox, they can leave it in this box. All the public keys can do is lock the box. Your private key is the only one that can open it.

This is public key cryptography. Everyone knows that if they put something in the box and lock it, only you can open it with your private key.

With symmetric cryptography, everyone could open your box if they had the key. Now, no one apart from you can open the box.

Public key cryptography was first formulated by [Whitfield-Diffie](https://www.wikiwand.com/en/Diffie%E2%80%93Hellman_key_exchange) or [James Ellis](https://www.wikiwand.com/en/James_H._Ellis) (Ellis discovered first, but he didn't publish it. Whitfield-Diffie published first). Both Ellis and Whitfield-Diffie enjoyed that public key cryptography could work in theory, but never managed to figure out how it would work in practice.

The production of a working Public Key Encryption system is attributed to [Rivest–Shamir–Adleman](https://www.wikiwand.com/en/RSA_(cryptosystem)) (RSA) or [Clifford Cocks](https://www.wikiwand.com/en/Clifford_Cocks). Like above, Cocks discovered first, but he didn't publish it. Rivest–Shamir–Adleman published first. 

Let's look at how this works mathematically.

---

### The maths behind public key cryptography

While the box analogy was something physical, we're going to go back to encrypting messages much like we did with Caeser Cipher.

$$ K^-_b(K^+_b(m)) = m$$

When you apply the public key ($K^+$) to the encrypted message, and then the private key ($K^-$) to the encrypted message you get the plaintext message. We are also looking for these attributes:

It is computationally easy to:

- Generate a set of keys
- Encrypt / Decrypt using these keys

But it is also computationally infeasible to:

- Determine the private key from the public key
- Bruteforce the private key from the public key and bruteforce the ciphertext

---

### Turning messages into numbers

We want to turn a message into numbers. Previously we assigned a number to each letter, A = 1 and so on. The *American Standard Code for Information Interchange* (ASCII) is a table of all English letters and most symbols along with their associated ASCII code & Binary output.

When you press a key on the keyboard, the keyboard converts this to Ascii as numbers are easier to work with than letters for a computer. If you want to learn more about ASCII, check out this [video](https://www.youtube.com/watch?v=MijmeoH9LT4).

<figure>
    <img src="/media/rsa/4.png">
    <figcaption><figcaption>
</figure>

Let's encrypt the word "cats". In binary, according to Ascii, this is:

$$c = 01100011$$

$$a = 01100001$$

$$t=01110100$$ 

$$s = 01110011$$

If you add them all together and convert to base 10, you get 4430123. For our example, we're going to look at how Rivest–Shamir–Adleman (RSA), a public key cipher, calculates public & private keys. We're also going to use much smaller numbers, so the maths isn't as hard to read.

Below is a calculator I created for turning ASCII into Binary.

```python
# https://stackoverflow.com/a/40949538
def string2bits(s=''):
    return [bin(ord(x))[2:].zfill(8) for x in s]

# edit the text below to see how this works
text = 'cats'
bits = string2bits(text)

for x in bits:
    print(x)
```
    

---

### RSA

1. Choose 2 large prime numbers, p & q.

Prime numbers are numbers that only have 2 [factors](https://www.bbc.com/bitesize/topics/zfq7hyc), 1 and itself. We're going to pick 5 & 7, not large prime numbers but small for brevity.

2. Compute n = pq, z = (p-1)(q-1)

$$n = 5 * 7 = 35$$

$$z = (5 - 1)(7-1) = 4 * 6 = 24$$

3. Choose e (with e < z) such that e has no common factors with z.

$$ e = 5$$

5 has no common factors with 24, and it is smaller than 24.

4. Choose d such that $ed - 1$ is exactly divisible by z.

The easiest way to do this would be to loop over all possible values of d in code. This code is written in [Functional Python](/learn-functional-python-in-10-minutes/), but the language and paradigm doesn't matter.

Since we're using such small numbers, we have overlap. Both e and d are 5. Let's set d to 29, just so we don't have this overlap. 

$$ d = 29 $$

5. The public key is (n, e). The private key is (n, d)

$$key_{public} = (35, 5)$$

$$key_{private} = (35, 29)$$

Below is code to generate RSA keys. Note that we have overlap on d with p = 5 and q = 7, as discussed above.

```python
def rsa(p, q):
    n = p * q
    z = (p - 1) * (q - 1)
    
    # calculate e such that e is less than z
    # and e has no common factors with z
    for i in range(1, z - 1):
    if z % i != 0:
        e = i
        break
        
    d = (filter(lambda x: ((x * 5) - 1) % 24 == 0, range(1, 200)))[0]
    return{"Public key": [n, d], "Private Key": [n, e]}

# change p and q here to any prime numbers of your choice
p = 5
q = 7

print(rsa(p, q))
```
    

To send an encrypted message, Bob computes $C = m^e \; mod \; n$ for message m and key e. To decrypt the message, Alice computes $m = c^d \; mod \; n$.

Encrypting "cats" gives us  $427^5 \; mod \; 35 = 7$.

Decrypting "cats" gives us 4430123.

Then to send a message m, Bob computes $c=m^e \; (mod \; N)$ and sends it to Alice and Alice decrypts the message using her private key d with $m=c^d \; (mod \; N)$

## Why does it work?

Prime factorisation. It's easy to multiply two prime numbers together, but it's incredibly hard to find out what prime numbers were used to make that number. You can easily multiply these two together:

$$ 23,719 * 41,843 = 992,474,117$$

But if I gave you 992,474,117 and told you to find the prime numbers that were used to make this number, it's not computationally feasible. Even more so when you realise the prime numbers used are very, very large.

This is known as a trap-door function or a one-way function. While it is easy to go through one way, it is computionally infeasiable to go the other way. Boiling an egg is a one-way function because it is easy to boil an egg, but it is not possible to un-boil an egg. Let's go deeper into the mathematics and explore modular arithmetic.

### Back to modular arithmetic

Imagine a finite range of numbers, for example, 1 to 12. These numbers are arranged in a circle, much like a clock (modular arithmetic is sometimes called clock arithmetic because of this)

<figure>
    <img src="/media/rsa/5.png">
    <figcaption><figcaption>
</figure>

Count 13 around this clock. You get to 12 and then you need to count 1 more - so you go back to 1. Modular arithmetic is still defined as the remainder of division, however it can also be defined (and is more commonly defined) as a clock.

Functions using modular arithmetic tend to perform erratically, which in turn sometimes makes them one-way functions. Let's see this with an example by taking a regular function and seeing how it works when it becomes a modular arithmetic function.

$$3^x$$

When we insert 2 into this function, we get $3^2 = 6$. Insert 3 and we get $3^3 = 9$

This function is easy to reverse. If we're given 9, we can tell that the function had an input of 3, because of $3^3 = 9$.

However, with modular arithmetic added, it doesn't behave sensibly.

Image we had this formula:

$$ 3^x mod \; 7 = 1$$

How would you find out what x is? You can't put the mod on the other side, because there isn't really an inverse of modular arithmetic. What about guessing? Let's input 5:

$$ 3^5 mod \; 7 = 5$$

Okay, that was too big. You might want to go lower, maybe 4 or 3 but actually this is the wrong direction. When x is 6, it is equal to 1.

In normal arithmetic, we can test numbers and get a feel for whether we are getting warmer or colder, but this isn't the case with modular arithmetic.

Often the easiest way to reverse modular arithmetic is to compile a table for all values of x until the right answer is found. Although this may work for smaller numbers, it is computationally infeasible to do for much larger numbers. This is often why modular arithmetic is known as a one-way function.

If I gave you a number such as 5787 and told you to find the function for it, it would be infeasible. In fact, if I gave you the ability to input any number into the function it would still be hard. It took me a mere few seconds to make this function, but it'll take you hours or maybe even days to work out what x is.

RSA is a one-way function. While it is relatively easy to carry out this function, it is computationally infeasible to do the reverse of the function and find out what the keys are. Although, it is possible to reverse an RSA encryption if you know some numbers such as N.

## Let's talk about N

Recall earlier where I detailed how the RSA algorithm worked. There was one number, $n$. This n is special because under some circumstances n can make this one-way function reversible

N is a product of 2 prime numbers. As we saw earlier, if we take $5$ and $7$ and multiply them together, we get:

$$n = 35$$

In order for Bob to send Alice a message, he encrypts the message using Alice's public key. Now that the message is encrypted, there has to be some way for Alice to decrypt it. There has to be some way for Alice to reverse this, but only for Alice to reverse it. You can't have Eve or Niamh or Hannah reversing it - because that beats the point of encrypting it.

RSA is designed so the person who knows P and Q (the two prime numbers that are multiplied together to give N) can decrypt the message.

Although Alice has told the world her public key is $n = 35$, no one apart from Alice knows that $P = 7, Q = 5$. Note that the prime numbers are intentionally small for brevity.

You may be thinking "it's easy to guess that 35's prime factors are 5 and 7" and you would be right. But, with large enough numbers it is virtually impossible to find $p$ and $q$.

In fact, with large enough numbers multiplying p and q are essentially one way functions. It is possible that in the future, perhaps the near future (with the invention of quantum computers) that factoring numbers becomes easy. Mathematicians have tried and failed for thousands of years to find an efficient way to factor numbers, so for now it is considered secure.

## Let's look more into the maths

Okay, let's look at how modulus works in all of this. You understand why multiplication works, and how modulus works. But what about the other equations? What are they for?

Let's demonstrate the deciphering algorithm using an identity due to Euler and Fermate:

> For any integer (M), M is relatively prime to n:

$$M^{\phi(n)} \equiv 1 (mod n)$$

Here, $\phi (n)$ is the Euler totient function giving the number of positive integers less than n which are relatively prime to n. Relatively prime is where 2 numbers only share the factor $1$ with each other. In modern day we use [Carmichael's function](https://www.wikiwand.com/en/Carmichael_function) over Euler's function, as Euler's function can sometimes produce numbers too large to use. However, we're using Euler's totient function as it is what the original RSA paper used.

This sounds confusing, but let's break it down. By elementary properties of the totient function:

$$\phi (n) = \phi (p) * \phi (q)$$

$$ = (p - 1) * (q - 1)$$

$$ = n - (p + q) + 1$$

Since d is relatively prime to $\phi i (n)$, it has a multiplicative inverse $e$ in the ring of integers modulo $\phi (n)$. What this means is that the formula we used for RSA can be reversed (the trap door can be reversed) given some knowledge about the numbers used.

Without this special mathematical property it wouldn't be possible to reverse the encryption and find out the ciphertext if you know some of the numbers used. 

The [modular multiplicative inverse](https://www.wikiwand.com/en/Modular_multiplicative_inverse) of the encryption algorithm $c = m^e \; mod \; n$ is $m = c^d \; mod \; n$. All of this maths has built up to this. Modular arithmetic and one-way functions are heavily involved here. In order to encrypt, you calculate c. In order to decrypt, you calculate m. Both of these require knowledge of $n$, which is the special number we talked about earlier.

If you want to learn more about the maths of RSA, I highly recommend the readable, [original RSA paper](https://people.csail.mit.edu/rivest/Rsapaper.pdf).

---

## Authentication

How do you prove that a message sent by Bob was actually sent by Bob, and not sent by Eve? You need a way to authenticate them. In the real world, we authenticate using signatures. Although these can be forged, you can authenticate using a biometric scanner, but your fingerprints can be lifted and copied.

You can use a passcode, but again much like how Caeser's cipher and its single key is useless, authentication methods that use single keys aren't as perfect.

$$ K^-_b(K^+_b(m)) = m = K^+_b(K^-_b(m)) $$

Let's say Bob wants to prove to Alice that Bob wrote the message he sent her. Bob sends his original message with an encrypted version of the message with his private key ($k^-$). Alice uses Bob's public key($k^+$) which, using the formula above, turns the encrypted message back into the normal message. Then Alice checks the message Bob sent with the message she got from the encrypted message. If they match, she can be sure that someone with Bob's private key (probably Bob) sent it.

This method sucks for encrypting because if Bob encrypts his message with his private key, anyone can read it with his private key. Also, it's computationally expensive to prove that Bob sent something. This is why we create a digest of the message and encrypt that instead to verify Bob. This digest of a message is done using a *hash function.*

To learn more about hash functions, I wrote a sister article which explains them [here](/hash-functions/).

### Back to cryptography

By encrypting the hash of the message we speed up the process of encrypting it, which makes authentication a lot faster. Now, let's play a prank on Bob.

We create an e-mail order to a pizza shop asking for 4 pepperoni pizzas. We sign this email with our private key. We send the pizza store our public key, but we tell them that Bob's phone is dead and that our public key is actually Bob's public key.

The pizza store verifies the signature and sends 4 pepperoni pizzas 🍕 to Bob. The worst part is, Bob doesn't even like pepperoni. This is where a *certification authority *comes into play.

### Certificate Authorities

Certificate authorities (CA) bind a public key to a specific entity. This entity provides proof of identity to the CA, the CA then creates a certificate binding the entity to its public key. The idea is to take the trust out of trusting an individual for public keys. You still have to trust an organisation, but many people find trusting an organisation is better than trusting an individual.

The certificate containing the entities public key is digitally signed by the CA. This signing is the CA saying "this is the entities public key".

<figure>
    <img src="/media/rsa/7.png">
    <figcaption><figcaption>
</figure>

When Alice want's Bob's public key, she gets Bob's certificate. She then applies the CA's public key to Bob's certificate to get Bob's public key.

<figure>
    <img src="/media/rsa/7.png">
    <figcaption><figcaption>
</figure>

Cloudflare has an amazing article on certificate authorities [here](https://blog.cloudflare.com/how-to-build-your-own-public-key-infrastructure/).

---

## Secure Email with Pretty Good Privacy

[Phil Zimmerman](https://www.wikiwand.com/en/Phil_Zimmerman) invented [Pretty Good Privacy](https://www.wikiwand.com/en/Pretty_Good_Privacy) (PGP), the de facto standard for email encryption. Zimmerman used RSA in PGP. RSA is patented and he did not have permission from RSA inc (the company that holds the patent) to publish another cipher using RSA.

Zimmerman was also a target of a 3-year U.S federal investigation because at the time cryptography programs were considered munitions under U.S law. When asked whether all of the trouble was worth it to publish PGP, he [said ](https://philzimmermann.com/EN/essays/index.html)he had "no regrets". Let's look at how this used to be illegal algorithm works.

When Alice wants to send a confidental email to Bob, she:

1. Generates random symmetric private key, $k_s$.
2. Encrypts her email with $k_s$ (for effiency)
3. Also encrypts $k_s$ with Bob's public key.
4. Alice digitally signs the encrypted message.
5. Alice sends Bob both $k_s(m)$ , $k^+_b(k_s))$ and her digital signature.

In total, Alice uses three keys. Her private key, Bob's public key, and the newly created symmetric key.

<figure>
    <img src="/media/rsa/8.png">
    <figcaption>Pretty Good Privacy (PGP). <figcaption>
</figure>

This idea of encrypting a symmetric key with a public key is called a [Hybrid Cryptosystem](https://www.wikiwand.com/en/Hybrid_cryptosystem). Some email messages can be incredibly large, encrypting these with a public key system would take a very long time. 

Use a symmetric key system such as [AES](https://www.wikiwand.com/en/Advanced_Encryption_Standard), which is incredibly hard to break (but not as hard as RSA). Encrypt the AES key (and only the key, not the whole email) with the public key. This way, the receiver can apply their private key and find out the AES symmetric key to decrypt the email.

Not many people use PGP, because of how difficult it is to set up. At most, you need to download a program you trust to correctly implement PGP. In 2018 it was [shown](https://www.wired.co.uk/article/efail-pgp-vulnerability-outlook-thunderbird-smime) that email clients such as Apple Mail, Thunderbird, and Outlook - who have settings to enable PGP can be forced to show the non-encrypted versions.

Not to mention how suspicious it looks for one person to send encrypted emails on a network of non-encrypted emails. The only email client (and address provider) which enables PGP by default is ProtonMail, but even then it's only for Proton-to-Proton emails and you have to trust the company to implement it correctly.

{{< tweet 955192767952629760 >}}

---

### Conclusion

Cryptography has been used for thousands of years, almost as long as mankind has held secrets. In our constant effort to keep our secrets secret to everyone apart from a select few we've found this magical algorithm that works pretty well. No doubt, in 300 or 400 years it will have been broken much like how Caeser thought his cipher would never be broken.

If you're feeling extra generous, I have a [PayPal ](https://www.paypal.me/BrandonSkerritt) and even a [Patreon](https://www.patreon.com/user?u=15993188). I'm a university student who writes these articles in my spare time. This blog is my full time job, so any and all donations are appreciated
