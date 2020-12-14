---
title: How linked lists work with an application to Blockchain
slug: you-dont-understand-blockchain-unless-you-understand-this-simple-data-structure
date_published: 2019-01-08T00:23:58.000Z
date: 2019-10-10T16:19:24.000Z
tags: 
  - "University"
  - "Computer Science"
excerpt: Linked lists!
---

The blockchain is an immutable, ordered, back-linked list of blocks of transactions. If you want to truly understand blockchain you need to understand linked lists.

Linked Lists are a linear collection of data elements. Linearty in a linked list is not defined by each element’s physical placement. Instead each data node in a linked list points to one or two other nodes in the linked list.

With an array such as [1, 2, 3] you know that the element 1 is at position [0] and element 2 is at position [1].

The **physical** placement of each element defines the linearty of the array. This does not happen with linked lists.

Nodes make up elements in linked lists. Every node has a data section to it. As well as data, each node has a “forwards” and “backwards” section pointing to the previous and next node in the list.

In an array if you want to insert an item at [0] you need to shift every element in the array 1 to the right to make space at [0].

With a linked list you can insert data items anywhere in the list without having to shift the entire list. To do this you have to tell the next and previous node to point to this new node.

Let’s say you have an array that grows every day. One day the array has 5000 elements in it. To insert an item at [0] you’ll have to move 5000 elements.

With a linked list you do not have to shift any items, you can insert them. This makes them useful for lists which may grow in size at an expeditious rate.

Linked lists are scalable and adaptable.

We call the “forwards” and “backwards” elements of a node the pointers of the node. Nodes have 2 / 3 elements in them depending on whether it is a singly linked list or a doubly linked list.

### Singly Linked Lists
![](https://cdn-images-1.medium.com/max/800/1*tZeQ7c4s8mIdgQPFs6DpPw.png)A Node of a Singly Linked List
A Singly Linked List has a data element to it and a pointer pointing to the next node. When the pointer is pointing at nothing we say that it is pointing at Null.

2 **components** make up the singly linked list node — the data and the pointer.

Singly linked lists cannot point backwards as they do not have a “backwards” pointer.

A pointer does not store any data other than where the next node is. It is literally a pointer.
![](https://cdn-images-1.medium.com/max/800/1*d3f_qh9xp1JCGvBM1yRtrQ.png)2 nodes in a linked list. One of them is correctly pointing to NULL.
A new node has been added to show what the singly linked list looks like with more than 1 node in it.
![](https://cdn-images-1.medium.com/max/800/1*5TjzOrO0_kOx2eFXf0_rKQ.png)3 nodes in a linked list, with a header and tail pointer.
Depending on the implementation a linked list could also have 2 special pointers — head and tail.

The head pointer points to the very first node in the linked list. The tail pointer points to the last node in the linked list.

If you only have one node in the linked list the convention is for head to point to it and for tail to point to null. Although this is entirely up to the programmers and in some cases head and tail can point to the same singular node.

Programmers create special functions for linked lists to make them mroe usable. These functions are:

- node.data = get data from current node
- node.next = go to next node

### Doubly Linked List

A doubly linked list is a singly linked list that has a “backwards” component.
![](https://cdn-images-1.medium.com/max/800/1*AdjEZlPyCe-yXhXwFhUrJA.png)A node in a doubly linked list with 3 components
Each **node** in a doubly linked list has 3 **components**. A backwards pointer, a data element and a forwards pointer.
![](https://cdn-images-1.medium.com/max/800/1*WBc-5orIYMBzOvwzAjKs1Q.png)2 nodes in a doubly linked list. Both nodes are correctly pointing at NULL. There are header and tail pointers in this linked list.
Like with singly linked lists, doubly linked lists have special functions. These functions are:

- node.data = get data from current node
- node.next = go to next node
- node.prev = go to previous node

If you use node.prev on the head node then the function will error or produce a NULL value. If you use node.next on the tail node then the function will error or produce a NULL value.

### Traversing Linked Lists

Something we want to do a lot of with linked lists is to traverse them. Go up and down the linked list.

The first thing we need to do is to define where we start. Well, the starting point of the linked list (head) is a good place.

Now we want a loop that goes through the entire list. We want to go through every single node until the currently selected node is “NULL” or None in Python. Once we hit a “None” node we know we are at the end.

Now we want to do something with our linked list as we traverse it. Let’s print every data element in every node in our linked list.

Now to actually move to the next node we use the node.next function:

The notation of:

is called **dot** notation because we are calling the linked list’s function “next”. We will see how to program a linked list shortly.

[The time complexity to search and traverse through linked lists is O(n). If you do not understand big O notation I highly recommend this article:](https://skerritt.blog/big-o/)
[

All You Need to Know About Big O Notation [Python Examples]

By the end of this article, you’ll thoroughly understand Big O notation. You’ll
also know how to use it in the real world, and even the mathematics behind it! In computer science, time complexity is the computational complexity that
describes the amount of time it takes to run an algorithm. Big O …

![](https://skerritt.blog/favicon.png)Brandon SkerrittBrandon's Blog

![](/content/images/2019/10/Copy-of-Copy-of-Copy-of-Copy-of-Dynamic-Programming-with-Python-The-Ultimate-Guide-1.png)
](https://skerritt.blog/big-o/)
### Programming Linked Lists

Linked Lists aren’t available in most languages so we have to program it ourselves.

Because a node will have the same functions and look the same across our linked list it is best to create this as a class.

A class is a template for an **object**. You can create many objects from one class.

Let’s design the linked list in Java.

You can apply 3 methods to this node using the dot notation:

The class has a “constructor” method which runs every time we make a new node. This initialises the node for us. The constructor method sets the next and previous pointers to point to “null”. It then sets the data to “i” which is what the user wants to put into the node.

If we wanted to make a single node we just need to write this code:

This creates an **instance** of the Node class and provides the number “5” to it as the data element of that node.

Now of course having one singular node isn’t useful at all. We want to add more nodes to the linked list.

Remember that example from earlier where adding an element to the front of an array requires shifting every element to the right by 1?

We’re going to show how this is easier done using linked lists.

In order to add a new node to the front of the list we will need a method (function) that does this

Before we can add a node to the front we first must create a node with the value we want:
![](https://cdn-images-1.medium.com/max/800/1*cwNAmCQNH3biOcA8WgpC7Q.png)A doubly linked list already exsists with data 15 and 14. We create a new node with data Value that is not currently connected to the linked list; as such both pointers point to NULL.
Now from our definition of the node class earlier the node’s functions node.next and node.prev points to null. Let’s change that:

We have not updated the head pointer, so it still points to the head of the linked list which is what we want to make the second node in the linked list. We make the node.next pointer point at where the head pointer is pointing at.
![](https://cdn-images-1.medium.com/max/800/1*WSxgCOxx3g1ULbYS27m8Uw.png)We begin to attach the new node to the rest of the linked list. We tell the forward component to point at where head is pointing at.
Because we are inserting a new node at the front of the linked list we will need to update the head pointer soon. First, we’ll define where the new nodes previous pointer points to.

We actually didn’t need to update newNode.prev to be null because it’s already done in the Node class; however to make things clear the code has been put there.
![](https://cdn-images-1.medium.com/max/800/1*WSxgCOxx3g1ULbYS27m8Uw.png)Since we defined both pointers of a doubly linked list node to point to NULL nothing has changed. The code has been put here for extra clarity. This has **not** changed the linked list.
Now we need to update the second node, the node that the head pointer is still pointing at. It needs to know that node.previous points to an actual node now and not just null.

If the head pointer is not pointing at anything as the linked list has not been created yet then we do not need to update the node.
![](https://cdn-images-1.medium.com/max/800/1*3Vi7Omq3KWb0q9JbnBU1BQ.png)The second node (head node) has been updated so the previous component points at our new node.
If the head pointer is pointing at a node then inform that node that it’s .prev function points to the new node we have just inserted.

Else if the head is pointing at nothing make the tail the newNode. Earlier we talked about whether a singular node has a head or tail pointer pointing at it. This is the part where the programmer decides. Here we have elected to make the singular node the tail and the head at the same time.

We now just need to update the head pointer to point to the new head of the linked list:
![](https://cdn-images-1.medium.com/max/800/1*1oa2rx4xWSKxij6Y6EcTgQ.png)The new node has been inserted at the head of the linked list. We have just updated the head pointer to point to the new head.
We can also delete a node at the front of the linked list in a similar fashion:

We assume here that curr is a pointer that points to any node in the linked list.

We then want to set curr to head, since we’re deleting the head node:
![](https://cdn-images-1.medium.com/max/800/1*X1gmq_aVCT4lY6usR96JgA.png)The curr pointer is pointing at the same place the head pointer is.
We want to make sure that head is pointing at something. curr is not equal to null as there is a node there.

We move the head pointer 1 to the right.
![](https://cdn-images-1.medium.com/max/800/1*Cf6j4zPjrkEeIvvfdbPwow.png)We have moved the head pointer to the right
We also make head.prev into null.

Now we remove curr.next’s pointer
![](https://cdn-images-1.medium.com/max/800/1*2TQS4dmYjQji0quKcQR4uQ.png)The Curr node is completely disconnected from the linked list.
Now we have this node sitting in a space doing nothing. We return the node in case we want to do something else with it.

And that’s it! The node is no longer connected to the linked list, thus making it ‘deleted’.

### Inserting Items into Linked Lists

The true power of a linked list is being able to insert items anywhere in them.

Inserting an item anywhere in a linked list is similar to inserting an item at the head. You just change a few variables, the idea is still the same.

Whenever we want to insert a new node, we just have to tell the node what the next and previous nodes are.

### Searching a Linked List

Linked lists are normally sorted. Items can be inserted anywhere in a linked list, so it makes sense to put them in the right place. If you have a linked list with data of 3, 4, 6 the programmer would likely put the new node containing 5 between 4 and 6. But this is entirely down to the programmer.

We could use binary search to search the list. But, this is a bad idea. We don’t know where the middle of a linked list is. Everytime we wanted to find the middle we would have to count every single node in the list and half that by 2.

We can use a modified version of sequential search to search a linked list.

Assume the linked list is sorted in ascending order. we can use this information to make sequential search faster.

Since the linked list is sorted sequentially we know that the nodes in the linked list go in some order, like 1, 2, 3, 4, 5 for example. If node.data is more than the key (what we’re looking for) we know it’s not in the list, because it is sorted.

So if we wanted to find 2.5 we would do this:

1 is selectedis 1 goal? - nois 1 > 2.5? no2 is selectedis 2 goal? nois 2 > 2.5? no3 is selectedis 3 goal? nois 3 > 2.5? yes - we can assume 2.5 is not in list and thus end the search here

There are many search algorithms out there. But most of the time if you know a little bit of information about the data you can change a search algorithm to be more efficient. In general, binary search is extremely effective but here it’s not so good. Don’t use an algorithm because Stack Overflow says that it is the fastest, best algorithm for the job.

Algorithms are like programming languages. We all have our favourites and sometimes we say that one programming language is better than another (Python, I love you). But at the end of the day it would be foolish and naive to say that one programming language is better than all the others. Use the right tool for the job, and change it if you want to!

### Blockchains
![img](https://cdn-images-1.medium.com/max/800/1*qYKsqQ6aV-DgFD0REfcnig.png)
Back to blockchain technology. Earlier I said:

> *The blockchain is an immutable, ordered, back-linked list of blocks of transactions.*

So let’s work through this.

The blockchain is immutable. You cannot in theory change the blockchain. It is possible but it is very very hard to do, especially to a blockchain such as Bitcoin’s blockchain.

The blockchain is ordered in terms of most frequent transaction is “on top” of the chain. Or most frequent transaction is furthest to the right.

The blockchain is linked “back” referring to the previous block in the chain. Every block refers to the block behind it.

Each block is a transaction.

You should now have a firm understanding of linked lists and how they work. You should also understand the linked list part of the blockchain.

### If you liked this article, connect with me!

[LinkedIn](https://www.linkedin.com/in/brandonls/) | [Twitter](https://twitter.com/brandon_skerrit) | [Website](http://brandonskerritt.github.io/) | [Newsletter](https://upscri.be/885736-2/)
