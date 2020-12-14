---
title: Designing effective p2p networks
slug: designing-p2p-networks
date: 2020-01-06T20:52:00.000Z
draft: false
---

This is an opinion piece on designing effective peer to peer (p2p) networks. I've written extensively about peer to peer networks, and have even designed my own (albeit, bad) cryptocurrency. Very often, I'll drea\m up and design peer to peer networks. So this is more of an informed opinion than a random opinion.d

---

# When should I use a peer to peer network?

This is a hard question to answer, because P2P networks can be used for all networking. Just like with programming, we need to use the right tool for the job.

P2P networks are very good at scaling incredibly fast, automatically. Effective p2p networks improve with more users,  not degrade. 

If you are building a platform with a shared goal (ie share files) and you can imagine the platform growing uncontrollably big, p2p networks are good. Or if you do not want anyone to shut down your network (in a client-server model, turn off your servers) a p2p network is effective.

Let's walk through what all good peer to peer networks share.

---

# Rewards

All peer to peer networks have a reward system in place. The user does some work, and they are rewarded. Even if the reward isn't clearly defined, there is always a reward for taking part in the peer to peer network.

In Bitcoin, this is clearly earning Bitcoin. Bittorrent rewards participants with faster download speeds. Tor rewards other Tor members with more privacy. 

The idea of a reward is to disper free-riders. Those that partake in the network without giving anything back. There are 2 ways to defer free-riders:

- Forcing every user to give back.
- Rewarding users who give back.

Tor is the former, all users who join Tor are part of the network. The only reward that can be given is to become a guard node, which provides no obvious benefit for the user other than to feel good about themselves.

Most peer to peer networks choose the latter, rewarding users who give back.

In Bittorrent,  those who seed are rewarded with higher download rates. The more you seed, the faster you  can download. In Bitcoin, users are rewarded for mining the blockchain in the form of Bitcoin. 

Thus, this leads us to look at peer to peer networks from 2 interesting perspectives. Human civilisations, or reinforcement learning machines.

Since reinforcement learning closely resmbles how humans work, I will not discuss it much. But the implications are important. Agents in the network seek to optimise their own personal reward, which in turn, if the network is made correctly, optimises the whole network.

---

# Optimisation of the network

An ideal p2p network will improve the more people that use it. In Tor, the more people that use it the more privacy is given to those who need it. 

A simple distinction, but one that must be made. As the network grows older, ideally it forever reaches its global optimised state. 

Unlike client-server, where the more users there are the harder it becomes to maintain the network, an effective peer to peer network gets **better** the more people that use it.

Optimisation of the network as it grows is often done through the rewards system. As Tor grows, the privacy of each user increases. Thus, the more that use Tor, the better. And each user has their own personal reward, but together this creates a positive movement for the whole network.

In Bitcoin, the more that mine Bitcoin the larger incentive it is to use better computers. Better computers = faster mines = more money. This creates a competition amongst users. **Who can contribute to the network the most? **Without getting into economics, the miners will spend more on Bitcoin. Meaning that they have to sell Bitcoin at a higher rate to make profit back. Meaning that the price of Bitcoin goes up. Which, can be seen as a positive for the whole network. 

Not to mention that Bitcoin's security from a 51% attack relies on more users on the network. Again, as the network grows the better it becomes.

When choosing a reward, it is important to look at the local rewards (what the user themselves gets) and to look at the greater rewards, what the network will get for participating. 

I also reccomend rewards which increase as the network grows. Scalable rewards.

<Img of client-server starting to struggle, but peer to peer network having a good time>

### So, at the start the network sucks?

Yup! That's how these things work. With a client-server architecture, it can be amazing from the start. But with a peer to peer network, it kinda sucks a lot for the first users. With Bitcoin, what was the incentive? You get this coin that's worth.... nothing at all, actually.

Tor. The incentive? Well, if there's only 3 users then there is no incentive.

Bittorrent. The incentive? You can download this one persons files. 

In peer  to peer networks, generally they suck for the first couple users and only increase over time. So how then, do we build an effective peer to peer network that other people will want to use? 

There are 2 methods to this.

- Forceful use (navy)
- Incredible technology

You can force users to use the network. This is how Tor got its start. The US Navy built Tor, and effectively they could force others in the Navy to use it.

The other option is incredible technology. In a peer to peer network, the first few users are often users who recgonise how incredible the technology is. Think about Bitcoin. The first few users fell in love with the technology behind it, and truly believed it could one day be great. 

With a great rewards system in place, the first users of Bitcoin realised it could grow up to be something huge. Amazing technology attracts the first few users, and those users are often technologically minded.

---

## Automatic Optimisation

Here is my opinion part! I believe that we can use artifical intelligence to automatically optimise a p2p network. Humans are cool and all, but we're pretty slow when it comes to making changes.

p2p networks already use technology to find shortest routes, or preferred routes. As networks become more and more complicated, simple hand written algorithms might not be enough.

Picture this.

In our network, we have multiple nodes all interconnected. Each node has a rating. This rating signifies how good that node is. Good here, could mean fast, it could mean trust worthy or the likes. We'll generalise it to mean "good" that encompasses everything. 

Everytime another node uses this node, its "good" rating increases. Much like a neural network. 

Nodes can have a "good" rating of 0, as in they do not contribute to the network. 

How would a node with a rating of 0 ever increase its good rating if we were using simple pathfinding algorithms? If a node has a good rating of 1, does that mean every bit of data would go through this node?

What if we introduce more numbers. The speed of the node. The amount of time the node has spent contributing to the network. The contributions made. User ratings.  And more. 

And our goal was to create the "best" path across the network, taking into account all of these numbers and to maximise our own personal reward, whatever that may be. 

This seems like a perfect scenario for reinforcement learning. Multiple inputs in an effort to maximise our own personal reward. Exploratory choices, meaning that a node with a "good" rating of 0 may be chosen. 

Us humans would eventually work it out like this anyway, where we choose certain nodes to have more privlege than others (in Tor, this is called a guard node. Generally speaking these are not true p2p networks, but instead hybrid). 

Now we have a rough picture of how to use reinforcement learning to optimise the network, optimise our personal reward and to give everyone in the network a fair shot. Let's see why assigning nodes with a higher "good" value than others is a great idea.

---

# Jobs for the people

In almost all peer to peer networks, jobs are assigned to nodes. Dependent mostly on whether they want it or not, sometimes jobs are given to nodes at random.

In Bitcoin, we have miners whose job it is to mine the blockchain. In Tor, we have guard nodes. In some other cryptocurrencies, nodes have higher privlegedes than others.

At the moment, peer to peer networking is seen as more of a communistic vision. Which is cool, but humans assign other humans jobs based on their skills. And in some networks, we do the same. 

If a node has proven to be trustworthy, than we shall make it a guard node. If a node wants to mine the blockchain, it becomes a miner.

I'd like to make a distinction here. These nodes do not have more rights than the other nodes, they simply have a job to do. 

If we give everyone the same job, the network will tend towards global optimisation much slower. Let's say we have a new file sharing system. Our system will let you download files from others. 

We have a file, Ubuntu.iso, which is being seeded by 10 people. We choose at randomly a seed. This seed has an upload speed of 1 mbps while all the other seeders have an upload speed of 200mbps. It makes logical sense to use the uploaders with faster speed, as the one users upload speed will be poorly affected by us requesting a file. Resulting in an unhappy human who cannot upload a Facebook image!

It makes sense logically to choose from a subsection of people with high upload  speeds. Effectively, we have given these people 'jobs'. 

There are 2 types of jobs in peer to peer networks:

- Rewarded Jobs
- Unpaid Internships (jobs)

With rewarded jobs, the uploaders get a higher reward for working as an effective uploader. This reward might be priority access to downloads from other high uploaders. This is how Bittorrent works.

With unpaid jobs, there is no reward. There is no incentive for one to choose a job, it is simply gifted to those. This is how guard nodes work in Tor. 

Deciding on what jobs to give, and whether it is rewarded or not is problem specific. Say, for example, we have a job called "maintainer of the Blockchain". This job means that these people each have a copy of the blockchain. And only they do, no one else can. Any cryptocurrency nerd reading this may already see the problem.

In order to view the blockchain, you need to have this job. But not every citizen of the world has a spare 300gb to view the chain. They cannot get the job, because they do not meet the required specification.

This is another issue. Do people choose their own jobs? Are they automatically assigned? Can we reject people if they do not meet the job specification?

With only a small percent controling the blockchain, it leaves it open to a 51% attack. A small few will hold all the power. It will not work well in this instance. 

I propose that jobs are automatically assigned based on the specification of the user, but any user can request a job. The only jobs they should be rejected for is high trust jobs, such as guard nodes. But, the specification of their computer should not be taken into account for trust jobs. 

Humans that pick their own jobs is just too slow, the network needs to react fast and scale fast. Humans are not fast. But we do not want to prevent humans from accessing resources because of their circumstances.

When assigning jobs, it is important that the jobs work in harmony. 

I suggest taking inspiration from bee hives or ant colonies for this. Human jobs are simply too hard to model, to focus on a much smaller example is wise. Afterall, you don't see ants that are SEO experts 😉 

Another thing to consider if you follow my advice of automatically assigned jobs + opt in is punishment. Should there be a punishment if someone takes a job for which they are unfit? Should a 30gb computer take a punishment for trying to maintain a 300gb file?

On the one hand, only a very small percent of the population will choose their own jobs, and will ignore the assigned job and choose something for which they are unfit. But, to achieve global optimisation we must make sure every single thing is accounted for.  Unforunately, in this world, those that do jobs that they are not capable of should be punished. I would not say to reduce the resources available to them through the job, but perhaps reduce the reward of using the network in some way.

---

# Data Structures

Every single effective peer to peer network uses data structures. The blockchain is just a fancy linked list with some extra properties. Bittorrent's magnet links work based on distributed hash tables. 

Data structures are absolutely vital to peer to peer networks. I do not want to get into every data structure available, but knowledge of them is important. 

We can design a network using a [distributed data structure](https://en.wikipedia.org/wiki/Category:Distributed_data_structures) that already exists, or we can build a new data structure / algorithm based on pre-existing ones.

---

# Policy changes

Throughout this article, I have talked about designing the network to be perfect from the get go. Any human knows this isn't possible. So how then, do we change the network when it's in effect? How do we implement policy changes?

1. Dictatorship
2. Let the people decide
3. The people can form a democracy

In our first instance, we have dictatorship. You, the creator decides on changes. You create these changes, and they go out to the network. We don't care what the participants think, only that the change has taken place.

This is the most effective for easily implementing policy changes, but it ruins the trust. In my opinion, a good peer to peer network reduces trust. We should not need to trust anyone. However, trust is important in some networks. It depends on the network itself. 

If the network was for a digital currency, why would you trust this entire currency in the hands of a single person? But for a privacy centered network, having this trust in one person or body of people can increase the trust throughout the network. It reduces the chance of a 51% attack backdoor in the early days, building trust from day 0.

As the network progresses, it strays further and further away from a 51% attack. Which means we lose trust, we do not need to trust that it is safe from a 51% attack if the network is large enough.

In my opinion, an effective p2p network should move from a dictatorship and move towards a democracy. As time progresses, the will of one indivudal can change. They may sell out the network. 

But again, this brings problems. What if there is a critical failure in the code and there needs to be a change made? This is for the designer to decide.

We can alternatively let the people decide. From the get go, no single person has full control. Every time a change is made, a % of the network (likely 51) will need to agree to the change. Complete control for the network. No trusting the developer involved. 

At the start, this may be problematic. Although if no one cares about your network at the start, it's better that way. Humans are incredibly slow too. Imagine a critical bug in the code that had to be fixed right there and then. Humans may take weeks to decide. Many will not even respond to the decision. 

The alternative, is a democracy. Give certain people more power than others. Have the community vote in leaders, or have the leaders be pre-selected. These leaders than decide on changes to the codebase. This reduces the trust, especially if they are voted in. But nothing is stopping them from teaming together to get the maximum personal reward while not doing anything for the many.

All in all, deciding on policy changes is a tricky subject. And one that should be decided before the network is made. 

Although something to remember is trust. Will the users need to trust you, personally? If so, try and work towards a goal where that trust is reduced. Diversify that trust over to others. Remove trust completely, make them only trust themselves. Effective peer to peer networks are unlike client-server models where one person controls all the power. Effective P2P networks are for the people.

---

# Conclusion

Because p2p networks are problem specific, this article serves mainly as a list of questions to answer in designing an effective p2p network. 
