---
title: Complexity of algorithms (notes)
slug: complexity-of-algorithms
date_published: 2019-04-14T00:01:00.000Z
date_updated: 2019-05-22T15:41:55.000Z
tags: 
    - University
draft: true
---

For Big O, Theta, Omega check this out:

[https://skerritt.blog/you-need-to-understand-big-o-notation-now/](https://skerritt.blog/you-need-to-understand-big-o-notation-now/)
![](/content/images/2019/02/image.png)
If you like a song from an album, you may choose to listen to another song from the album. When do you decide to, instead of streaming, you buy the whole album?
![](/content/images/2019/02/image-1.png)![](/content/images/2019/02/image-2.png)
This algorithm does not know the future, only the past. However, if it is an offline algorithm then it knows the whole sequence of events. The mistake is a factor of 2 only. With the algorithm "given a listen to 10 songs in the album, buy the album" means you can only overpay by a factor of 2. This is called 2-competitive.
![](/content/images/2019/02/image-3.png)
We will now show a 2-competitive algorithm for this problem. The first request comes, the algorithm has to take the decision without knowing the content of the future request. Cost(A, R) is the cost the online algorithm comes. 

An online algorithm A is c-competitive for some c factor if:

$$Cost(A, R) \le c * \; cost(OPT, R) + b,$$

For some constant b > 0.

The "b" is a shift. Let's pretend this doesn't exist for now.

If c = 2, then it pays more than opt by at most a factor of 2. So if op pays 50, it might pay at most 100. if opt pays 100, it pays at most 200.

How do we get such an algorithm?

If b = 0, then it is "strictly" c-competitive.
![](/content/images/2019/02/image-4.png)
A single request is a pair (s,  l) where s is the song and l is either 0 or 1. If it's 1, she wants to listen to the song. If she doesn't, it's 0. 

If the request is (s, 1) she pays x. If she streams, its 10x. If the request is (s, 0) she does nothing as she doesnt want to listen to the song.
![](/content/images/2019/02/image-5.png)![](/content/images/2019/02/image-6.png)
The following stratergy is 2-competitive. "Rent for 10 times, and then buy the album" is 2-competitive. 

"Rent for 10 times, then buy the album" is strictly 2-competitive. When you have 11 requests to listen to the song, we're hedging against the future so then we buy the album. 

You cannot be worse than opt, as you've already paid 10x and you pay another 10x for the album so it is a factor of 2. Wikipedia is the only good source I can find online about competitive algorithms. [https://www.wikiwand.com/en/Competitive_analysis_(online_algorithm)](https://www.wikiwand.com/en/Competitive_analysis_(online_algorithm))

So the next couple slides he talks about what an array is, and then what linked lists are. I have another article on linked lists here:

[https://skerritt.blog/you-dont-understand-blockchain-unless-you-understand-this-simple-data-structure/](https://skerritt.blog/you-dont-understand-blockchain-unless-you-understand-this-simple-data-structure/)

Just to let you know, I'm skipping the slides on linked lists because of the blog post above. There's nothing new there that isn't in that blogpost. 
![](/content/images/2019/02/image-28.png)
This is actually interesting. In Java, it's called a hashmap (although most languages use dictionaries). It looks like this:

    {"hello": 0, "goodbye": 1}

Where each `key` has a corresponding `value` assiocated with it. This slide says that you can order a dictionary by its keys. 
![](/content/images/2019/02/image-29.png)
Okay so searching with linked lists is kinda slow and sucky (read the blog post ‼‼‼😉), but we can instead store an ordered dictionary in an array by ascending values (he says non-descreasing values, which is the same as ascending....? Thanks for confusing the whole class 😅)
![](/content/images/2019/02/image-30.png)
Uhhhhh I would rather die than look at binary search for the 59th time since I've been at uni but if you *really *want us to know it then sure lmao. He does a couple slides on how binary search works, but tbh you probably already know. If not, just google it. It's super easy.
![](/content/images/2019/02/image-31.png)
This is an introduction to recurrence too, a popular topic that'll come up in the exam.
![](/content/images/2019/02/image-32.png)![](/content/images/2019/02/image-33.png)![](/content/images/2019/02/image-34.png)![](/content/images/2019/02/image-35.png)![](/content/images/2019/02/image-36.png)![](/content/images/2019/02/image-37.png)![](/content/images/2019/02/image-38.png)
This is the depth of a node, not the height of the tree. I got confused by this first time around.
![](/content/images/2019/02/image-39.png)![](/content/images/2019/02/image-40.png)![](/content/images/2019/02/image-41.png)![](/content/images/2019/02/image-42.png)![](/content/images/2019/02/image-43.png)![](/content/images/2019/02/image-44.png)![](/content/images/2019/02/image-45.png)![](/content/images/2019/02/image-46.png)![](/content/images/2019/02/image-47.png)![](/content/images/2019/02/image-48.png)![](/content/images/2019/02/image-49.png)![](/content/images/2019/02/image-50.png)![](/content/images/2019/02/image-51.png)
Sorry for not writing much, but I think the slides here are actually really good.
![](/content/images/2019/02/image-52.png)
AVL trees are one of the tutorials so this is important !!
![](/content/images/2019/02/image-53.png)![](/content/images/2019/02/image-54.png)![](/content/images/2019/02/image-55.png)![](/content/images/2019/02/image-56.png)![](/content/images/2019/02/image-57.png)![](/content/images/2019/02/image-58.png)![](/content/images/2019/02/image-59.png)![](/content/images/2019/02/image-60.png)![](/content/images/2019/02/image-61.png)![](/content/images/2019/02/image-62.png)![](/content/images/2019/02/image-63.png)![](/content/images/2019/02/image-64.png)![](/content/images/2019/02/image-65.png)![](/content/images/2019/02/image-66.png)![](/content/images/2019/02/image-67.png)![](/content/images/2019/02/image-68.png)![](/content/images/2019/02/image-69.png)![](/content/images/2019/02/image-70.png)![](/content/images/2019/02/image-71.png)![](/content/images/2019/02/image-72.png)![](/content/images/2019/02/image-73.png)![](/content/images/2019/02/image-74.png)![](/content/images/2019/02/image-75.png)![](/content/images/2019/02/image-108.png)![](/content/images/2019/02/image-109.png)![](/content/images/2019/02/image-110.png)
This is O(log n) but he writes O(log m).
![](/content/images/2019/02/image-111.png)![](/content/images/2019/02/image-112.png)![](/content/images/2019/02/image-113.png)![](/content/images/2019/02/image-115.png)![](/content/images/2019/02/image-116.png)![](/content/images/2019/02/image-117.png)![](/content/images/2019/02/image-118.png)![](/content/images/2019/02/image-119.png)![](/content/images/2019/02/image-120.png)![](/content/images/2019/02/image-121.png)![](/content/images/2019/02/image-122.png)![](/content/images/2019/02/image-123.png)![](/content/images/2019/02/image-124.png)![](/content/images/2019/02/image-125.png)
This is based on divide and conquer algorithms, which I have a blogpsot about here:

[https://skerritt.blog/divide-and-conquer-algorithms/](https://skerritt.blog/divide-and-conquer-algorithms/)
![](/content/images/2019/02/image-126.png)![](/content/images/2019/02/image-127.png)![](/content/images/2019/02/image-128.png)![](/content/images/2019/02/image-129.png)![](/content/images/2019/02/image-130.png)
Ok so this one pisses me off because it's not explained 'nicely'. Basically, an inversion on a number is how many numbers smaller than that number appear later in the list. Let's see a simpler example.

    10 2 1

10 has 2 inversions. 2 and 1 are smaller than 10, but they appear after 10. 2 has 1 inversion. 1 is smaller than 2, but it appears later in the list. **All sorted lists have 0 inversions**. We say the entire set has 3 inversions. 

    1 2 10

Has 0 inversions and is sorted.
![](/content/images/2019/02/image-131.png)
The maximum number of inversions is $\frac{n(n-1)}{2}$ where n is how many numbers there are.
![](/content/images/2019/02/image-132.png)![](/content/images/2019/02/image-133.png)![](/content/images/2019/02/image-134.png)![](/content/images/2019/02/image-135.png)![](/content/images/2019/02/image-137.png)![](/content/images/2019/02/image-136.png)![](/content/images/2019/02/image-138.png)![](/content/images/2019/02/image-139.png)![](/content/images/2019/02/image-140.png)![](/content/images/2019/02/image-141.png)![](/content/images/2019/02/image-142.png)![](/content/images/2019/02/image-143.png)![](/content/images/2019/02/image-144.png)![](/content/images/2019/02/image-145.png)![](/content/images/2019/02/image-149.png)![](/content/images/2019/02/image-154.png)![](/content/images/2019/02/image-155.png)![](/content/images/2019/02/image-156.png)![](/content/images/2019/02/image-157.png)![](/content/images/2019/02/image-158.png)![](/content/images/2019/02/image-159.png)![](/content/images/2019/02/image-160.png)![](/content/images/2019/02/image-161.png)![](/content/images/2019/02/image-162.png)![](/content/images/2019/02/image-163.png)![](/content/images/2019/02/image-164.png)![](/content/images/2019/02/image-165.png)![](/content/images/2019/02/image-166.png)![](/content/images/2019/02/image-167.png)![](/content/images/2019/02/image-168.png)![](/content/images/2019/02/image-169.png)![](/content/images/2019/02/image-170.png)![](/content/images/2019/02/image-171.png)![](/content/images/2019/02/image-172.png)![](/content/images/2019/02/image-173.png)
The best way to study the greedy method is to look at the fractional knapsack problem.
![](/content/images/2019/02/image-174.png)
Sorted arrays can be used for this. Running time is O(n log n)
![](/content/images/2019/02/image-175.png)![](/content/images/2019/02/image-176.png)![](/content/images/2019/02/image-177.png)
With fractional knapsack, calculate the ratio value/weight for each item and sort the item on  basis of this ratio. Then take the item with the highest ratio and add  them until we can’t add the next item as a whole and at the end add the  next item as much as we can. Which will always be the optimal solution  to this problem.
![](/content/images/2019/02/image-178.png)![](/content/images/2019/03/image-4.png)![](/content/images/2019/03/image-5.png)![](/content/images/2019/03/image-6.png)![](/content/images/2019/03/image-7.png)![](/content/images/2019/03/image-8.png)![](/content/images/2019/03/image-9.png)
So he proves it, but his hand writing.... I'm not including this here.
![](/content/images/2019/03/image-10.png)![](/content/images/2019/03/image-11.png)![](/content/images/2019/03/image-12.png)![](/content/images/2019/03/image-13.png)![](/content/images/2019/03/image-14.png)![](/content/images/2019/03/image-16.png)![](/content/images/2019/03/image-17.png)![](/content/images/2019/03/image-18.png)![](/content/images/2019/03/image-19.png)![](/content/images/2019/03/image-20.png)![](/content/images/2019/03/image-21.png)![](/content/images/2019/03/image-22.png)![](/content/images/2019/03/image-23.png)
