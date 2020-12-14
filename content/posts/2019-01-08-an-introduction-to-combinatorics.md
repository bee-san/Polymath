---
title: An Introduction to Combinatorics
slug: an-introduction-to-combinatorics
date_published: 2019-01-08T00:37:44.000Z
date: 2019-01-26T15:16:12.000Z
tags: 
  - "University"
  - "Computer Science"
---

Please consider the following problems:

- How many possible sudoku puzzles are there?
- Do 37 Londoners exist with the same number of hairs on their head?
- In a lottery where 6 balls are selected from 49, how often do two winning balls have consecutive numbers?
- In how many ways can we give change for £1 using only 10p, 20p, and 50p pieces?
- How many ways are there of rearranging the letters in the word “ABRACADABRA”?

What do you notice about these problems?

First of all, unlike many mathematical problems that involve much abstract and technical language, they’re all easy to understand — even though some of them turn out to be frustratingly difficult to solve. This is one of the main delights of the subject.

Secondly, although these problems may appear diverse and unrelated, they mainly involve selecting, arranging, and counting objects of various types. In particular, many of them have the forms. Does such-and-such exist? If so, how can we construct it, and how many of them are there? And which one is the ‘best’?

The subject of combinatorial analysis or combinatorics (pronounced com-bin-a-tor-ics) is concerned with such questions. We may loosely describe it as the branch of mathematics concerned with selecting, arranging, constructing, classifying, and counting or listing things.

This is really important, so make sure to memorise it: Permutations are **ordered** combinations. We don’t care about the order of combinations. If you have a locker number, 4457, you care about the order because 5474 wouldn’t work.

### Product Rule

If there is a sequence of K events with n1 … nk possible outcomes, then the total number of outcomes for the sequence of K events is n1 x n2 x … nk

It will be best to show this through an example.

### Example 1

In Kent, license plates are made up of two letters followed by 3 digits. How many possible license plates are there?

Well, the first letter has 26 possible letters and so does the second letter. The first digit has 10 possible choices for the first digit, 10 for the second and 10 for the third.

Therefore there is a total combination of: 26² * 10³ = 676,000

### Disjoint Events

Two events are said to be disjoint if they cannot happen at the same time.

### The Sum Rule

If A and B are disjoint events and there are N possible outcomes for A and X possible outcomes for B then there are N + X possible outcomes for the event “**Either** A or B”

### Example 1

How many 3 digit numbers begin with 3 or 2? It’s best to get used to this notation. {0..9} means 0 through to 9, which is 10 numbers. Anyway, back to the question.

We represent the first number, starting with a 3 as

3{0..9}{0..9}

So there is 1 * 10 * 10 for the first possible number.

For the second number starting with a 2, it is:

2{0..9}{0..9}

Which is 1 * 10 * 10 for the second possible number.

Then to find out how many 3 digit numbers begin with a 3 or 2 we do

(10 * 10) + (10*10) = 100 + 100 = 200 possible 3 digit numbers.

### Example 2

I want to take two pieces of fruit with me for lunch. I have three bananas, four apples and two pears. How many ways can I select two pieces of fruit of different types?

We can split this question up into three parts:

Banana or Pear = 3 * 2 = 6 Banana or Apple = 3 * 4 = 12 Apple or Pear = 4 * 2 = 8

Note: Banana or pear = 3 * 2 is because there are 3 bananas and 2 pears.

then we just add them all together 6 + 12 + 8 = 26

### Set-Theoretic Interpretation

If A and B are disjoint events (that is, the union of A and B is equal to the empty set) then A∪B = A + B

A computer password is a string of 8 charecters where each charecter is an uppercase or digit. Each password must contain at least one digit. How many different passwords are there?

So there are 8 charecters `_ _ _ _ _ _ _ _`

And each one is either an uppercase character or digit. We will make a variable to shorten it. X = {A..Z or 0..9} So there is 26 uppercase letters and 10 digits and we want to know what |{A..Z or 0..9}| is so using the above formula we could just do |A| + |B| which is just 26 + 10 = 36 possible outcomes for every charecter in the password.

But, there is a problem. There exists passwords which do not have numbers in them, at all. Becuase of this, we need to take them out of the data set.

So, there are 36⁸ possible password permutations. We know the alphabet is 26 letters long, so therefore there must be 26⁸ passwords which only contain letters (pigeon hole principle). Now we need to take away.

36⁸ — 26⁸ = 2612282842880.

### Hacking Apple’s Passwords

A more fun and useful problem. Apple’s default password settings are one character has to be upper case, there has to be numbers and it has to be at least 7 characters long.

That means there is 26 * 2 possibilities for any given character in the password, so 52 possible outcomes and then add 10 as it could be a digit, 62⁷ = 3521614606208

But we can guess some things. Firstly, the typical user will have a capital letter at the start of their password and most often they will only use lowercase after that. The lowercase charecters will consist of {a..b or 0..9} as it has to include a number somewhere.

{A..B}xxxxxx

So that’s 26 + 10 = 36, therefore the password is now 26¹ * 36⁶ = 56596340736 since the first charecter is an uppercase letter.

Buttt we can guess more information. The user’s password will start with a capital letter, contain only lower-case letters in it and end with a number. Do you have a password like this?Well, after this you might want to change it…

So, the format is:

{A..B}xxxxx{0..9}

Where x = {a..b}

Okay, so work this out one at a time.

26¹ * 26⁵ * 10¹ = 3089157760.

The possibilities of passwords decreased by 300% by knowing some simple things about their password.

But wait, we can guess some more.

The password will likely be a word, followed by a number.

According to [this](https://brandonskerritt.github.io/maths/An-Introduction-To-Combinatronics/wordfinder.yourdictionary.com/letter-words/6) there are 15,000 words that are 6 letters long.

We know that the first letter will be a capital letter, snd we know that it ends with a number.

{A..Z{(5 letters here to make the world}{0..9}

So we know that the first section will be 15,000 and then it’s followed by a random number, 0 to 9. So we have 15,000 + 10 = 15010

A lot less than what was originally guessed. Knowing some basic information about a user, you can cut down the time it takes to hack their password by 3/4ths.

### Combinations Formula

The combinations formula is used to find out how many combinations are possible. The formula is:
![](https://cdn-images-1.medium.com/max/800/0*Mrnh0TwGqLIjaS4J.png)
Let’s say we have a deck of playing cards (52) and we want to find out how many different hands you can make when you pull out 5 cards, how would we work that out?

In this problem the order is irrelevant since it doesn’t matter what order we select the cards.

Well, a typical hand might look like: 5 of Spades, 6 of Clubs, King of Hearts, Queen of Diamonds. and another typical hand might look like: 6 of Clubs, 5 of Spades, King of Hearts, Queen of Diamonds.

The order doesn’t matter here.
![](https://cdn-images-1.medium.com/max/800/0*Gd9rYPiTw-Vbepzf.png)
And that’s how we work it out, using combinations. By diving by the number of hands that are different permutations but the same combination, aka how many different ways there are to arrange 5 cards.

### Example 2

Consider the problem of choosing 5 members from a group of 12 to work on a special project. How many distinct five-person teams can be chosen?

The number of 5-person teams is the same as the number of subsets of 5-combinations size that can be chosen from the set of twelve. So we would use the combinations formula for this:

And simplifying this (by simply expanding the factorials and dividing the numbers by hand) we get 11 * 9 * 8 which is 792.

The subtraction rule is really simple. If given 2 sets, A and B and they share common outcomes between them then the total number of outcomes is A + B — (A intersection B)

### Teams that contain both or neither

Suppose two members of the group of 12 insist on working as a pair — any team must contain either both or neither. How many five-person teams can be formed?

Call the two members of the group that insist on working as a pair A and B. Then any team formed must contain both A and B or neither A nor B.

Because a team that contains both A and B contains exactly three other people from the remaining ten in the group, there are as many such teams as there are subsets of three people that can be chosen from the remaining ten.

By the combinations formula we get

Which is 120.

Because a team that contains neither A nor B contains exactly five from the other remaining ten, there are as many such teams as there are subsets of five people that can be chosen from the remaining ten. By the combination therom again there is

Which is 252.

Because the set of teams that contain both A and B is disjoint from the set of teams that contain neither A nor B, by the addition rule:

Number of teams containing both A and B or neither A nor B = Number of teams containing A and B + Number of teams containing neither A nor B which in maths is 120 + 252 = 372.

### K-permutations

If you a selection of K distinct elements of a set, where order matters then you would use this formula:

### Example question

How many ways are there to select 3 students for a prospectus photograph (order matters) from a group of 5?

P(5, 3) = 5! / 2! = 60 Note: (5, 3) notes that you want to select 3 students from a set of 5.

#### Further reading

[**Combinations vs Permutations**](https://medium.com/i-math/combinations-permutations-fa7ac680f0ac)
[*We throw around the term “combination” loosely, and usually in the wrong way. We say things like, “Hey, what’s your…*medium.com](https://medium.com/i-math/combinations-permutations-fa7ac680f0ac)
