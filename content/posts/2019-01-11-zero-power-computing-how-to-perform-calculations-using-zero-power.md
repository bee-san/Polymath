---
title: Zero Power Computing — How to Perform Calculations Using Zero Power
slug: zero-power-computing-how-to-perform-calculations-using-zero-power
date_published: 2019-01-11T09:00:00.000Z
date: 2019-04-08T00:28:02.000Z
tags: 
  - Computer Science
---

Moore’s law is dying. There have been [countless ](https://www.extremetech.com/computing/256558-nvidias-ceo-declares-moores-law-dead)[articles ](https://www.technologyreview.com/s/601441/moores-law-is-dead-now-what/)on [this](https://www.electronicsweekly.com/news/moores-law-still-law-2017-09/). We cannot keep on packing transistors into a given unit of space, expecting each time that the power of the CPU doubles every year.

The smaller and smaller the chips are made, the more problems that are produced. To think this rule would last forever is naïve, we’re running out of space and it’s going to cause problems. Luckily there’s a storm brewing. It is theoretically possible to perform computations with **zero power**. This article will explain how that is possible.

---

In the 1950s Computer Scientists wanted to know if it is possible to build an accurate simulation of classical physics. Not a “close to” simulation, but 100% accurate.

Whilst working this problem, they discovered something interesting:

**Newton’s Laws of Physics are reversible**

Let’s say you see a ball from a basketballers hand in an alternate world. In this world, friction doesn’t exist. For the next few examples, remember that** in this world friction doesn’t exist. **The ball is dropped, bouncing off the ground to the same starting height it started at.Gif by [Michelle Sherrina](https://twitter.com/Sherchle) on [Giphy](https://giphy.com/gifs/basketball-dribble-dribbling-3o6ZtpY1ws3DohMK1W). Gif depicting a headless basketball player bouncing a basketball.

Let’s put some arbitrary numbers on this now. Let’s say that the ball gains 6 units of energy to reach the floor.

When the ball touches the floor, it goes back up again — using 6 units of energy.

In this world of pure Newtonian physics, the laws are reversible.

If we made a movie out of the ball falling; the ball would look the same going forwards in time as it would going backwards in time.

Let’s see another example from this same world — taken from the book “Computing with Quantum Cats”.

Let’s assume you have 2 balls of the same colour on a snooker table. One of the balls hits the other and you filmed this interaction. If you reversed the film it would make as much sense as it did going forward. If you presented this film to someone and asked them “Which ball hit the other ball?” they would not know the answer.

---

Take a look at the ball below. We do not hold any information about how the ball got there, only that it is there. We don’t know whether it was placed, kicked, dropped or even teleported there.
![](https://cdn-images-1.medium.com/max/600/1*r-M4KIgAsF-v3jFIFzgXdA.jpeg)Photo by [Ben Hershey](https://unsplash.com/photos/VEW78A1YZ6I?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText) on [Unsplash](https://unsplash.com/search/photos/ball?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText). Image depicting a motionless tennis ball on the floor.
We don’t know whether the ball was dropped from 40ft or 50ft, we hold no information about this ball.

From the last few examples we can see that there is an interesting link between information and energy.

Although each individual action is reversible, if we add more balls it’s not reversible. Let’s say we take the snooker example from earlier, but this time we watch a break at the start of the game:Image from [Giphy](https://giphy.com/). Image depicting a break in pool.

We can always tell which one is the future and which one is the past. The future is the one with more *disorder*.

As the [second law of thermodynamics](https://www.wikiwand.com/en/Second_law_of_thermodynamics) states:

> The amount of disorder in a system always increases and the result is not reversible.

The term disorder is often called *entropy. *These rules of thermodynamics and entropy is useful to us since entropy is measured in *information.*

What’s important to note here is that the relationship between thermodynamics, reversibility, and information are all based on the act of computation itself. Not the power required to run the computer or the power required to run the monitors.

Rolf Landauer found out in 1961 whilst a researcher at IBM that some computation does not need to dissipate energy. He found out that computation and the physical reality are united. In his own words:
![](https://cdn-images-1.medium.com/max/600/1*Ckfz1x26OvLWH1aVLiZt_A.jpeg)Photo of Rolf Landauer from [here](http://ethw.org/Rolf_Landauer)
*“Information is not a disembodied abstract entity; it is always tied to a physical representation. It is represented by engraving on a stone tablet, a spin, a charge, a hole in a punched card, a mark on paper, or some other equivalent. This ties the handling of information to all the possibilities and restrictions of our real physical word.” — *Rolf Landauer

We have a connection between reversibility and thermodynamics. We have a connection between thermodynamics and information. Therefore we have a connection between reversibility and information.

The author [John Gribbin](https://www.wikiwand.com/en/John_Gribbin) describes a fun thought experiment to better get an overall view of this thinking.
![](https://cdn-images-1.medium.com/max/800/1*SM_za4xcpq2v-ktDFasNlQ.png)Figure 1 — Image depicting a ball on a box with the number “0” under it. There is another box with the number “1” on it over a hill.
The 0 and 1 here represent binary bits. The hill represents the physical aspect to toggling the binary bit. When the ball goes over the hill and down the other side, it’ll toggle the binary bit to be 1.

When it does the reverse, it’ll toggle the binary bit to be 0.

The ball traversing the hill would look like this:
![](https://cdn-images-1.medium.com/max/800/1*qeILnsLCkz2GhZG_iz6X9A.png)Figure 2- image depicting a ball going up one side of the hill using +6 energy and going down the other side of the hill using -6 energy. The ball eventually toggles the switch to 1.
The ball gains an arbitrary amount of energy as it is pushed up the hill and it releases this energy going down the hill.

It has, effectively, cost 0 energy to toggle the binary bit. This is an important statement. John Von Neumann once said “it costs energy to toggle a switch” but our little experiment has displayed that it it possible to not expend energy.

Although it cost nothing to toggle the switch (moving the ball from one side to the other) it will cost something to check where the ball is. It will cost something to check what position the switch is in.

The act of the computation itself can cost nothing, but everything else might cost something.

Computers are entirely made up of toggles like this. If it costs nothing to toggle a simple switch like this, we can have entire circuit boards built up of gates that cost nothing.

---

#### Gates

Let’s take a look at some logic gates.

A logic gate is a decision making tool. You give it some input and it gives out an output. One of the simpler logic gates is the AND gate.
![](https://cdn-images-1.medium.com/max/800/0*nD0uUIs3RzlTc9MB.jpg)And gate taken from my post on logic gates, [here](https://medium.com/brandons-computer-science-notes/mathematical-logic-f53f9c60d8d9)
Logic gates can only take 0 or 1 as input. The AND gate outputs the product of A and B. Or in other words, it only outputs 1 when A **and **B are 1.
![](https://cdn-images-1.medium.com/max/800/1*qzJioXkK8ir2AOlWSQpFIg.png)Truth table taken from my article [here](https://medium.com/brandons-computer-science-notes/mathematical-logic-f53f9c60d8d9)
In all other instances when A and B are not both 1 the AND gate will output 0.

If we come across an AND gate and the output is 1 — we know for sure that the 2 inputs were 1 and 1.

If we come across an AND gate and the output is 0, we don’t know what the input was. It could of been A = 0, B = 1 or A = 1, B = 0 or A = 0, B = 0.

We cannot *reverse *the AND gate to find out what the input is when the output is 0.

A reversible computer has to be built out of logic gates that can be reversed. The AND gate is not a reversible logic gate so it is not useful here. To build a computer which can replicate classical physics the components of the computer have to be reversible too.

---

#### Reversible Programs

Charles Bennet in 1973, whilst working at IBM, created a few simple reversible computer programs. The first half would do the computations and the second half would undo the computations. In his words:
![](https://cdn-images-1.medium.com/max/600/0*MmbMpqgIF34EuSdd.jpg)Photo of Charles H. Bennet. Image from [here](about:invalid#zSoyz)
*“The first half would generate the desired answer … as well as typically, some other information … the second half would dispose of the extranous information by reversing the process that generated it but would keep the desired answer.*

*This led me to believe that any computation could be rendered into this reversable format by accumulating a history of all information that would normally be thrown away, then disposing of this history by the reverse of the process that generated it. To prevent the reverse stage from destroying the desired output along with the undesired history, it suffices, before begginging the reverse stage, to copy the output on blank tape. Copying onto blank tape is already logically reversible.” — *Charles Bennet

Simply put the proces is as follows:

- Compute the answer
- Write the answer down somewhere
- reverse all computations to get back to the original state

---

#### Fredkin Gates

The Fredkin gate is a *universal *gate. Meaning that any logical or arthimetic instruction can be created using a Fredkin gate. Any logic circuit can be created using just Fredkin gates. This means that any computer can be made entirely out of Fredkin gates.

If you are not so sure on logic and gates, check out this previous article I’ve written [here](https://medium.com/brandons-computer-science-notes/mathematical-logic-f53f9c60d8d9).
![](https://cdn-images-1.medium.com/max/800/0*kpZYPpWmSUsQh3tE.png)Image of a Fredkin gate from [here](https://www.wikiwand.com/en/Fredkin_gate)
[Wikipedia ](https://www.wikiwand.com/en/Fredkin_gate)has a nice explanation for how Fredkin gates work, copied here with slight changes.

The Fredkin gate maps three inputs (A, B, C) onto three outputs (P, Q, R). The C input is mapped directly to the R output. If C = 0, no swap is performed; A maps to P and B maps to Q.

Otherwise (if C = 1) the outputs are swapped. A maps to Q and B maps to P. C is **always **mapped to R.

If this is run backwards, it undoes itself. If the output of this Fredkin gate is fed to the input of another Fredkin gate (P to A, Q to B, R to c) the output of the second Fredkin gate is the same as the input of the first Fredkin gate.

---

#### Conclusion

If we build a perfect Fredkin gate we will get zero power computation. Computing would no longer cost energy. This can change everything. Blockchain uses up enough energy to [power a country](https://www.technologyreview.com/s/609480/bitcoin-uses-massive-amounts-of-energybut-theres-a-plan-to-fix-it/). Imagine a blockchain that consumed next to 0 energy, the only limitations for it would be the memory problems.

The battery life of a mobile phone would be 10x that of a phone today. The phone no longer has to waste power in computing things, the only power it wastes is keeping the screen on. But, there are always downsides to the upsides.

The problem with building a reversible computer is that it’s hard. It requires us to completely shift our mindset away from everything we know. Computer Scientists have always built computers to consume electricity. Which have always been built using traditional logic gates. This is a quantum shift in not only our thinking but, fundamentally, how every single device on the planet should behave.

It’s also a slow process. Although Fredkin gates can reverse and give us back the computational energy they can never give back time. What might take something 4 seconds on a CPU to compute would take 8 seconds on a Fredkin gate to compute. This is due to the fact that once you have computed it, you have to undo all the calculations — effectively 2 times the process.

It’s also impossible as of yet. Throughout this article we have assumed that we live in a frictionless world, which isn’t very reasonable. It’s theoretically possible, but not much work has been done here.

In the 1990s a research team [discovered](https://cs.stackexchange.com/a/38053) that the energy savings from a Fredkin gate are linearly proportional to how *slowly* you run them.

In 2016 it was [announced](http://advances.sciencemag.org/content/2/3/e1501531) that researchers had created a quantum Fredkin gate which could be used to build a quantum computer. This is a quantum gate, so cannot be used in ordinary analogue computing. It’s one step closer to building computers which can perform zero power computations, but it’s still a long way off.

---

Hey 👋 Want to subscribe to my blog and stay up to date with posts similar to this one? Subscribe to my email list below. I won't spam you. I will only send you posts similar to this one 😊✨

	#mc_embed_signup{background:#fff; clear:left; font:14px Helvetica,Arial,sans-serif; }
	/* Add your own Mailchimp form style overrides in your site stylesheet or in this style block.
	   We recommend moving this block and the preceding CSS link to the HEAD of your HTML file. */

	#mc-embedded-subscribe-form input[type=checkbox]{display: inline; width: auto;margin-right: 10px;}
	#mergeRow-gdpr {margin-top: 20px;}
	#mergeRow-gdpr fieldset label {font-weight: normal;}
	#mc-embedded-subscribe-form .mc_fieldset{border:none;min-height: 0px;padding-bottom:0px;}

Like this article? Subscribe to my mailing list to get more like this✨ 

Please tick this box to let me know you want to be contacted via email.
Email

If you're feeling extra generous, I have a [PayPal ](https://www.paypal.me/BrandonSkerritt) and even a [Patreon](https://www.patreon.com/user?u=15993188). I'm  a university student who writes these blogs in their spare time. This blog is my full time job, so any and all donations are appreciated!
