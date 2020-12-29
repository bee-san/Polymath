---
title: Quicksort Explained Like I'm 5 
slug: quicksort 
date: 2020-12-28T16:43:37.000Z
draft: true 
socialImage: /media/p2p.jpg
description: "Quicksort explained like I'm 5"
ShowToc: true
math: true
tags:
  - "Datastructures and Algorithms"
---

## What is Quicksort?

Quicksort is a sorting algorithm designed by British computer scientist [Tony Hoare](https://en.wikipedia.org/wiki/Tony_Hoare).

Quicksort is fast. When implemented correctly it is 2 or 3 times faster than Mergesort or Heapsort. 

However, let's compare the [Big O](https://skerritt.blog/big-o-notation/) run times of these.

| Quicksort |    Mergesort     |     Heapsort     |
| --------  |   -----------    |     --------     |
| $O(n^2)$  | $O(n \ log \ n)$ | $O(n \ log \ n)$ |

Quicksort is wore in the worst case time than the other two, but it's fasteer -- how?

This is because of [amoretized time](https://skerritt.blog/big-o-notation/). In Big O it's slower, but in the real world it's faster.

These are the things that make quicksort faster on average than the others:
* Caching - Quicksort requires little additional memory, so more elements will be in our cache compared to Mergesort.
* We can avoid Quicksort's $O(n^2)$ runtime by using an appropriate pivot (discussed later).

Quicksort wins out if we are assuming constant time access to any element, such as in a [set](https://skerritt.blog/sets/). If our data structure lived on a hard drive, it would be much slower.

## The 2 functions 

In Quicksort, there are 2 main functions we use.

1. Split. 
2. Partioning.

### Split 

Quicksort is similar to Mergesort. The first thing it does is splits the data, it's a [Divide & Conquer](https://skerritt.blog/divide-and-conquer-algorithms/) algorithm. 

The algorithm breaks a large problem down into smaller sub-problems and recursively solves them to get an sorted array.

Given a pivot point, the algorithm splits the array into 2 and calcualtes a new pivot point. 

The code is:

```python
def quicksort(array, pivot, length):
	if pivot < length:
		q = partition(array, pivot, length)
		quicksort(array, pivot, q - 1)
		quicksort(array, q + 1, length)
```



## The 2 functions

Quicksort has 2 main functions, split (quicksort) which splits the input, and the partition which gives us a pivot.

* Split
* Partiioning

### Splitting

The partitioning function chooses a _pivot_.

_How_ it chooses the pivot is important, but for now let's choose the last element. What's more important is that we understand how the splitting function works before we learn how pivoting works.

Let's look at a quick example.

![We have a list consisting of 3, 4, 5, 8, 9, 7. We have 2 pointers. "L" is at 3 (position 0), "R" is at 7 (last position). Our pivot is 7 (last element)](/media/quicksort/split1.svg)

We set the pivot point to the last element. No reason, it was just simpler to explain.

We have a left (l) bound and a right (r) bound. Our left starts at 0 and our right starts at the end of the array (length - 1).

With recursion, we ask the question:

> "Within this iteration, what am I trying to do?"

And by solving the problem in each iteration, we build up to a solution for the whole.

For our split function, our answer is:

> "In this iteration we need to split the array in half. Elements smaller than the pivot on the left, elements larger than the pivot on the right."

To work this out, we introduce 2 new pointers.

![](/media/quicksort/split2.svg)

* i - Remember the last position that an element was inserted into, before the pivot. Keeps track of the tail.
* j - Scan from the left boundary to the right boundary to see if any elements are less than or equal to the pivot.

At this iteration, `j` advances. This is because we're at the lower boundary and `j` cannot touch boundaries.

![j moves to 4](/media/quicksort/split3.svg)

`j` asks the questtion:

> "Is 4 less than or equal to the pivot (7)?"

This is true, we swap `i` and `j`'s values. Position 0 now contains "4", and position 1 is "3".

![3 and 4 swap](/media/quicksort/split4.svg)

`i` then advances. Remember, **`i`'s job is to keep track of the last element we swapped, the tail.**


![i advances to 3](/media/quicksort/split5.svg)

Here we need to think "what is my job within this iteration?" and our job ist ofind the position for the pivot. Quicksort's job wqithin the paritioning subroutine is to find a position for the pivot.

Once we find it, we return the index so our split function knows where to chop the array into halves.

Think of pivot as the item we want to find a position for. 

Search the array and bring all the elements less than the pivot to the left, and all the elements greater than the pivot to the right.


is 3 less than or equal to pivot? 3 is greater so we do not execute a swap. 


j hits the right boundary, so we don't do anything -- we exit. 

Every single item from i to r is greater than the pivot. 

PIC1

Everything from l and behind is less than the pivot.

PIC2

We swap the item at the pivot position into i + 1 because we make no swaps into i. 

PIC3

We sandwich between the less and greater section, and we swap between the pivot item and `i`. `i`. is the ending of the section of items less than the pivot. 

```
1 7 8 2 3
```

We found `i`'s home by sandwiching it. We now have `1`'s final position. 

We run quicksort on the left half and the right half.

PIC4

Our example is the worst case. If the pivot is the greatest item or the least, in our partion space the least item is going to be at the start or if its the greatest we'll find a position i nthe right boundary. 

The worstcase of quicksort is $O(n^2)$ because we do n - 1 pivots, n - 2 pivots and so on in this worst case scenario.

In a nicer case of quicksort:

```
L	  R
3 4 5 8 9 7
i
j

pivot = 7
```

We chose 7 as our pivot, but it can be anything really. The best pivot is when the item is the median of the partition space. 

All i's job is to remember the last place where we put the item before the pivot. Keeps a tail of where the pivot needs to be swapped into.

We advance j.


```
L	  R
3 4 5 8 9 7
i
  j

pivot = 7
```

4 is less than or equal to 7, so we swap i and j.

```
L	  R
4 3 5 8 9 7
i
  j

pivot = 7
```
We advance i as we did a swap.

```
L	  R
4 3 5 8 9 7
  i
    j

pivot = 7
```

and we advance j as we already looked at the element there. 

j is the investigator, i is keeping memory.

5 is less than 7 so we swap 5 and 3 and move i up.

```
L	  R
4 5 3 8 9 7
    i
      j

pivot = 7
```

8 is not less than or equal so we advance j.

neither is 9, so j touches the right boundary and it stops. 

```
L	  R
4 5 3 8 9 7
    i
          j

pivot = 7
```

PIC5

All the items less than pivot are left, all the itmes grater than pivot are right.

j's job is to scan and say "i found an item less than a pivot, let me throw it back to you i" and i keeps track of the last element that was thrown to it -- the tail oof the items less than the pivot. 

The pivot gets sandwiched between the sections. We need to swap the pivot into the section after i, which is i + 1

```
L	  R
4 5 3 7 9 8
    i
          j

pivot = 7
```

Like this. Our pivot was good. 

Quicksort is all about cutting the space into "less than an item" and more than an item. recursively we call quicksort on each other and we return the index. 

Let's look at the worst case.

```
9 8 6 7 1

pivot = 1
```

If I choose a bad pivot, we'll do n - 1 comparisons and our pivot value is at index 0 (9). We split to the left and right. 

PIC6

WE split to the left with 0 items, and to the right with n - 1 items. 

If we pick another bad pivot, we split to the left with 0 items and to the right with n - 2 items.

PIC7 

That'll keep going. We'll split our input downards and at each level we will do n - 1, next level we do (n - 1) - 1 work. The input size is (n - 1) but in the work we do in that call we do n - 1 work, so we plug in the size of the input.

Eventually we go from n - 1 until we get down to 1 item. 

Using summations we do:

$$ \sigma_{i = 1}^{n - 1} i$$

work.

This is equal to (using [Gaussian Sum](https://en.wikipedia.org/wiki/Gauss_sum#:~:text=Gauss%20sums%20over%20a%20residue,Plancherel%27s%20theorem%20on%20finite%20groups.):

$$\frac{n(n + 1)}{2} = \frac{n - 1 ((n - 1) - 1)}{2} = \frac{(n - 1) n}{2}$$

comparisons at worst. Our big O upper bound is $O(n^2)$.

We make our recursion tree very, very deep.
