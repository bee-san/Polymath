# What is this?

Name-that-hash is an hash-identifcation system. Hashes are important in cyber security and used everywhere, but there are so many different types.

Attackers often want to know what type of hash something is. A hash-identification system tells you what the hash is.

# How?

Hashes are design to look random, so how can we identify which types are which?

There are some indicators. They may have markers such as `$6$`, they may be of a certain lenght, a certain character set.

In short, we use Regex! We have a database of Regex that matches hashes. Most regex matches multiple-type sof accuracy, so while we cannot get get a 100% accuracy rating we can say for certain that iif it is a hash, it is within a subset of the database (which the user will see).

Given some input, return all the regex that match against it.

Simple, right? Let's take a look at our competitors thus far.

# The competition

Hash-identification is kind of a solved problem. It's just Regex. 

The 2 biggest competitors are HashId and Hash-Identifier.

HashID is the original, last updated in 2011.

# The CLI

# The API
Base64

# The webapp
