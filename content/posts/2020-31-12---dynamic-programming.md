---
title: What Is Dynamic Programming With Python Examples
slug: dynamic-programming-2
date_published: 2019-06-05T16:03:32.000Z
date: 2020-12-31T01:44:21.000Z
math: true
draft: true
ShowToc: true
tags: 
    - University
    - Computer Science
    - Datastructures and Algorithms
    - Popular
draft: true
cover:
    image: "/media/p2p.jpg"

excerpt: Dynamic programming (DP) is breaking down an optimisation problem into smaller sub-problems, and storing the solution to each sub-problems so that each sub-problem is only solved once.
---

# ToDo
DP is just fancy bruteforcing 

Backtracing? 
* Fibonnacci 
* Spell check
* Make images accessible 
* Every single DP problem is about solving the problem at each step, make sure its obvious
* Start with top down and then bottom-up
# SEO
* Subsequence
* Interview
* How to get better at dynamic programming
* What is dynamic programming?
* leetcode dynamic programming

# What is Dynamic Programming?

Dynamic programming is breaking down a problem into smaller sub-problems, solving each sub-problem and storing the solutions to each of these sub-problems in an array (or similar data structure) so each sub-problem is only calculated once. 

It's smart bruteforcing. We bruteforce, but remember what we've done along the way.

It is both a [mathematical optimisation](https://en.wikipedia.org/wiki/Mathematical_optimization) method and a computer programming method.

*Optimisation problems* seek the maximum or minimum solution. The general rule is that if you encounter a problem where the initial algorithm is solved in O(2n) time, it is better solved using Dynamic Programming.

---

## Why Is Dynamic Programming Called Dynamic Programming?
![](/media/dp/undraw1.svg)

[Richard Bellman](https://en.wikipedia.org/wiki/Richard_E._Bellman) invented DP in the 1950s. [Bellman named it Dynamic Programming](https://en.wikipedia.org/wiki/Dynamic_programming#History) because at the time, RAND (his employer), disliked mathematical research and didn't want to fund it. He named it Dynamic Programming to hide the fact he was really doing mathematical research.

Bellman explains the reasoning behind the term Dynamic Programming in his autobiography, Eye of the Hurricane: An Autobiography (1984, page 159). He explains:

> "I spent the Fall quarter (of 1950) at RAND. 
> 
> My first task was to find a name for multistage decision processes. An interesting question is, Where did the name, dynamic programming, come from? 
> 
> The 1950s were not good years for mathematical research. We had a very interesting gentleman in Washington named Wilson. He was Secretary of Defense, and he actually had a pathological fear and hatred of the word research. I’m not using the term lightly; I’m using it precisely. 
> 
> His face would suffuse, he would turn red, and he would get violent if people used the term research in his presence. You can imagine how he felt, then, about the term mathematical. The RAND Corporation was employed by the Air Force, and the Air Force had Wilson as its boss, essentially. Hence, I felt I had to do something to shield Wilson and the Air Force from the fact that I was really doing mathematics inside the RAND Corporation. 
> What title, what name, could I choose? In the first place I was interested in planning, in decision making, in thinking. But planning, is not a good word for various reasons. I decided therefore to use the word “programming”. I wanted to get across the idea that this was dynamic, this was multistage, this was time-varying. I thought, let's kill two birds with one stone. Let's take a word that has an absolutely precise meaning, namely dynamic, in the classical physical sense. 
> It also has a very interesting property as an adjective, and that is it's impossible to use the word dynamic in a pejorative sense. Try thinking of some combination that will possibly give it a pejorative meaning. It's impossible. Thus, I thought dynamic programming was a good name. It was something not even a Congressman could object to. So I used it as an umbrella for my activities."

---

## What are Sub-Problems?
![](/media/dp/undraw2.svg)

Sub-problems are smaller versions of the original problem. Let's see an example. With the equation below:

$$1 + 2 + 3 + 4$$

We can break this down to:

$$1 + 2$$

$$3 + 4$$

Once we solve these two smaller problems, we can add the solutions to these sub-problems to find the solution to the overall problem.

Notice how these sub-problems breaks down the original problem into components that build up the solution. This is a small example but it illustrates the beauty of Dynamic Programming well. If we expand the problem to adding 100's of numbers it becomes clearer why we need Dynamic Programming. Take this example:

$$6 + 5 + 3 + 3 + 2 + 4 + 6 + 5$$

We have $6 + 5$ twice. The first time we see it, we work out $6 + 5$. When we see it the second time we think to ourselves:

> "Ah, 6 + 5. I've seen this before. It's 11!"

In Dynamic Programming we store the solution to the problem so we do not need to recalculate it. By finding the solutions for every single sub-problem, we can tackle the original problem itself.

*Memoisation *is the act of storing a solution.

---

## What is Memoisation in Dynamic Programming?
![](/media/dp/undraw3.svg)

Let's see why storing answers to solutions make sense. We're going to look at a famous problem, *[Fibonacci sequence](https://www.mathsisfun.com/numbers/fibonacci-sequence.html)*. This problem is normally solved in Divide and Conquer. 

There are 3 main parts to [divide and conquer](/divide-and-conquer-algorithms/):

1. **Divide** the problem into smaller sub-problems of the same type.
2. **Conquer** - solve the sub-problems recursively.
3. **Combine** - Combine all the sub-problems to create a solution to the original problem.

Dynamic programming has one extra step added to step 2. This is memoisation. 

The Fibonacci sequence is a sequence of numbers. It's the last number + the current number. We start at 1. 

$$1 + 0 = 1$$

$$1 + 1 = 2$$

$$2 + 1 = 3$$

$$3 + 2 = 5$$

$$5 + 3 = 8$$

In Python, this is:

```python
def F(n):
    if n == 0 or n == 1:
    return n
    else:
    return F(n-1)+F(n-2)
```
    

If you're not familiar with recursion I have a [blog post written for you that you should read first.](/divide-and-conquer-algorithms/)

Let's calculate F(4). In an execution tree, this looks like:

![](/content/images/2019/06/image-8.png)

<figure>
	<img src="/media/dp/execution_tree.png" alt="Starts at 4, it splits into two. Fibonacci 3 and 2. Each of these 2 then split into 2 more for a total of 4. 1, 2, 0, and 1. We stop splitting when we reach 0 or 1. 2 is split again, into 1 and 0. The levels go from top to bottom. They look like this: 4 new level 3, 2 new level 1, 2,  0, 1 new level 1, 0">
	<figcaption><figcaption>
</figure>

We calculate F(2) twice. On bigger inputs (such as F(10)) the repetition builds up. The purpose of dynamic programming is to not calculate the same thing twice.

Instead of calculating F(2) twice, we store the solution somewhere and only calculate it once.

We'll store the solution in an array. F[2] = 1. Below is some Python code to calculate the Fibonacci sequence using Dynamic Programming.

```python
def fibonacciVal(n):
    memo[0], memo[1] = 0, 1
    for i in range(2, n+1):
        memo[i] = memo[i-1] + memo[i-2]
    return memo[n]
```

---

## How to Identify Dynamic Programming Problems
![](/media/dp/undraw4.svg)

In theory, Dynamic Programming can solve every problem. The question is then:

> "When should I solve this problem with dynamic programming?"

We should use dynamic programming for problems that are between *tractable *and *intractable *problems. 

*[Tractable problems](https://www.britannica.com/technology/tractable-problem)* are those that can be solved in polynomial time. That's a fancy way of saying we can solve it in a fast manner. Binary search and sorting are all fast. *[Intractable problems](https://www.umsl.edu/~siegelj/information_theory/classassignments/Lombardo/04_intractableproblems.html)* are those that run in exponential time. They're slow. Intractable problems are those that can only be solved by bruteforcing through every single combination ([NP hard](https://www.youtube.com/watch?v=YX40hbAHx3s)).

When we see terms like:

> "shortest/longest, minimized/maximized, least/most, fewest/greatest, "biggest/smallest" 

We know it's an optimisation problem. 

Dynamic Programming algorithms proof of correctness is usually self-evident. Other algorithmic strategies are often much harder to prove correct. Thus, more error-prone.

When we see these kinds of terms, the problem may ask for a specific number ( "find the minimum number of edit operations") or it may ask for a result ( "find the longest common subsequence"). The latter type of problem is harder to recognize as a dynamic programming problem. If something sounds like optimisation, Dynamic Programming can solve it.

Imagine we've found a problem that's an optimisation problem, but we're not sure if it can be solved with Dynamic Programming. First, identify what we're optimising for. Once we realize what we're optimising for, we have to decide how easy it is to perform that optimisation. Sometimes, the [greedy approach](https://brilliant.org/wiki/greedy-algorithm/) is enough for an optimal solution.

Dynamic programming takes the brute force approach. It Identifies repeated work, and eliminates repetition. 

Before we even start to plan the problem as a dynamic programming problem, think about what the brute force solution might look like. Are sub steps repeated in the brute-force solution?  If so, we try to imagine the problem as a dynamic programming problem.

Mastering dynamic programming is all about understanding the problem. List all the inputs that can affect the answers. Once we've identified all the inputs and outputs, try to identify whether the problem can be broken into subproblems. If we can identify subproblems, we can probably use Dynamic Programming. 

Then, figure out what the recurrence is and solve it. When we're trying to figure out the recurrence, remember that whatever recurrence we write has to help us find the answer. Sometimes the answer will be the result of the recurrence, and sometimes we will have to get the result by looking at a few results from the recurrence.

Dynamic Programming can solve many problems, but that does not mean there isn't a more efficient solution out there. Solving a problem with Dynamic Programming feels like magic, but remember that dynamic programming is merely a clever brute force. Sometimes it pays off well, and sometimes it helps only a little.
<figure>
	<img src="/media/dp/flow.png">
	<figcaption><figcaption>
</figure>

---

## Tabulation (Bottom-Up) vs Memoisation (Top-Down)
![](/media/dp/undraw10.svg)

There are 2 types of dynamic programming. Tabulation and Memoisation. 

### Memoisation (Top-Down)

We've computed all the subproblems but have no idea what the optimal evaluation order is. We would then perform a recursive call from the root, and hope we get close to the optimal solution or obtain a proof that we will arrive at the optimal solution. Memoisation ensures you never recompute a subproblem because we cache the results, thus duplicate sub-trees are not recomputed. 

![](/media/dp/tree.png)

From our Fibonacci sequence earlier, we start at the root node. The subtree F(2) isn't calculated twice.

This starts at the top of the tree and evaluates the subproblems from the leaves/subtrees back up towards the root. **Memoisation is a top-down approach.**

### Tabulation (Bottom-Up)

We've also seen Dynamic Programming being used as a 'table-filling' algorithm. Usually, this table is multidimensional. This is like memoisation, but with one major difference. We have to pick the exact order in which we will do our computations. The knapsack problem we saw, we filled in the table from left to right - top to bottom. We knew the exact order of which to fill the table.

Sometimes the 'table' is not like the tables we've seen. It can be a more complicated structure such as trees. Or specific to the problem domain, such as cities within flying distance on a map.

### Tabulation & Memosation - Advantages and Disadvantages

Generally speaking, memoisation is easier to code than tabulation. We can write a 'memoriser' wrapper function that automatically does it for us. With tabulation, we have to come up with an ordering.

Memoisation has memory concerns. If we're computing something large such as F(10^8), each computation will be delayed as we have to place them into the array. And the array will grow in size very quickly.

Either approach may not be time-optimal if the order we happen (or try to) visit subproblems is not optimal.  If there is more than one way to calculate a subproblem (normally caching would resolve this, but it's theoretically possible that caching might not in some exotic cases). Memoisation will usually add on our time-complexity to our space-complexity. For example with tabulation we have more liberty to throw away calculations, like using tabulation with Fib lets us use O(1) space, but memoisation with Fib uses O(N) stack space).

<table>
    <thead>
        <tr>
            <th colspan="3">Memoisation vs Tabulation</th>
        </tr>
    </thead>
    <tbody>
        <tr>
          <td></td>
          <td><b>Tabulation</b></td>
          <td><b>Memoisation</b></td>
        </tr>
      <tr>
        <td>Code</td>
        <td>Harder to code as you have to know the order</td>
        <td>Easier to code as functions may already exist to memoise</td>
      </tr>
      <tr>
        <td>Speed</td>
        <td>Fast as you already know the order and dimensions of the table</td>
        <td>Slower as you're creating them on the fly </td>
      </tr>
      <tr>
        <td>Table completeness</td>
        <td>The table is fully computed</td>
        <td>Table does not have to be fully computed</td>
    </tbody>
</table>

Personally, I prefer bottom-up dynamic programming. With top-down we have to think in terms of recurrences and trees, but with bottom-up we create a table and we answer:

> "What do I need to do here, in this exact row / colum, to calculate the value?"

When we answer this, we get the recurrence and we can write code that loops over our table annd answers this question for every square.

I'd suggest learning both top-down and bottom-up. Some problems are easier to solve with bottom-up, some are easier with top-down.

Take Fibonnaci sequence as an examplei. Everyone knows the Fibonnaci recurrence, so we don't need to work that out again.

In Python:

```python
def fib(n):
	if n <= 1:
		return n
	else:
		return fib(n - 1) + fib(n - 2)
```

In bottom-up, this becomes:

```python
def fib(n):
	dp = [i for i in range(0, n)]
	for i in range(2, n):
		dp[i] = dp(i - 1) + dp(i - 2)
	return dp[-1]

```

Notice lines 2 and 3:



```python {linenos=table,hl_lines=3,linenostart=1}
def fib(n):
	dp = [i for i in range(0, n)]
	for i in range(2, n):
		dp[i] = dp(i - 1) + dp(i - 2)
	return dp[-1]
```


On line 3, we do `range(2, n)`. Why do we start from 2?

It's because on line 3, we the first 2 items of our array is `0, 1`.

Remember our recursion tree from earlier?

![](/media/dp/tree.png)

Our basecases were:
* `[0] = 0`
* `[1] = 1`

**Going top-down, we stop at the basecases.

Going bottom-up, we start at the basecases.**

That's why our array starts with `[0, 1, ....]` and we start our range at `2`. This is a factor that will come into play in many bottom-up dynamic programming problems.

But with top-down, this becomes:

```python
from functools import cache

@cache
def fib(n):
	if n <= 1:
		return n
	else:
		return fib(n - 1) + fib(n - 2)
```

Python has a decorator function called `cache` from [functools](https://docs.python.org/3/library/functools.html) which memoises the inputs. That means we now have a top-down dynamic programming solution by adding `@cache` to our function.

If you're using a language that doesn't support caching decorators, you'd have to use a hashmap and check if `n` is in the hashmap before computation, like so:

```python
def fib(n, dp = {}):
		if n <= 1:
				return n
		else:
				dp[n] = fib(n - 1) + fib(n - 2)
		return dp[n]
```

Sometimes we use lists, where `dp[n]` corresponds to the `nth` element which is also the value. See [Bitmaps](https://en.wikipedia.org/wiki/Bitmap) for more.

Sometimes bottom-up is easier, sometimes top-down is easier.

# **check** ^^ 
the code might not be right for bottom-up


## How to Solve Problems using Dynamic Programming
![](/media/dp/undraw5.svg)

Now we have an understanding of what Dynamic programming is and how it generally works. Let's look at to create a Dynamic Programming solution to a problem. We're going to explore the process of Dynamic Programming using the *[Weighted Interval Scheduling Problem](https://courses.cs.washington.edu/courses/cse521/13wi/slides/06dp-sched.pdf)*.

Pretend you're the owner of a dry cleaner. You have *n* customers come in and give you clothes to clean. You can only clean one customer's pile of clothes (PoC) at a time. Each pile of clothes, *i*, must be cleaned at some pre-determined start time $s_i$ and some predetermined finish time $f_i$.

Each pile of clothes has an associated value, $v_i$, based on how important it is to your business. For example, some customers may pay more to have their clothes cleaned faster. Or some may be repeating customers and you want them to be happy. 

As the owner of this dry cleaners you must determine the optimal schedule of clothes that maximises the total value of this day. This problem is a re-wording of the *Weighted Interval scheduling problem*. 

You will now see 4 steps to solving a Dynamic Programming problem. Sometimes, you can skip a step. Sometimes, your problem is already well defined and you don't need to worry about the first few steps.

## Step 1. Write the Problem out
![](/media/dp/undraw6.svg)

Grab a piece of paper. Write out:

- What is the problem?
- What are the sub-problems?
- What would the solution roughly look like?

In the dry cleaner problem, let's put down into words the subproblems. What we want to determine is the maximum value schedule for each pile of clothes such that the clothes are sorted by start time.

Why sort by start time? Good question! We want to keep track of processes which are currently running. If we sort by finish time, it doesn't make much sense in our heads. We could have 2 with similar finish times, but different start times. Time moves in a linear fashion, from start to finish. If we have piles of clothes that start at 1 pm, we know to put them on when it reaches 1pm. If we have a pile of clothes that finishes at 3 pm, we might need to have put them on at 12 pm, but it's 1pm now. 

We can find the maximum value schedule for piles $n - 1$ through to n. And then for $n - 2$ through to n. And so on. By finding the solution to every single sub-problem, we can tackle the original problem itself. The maximum value schedule for piles 1 through *n*. Sub-problems can be used to solve the original problem, since they are smaller versions of the original problem.

With the interval scheduling problem, the only way we can solve it is by brute-forcing all subsets of the problem until we find an optimal one. What we're saying is that instead of brute-forcing one by one, we divide it up. We brute force from $n-1$ through to n. Then we do the same for $n - 2$ through to n. Finally, we have loads of smaller problems, which we can solve dynamically. We want to build the solutions to our sub-problems such that each sub-problem builds on the previous problems.

## 2. Mathematical Recurrences
![](/media/dp/undraw7.svg)

I know, mathematics sucks. If you'll bare with me here you'll find that this isn't that hard. [Mathematical recurrences](https://en.wikipedia.org/wiki/Recurrence_relation) are used to:

> Define the running time of a divide and conquer (dynamic programming) technique

Recurrences are also used to define problems. If it's difficult to turn your subproblems into maths, then it may be the wrong subproblem.

There are 2 steps to creating a mathematical recurrence:

### 1: Define the Base Case

Base cases are the smallest possible denomination of a problem.

When creating a recurrence, ask yourself these questions:

> "What decision do I make at step 0?"

It doesn't have to be 0. The base case is the smallest possible denomination of a problem. We saw this with the Fibonacci sequence. The base was:

- If n == 0 or n == 1, return 1

It's important to know where the base case lies, so we can create the recurrence. In our problem, we have one decision to make:

- Put that pile of clothes on to be washed

or

- Don’t wash that pile of clothes today

If n is 0, that is, if we have 0 PoC then we do nothing. Our base case is:

> if n == 0, return 0

### 2: What Decision Do I Make at Step n?

Now we know what the base case is, if we're at step n what do we do? For each pile of clothes that is compatible with the schedule so far. Compatible means that the start time is after the finish time of the pile of clothes currently being washed. The algorithm has 2 options:

1. Wash that pile of clothes
2. Don't wash that pile of clothes

We know what happens at the base case, and what happens else. We now need to find out what information the algorithm needs to go backwards (or forwards).

> "If my algorithm is at step i, what information would it need to decide what to do in step i+1?"

To decide between the two options, the algorithm needs to know the next compatible PoC (pile of clothes). The next compatible PoC for a given pile, p, is the PoC, n, such that $s_n$ (the start time for PoC n) happens after $f_p$ (the finish time for PoC p). The difference between $s_n$ and $f_p$ should be minimised.

In English, imagine we have one washing machine. We put in a pile of clothes at 13:00. Our next pile of clothes starts at 13:01. We can't open the washing machine and put in the one that starts at 13:00. Our next compatible pile of clothes is the one that starts after the finish time of the one currently being washed.

> "If my algorithm is at step i, what information did it need to decide what to do in step i-1?"

The algorithm needs to know about future decisions. The ones made for PoC *i* through *n* to decide whether to run or not run PoC *i-1*. 

Now that we’ve answered these questions, we’ve started to form a  recurring mathematical decision in our mind. If not, that’s also okay, it becomes easier to write recurrences as we get exposed to more problems.

Here’s our recurrence:

{{< math.inline >}}
<p>
$$
OPT(i) = \begin{cases} 0, \quad \text{If i = 0} \\ max{v_i + OPT(next[i]), OPT(i+1)},  \quad \text{if n > 1} \end{cases}\end{cases}
$$
</p>
{{< /math.inline >}}

Let's explore in detail what makes this mathematical recurrence. OPT(i) represents the maximum value schedule for PoC *i* through to *n* such that PoC is sorted by start times. OPT(i) is our subproblem from earlier.

We start with the base case. All recurrences need somewhere to stop. If we call OPT(0) we'll be returned with 0.

To determine the value of OPT(*i*), there are two options. We want to take the maximum of these options to meet our goal. Our goal is the *maximum value schedule* for all piles of clothes. Once we choose the option that gives the maximum result at step *i,* we memoize its value as OPT(*i*).

Mathematically, the two options - run or not run PoC *i*, are represented as:

$$v_i + OPT(next[n])$$

This represents the decision to run PoC *i*. It adds the value gained from PoC i to OPT(next[n]), where next[n] represents the next compatible pile of clothing following PoC *i*. When we add these two values together, we get the maximum value schedule from *i* through to n such that they are sorted by start time if *i* runs.

Sorted by start time here because next[n] is the one immediately after v_i, so by default, they are sorted by start time.

$$OPT(i + 1)$$

If we decide not to run *i*, our value is then OPT(i + 1). The value is not gained. OPT(i + 1) gives the maximum value schedule for i+1 through to n, such that they are sorted by start times. 

## 3. Determine the Dimensions of the Memoisation Array and the Direction in Which It Should Be Filled
![](/media/dp/undraw8.svg)

**Note:** This is for bottom-up dynamic programming, for top-down you do not need to do this.

The solution to our Dynamic Programming problem is OPT(1). We can write out the solution as the maximum value schedule for PoC 1 through n such that PoC is sorted by start time. This goes hand in hand with "maximum value schedule for PoC i through to n". 

From step 2:

$$OPT(1) = max(v_1 + OPT(next[1]), OPT(2))$$

Going back to our Fibonacci numbers earlier, our Dynamic Programming solution relied on the fact that the Fibonacci numbers for 0 through to n - 1 were already memoised. That is, to find F(5) we already memoised F(0), F(1), F(2), F(3), F(4). We want to do the same thing here.

The problem we have is figuring out how to fill out a memoisation table. In the scheduling problem, we know that OPT(1) relies on the solutions to OPT(2) and OPT(next[1]). PoC 2 and next[1] have start times after PoC 1 due to sorting. We need to fill our memoisation table from OPT(n) to OPT(1).

We can see our array is one dimensional, from 1 to n. But, if we couldn't see that we can work it out another way. The dimensions of the array are equal to the number and size of the variables on which OPT(x) relies. In our algorithm, we have OPT(*i*) - one variable, *i*. This means our array will be 1-dimensional and its size will be n, as there are n piles of clothes.

If we know that *n* = 5, then our memoisation array might look like this:

```python
memo = [0, OPT(1), OPT(2), OPT(3), OPT(4), OPT(5)]
```

0 is also the base case. memo[0] = 0, per our recurrence from earlier.

## 4. Coding Our Solution

When I am coding a Dynamic Programming solution, I like to read the recurrence and try to recreate it. Our first step is to initialise the array to size (n + 1). In Python, we don't need to do this. But you may need to do it if you're using a different language.

Our second step is to set the base case. 

To find the profit with the inclusion of job[i]. we need to find the latest job that doesn’t conflict with job[i].  The idea is to use Binary Search to find the latest non-conflicting job. I've copied the code from [here ](https://www.geeksforgeeks.org/weighted-job-scheduling-log-n-time/)but edited.

First, let's define what a "job" is. As we saw, a job consists of 3 things:

```python
    # Class to represent a job 
class Job: 
    def __init__(self, start, finish, profit): 
        self.start = start 
        self.finish = finish 
        self.profit = profit 
```

Start time, finish time, and the total profit (benefit) of running that job.

The next step we want to program is the schedule.

```python
# The main function that returns the maximum possible 
# profit from given array of jobs
def schedule(job): 
    # Sort jobs according to start time 
    job = sorted(job, key = lambda j: j.start) 

    # Create an array to store solutions of subproblems. table[i] 
    # stores the profit for jobs till arr[i] (including arr[i]) 
    n = len(job) 
    table = [0 for _ in range(n)] 

    table[0] = job[0].profit
```

Earlier, we learnt that the table is 1 dimensional. We sort the jobs by start time, create this empty table and set table[0] to be the profit of job[0]. Since we've sorted by start times, the first compatible job is always job[0].

Our next step is to fill in the entries using the recurrence we learnt earlier. To find the next compatible job, we're using Binary Search. In the full code posted later, it'll include this. For now, let's worry about understanding the algorithm.

If the next compatible job returns -1, that means that all jobs before the index, i, conflict with it (so cannot be used). `Inclprof` means we're including that item in the maximum value set. We then store it in table[i], so we can use this calculation again later.

```python
    # Fill entries in table[] using recursive property 
    for i in range(1, n): 

        # Find profit including the current job 
        inclProf = job[i].profit 
        l = binarySearch(job, i) 
        if (l != -1): 
            inclProf += table[l]; 

        # Store maximum of including and excluding 
        table[i] = max(inclProf, table[i - 1]) 
```

Our final step is then to return the profit of all items up to n-1.

```python
    	return table[n-1] 
```

The full code can be seen below:

```python
    # Python program for weighted job scheduling using Dynamic 
    # Programming and Binary Search 
    
    # Class to represent a job 
    class Job: 
    	def __init__(self, start, finish, profit): 
    		self.start = start 
    		self.finish = finish 
    		self.profit = profit 
    
    
    # A Binary Search based function to find the latest job 
    # (before current job) that doesn't conflict with current 
    # job. "index" is index of the current job. This function 
    # returns -1 if all jobs before index conflict with it. 
    def binarySearch(job, start_index): 
    	# https://en.wikipedia.org/wiki/Binary_search_algorithm
    
    	# Initialize 'lo' and 'hi' for Binary Search 
    	lo = 0
    	hi = start_index - 1
    
    	# Perform binary Search iteratively 
    	while lo <= hi: 
    		mid = (lo + hi) // 2
    		if job[mid].finish <= job[start_index].start: 
    			if job[mid + 1].finish <= job[start_index].start: 
    				lo = mid + 1
    			else: 
    				return mid 
    		else: 
    			hi = mid - 1
    	return -1
    
    # The main function that returns the maximum possible 
    # profit from given array of jobs 
    def schedule(job): 
    	# Sort jobs according to start time 
    	job = sorted(job, key = lambda j: j.start) 
    
    	# Create an array to store solutions of subproblems. table[i] 
    	# stores the profit for jobs till arr[i] (including arr[i]) 
    	n = len(job) 
    	table = [0 for _ in range(n)] 
    
    	table[0] = job[0].profit; 
    
    	# Fill entries in table[] using recursive property 
    	for i in range(1, n): 
    
    		# Find profit including the current job 
    		inclProf = job[i].profit 
    		l = binarySearch(job, i) 
    		if (l != -1): 
    			inclProf += table[l]; 
    
    		# Store maximum of including and excluding 
    		table[i] = max(inclProf, table[i - 1]) 
    
    	return table[n-1] 
    
    # Driver code to test above function 
    job = [Job(1, 2, 50), Job(3, 5, 20), 
    	Job(6, 19, 100), Job(2, 100, 200)] 
    print("Optimal profit is"), 
    print(schedule(job))
    
```

Congrats! 🥳 We've just written our first dynamic program!  Now that we’ve wet our feet,  let's walk through a different type of dynamic programming problem.


![](/media/dp/infographic.jpg)

---


# Knapsack Problem
![](/content/images/2019/06/undraw_travelers_qlt1.svg)
Imagine you are a criminal. Dastardly smart. You break into Bill Gates’s mansion. Wow, okay!?!? How many rooms is this? His washing machine room is larger than my entire house??? Ok, time to stop getting distracted. You brought a small bag with you. A knapsack - if you will. 

You can only fit so much into it. Let’s give this an arbitrary number. The bag will support weight 15, but no more. What we want to do is maximise how much money we'll make, $b$.

The greedy approach is to pick the item with the highest value which can fit into the bag. Let's try that. We're going to steal Bill Gates's TV. £4000? Nice. But his TV weighs 15. So... We leave with £4000.

```python
TV = (£4000, 15)
# (value, weight)
```

Bill Gates has a lot of watches. Let's say he has 2 watches. Each watch weighs 5 and each one is worth £2250. When we steal both, we get £4500 with a weight of 10.

```python
watch1 = (£2250, 5)
watch2 = (£2250, 5)
watch1 + watch2
>>> (£4500, 10)
```

In the greedy approach, we wouldn't choose these watches first. But to us as humans, it makes sense to go for smaller items which have higher values. The Greedy approach cannot optimally solve the {0,1} Knapsack problem. The {0, 1} means we either take the item whole item {1} or we don't {0}. However, Dynamic programming can optimally solve the {0, 1} knapsack problem.

The simple solution to this problem is to consider all the subsets of all items. For every single combination of Bill Gates's stuff, we calculate the total weight and value of this combination.

Only those with weight less than $W_{max}$ are considered. We then pick the combination which has the highest value. This is a disaster! How long would this take? Bill Gates's would come back home far before you're even 1/3rd of the way there! In [Big O](/big-o/), this algorithm takes $O(n^2)$ time.

You can see we already have a rough idea of the solution and what the problem is, without having to write it down in maths!

---

## Maths Behind {0, 1} Knapsack Problem
![](/content/images/2019/06/undraw_to_do_list_a49b.svg)
Imagine we had a listing of every single thing in Bill Gates's house. We stole it from some insurance papers. Now, think about the future. What is the optimal solution to this problem?

We have a subset, L, which is the optimal solution. L is a subset of S, the set containing all of Bill Gates's stuff.

Let's pick a random item, N. L either contains N or it doesn't. If it doesn't use N, the optimal solution for the problem is the same as ${1, 2, ..., N-1}$. This is assuming that Bill Gates's stuff is sorted by $value / weight$.

Suppose that the optimum of the original problem is not optimum of the sub-problem. if we have sub-optimum of the smaller problem then we have a contradiction - we should have an optimum of the whole problem.

If L contains N, then the optimal solution for the problem is the same as ${1, 2, 3, ..., N-1}$. We know the item is in, so L already contains N. To complete the computation we focus on the remaining items. We find the optimal solution to the remaining items.

But, we now have a new maximum allowed weight of $W_{max} - W_n$. If item N is contained in the solution, the total weight is now the max weight take away item N (which is already in the knapsack).

These are the 2 cases. Either item N is in the optimal solution or it isn't.

If the weight of item N is greater than $W_{max}$, then it cannot be included so case 1 is the only possibility.

To better define this recursive solution, let $S_k = {1, 2, ..., k}$ and $S_0 = \emptyset$

Let B[k, w] be the *maximum total benefit* obtained using a subset of $S_k$. Having total weight at most w.

Then we define B[0, w] = 0 for each $w \le W_{max}$.

Our desired solution is then B[n, $W_{max}$].

{{< math.inline >}}
<p>
$$
OPT(i) = \begin{cases} B[k - 1, w], \quad \text{If w < }w_k \\ max{B[k-1, w], b_k + B[k - 1, w - w_k]}, \ \quad \text{otherwise} \end{cases}
$$
</p>
{{< /math.inline >}}


### Tabulation of Knapsack Problem

Okay, pull out some pen and paper. No, really. Things are about to get confusing real fast. This memoisation table is 2-dimensional. We have these items:

```
(1, 1), (3, 4), (4, 5), (5, 7)
```

Where the tuples are `(weight, value)`.

We have 2 variables, so our array is 2-dimensional. The first dimension is from 0 to 7. Our second dimension is the values. 

And we want a weight of 7 with maximum benefit.

<table>
<tbody>
	<tr>
		<td> </td>
		<td>0</td>
		<td>1</td>
		<td>2</td>
		<td>3</td>
		<td>4</td>
		<td>5</td>
		<td>6</td>
		<td>7</td>
			
</tr>
<tr>
	<td>(1, 1)</td>
	<td></td>
	<td></td>
	<td></td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
</tr>
<tr>
	<td> (4, 3)</td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
</tr>
<tr>
	<td> (5, 4)</td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
</tr>
<tr>
	<td>(7, 5)</td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
</tr>
</tbody>
</table>

The weight is 7. We start counting at 0. We put each tuple on the left-hand side. Ok. Now to fill out the table!

<table >
<tbody>
<tr>
	<td> </td>
	<td>0</td>
	<td>1</td>
	<td>2</td>
	<td>3</td>
	<td>4</td>
	<td>5</td>
	<td>6</td>
	<td>7</td>
	
</tr>
<tr>
	<td>(1, 1)</td>
	<td>0</td>
	<td></td>
	<td></td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
</tr>
<tr>
	<td> (4, 3)</td>
	<td> 0</td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
</tr>
<tr>
	<td> (5, 4)</td>
	<td> 0</td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
</tr>
<tr>
	<td>(7, 5)</td>
	<td> 0</td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
</tr>
</tbody>
</table>


The columns are weight. At weight 0, we have a total weight of 0. At weight 1, we have a total weight of 1. Obvious, I know. But this is an important distinction to make which will be useful later on.

When our weight is 0, we can't carry anything no matter what. The total weight of everything at 0 is 0.

<table >
<tbody>
<tr>
	<td> </td>
	<td>0</td>
	<td>1</td>
	<td>2</td>
	<td>3</td>
	<td>4</td>
	<td>5</td>
	<td>6</td>
	<td>7</td>
	
</tr>
<tr>
	<td>(1, 1)</td>
	<td>0</td>
	<td>1</td>
	<td></td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
</tr>
<tr>
	<td> (4, 3)</td>
	<td> 0</td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
</tr>
<tr>
	<td> (5, 4)</td>
	<td> 0</td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
</tr>
<tr>
	<td>(7, 5)</td>
	<td> 0</td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
</tr>
</tbody>
</table>

If our total weight is 1, the best item we can take is (1, 1). As we go down through this array, we can take more items. At the row for (4, 3) we can either take (1, 1) or (4, 3). But for now, we can only take (1, 1). Our maximum benefit for this row then is 1. 

<table >
<tbody>
<tr>
	<td> </td>
	<td>0</td>
	<td>1</td>
	<td>2</td>
	<td>3</td>
	<td>4</td>
	<td>5</td>
	<td>6</td>
	<td>7</td>
	
</tr>
<tr>
	<td>(1, 1)</td>
	<td>0</td>
	<td>1</td>
	<td>1</td>
	<td>1</td>
	<td>1 </td>
	<td>1 </td>
	<td>1 </td>
	<td> 1</td>
</tr>
<tr>
	<td> (4, 3)</td>
	<td> 0</td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
</tr>
<tr>
	<td> (5, 4)</td>
	<td> 0</td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
</tr>
<tr>
	<td>(7, 5)</td>
	<td> 0</td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
</tr>
</tbody>
</table>

If our total weight is 2, the best we can do is 1. We only have 1 of each item. We cannot duplicate items. So no matter where we are in row 1, the absolute best we can do is (1, 1).

Let's start using (4, 3) now. If the total weight is 1, but the weight of (4, 3) is 3 we cannot take the item yet until we have a weight of at least 3.

<table >
<tbody>
<tr>
	<td> </td>
	<td>0</td>
	<td>1</td>
	<td>2</td>
	<td>3</td>
	<td>4</td>
	<td>5</td>
	<td>6</td>
	<td>7</td>
	
</tr>
<tr>
	<td>(1, 1)</td>
	<td>0</td>
	<td>1</td>
	<td>1</td>
	<td>1</td>
	<td>1 </td>
	<td>1 </td>
	<td>1 </td>
	<td> 1</td>
</tr>
<tr>
	<td> (4, 3)</td>
	<td> 0</td>
	<td> 1</td>
	<td> 1</td>
	<td></td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
</tr>
<tr>
	<td> (5, 4)</td>
	<td> 0</td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
</tr>
<tr>
	<td>(7, 5)</td>
	<td> 0</td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
</tr>
</tbody>
</table>

Now we have a weight of 3. Let's compare some things. We want to take the max of:

$$MAX(4 + T[0][0], 1)$$

If we're at 2, 3 we can either take the value from the last row or use the item on that row. We go up one row and count back 3 (since the weight of this item is 3).

Actually, the formula is whatever weight is remaining when we minus the weight of the item on that row. The weight of (4, 3) is 3 and we're at weight 3. $3 - 3 = 0$. Therefore, we're at `T[0][0]`. `T[previous row's number][current total weight - item weight]`.

$$MAX(4 + T[0][0], 1)$$

The 1 is because of the previous item. The max here is 4.

<table >
<tbody>
<tr>
	<td> </td>
	<td>0</td>
	<td>1</td>
	<td>2</td>
	<td>3</td>
	<td>4</td>
	<td>5</td>
	<td>6</td>
	<td>7</td>
	
</tr>
<tr>
	<td>(1, 1)</td>
	<td>0</td>
	<td>1</td>
	<td>1</td>
	<td>1</td>
	<td>1 </td>
	<td>1 </td>
	<td>1 </td>
	<td> 1</td>
</tr>
<tr>
	<td> (4, 3)</td>
	<td> 0</td>
	<td> 1</td>
	<td> 1</td>
	<td>4</td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
</tr>
<tr>
	<td> (5, 4)</td>
	<td> 0</td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
</tr>
<tr>
	<td>(7, 5)</td>
	<td> 0</td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
</tr>
</tbody>
</table>

$$max(4 + t[0][1], 1)$$

Total weight is 4, item weight is 3. 4 - 3 = 1. Previous row is 0. `t[0][1]`.

<table >
<tbody>
<tr>
	<td> </td>
	<td>0</td>
	<td>1</td>
	<td>2</td>
	<td>3</td>
	<td>4</td>
	<td>5</td>
	<td>6</td>
	<td>7</td>
	
</tr>
<tr>
	<td>(1, 1)</td>
	<td>0</td>
	<td>1</td>
	<td>1</td>
	<td>1</td>
	<td>1 </td>
	<td>1 </td>
	<td>1 </td>
	<td> 1</td>
</tr>
<tr>
	<td> (4, 3)</td>
	<td> 0</td>
	<td> 1</td>
	<td> 1</td>
	<td>4</td>
	<td>5</td>
	<td> </td>
	<td> </td>
	<td> </td>
</tr>
<tr>
	<td> (5, 4)</td>
	<td> 0</td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
</tr>
<tr>
	<td>(7, 5)</td>
	<td> 0</td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
</tr>
</tbody>
</table>

I won't bore you with the rest of this row, as nothing exciting happens. We have 2 items. And we've used both of them to make 5. Since there are no new items, the maximum value is 5. 

<table >
<tbody>
<tr>
	<td> </td>
	<td>0</td>
	<td>1</td>
	<td>2</td>
	<td>3</td>
	<td>4</td>
	<td>5</td>
	<td>6</td>
	<td>7</td>
	
</tr>
<tr>
	<td>(1, 1)</td>
	<td>0</td>
	<td>1</td>
	<td>1</td>
	<td>1</td>
	<td>1 </td>
	<td>1 </td>
	<td>1 </td>
	<td> 1</td>
</tr>
<tr>
	<td> (4, 3)</td>
	<td> 0</td>
	<td> 1</td>
	<td> 1</td>
	<td>4</td>
	<td>5</td>
	<td>5</td>
	<td>5</td>
	<td>5</td>
</tr>
<tr>
	<td> (5, 4)</td>
	<td> 0</td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
</tr>
<tr>
	<td>(7, 5)</td>
	<td> 0</td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
</tr>
</tbody>
</table>

Onto our next row:

<table >
<tbody>
<tr>
	<td> </td>
	<td>0</td>
	<td>1</td>
	<td>2</td>
	<td>3</td>
	<td>4</td>
	<td>5</td>
	<td>6</td>
	<td>7</td>
	
</tr>
<tr>
	<td>(1, 1)</td>
	<td>0</td>
	<td>1</td>
	<td>1</td>
	<td>1</td>
	<td>1 </td>
	<td>1 </td>
	<td>1 </td>
	<td> 1</td>
</tr>
<tr>
	<td> (4, 3)</td>
	<td> 0</td>
	<td> 1</td>
	<td> 1</td>
	<td>4</td>
	<td>5</td>
	<td>5</td>
	<td>5</td>
	<td>5</td>
</tr>
<tr>
	<td> (5, 4)</td>
	<td> 0</td>
	<td>1</td>
	<td>1 </td>
	<td>4 </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
</tr>
<tr>
	<td>(7, 5)</td>
	<td> 0</td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
</tr>
</tbody>
</table>

Here's a little secret. Our tuples are ordered by weight! That means that we can fill in the previous rows of data up to the next weight point. We know that 4 is already the maximum, so we can fill in the rest.. This is where memoisation comes into play! We already have the data, why bother re-calculating it?

We go up one row and head 4 steps back. That gives us:

$$max(4 + T[2][0], 5)$$.

<table >
<tbody>
<tr>
	<td> </td>
	<td>0</td>
	<td>1</td>
	<td>2</td>
	<td>3</td>
	<td>4</td>
	<td>5</td>
	<td>6</td>
	<td>7</td>
	
</tr>
<tr>
	<td>(1, 1)</td>
	<td>0</td>
	<td>1</td>
	<td>1</td>
	<td>1</td>
	<td>1 </td>
	<td>1 </td>
	<td>1 </td>
	<td> 1</td>
</tr>
<tr>
	<td> (4, 3)</td>
	<td> 0</td>
	<td> 1</td>
	<td> 1</td>
	<td>4</td>
	<td>5</td>
	<td>5</td>
	<td>5</td>
	<td>5</td>
</tr>
<tr>
	<td> (5, 4)</td>
	<td> 0</td>
	<td>1</td>
	<td>1 </td>
	<td>4 </td>
	<td>5</td>
	<td></td>
	<td></td>
	<td></td>
</tr>
<tr>
	<td>(7, 5)</td>
	<td> 0</td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
</tr>
</tbody>
</table>

Now we calculate it for total weight 5. 

$$max(5 + T[2][1], 5) = 6$$

<table >
<tbody>
<tr>
	<td> </td>
	<td>0</td>
	<td>1</td>
	<td>2</td>
	<td>3</td>
	<td>4</td>
	<td>5</td>
	<td>6</td>
	<td>7</td>
	
</tr>
<tr>
	<td>(1, 1)</td>
	<td>0</td>
	<td>1</td>
	<td>1</td>
	<td>1</td>
	<td>1 </td>
	<td>1 </td>
	<td>1 </td>
	<td> 1</td>
</tr>
<tr>
	<td> (4, 3)</td>
	<td> 0</td>
	<td> 1</td>
	<td> 1</td>
	<td>4</td>
	<td>5</td>
	<td>5</td>
	<td>5</td>
	<td>5</td>
</tr>
<tr>
	<td> (5, 4)</td>
	<td> 0</td>
	<td>1</td>
	<td>1 </td>
	<td>4 </td>
	<td>5</td>
	<td>6</td>
	<td></td>
	<td></td>
</tr>
<tr>
	<td>(7, 5)</td>
	<td> 0</td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
</tr>
</tbody>
</table>

We do the same thing again:

$$max(5 + T[2][2], 5) = 6$$
<table >
<tbody>
<tr>
	<td> </td>
	<td>0</td>
	<td>1</td>
	<td>2</td>
	<td>3</td>
	<td>4</td>
	<td>5</td>
	<td>6</td>
	<td>7</td>
	
</tr>
<tr>
	<td>(1, 1)</td>
	<td>0</td>
	<td>1</td>
	<td>1</td>
	<td>1</td>
	<td>1 </td>
	<td>1 </td>
	<td>1 </td>
	<td> 1</td>
</tr>
<tr>
	<td> (4, 3)</td>
	<td> 0</td>
	<td> 1</td>
	<td> 1</td>
	<td>4</td>
	<td>5</td>
	<td>5</td>
	<td>5</td>
	<td>5</td>
</tr>
<tr>
	<td> (5, 4)</td>
	<td> 0</td>
	<td>1</td>
	<td>1 </td>
	<td>4 </td>
	<td>5</td>
	<td>6</td>
	<td>6</td>
	<td></td>
</tr>
<tr>
	<td>(7, 5)</td>
	<td> 0</td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
</tr>
</tbody>
</table>
Now we have total weight 7. We choose the max of:

$$max(5 + T[2][3], 5) = max(5 + 4, 5) = 9$$
<table >
<tbody>
<tr>
	<td> </td>
	<td>0</td>
	<td>1</td>
	<td>2</td>
	<td>3</td>
	<td>4</td>
	<td>5</td>
	<td>6</td>
	<td>7</td>
	
</tr>
<tr>
	<td>(1, 1)</td>
	<td>0</td>
	<td>1</td>
	<td>1</td>
	<td>1</td>
	<td>1 </td>
	<td>1 </td>
	<td>1 </td>
	<td> 1</td>
</tr>
<tr>
	<td> (4, 3)</td>
	<td> 0</td>
	<td> 1</td>
	<td> 1</td>
	<td>4</td>
	<td>5</td>
	<td>5</td>
	<td>5</td>
	<td>5</td>
</tr>
<tr>
	<td> (5, 4)</td>
	<td> 0</td>
	<td>1</td>
	<td>1 </td>
	<td>4 </td>
	<td>5</td>
	<td>6</td>
	<td>6</td>
	<td>9</td>
</tr>
<tr>
	<td>(7, 5)</td>
	<td> 0</td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
	<td> </td>
</tr>
</tbody>
</table>
If we had total weight 7 and we had the 3 items (1, 1), (4, 3), (5, 4) the best we can do is 9.

Since our new item starts at weight 5, we can copy from the previous row until we get to weight 5.
<table >
<tbody>
<tr>
	<td> </td>
	<td>0</td>
	<td>1</td>
	<td>2</td>
	<td>3</td>
	<td>4</td>
	<td>5</td>
	<td>6</td>
	<td>7</td>
	
</tr>
<tr>
	<td>(1, 1)</td>
	<td>0</td>
	<td>1</td>
	<td>1</td>
	<td>1</td>
	<td>1 </td>
	<td>1 </td>
	<td>1 </td>
	<td> 1</td>
</tr>
<tr>
	<td> (4, 3)</td>
	<td> 0</td>
	<td> 1</td>
	<td> 1</td>
	<td>4</td>
	<td>5</td>
	<td>5</td>
	<td>5</td>
	<td>5</td>
</tr>
<tr>
	<td> (5, 4)</td>
	<td> 0</td>
	<td>1</td>
	<td>1 </td>
	<td>4 </td>
	<td>5</td>
	<td>6</td>
	<td>6</td>
	<td>9</td>
</tr>
<tr>
	<td>(7, 5)</td>
	<td> 0</td>
	<td> 1</td>
	<td> 1</td>
	<td> 4</td>
	<td>5</td>
	<td> </td>
	<td> </td>
	<td> </td>
</tr>
</tbody>
</table>
We then do another max.

Total weight - new item's weight. This is $5 - 5 = 0$. We want the previous row at position 0.

$$max(7 + T[3][0], 6)$$

The 6 comes from the best on the previous row for that total weight. 

$$max(7 + 0, 6) = 7$$
<table >
<tbody>
<tr>
	<td> </td>
	<td>0</td>
	<td>1</td>
	<td>2</td>
	<td>3</td>
	<td>4</td>
	<td>5</td>
	<td>6</td>
	<td>7</td>
	
</tr>
<tr>
	<td>(1, 1)</td>
	<td>0</td>
	<td>1</td>
	<td>1</td>
	<td>1</td>
	<td>1 </td>
	<td>1 </td>
	<td>1 </td>
	<td> 1</td>
</tr>
<tr>
	<td> (4, 3)</td>
	<td> 0</td>
	<td> 1</td>
	<td> 1</td>
	<td>4</td>
	<td>5</td>
	<td>5</td>
	<td>5</td>
	<td>5</td>
</tr>
<tr>
	<td> (5, 4)</td>
	<td> 0</td>
	<td>1</td>
	<td>1 </td>
	<td>4 </td>
	<td>5</td>
	<td>6</td>
	<td>6</td>
	<td>9</td>
</tr>
<tr>
	<td>(7, 5)</td>
	<td> 0</td>
	<td> 1</td>
	<td> 1</td>
	<td> 4</td>
	<td>5</td>
	<td>7</td>
	<td> </td>
	<td> </td>
</tr>
</tbody>
</table>
$$max(7 + T[3][1], 6) = 8$$
<table >
<tbody>
<tr>
	<td> </td>
	<td>0</td>
	<td>1</td>
	<td>2</td>
	<td>3</td>
	<td>4</td>
	<td>5</td>
	<td>6</td>
	<td>7</td>
	
</tr>
<tr>
	<td>(1, 1)</td>
	<td>0</td>
	<td>1</td>
	<td>1</td>
	<td>1</td>
	<td>1 </td>
	<td>1 </td>
	<td>1 </td>
	<td> 1</td>
</tr>
<tr>
	<td> (4, 3)</td>
	<td> 0</td>
	<td> 1</td>
	<td> 1</td>
	<td>4</td>
	<td>5</td>
	<td>5</td>
	<td>5</td>
	<td>5</td>
</tr>
<tr>
	<td> (5, 4)</td>
	<td> 0</td>
	<td>1</td>
	<td>1 </td>
	<td>4 </td>
	<td>5</td>
	<td>6</td>
	<td>6</td>
	<td>9</td>
</tr>
<tr>
	<td>(7, 5)</td>
	<td> 0</td>
	<td> 1</td>
	<td> 1</td>
	<td> 4</td>
	<td>5</td>
	<td>7</td>
	<td>8</td>
	<td> </td>
</tr>
</tbody>
</table>
$$max(7+T[3][2], 9) = 9$$
<table >
<tbody>
<tr>
	<td> </td>
	<td>0</td>
	<td>1</td>
	<td>2</td>
	<td>3</td>
	<td>4</td>
	<td>5</td>
	<td>6</td>
	<td>7</td>
	
</tr>
<tr>
	<td>(1, 1)</td>
	<td>0</td>
	<td>1</td>
	<td>1</td>
	<td>1</td>
	<td>1 </td>
	<td>1 </td>
	<td>1 </td>
	<td> 1</td>
</tr>
<tr>
	<td> (4, 3)</td>
	<td> 0</td>
	<td> 1</td>
	<td> 1</td>
	<td>4</td>
	<td>5</td>
	<td>5</td>
	<td>5</td>
	<td>5</td>
</tr>
<tr>
	<td> (5, 4)</td>
	<td> 0</td>
	<td>1</td>
	<td>1 </td>
	<td>4 </td>
	<td>5</td>
	<td>6</td>
	<td>6</td>
	<td>9</td>
</tr>
<tr>
	<td>(7, 5)</td>
	<td> 0</td>
	<td> 1</td>
	<td> 1</td>
	<td> 4</td>
	<td>5</td>
	<td>7</td>
	<td>8</td>
	<td>9</td>
</tr>
</tbody>
</table>
9 is the maximum value we can get by picking items from the set of items such that the total weight is $\le 7$.

### Finding the Optimal Set for {0, 1} Knapsack Problem Using Dynamic Programming

Now, what items do we actually pick for the optimal set? We start with this item:
<table >
<tbody>
<tr>
	<td> </td>
	<td>0</td>
	<td>1</td>
	<td>2</td>
	<td>3</td>
	<td>4</td>
	<td>5</td>
	<td>6</td>
	<td>7</td>
	
</tr>
<tr>
	<td>(1, 1)</td>
	<td>0</td>
	<td>1</td>
	<td>1</td>
	<td>1</td>
	<td>1 </td>
	<td>1 </td>
	<td>1 </td>
	<td> 1</td>
</tr>
<tr>
	<td> (4, 3)</td>
	<td> 0</td>
	<td> 1</td>
	<td> 1</td>
	<td>4</td>
	<td>5</td>
	<td>5</td>
	<td>5</td>
	<td>5</td>
</tr>
<tr>
	<td> (5, 4)</td>
	<td> 0</td>
	<td>1</td>
	<td>1 </td>
	<td>4 </td>
	<td>5</td>
	<td>6</td>
	<td>6</td>
	<td>9</td>
</tr>
<tr>
	<td>(7, 5)</td>
	<td> 0</td>
	<td> 1</td>
	<td> 1</td>
	<td> 4</td>
	<td>5</td>
	<td>7</td>
	<td>8</td>
	<td><mark><b>9</b></mark></td>
</tr>
</tbody>
</table>
We want to know where the 9 comes from. It's coming from the top because the number directly above 9 on the 4th row is 9. Since it's coming from the top, the item (7, 5) is not used in the optimal set.

Where does this 9 come from?
<table >
<tbody>
<tr>
	<td> </td>
	<td>0</td>
	<td>1</td>
	<td>2</td>
	<td>3</td>
	<td>4</td>
	<td>5</td>
	<td>6</td>
	<td>7</td>
	
</tr>
<tr>
	<td>(1, 1)</td>
	<td>0</td>
	<td>1</td>
	<td>1</td>
	<td>1</td>
	<td>1 </td>
	<td>1 </td>
	<td>1 </td>
	<td> 1</td>
</tr>
<tr>
	<td> (4, 3)</td>
	<td> 0</td>
	<td> 1</td>
	<td> 1</td>
	<td>4</td>
	<td>5</td>
	<td>5</td>
	<td>5</td>
	<td>5</td>
</tr>
<tr>
	<td> (5, 4)</td>
	<td> 0</td>
	<td>1</td>
	<td>1 </td>
	<td>4 </td>
	<td>5</td>
	<td>6</td>
	<td>6</td>
	<td><mark><b>9</td>
</tr>
<tr>
	<td>(7, 5)</td>
	<td> 0</td>
	<td> 1</td>
	<td> 1</td>
	<td> 4</td>
	<td>5</td>
	<td>7</td>
	<td>8</td>
	<td>9</td>
</tr>
</tbody>
</table>
This 9 is not coming from the row above it. **Item (5, 4) must be in the optimal set.**

We now go up one row, and go back 4 steps. 4 steps because the item, (5, 4), has weight 4.
<table >
<tbody>
<tr>
	<td> </td>
	<td>0</td>
	<td>1</td>
	<td>2</td>
	<td>3</td>
	<td>4</td>
	<td>5</td>
	<td>6</td>
	<td>7</td>
	
</tr>
<tr>
	<td>(1, 1)</td>
	<td>0</td>
	<td>1</td>
	<td>1</td>
	<td>1</td>
	<td>1 </td>
	<td>1 </td>
	<td>1 </td>
	<td> 1</td>
</tr>
<tr>
	<td> (4, 3)</td>
	<td> 0</td>
	<td> 1</td>
	<td> 1</td>
	<td><mark><b>4</td>
	<td>5</td>
	<td>5</td>
	<td>5</td>
	<td>5</td>
</tr>
<tr>
	<td> (5, 4)</td>
	<td> 0</td>
	<td>1</td>
	<td>1 </td>
	<td>4 </td>
	<td>5</td>
	<td>6</td>
	<td>6</td>
	<td>9</td>
</tr>
<tr>
	<td>(7, 5)</td>
	<td> 0</td>
	<td> 1</td>
	<td> 1</td>
	<td> 4</td>
	<td>5</td>
	<td>7</td>
	<td>8</td>
	<td>9</td>
</tr>
</tbody>
</table>
4 does not come from the row above. The item (4, 3) must be in the optimal set.

The weight of item (4, 3) is 3. We go up and we go back 3 steps and reach:
<table >
<tbody>
<tr>
	<td> </td>
	<td>0</td>
	<td>1</td>
	<td>2</td>
	<td>3</td>
	<td>4</td>
	<td>5</td>
	<td>6</td>
	<td>7</td>
	
</tr>
<tr>
	<td>(1, 1)</td>
	<td><mark><b>0</td>
	<td>1</td>
	<td>1</td>
	<td>1</td>
	<td>1 </td>
	<td>1 </td>
	<td>1 </td>
	<td> 1</td>
</tr>
<tr>
	<td> (4, 3)</td>
	<td> 0</td>
	<td> 1</td>
	<td> 1</td>
	<td>4</td>
	<td>5</td>
	<td>5</td>
	<td>5</td>
	<td>5</td>
</tr>
<tr>
	<td> (5, 4)</td>
	<td> 0</td>
	<td>1</td>
	<td>1 </td>
	<td>4 </td>
	<td>5</td>
	<td>6</td>
	<td>6</td>
	<td>9</td>
</tr>
<tr>
	<td>(7, 5)</td>
	<td> 0</td>
	<td> 1</td>
	<td> 1</td>
	<td> 4</td>
	<td>5</td>
	<td>7</td>
	<td>8</td>
	<td>9</td>
</tr>
</tbody>
</table>
As soon as we reach a point where the weight is 0, we're done. Our two selected items are (5, 4) and (4, 3). The total weight is 7 and our total benefit is 9. We add the two tuples together to find this out. 

Let's begin coding this. 

---

### Coding {0, 1} Knapsack Problem in Dynamic Programming With Python

Now we know how it works, and we've derived the recurrence for it - it shouldn't be too hard to code it. If our two-dimensional array is i (row) and j (column) then we have:

```python
if j < wt[i]:
```

If our weight j is less than the weight of item i (i does not contribute to j) then:

```python
if j < wt[i]:
	T[i][j] = T[i - 1][j]
else:
	# weight of i >= j
	T[i][j] = max(val[i] + t[i - 1][j-wt(i), t[i-1][j])
	# previous row, subtracting the weight of the item from the total weight or without including ths item
```

This is what the core heart of the program does. I've copied some code from [here](https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/) to help explain this. I'm not going to explain this code much, as there isn't much more to it than what I've already explained. If you're confused by it, leave a comment below or email me 😁

```python
# Returns the maximum value that can be put in a knapsack of 
# capacity W 
def knapSack(W , wt , val , n): 
	
	# Base Case 
	if n == 0 or W == 0: 
		return 0
	
	# If weight of the nth item is more than Knapsack of capacity 
	# W, then this item cannot be included in the optimal solution 
	if (wt[n-1] > W): 
		return knapSack(W , wt , val , n-1) 
	
	# return the maximum of two cases: 
	# (1) nth item included 
	# (2) not included 
	else: 
		return max(val[n-1] + knapSack(W-wt[n-1] , wt , val , n-1), 
					knapSack(W , wt , val , n-1)) 
	
	
# To test above function 
val = [60, 100, 120] 
wt = [10, 20, 30] 
W = 50
n = len(val) 
print(knapSack(W , wt , val , n))
# output 220
```

---

# Problems

Let's go thrugh a bunch of Dyanmic Programming problems to understand how it works.

There are 5 main patterns to dynamic programming. If you learn these patterns, you will be able to solve 99% of all problems.

This [Leetcode post](https://leetcode.com/discuss/general-discussion/458695/dynamic-programming-patterns) explains what the patterns are and how to use them. Within this section I will use these patterns and explain one core problem from each. 

### Minimum (Maximum) Path to Reach a Target

We know we have this type of problem when the question asks:

> "Find the maximum/minimum cost / path / sum to reach the target"

The solution to this will always be to choose the minimum/maximum path among all possible paths before the current state, then add the values for the curent state.

The optimal solution generally looks like:

```python
for i in range(0, target):
	for y in range(0, len(ways)):
		if ways[j] <= i:
			dp[i] = min(dp[i], dp[i - ways[j]] + cost)
```

This is a bottom-up solution. We have an array/table `dp`, we have a `target` and we want to calculate the minimum path to the target. 

`ways` is every possible way to get to the current state.

We've already seen a solution to a similar problem -- Fibonacci sequence!

#### Minimum Cost Climbing Stairs

Let's look at a similar problem, [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs)

> On a staircase, the i-th step has some non-negative cost cost[i] assigned (0 indexed).
>
> Once you pay the cost, you can either climb one or two steps. You need to find minimum cost to reach the top of the floor, and you can either start from the step with index 0, or the step with index 1.

```
Input: cost = [10, 15, 20]
Output: 15
Explanation: Cheapest is start on cost[1], pay that cost and go to the top.
```

Given a `cost` array, find the minimum cost.

##### Top-down

Let's look at a top-down approach.

Unlike Fibonacci, the first 2 steps pre-calculated for us. As we can either walk one step, or two steps.

We can choose to start on step 1, or step 2 -- meaning we don't pay a cost. Thus we do not need to calculate the cost for step 2.

Our base case is then:


```python
def min_cost(costs, n):
		if n <= 1:
				return n

```

Because:
* `[0] = 0`
* `[1] = 1`



Imagine we are on the 3rd step. We do not care about any further steps. 

What is our action at the third step? This is the most important part of Dynamic Programming. **We only care about what one step is doing, and all steps follow the same pattern and we recurse to get the answer.**

Our choices at step 3 are:
* 3 (current step number) + step 2
* 3 + step 1

Remember, we can start on either step 1 or 2 and can move forward 1 step or 2. 

And we want to calculate the minimum cost to get to the current step. To calculate the minimum to get to the current step, we need to calculat the minimum to get to the steps before us and so on.

Therefore our recurrence relation is:

```python
# cost of step i + the minimum cost to get to step i - 1 or step i -2
cost[i] + min(min_cost(i - 1), min_cost(i - 2))
```

We start at `n` steps, and we calculate the cost of `n` by calculating the cost of `n - 1`. and then `n - 2` and then `n - 3` and so on.

_if_ we solve the subproblem at `n`, we only need to pass it to recursion to solve all of our subproblems.

Our total recursive code looks like:

```python
def main(cost):
		n = len(cost)
		# Because we can reach the top of the stairs by either 1 step or 2 steps
		return min(min_cost(cost, n - 1), min_cost(cost, n - 2))

def min_cost(cost, n):
		if n <= 1:
				return cost[n]
		return cost[n] + min(min_cost(cost, n - 1), min_cost(cost, n - 2))
```

# Check the above ********************************************************************************

Recurrence is all about:
* Solving one small subproblem.
* Handing the rest of the world off to recursion.

Once we solve one small subproblem, we don't need to do any more work -- the recursion does it all for us.

To memoise this in Python:

```python

from functools import cache

def main(cost):
		n = len(cost)
		# Because we can reach the top of the stairs by either 1 step or 2 steps
		return min(min_cost(cost, n - 1), min_cost(cost, n - 2))

@cache
def min_cost(cost, n):
		if n <= 1:
				return cost[n]
		return cost[n] + min(min_cost(cost, n - 1), min_cost(cost, n - 2))
```


##### Bottom-Up

Now let's convert out top-down memoisation approach to a bottom-up approach. 

When we finish our top-down approach, we have a memoised array of the answers. When we start from bottom-up, we start with that array already but the values aren't computed yet.

Bottom-up is the exact opposite of top-down, just imagine you're at the bottom of the execution tree and you're working upwards.

First, we need an array.

```python
def main(cost):
		n = len(cost)
		dp = [float("inf")] * n
```

This makes an array of size `n` where each value is infinity. In Python, we can't make an array of sizie `n` without initialising the values. We use `float("inf")` for minima problems, and `float("-inf")` for maxima problems.

In top-down, we started at `n` and our answer was at `0` (well, it was the result of all the nodes that have hit the base case). 

In bottom-up, we start at `0` and our answer is the last element in the array.


![](/content/images/2019/06/image-8.png)

Instead of starting at the top of the tree, in bottom-up we start at the basecases.

Since we start at the start of the array, the basecases go there too.

```python
def main(cost):
		n = len(cost)
		dp = [float("inf")] * n
		dp[0] = cost[0]
		dp[1] = cost[1]
```

Now we need to loop through all of our values.

Our loop will then look like:

We loop through the `cost` array from 2:

```python
def main(cost):
		n = len(cost)
		dp = [float("inf")] * n
		for i in range(2, n):
				
```

Remember:
* Top-down we start at the top and end at the basecases.
* Bottom-up we start from the basecases and end at the top.

Our basecases start at index 2.

Now, the recurrence. We've already calculated our recurrence from earlier. All we need to do is insert it into the `dp` array.

```python
def main(cost):
		n = len(cost)
		dp = [float("inf")] * n
		for i in range(2, n):
				dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
				
```

Since we have already calculated the previous values, we do not need to use any recursion here. However, the recurrence is being used to calculate the values

Remember our `main` function from the top-down approach:

```python
def main(cost):
		n = len(cost)
		# Because we can reach the top of the stairs by either 1 step or 2 steps
		return min(min_cost(cost, n - 1), min_cost(cost, n - 2))
```

At the end of the stairs, we can either finish it by climing 2 steps or 1.

We need to do the same here.

```python
def main(cost):
		n = len(cost)
		dp = [float("inf")] * n
		for i in range(2, n):
				dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
		return min(dp[n - 1], dp[n - 2])
```

We've now turned a recursive approach into top-down dynamic programming, and flipped that into bottom-up dynamic programming.

If you remember one thing, it's this:

> The most important part about solving any dynamic programming problem is to solve a single subproblem.

#### Coin Change

[Leetcode Problem](https://leetcode.com/problems/coin-change/).

Our first thought when seeing "Make Change" is [Greedy](https://skerritt.blog/greedy-algorithms/). But, that doesn't always work.

Given the coins:

```
[1, 15, 25]
```

And being told to make change for `30`, our Greedy algorithm does:

```
5x 1 pence coins
1x 25 pence coin
```

This works so long as:
* The first coin is $1$.
* Our second coin is $\frac{n}{2}$.
* Our final coin is between our second coin and the change amount.

To make change for $30$, that means if our coins were:
* 1
* 15
* 25 (between 15 and 30)

It would fail. It'd also fail if our coin was 16. So long as our largest coin is larger than the most optimal 2nd coin, we can never pick the 2nd coin in Greedy so it will always fail.

In the case it does work, it's called a [Canonical Coin System](https://graal.ens-lyon.fr/~abenoit/algo09/coins2.pdf).

Dynamic Programming allows us to solve this problem efficiently.

Given a sum, `change`, we want to find the optimal path that minimises the amount of coins we use.

We're going to use bottom-up here, as it's much easier than top-down. Some problems are easieir with bottom-up, some are easier with top-down. This is a bottom-up problem.

We can tell it is because we have to think in multiple dimensions, and we know it's multiple dimensions because of the recurrence.

Let's take a small look at it.

For every amount up to 15 we want to calculate:
* The smallest amount of coins up to that point.

This means our code, iin iterative, looks roughly like:

```python
for i in range(0, 15):
		for y in coins:
				# do stuff
```

For each level of the recurrence, we need to loop through all the coins to find the ones that optimally fit. 

In a top-down approach, our recurrence function would need to have a `for` loop which iterates over the coins and works out the smallest possible denomination of coins for that amount.

Essentially, our top-down would look like:

```python
def top_down(amount, coins):
		for i in coins:
				top_down(amount, i)
```

Which gets messy, fast. It's easier for us to debug code if we used bottom-up here. Here's what the top-down approach looks like in C++ from [here](https://www.bogotobogo.com/Algorithms/dynamic_programming.php):

```cpp
int CoinChange(int amount, int d[], int size)
{
    if(amount <= 0) return 0;
	    int min_coins =(int)INT_MAX;

		for(int i = 0; i < size; i++) {
				if(d[i] <= amount) 
						    min_coins = min(min_coins, CoinChange(amount-d[i], d, size) + 1);
							    
		}
		    return min_coins;
			
}
```

We have to:
* Initialise min_coins each iteration.
* Loop through all coins each iteration.
* Calculate new min coins each iteration, which recursively calls the function again.

Bottom-up is much simpler, as we only need 2 for loops which is similar to our original bruteforce method, except memoised.

##### Bottom-Up Coin Change

Earlier I said that this was a "multi-dimensionsal" problem. To me, that means more than a 1-dimensional array. Let's explore _why_ I said this.

We know Dynamic Programming is Fancy Bruteforcing™, which means we want to calculate the minimum amount of coins for the change of 1, 2, 3, 4, ...., n where n is the amount we want to change.

For each amount, we want to loop through all of the coins. That means for every amount X, there is Y rows for each of the coins.

|   |0p | 1p | 2p | 3p |
|  ---- | ---- | ----- | ----- | ---- |  
| 1 pence coin | 0 | 1 | 2 | 3 |
| 2 pence coin| 0 | 1 | 1| 2 | 

This means our Dynamic Programming Table would be `X, Y` dimensions.

In the above case, we have 2 coins and 4 amounts we want to make change for. That means our Dynamic Programming table is `4, 2`.

But! We only care about the minimum amount of coins to make change, not all the possible ways. This means we do not need to have a 2-dimensional table with the Y column.

So for example, given the change `10` and the coins `1, 5, 10` our table would report we can make change with:
* 1x10p coin.
* 2x5p coins.
* 10x1p coins.

We don't care about the 5p or the 1p, we only care about the minimum amount which is 1x10p coin. If we cared about the total amount of ways to make change, we'd have to us a 2d array. 


Using a smaller example:

```
coins = [1, 2, 5]
change = 11
```

![an array of size 12 with boxes labelled from 0 to 11](/media/dp/coin-bottom-1.svg)

We need to build the array before we calculate. For bottom-up, we are calculating the minimum amount of coins for each amount up to the target amount.

We start at 0 and go up to target.

Therefore our array is size `amount + 1`

```python
class Solution:
	def coinChange(self, coins: List[int], amount: int) -> int: 

	# Generate the bottom-up array which is amount + 1
	dp = [float("inf")] * (amount + 1)

	# We can make 0 change with 0 coins
	dp[0] = 0
```

We start with our DP array and our basecase.

We chose infinity because Python doesn't allow us to use empty values and any value will always be less than infinity.

* Minimum == infinity.
* Maximum == -infinity.

For max problems, use negative infinity. Otherwise, positive infinity.

![Every item in the array is now "infinite" for it has infinite value.](/media/dp/bottom-coin2.svg)

We want to include 0 coins and 0 amount because of the [powerset](https://skerritt.blog/sets/#-power-set).

The most important question for all dynamic programming problems is:
> What is the solution to the subproblem?

Each of these cells is asking us a question, and we know previious answers to that question. 

For cell 0, the question is:

> How many coins do we need to make 0 change?

The answer is 0, this will serve as our basecase. We cannot make any coins with 0.

![](/media/dp/bottom-coin3.svg)

Our next step is **discovering the recurrence**.

The problem states that a single pence coin `1` will always be in the coins array.

That means we can always make any amount with a bunch of 1 pence coins.

$$60 \ change / 1p = 60 \ coins$$

We also have other values of coins. For example, to make change for `5` the 5 pence coin would be the minimal amount needed.

Our first thought is that we can calculcate the minimum amount of coins to be the nearest whole coin with additional 1's with this algorithm:

1. Given an amount, X.
2. Find the maximum coin that is less than X.
3. Use that coin, and then calculate:

$$X - coin$$

4. $X - coin$ is how many 1 pence coins we need.

However, this algorithm won't work. 

Given the change 10, our algorithm would select 6 coins (1x 5 pence coin, 5x 1 pence coins). _How_ do we make it work for all amounts?

We have an array:

```
[x, x, x, x, 1, x, x, x, x, Y]
```

![](/media/dp/bottom-coin4.svg)

We can change 1x5 pence coin for the amount `5`, so `[5] = 1`. For the last amount, `Y`, which is 10 we can change 2 coins.

We calculate this by performing `10 - coin`. Eventually we hit `10 - 5` which takes us to the 5th element which is 1 coin. 

$$10 - 1 = 9$$
$$10 - 2 = 8$$
$$10 - 5 = 5$$

We find the maximum coin that can fit in the amount.

Because we take away the denomination of the coin from our current amount, we find out the optimal minimum number of coins the last time we effectively used that coin.

For our example:

![](/media/dp/bottom-coin5.svg)

We take our highest coin, $5$, away from our amount $10$.

$$10 - 5 = 5$$.

We then go to position 5, which is amount 5.

![](/media/dp/bottom-coin6.svg)

This comes out to `1`, so we add `+ 1` to our counter meaning at spot `10` we have `2 coins`.

![](/media/dp/bottom-coin7.svg)

When we reach amount 15, we look back at amount 10 and see it took 2 coins to make that. So we say amount 15 takes 3 coins.

![](/media/dp/bottom-coin8.svg)

This method lets us use the most optimal amount of whole coins each time.

Unforunately if we only have 1 pence coins to change, this algorithm doesn't work. Because at position 5 it'd be 5, which means position 10 would be 6 coins which is not true. It'd be 10 coins as it's amount 10 with only 1 pence coins.

This means our recurrence is:

> Calculate the minimum of:
> * The amount to be changed in 1 pence coins
> * The minimum amount of times the whole coin was used for the previous amount + 1.

In code, this algorithm is:

```python
dp[to_make_change] = min(dp[to_make_change], dp[to_make_change - coin] + 1)
```

Where `to_make_chage` is the amount to make change for at step `y`, and `coin` is the current coin being used in the iteration.

So we know:
* The dimensions of our DP Array.
* The recurrence.
* That we need to loop over the coins.

We'll quickly build our program.


```python
class Solution:
	def coinChange(self, coins: List[int], amount: int) -> int: 

	# Generate the bottom-up array which is amount + 1
	dp = [float("inf")] * (amount + 1)

	# We can make 0 change with 0 coins
	dp[0] = 0

	# for every possible amount up to our amount + 1
	for y in range(1, amount + 1):
		# for every possible coin
		for coin in coins:
```

We start off by building the DP array and setting the basecase.

Then we loop through all possible amounts and all coins.

```python
class Solution:
def coinChange(self, coins: List[int], amount: int) -> int: 

# Generate the bottom-up array which is amount + 1
dp = [float("inf")] * (amount + 1)

# We can make 0 change with 0 coins
dp[0] = 0

# for every possible amount up to our amount + 1
for y in range(1, amount + 1):
	# for every possible coin
	for coin in coins:
		# If our coin doesn't fit, go to the next loop
		if y - coin < 0:
			continue
```

If our coin is 50, and our amount is 5, we get $5 - 50 = -45$. Negative change is impossible, so we tell our loop to skip this combination.

```python
class Solution:
def coinChange(self, coins: List[int], amount: int) -> int: 

# Generate the bottom-up array which is amount + 1
dp = [float("inf")] * (amount + 1)

# We can make 0 change with 0 coins
dp[0] = 0

# for every possible amount up to our amount + 1
for y in range(1, amount + 1):
	# for every possible coin
	for coin in coins:
		# If our coin doesn't fit, go to the next loop
		if y - coin < 0:
			continue

	# Else calculate what the minimum amount of coins 
	# for that amount is
	dp[y] = min(dp[y], dp[y - coin] + 1)
```

If we didn't skip it, we calculate the minimum using our recurrence from earlier.

```python
class solution:
	def coinchange(self, coins: list[int], amount: int) -> int: 

	# generate the bottom-up array which is amount + 1
	dp = [float("inf")] * (amount + 1)

	# we can make 0 change with 0 coins
	dp[0] = 0

	# for every possible amount up to our amount + 1
	for y in range(1, amount + 1):
		# for every possible coin
		for coin in coins:
			# if our coin doesn't fit, go to the next loop
			if y - coin < 0:
				continue

		# else calculate what the minimum amount of coins 
		# for that amount is
		dp[y] = min(dp[y], dp[y - coin] + 1)

	# if we couldn't make change, return -1
	if dp[-1] == float("inf"):
		return -1

	return dp[-1]

```

And finally, we return -1 if we couldn't make change, otherwise we return the last element of the DP array which is the answer.


### Distinct Ways

Given a target, find the number of distinct ways to reach that target.

To do so, we need to sum all the possible ways to reach the state.

We've seen this pattern a lot already. Let's look at Fibonacci numbers.

$$[1, 2, x]$$

We calculate x as:

$$list[-1] + list[-2]$$.

Now let's say there are multiple ways to reach the number 3. For example, if we're on a staircase and can go up either one step or two steps.

We calculate this with:

`How many steps it takes to get to list[-2] and how many steps it takes to get to list[-1]`

This is the min cost climbing stair problem from earlier, and is actually a great example of this small paradigm!

Since we've already gone over the cliimbing stairs problem, let's go over a different one.

#### Unique Paths

This [problem](https://leetcode.com/problems/unique-paths/) iis a more interesting one we can play with.

The first thing you'll notice is that we're no longer in a 1-dimensional world but rather a 2-dimensional world.

![](/media/dp/robot_maze.svg)

The first step in any dynamic programming problem is understanding the basecase.

The basecase of these problems are the first squares we can touch. In this case, our robot can:
* Move down.
* Move right.

Therefore our basecase is to the right and down from the robot.

From the robots starting point, there is only 1 unique path to either the square below it or to the left of it.

![](/media/dp/robot_maze2.svg)


To create a 2-dimensional DP array, we need 2 for loops. I like using [list comprehensions](https://skerritt.blog/functional/#-list-comprehensions) for this.

```python
def uniquePaths(m, n):
    dp = [[1 for x in range(n)] for y in range(m)]
```

This creates an n by n grid where all values are `1`.

This is our basecase. At the top-left the robot can only move down or right, which results in 1 unique path. We fill in all the squares with 1 because it can never be less than 1.

![](/media/dp/robot_maze3.svg)


```python
def uniquePaths(m, n):
    dp = [[1 for x in range(n)] for y in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            # do work
```

Our next step is looping over the grid itself. The robot starts in `[0, 0]` so we loop starting from there.

The robot can only move left or right, and we want to calculate all the unique paths possible.

![](/media/dp/robot_maze4.svg)

That means our recurrence is:
* Calculate all the unique paths it takes to get to the below square.
* Calculate all the unique paths it takes to get to the right square.

We do this by adding the previous square we were just on to the current square. 

And because we want to calculate them in total, we add both the right and the down square. Let's see this in action.

![](/media/dp/robot_maze5.svg)

Imagine our robot went right and down, or down and right. That means there are 2 ways to reach that point.

That means:

```
dp[1][1] = dp[1 - 1][1] + dp[1][1 - 1] = dp[0][1] + dp[1][0] = 1 + 1 = 2
```

We calculate how many unique paths there are to all unique squares that will let us reach this current square.

We know we can only go right or down, therefore we calculate with the above square or left square (as we have just traversed and want to look backwards).

![](/media/dp/robot_maze6.svg)

This is our recurrence, and so our code is now:

```python
def uniquePaths(m, n):
    dp = [[1 for x in range(n)] for y in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
```

What's important to note here is that we took a very small example and tried to find how it could be applied generally. Instead of using specific indices, we loop over it and use those variables.

Now we want to calculate our final sum, which is at `[-1][-1]`. We can do this with:

```python
def uniquePaths(m, n):
    dp = [[1 for x in range(n)] for y in range(m)]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
		return dp[-1][-1]
```

### Merging Intervals

Given a set of numbers, find an optimal solution for a problem considering the current number, the left side and the right side.

We approach it like:
```py
dp[i][j] = dp[i][k] + result[k] + dp[k+1][j]
```

Now, this sounds confusing so let's get right into an example.



### DP on Strings

This pattern is harder to spot, but usually involves:
> "Given two strings, return some result based on them"

These strings are often small, because larger strings result in larger DP tables which results in more memory required.

DP on Strings is often solved in $O(n^2)$ as there are two strings we are computing over.

#### Longest Common Subsequence

Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

If there is no common subsequence, return 0.

Let's look at some examples to get our head around it.

```
"A B C D G H"
"A E D F H R"
```

They both share A, D, and H. So the longest common subsequence is `ADH` which has length 3. So we return 3.

```
"A G G T A B"
"G X T X A B"
```

They share `GTAB` which has length 4.

Subsequences don't have to be contiguous, so for example:

```
"A B C"
"C P B"
```

String 2 starts with C, and string 1 ends with C. We still include them as subsequences do not have to be contiguous.

This raises some questions:
* How do we compute this without being contiguous?
* How do we make sure we don't use the same letter twice?

I find drawing execution trees helps.

![](/media/dp/Recursion_tree_common_sub.svg)

Here we only care about the last character. We want to cut this up into subproblems. 

These characters are the same. That means we have a lengthing of our longest common subsequence by 1.

![](/media/dp/Recursion_tree_common_sub1.svg)

The answer os `lcs("aab", "azb")` is 1 + the answer to `lcs("aa", "az")`.

NNow what is the answer to this subproblem? Our eyes go to the last character. 

![](/media/dp/Recursion_tree_common_sub2.svg)

They are not the same. So our problem is now:
* If we delete either of these characters, which subproblem will yield us a better longer subsequence?

![](/media/dp/Recursion_tree_common_sub3.svg)

At this point we calculate the maximum given by these 2 recurrences. Whichever of these yields a bigger common subsequence we will take that as the longest common subsequence given the subproblem `lcs("aa", "az")`.

When we have mismatching characters like "a" and "z" we have to remove one from each and compute the maximum.

But, our maximums don't match either.

```max(lcs("a", "az"), lcs("aa", "a"))```

For our first problem `lcs("a", "az")` we have to rip "a" from the left-hand side or "z" from the right-hand side.

![](/media/dp/Recursion_tree_common_sub4.svg)

And now for the left-hand side, they match `lcs("aa", "a")` so we do 1+ removing these characters.


![](/media/dp/Recursion_tree_common_sub5.svg)

When we see an empty string, we can't have anything in common with an empty string. Because nothing vs something has nothing in common.

SO we'll evaluate `lcs("", "az")` to 0.

![](/media/dp/Recursion_tree_common_sub6.svg)

Now we compare `lcs("a", "a")`. It's a match so we do 1 + removing both of them.

![](/media/dp/Recursion_tree_common_sub7.svg)

We now compare empty string vs an empty string. Nothing is in common so we return 0 from that recursive call.

![](/media/dp/Recursion_tree_common_sub8.svg)

The longest common subsequence between "a" and "a" is 1. 

![](/media/dp/Recursion_tree_common_sub9.svg)

The maximum of `max(0, 1)` is 1. So we return 1.

We drilled down into sub-problems until we got to a solid answer, and now we ride it back all the way up to the top with the solutions to these sub-problems.

![](/media/dp/Recursion_tree_common_sub10.svg)

Now the first half of the `max` is computed. We compute the 2nd half.

![](/media/dp/Recursion_tree_common_sub11.svg)

Skipping a step, we do 1 + 0 (as the maximum substring of empty string & empty string is 0). We evaluate it to 1. 

![](/media/dp/Recursion_tree_common_sub12.svg)

Our competition is finished. We evaluate `max(1, 1)` from both of our sub-problems.

![](/media/dp/Recursion_tree_common_sub13.svg)

Our competition is over, so we calculate $1 + 1$. Which is 2.

![](/media/dp/Recursion_tree_common_sub14.svg)

Now our output is 2. The answer to the overarching subproblem is 2.

Now we'll build a bottom-up dynamic programming table.

<table>
<thead>
  <tr>
    <th></th>
    <th>""</th>
    <th>A</th>
    <th>G</th>
    <th>G</th>
    <th>T</th>
    <th>A</th>
    <th>B</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>""</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>G</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>X</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>T</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>X</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>A</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Y</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>B</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</tbody>
</table>

Let's explain what each of these cells mean.

<table>
<thead>
  <tr>
    <th></th>
    <th>""</th>
    <th>A</th>
    <th>G</th>
    <th>G</th>
    <th>T</th>
    <th>A</th>
    <th>B</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>""</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>G</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>X</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>T</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>X</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>A</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Y</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>B</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>#####</td>
  </tr>
</tbody>
</table>

This cell means:

```
lcs("AGGTAB", "GXTXAYB")
```

These are subproblems. It's not different from what we did with the recursive tree. Each cell is a different function call with a specific set of strings.

<table>
<thead>
  <tr>
    <th></th>
    <th>""</th>
    <th>A</th>
    <th>G</th>
    <th>G</th>
    <th>T</th>
    <th>A</th>
    <th>B</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>""</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>G</td>
    <td></td>
    <td>#####</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>X</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>T</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>X</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>A</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Y</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>B</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</tbody>
</table>

This means:

```
LCS("AG", "G")
```

We construct these strings like so:
* Reading right to left from the columns, we go `"", A, G`. We can't use an empty string so we create `AG`.
* Reading rows top to bottom we go `"", G` and thus we have `G`.

<table>
<thead>
  <tr>
    <th></th>
    <th>""</th>
    <th>A</th>
    <th>G</th>
    <th>G</th>
    <th>T</th>
    <th>A</th>
    <th>B</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>""</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>G</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>X</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>T</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>X</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>A</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Y</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>B</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</tbody>
</table>

There is no common subsequence as `LCS("", A)` returns 0.

<table>
<thead>
  <tr>
    <th></th>
    <th>""</th>
    <th>A</th>
    <th>G</th>
    <th>G</th>
    <th>T</th>
    <th>A</th>
    <th>B</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>""</td>
    <td>0</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>G</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>X</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>T</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>X</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>A</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Y</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>B</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</tbody>
</table>

Again, `AG` vs `""` is 0 as nothing is in common with an empty string.

<table>
<thead>
  <tr>
    <th></th>
    <th>""</th>
    <th>A</th>
    <th>G</th>
    <th>G</th>
    <th>T</th>
    <th>A</th>
    <th>B</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>""</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>G</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>X</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>T</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>X</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>A</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Y</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>B</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</tbody>
</table>

Again, `AGG` vs empty string is an empty string.

We do this for all of them on this row, as none of them can ever be more than 0.

<table>
<thead>
  <tr>
    <th></th>
    <th>""</th>
    <th>A</th>
    <th>G</th>
    <th>G</th>
    <th>T</th>
    <th>A</th>
    <th>B</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>""</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>G</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>X</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>T</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>X</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>A</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Y</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>B</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</tbody>
</table>

Now we go top-to-bottom. `G` vs an empty string.

<table>
<thead>
  <tr>
    <th></th>
    <th>""</th>
    <th>A</th>
    <th>G</th>
    <th>G</th>
    <th>T</th>
    <th>A</th>
    <th>B</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>""</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>G</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>X</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>T</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>X</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>A</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Y</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>B</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</tbody>
</table>

Now `GX` vs an empty string is 0.

<table>
<thead>
  <tr>
    <th></th>
    <th>""</th>
    <th>A</th>
    <th>G</th>
    <th>G</th>
    <th>T</th>
    <th>A</th>
    <th>B</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>""</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>G</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>X</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>T</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>X</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>A</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Y</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>B</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</tbody>
</table>

And so on.

<table>
<thead>
  <tr>
    <th></th>
    <th>""</th>
    <th>A</th>
    <th>G</th>
    <th>G</th>
    <th>T</th>
    <th>A</th>
    <th>B</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>""</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>G</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>X</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>T</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>X</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>A</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Y</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>B</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</tbody>
</table>

We look at the letters A and G:

<table>
<thead>
  <tr>
    <th></th>
    <th>""</th>
    <th>A</th>
    <th>G</th>
    <th>G</th>
    <th>T</th>
    <th>A</th>
    <th>B</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>""</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>G</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>X</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>T</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>X</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>A</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Y</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>B</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</tbody>
</table>

They are not the same, so we compete (like in our recursion).
* If we cut the A off the end, we go left.
* If we cut the G off the end, we go up.

<table>
<thead>
  <tr>
    <th></th>
    <th>""</th>
    <th>A</th>
    <th>G</th>
    <th>G</th>
    <th>T</th>
    <th>A</th>
    <th>B</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>""</td>
    <td>0</td>
    <td>0<br>^<br>^</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>G</td>
    <td>0 &lt;&lt;</td>
    <td>###</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>X</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>T</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>X</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>A</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Y</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>B</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</tbody>
</table>

We take the `max(0, 0)` which is one up and one left. 

The answer is `0`.

<table>
<thead>
  <tr>
    <th></th>
    <th>""</th>
    <th>A</th>
    <th>G</th>
    <th>G</th>
    <th>T</th>
    <th>A</th>
    <th>B</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>""</td>
    <td>0</td>
    <td>0<br>^<br>^</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>G</td>
    <td>0 &lt;&lt;</td>
    <td>###</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>X</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>T</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>X</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>A</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Y</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>B</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</tbody>
</table>

The answer to the subproblem of A compared to G is 0.

We continue our iteration. G vs G:

<table>
<thead>
  <tr>
    <th></th>
    <th>""</th>
    <th>A</th>
    <th>G</th>
    <th>G</th>
    <th>T</th>
    <th>A</th>
    <th>B</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>""</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>G</td>
    <td>0</td>
    <td>0</td>
    <td>####</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>X</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>T</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>X</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>A</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Y</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>B</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</tbody>
</table>

We have a winner, they are the same. So we do `1 + removing both characters`.

Remember how to remove?

<table>
<thead>
  <tr>
    <th></th>
    <th>""</th>
    <th>A</th>
    <th>G</th>
    <th>G</th>
    <th>T</th>
    <th>A</th>
    <th>B</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>""</td>
    <td>0</td>
    <td>0</td>
    <td>0<br>^<br>^</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>G</td>
    <td>0</td>
    <td>0</td>
    <td>####</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>X</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>T</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>X</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>A</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Y</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>B</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</tbody>
</table>

We remove the horizontal G by going up.

And we remove the vertical G by going to the left.

<table>
<thead>
  <tr>
    <th></th>
    <th>""</th>
    <th>A</th>
    <th>G</th>
    <th>G</th>
    <th>T</th>
    <th>A</th>
    <th>B</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>""</td>
    <td>0</td>
    <td>0 &lt;&lt;</td>
    <td>0<br>^<br>^</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>G</td>
    <td>0</td>
    <td>0</td>
    <td>####</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>X</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>T</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>X</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>A</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Y</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>B</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</tbody>
</table>

Now our subproblem is the empty string and A. So we do 1 + the answer to this subproblem.

<table>
<thead>
  <tr>
    <th></th>
    <th>""</th>
    <th>A</th>
    <th>G</th>
    <th>G</th>
    <th>T</th>
    <th>A</th>
    <th>B</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>""</td>
    <td>0</td>
    <td>0 &lt;&lt;</td>
    <td>0<br>^<br>^</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>G</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>X</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>T</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>X</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>A</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Y</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>B</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</tbody>
</table>

Okay so now we compare G and G:

<table>
<thead>
  <tr>
    <th></th>
    <th>""</th>
    <th>A</th>
    <th>G</th>
    <th>G</th>
    <th>T</th>
    <th>A</th>
    <th>B</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>""</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>G</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>###</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>X</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>T</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>X</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>A</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Y</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>B</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</tbody>
</table>

We go here:

<table>
<thead>
  <tr>
    <th></th>
    <th>""</th>
    <th>A</th>
    <th>G</th>
    <th>G</th>
    <th>T</th>
    <th>A</th>
    <th>B</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>""</td>
    <td>0</td>
    <td>0</td>
    <td>0 &lt;&lt;</td>
    <td>0<br>^<br>^</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>G</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>###</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>X</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>T</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>X</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>A</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Y</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>B</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</tbody>
</table>

And add 1 + the answer to that subproblem to our current cell:

<table>
<thead>
  <tr>
    <th></th>
    <th>""</th>
    <th>A</th>
    <th>G</th>
    <th>G</th>
    <th>T</th>
    <th>A</th>
    <th>B</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>""</td>
    <td>0</td>
    <td>0</td>
    <td>0 &lt;&lt;</td>
    <td>0<br>^<br>^</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>G</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>X</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>T</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>X</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>A</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Y</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>B</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</tbody>
</table>

We do this for all of them, as all of our strings contain at least one letter "G".

Remember, we are doing:

```python
lcs("G", "A")
lcs("G", "AG")
lcs("G", "AGG")
lcs("G", "AGGT")
```

and so on, building the string as we go along the row.

<table>
<thead>
  <tr>
    <th></th>
    <th>""</th>
    <th>A</th>
    <th>G</th>
    <th>G</th>
    <th>T</th>
    <th>A</th>
    <th>B</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>""</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>G</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
  </tr>
  <tr>
    <td>X</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>T</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>X</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>A</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Y</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>B</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</tbody>
</table>

Now we go to X and A. It mismatches so we put 0:

<table>
<thead>
  <tr>
    <th></th>
    <th>""</th>
    <th>A</th>
    <th>G</th>
    <th>G</th>
    <th>T</th>
    <th>A</th>
    <th>B</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>""</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>G</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
  </tr>
  <tr>
    <td>X</td>
    <td>0</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>T</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>X</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>A</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Y</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>B</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</tbody>
</table>

X and G, these mismatch so we do `max(0, 1)` (0 from left, 1 from above) and it becomes 1.

<table>
<thead>
  <tr>
    <th></th>
    <th>""</th>
    <th>A</th>
    <th>G</th>
    <th>G</th>
    <th>T</th>
    <th>A</th>
    <th>B</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>""</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>G</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
  </tr>
  <tr>
    <td>X</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>T</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>X</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>A</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Y</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>B</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</tbody>
</table>

We have mismatches all along again:

<table>
<thead>
  <tr>
    <th></th>
    <th>""</th>
    <th>A</th>
    <th>G</th>
    <th>G</th>
    <th>T</th>
    <th>A</th>
    <th>B</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>""</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>G</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
  </tr>
  <tr>
    <td>X</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
  </tr>
  <tr>
    <td>T</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>X</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>A</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Y</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>B</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</tbody>
</table>

We can actually kind of cheat using our eyes here. We're now on T, so we know that all of our values will be:

```
max(left, up)
```

We can skip right up to T.

<table>
<thead>
  <tr>
    <th></th>
    <th>""</th>
    <th>A</th>
    <th>G</th>
    <th>G</th>
    <th>T</th>
    <th>A</th>
    <th>B</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>""</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>G</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
  </tr>
  <tr>
    <td>X</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
  </tr>
  <tr>
    <td>T</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>###</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>X</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>A</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Y</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>B</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</tbody>
</table>

Now we remove both T's. We go up and left (diagonally) to:

<table>
<thead>
  <tr>
    <th></th>
    <th>""</th>
    <th>A</th>
    <th>G</th>
    <th>G</th>
    <th>T</th>
    <th>A</th>
    <th>B</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>""</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>G</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
  </tr>
  <tr>
    <td>X</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>1 &lt;&lt;</td>
    <td>1<br>^<br>^</td>
    <td>1</td>
    <td>1</td>
  </tr>
  <tr>
    <td>T</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>###</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>X</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>A</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Y</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>B</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</tbody>
</table>

The answer to that subproblem is 1, so we add 1 to it for our cell.

<table>
<thead>
  <tr>
    <th></th>
    <th>""</th>
    <th>A</th>
    <th>G</th>
    <th>G</th>
    <th>T</th>
    <th>A</th>
    <th>B</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>""</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>G</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
  </tr>
  <tr>
    <td>X</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>1 &lt;&lt;</td>
    <td>1<br>^<br>^</td>
    <td>1</td>
    <td>1</td>
  </tr>
  <tr>
    <td>T</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>2</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>X</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>A</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Y</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>B</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</tbody>
</table>

We can see that there are no matches anymore using our eyes, so we can skip ahead.

<table>
<thead>
  <tr>
    <th></th>
    <th>""</th>
    <th>A</th>
    <th>G</th>
    <th>G</th>
    <th>T</th>
    <th>A</th>
    <th>B</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>""</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>G</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
  </tr>
  <tr>
    <td>X</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>1 &lt;&lt;</td>
    <td>1<br>^<br>^</td>
    <td>1</td>
    <td>1</td>
  </tr>
  <tr>
    <td>T</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>2</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>X</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>A</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Y</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>B</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</tbody>
</table>

Now onto the next row. 

We have no letter "X" in our columns, so we can skip ahead (computers won't do this, this is purely for our sanity):

<table>
<thead>
  <tr>
    <th></th>
    <th>""</th>
    <th>A</th>
    <th>G</th>
    <th>G</th>
    <th>T</th>
    <th>A</th>
    <th>B</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>""</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>G</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
  </tr>
  <tr>
    <td>X</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
  </tr>
  <tr>
    <td>T</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>2</td>
    <td>2</td>
    <td>2</td>
  </tr>
  <tr>
    <td>X</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>2</td>
    <td>2</td>
    <td>2</td>
  </tr>
  <tr>
    <td>A</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Y</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>B</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</tbody>
</table>

Now we get to A and A, this is a match. We remove the As and go to 0. 0 + 1 = 1.

<table>
<thead>
  <tr>
    <th></th>
    <th>""</th>
    <th>A</th>
    <th>G</th>
    <th>G</th>
    <th>T</th>
    <th>A</th>
    <th>B</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>""</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>G</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
  </tr>
  <tr>
    <td>X</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
  </tr>
  <tr>
    <td>T</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>2</td>
    <td>2</td>
    <td>2</td>
  </tr>
  <tr>
    <td>X</td>
    <td>0&lt;&lt;</td>
    <td>0<br>^<br>^</td>
    <td>1</td>
    <td>1</td>
    <td>2</td>
    <td>2</td>
    <td>2</td>
  </tr>
  <tr>
    <td>A</td>
    <td>0</td>
    <td>1</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Y</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>B</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</tbody>
</table>

We don't match again until the next A:

<table>
<thead>
  <tr>
    <th></th>
    <th>""</th>
    <th>A</th>
    <th>G</th>
    <th>G</th>
    <th>T</th>
    <th>A</th>
    <th>B</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>""</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>G</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
  </tr>
  <tr>
    <td>X</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
  </tr>
  <tr>
    <td>T</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>2</td>
    <td>2</td>
    <td>2</td>
  </tr>
  <tr>
    <td>X</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>2</td>
    <td>2</td>
    <td>2</td>
  </tr>
  <tr>
    <td>A</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>2</td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>Y</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>B</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</tbody>
</table>

We do 2 + 1 is 3:

<table>
<thead>
  <tr>
    <th></th>
    <th>""</th>
    <th>A</th>
    <th>G</th>
    <th>G</th>
    <th>T</th>
    <th>A</th>
    <th>B</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>""</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>G</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
  </tr>
  <tr>
    <td>X</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
  </tr>
  <tr>
    <td>T</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>2</td>
    <td>2</td>
    <td>2</td>
  </tr>
  <tr>
    <td>X</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>2</td>
    <td>2</td>
    <td>2</td>
  </tr>
  <tr>
    <td>A</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>2</td>
    <td>3</td>
    <td>3</td>
  </tr>
  <tr>
    <td>Y</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
  <tr>
    <td>B</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</tbody>
</table>

Y does not match anything, so we `max(left, up)`:

<table>
<thead>
  <tr>
    <th></th>
    <th>""</th>
    <th>A</th>
    <th>G</th>
    <th>G</th>
    <th>T</th>
    <th>A</th>
    <th>B</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>""</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>G</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
  </tr>
  <tr>
    <td>X</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
  </tr>
  <tr>
    <td>T</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>2</td>
    <td>2</td>
    <td>2</td>
  </tr>
  <tr>
    <td>X</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>2</td>
    <td>2</td>
    <td>2</td>
  </tr>
  <tr>
    <td>A</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>2</td>
    <td>3</td>
    <td>3</td>
  </tr>
  <tr>
    <td>Y</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>2</td>
    <td>3</td>
    <td>3</td>
  </tr>
  <tr>
    <td>B</td>
    <td>0</td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
  </tr>
</tbody>
</table>

B only matches the end letter, so we skip ahead again:

<table>
<thead>
  <tr>
    <th></th>
    <th>""</th>
    <th>A</th>
    <th>G</th>
    <th>G</th>
    <th>T</th>
    <th>A</th>
    <th>B</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>""</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>G</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
  </tr>
  <tr>
    <td>X</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
  </tr>
  <tr>
    <td>T</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>2</td>
    <td>2</td>
    <td>2</td>
  </tr>
  <tr>
    <td>X</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>2</td>
    <td>2</td>
    <td>2</td>
  </tr>
  <tr>
    <td>A</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>2</td>
    <td>3</td>
    <td>3</td>
  </tr>
  <tr>
    <td>Y</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>2</td>
    <td>3</td>
    <td>3</td>
  </tr>
  <tr>
    <td>B</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>2</td>
    <td>3</td>
    <td></td>
  </tr>
</tbody>
</table>

The solution to removing both B's is 3, so our result is `3 + 1` which is 4:

<table>
<thead>
  <tr>
    <th></th>
    <th>""</th>
    <th>A</th>
    <th>G</th>
    <th>G</th>
    <th>T</th>
    <th>A</th>
    <th>B</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td>""</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
    <td>0</td>
  </tr>
  <tr>
    <td>G</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
  </tr>
  <tr>
    <td>X</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
  </tr>
  <tr>
    <td>T</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>2</td>
    <td>2</td>
    <td>2</td>
  </tr>
  <tr>
    <td>X</td>
    <td>0</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>2</td>
    <td>2</td>
    <td>2</td>
  </tr>
  <tr>
    <td>A</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>2</td>
    <td>3</td>
    <td>3</td>
  </tr>
  <tr>
    <td>Y</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>2</td>
    <td>3</td>
    <td>3</td>
  </tr>
  <tr>
    <td>B</td>
    <td>0</td>
    <td>1</td>
    <td>1</td>
    <td>1</td>
    <td>2</td>
    <td>3</td>
    <td>4</td>
  </tr>
</tbody>
</table>

The solution to the longest common subsequence is 4.

The time & space complexity of our algorithm is:
* Time: $O(mn)$
* Space: $O(mn)$

Where n = the length of string 1 and m = the length of string 2.

#### String DP Conclusion

The table we created is important. Every single String DP problem requires the use of a similar table.

Similar problems are:
* [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/).
* [Shortest Common Subsequence](https://leetcode.com/problems/shortest-common-supersequence/).
* [Edit Distance](https://leetcode.com/problems/edit-distance/).


### Decision Making

Given a situation, at each step, decide whether or not to use the current step in the final calculation.

We make a decision at each step.

We most often see this when we use the `max()` or `min()` of something. Let's look at an example:

#### House Robbers

[House Robbers](https://leetcode.com/problems/house-robber/) is a fun problem.

> You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
>
> Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

```
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.
```

Our first step is to figure out the basecases, the recursion.

A robber has two options:
1. Rob current house.
2. Don't rob current house.

If _rob current house_ is selected than they can#t rob the previous `i - 1` house but can safely preceed to the one before the previous `i - 2` and get all the tems that follow.

If _don't rob current house_ is chosen the robber gets all the items from the robbery of `i - 1` and all the following buildings.

We have to calculate what is most profitable, the maximum of:
* Robbery of current house + items from houses before the previous.
* Items from the previous house robbery and any items captured before that.

```py
rob(i) = max(rob(i - 2) + currentHouseValue, rob(i - 1))
```

That means our basecases are:

```py
def rob(nums):
  # Because there is nothing to rob
  if not nums:
    return 0
  
  # We can only rob one house
  if len(nums) == 1:
    return nums[0]

  dp = [0] * len(nums)
  dp[0] = nums[0]

  # Deciding where to start
  dp[1] = max(nums[0], nums[1])
  for i in range(2, len(nums)):
    dp[i] = max(nums[i] + dp[i-2], dp[i-1])
  
  # returns the last element which is the maximum
  return dp[-1]
```

We can further reduce this by moving to a 2-variable model.

We only need to keep track of the previous and current house (like Fibonacci) which we can do with:

```py
def rob(nums):
  prev = curr = 0
  for num in nums:
    # nums[i-2]th value
    temp = prev 
    # nums[i-1]th value
    prev = curr
    # the max recursion formula we found earlier
    curr = max(num + temp, prev)
  return curr
```

#### Similar Problems
* [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
* [Best Time to Buy and Sell Stock with Transaction Fee](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/)
* [Best Time to Buy and Sell Stock with Cooldown](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/)


## Time Complexity of a Dynamic Programming Problem
![](/media/dp/undraw9.svg)

[Time complexity](/you-need-to-understand-big-o-notation-now/) is calculated in Dynamic Programming as:

$$Number \ of \ unique \ states * time \ taken \ per \ state$$

For our original problem, the Weighted Interval Scheduling Problem, we had n piles of clothes. Each pile of clothes is solved in constant time. The time complexity is:

$$O(n) + O(1) = O(n)$$

[I've written a post about Big O notation ](/big-o/)if you want to learn more about time complexities.

With our Knapsack problem, we had n number of items. The table grows depending on the total capacity of the knapsack, our time complexity is:

$$O(nw)$$

Where n is the number of items, and w is the capacity of the knapsack.

I'm going to let you in on a little secret. It's possible to work out the time complexity of an algorithm from its recurrence. You can use something called the Master Theorem to work it out. This is the theorem in a nutshell:

<figure>
    <img src="/media/dp/time1.png">
    <figcaption><a href="https://medium.com/@randerson112358/master-theorem-909f52d4364"> Taken from here </a><figcaption>
</figure>

Now, I'll be honest. The master theorem deserves a blog post of its own. For now, I've found this video to be excellent:

{{< youtube OynWkEj0S-s >}}


---

### Dynamic Programming vs Divide & Conquer vs Greedy

Dynamic Programming & [Divide and Conquer](/divide-and-conquer-algorithms/) are similar. Dynamic Programming is based on Divide and Conquer, except we memoise the results.

But, Greedy is different. It aims to optimise by making the best choice at that moment. Sometimes, this doesn't optimise for the whole problem. Take this question as an example. We have 3 coins:

1p, 15p, 25p

[And someone wants us to give a change of 30p](https://en.wikipedia.org/wiki/Change-making_problem). With Greedy, it would select 25, then 5 * 1 for a total of 6 coins. The optimal solution is 2 * 15. Greedy works from largest to smallest. At the point where it was at 25, the best choice would be to pick 25. 


<table>
    <thead>
        <tr>
            <th colspan="3">Greedy vs Divide & Conquer vs Dynamic Programming</th>
        </tr>
    </thead>
    <tbody>
        <tr>
          <td><b>Greedy</b></td>
          <td><b>Divide & Conquer</b></td>
          <td><b>Dynamic Programming</b></td>
        </tr>
      <tr>
        <td>Optimises by making the best choice at the moment</td>
        <td>Optimises by breaking down a subproblem into simpler versions of itself and using multi-threading & recursion to solve</td>
        <td>Same as Divide and Conquer, but optimises by caching the answers to each subproblem as not to repeat the calculation twice.</td>
      </tr>
      <tr>
        <td>Doesn't always find the optimal solution, but is very fast</td>
        <td>Always finds the optimal solution, but is slower than Greedy</td>
        <td>Always finds the optimal solution, but could be pointless on small datasets.</td>
      </tr>
      <tr>
        <td>Requires almost no memory</td>
        <td>Requires some memory to remember recursive calls</td>
        <td>Requires a lot of memory for memoisation / tabulation</td>
    </tbody>
</table>

---


---

# BackTracking
Backtracking is conceptually easy to understand. As we search for a solution, sometimes we reach a dead end and haev to go back.

The idea is easy, but implementing it isn't. Backtracking typically works with recursion, but it's tricky to understand.

We'll start with non-recursive backtracking code.

## Defining a maze


## Conclusion

Most of the problems you'll encounter within Dynamic Programming already exist in one shape or another. Often, your problem will build on from the answers for previous problems. [Here's a list of common problems that use Dynamic Programming.](https://en.wikipedia.org/wiki/Dynamic_programming#Algorithms_that_use_dynamic_programming)

I hope that whenever you encounter a problem, you think to yourself "can this problem be solved with ?" and try it. 
