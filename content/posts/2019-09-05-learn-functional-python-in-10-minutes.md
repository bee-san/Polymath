---
title: Learn Functional Python in 10 Minutes
slug: learn-functional-python-in-10-minutes
date_published: 2019-09-05T11:30:00.000Z
date: 2019-11-20T22:55:19.000Z
ShowToc: true
tags: 
    - University
    - Computer Science
    - Datastructures and Algorithms
    - Popular
excerpt: You’ll learn what the functional paradigm is as well as how to use functional programming in Python. You’ll also learn about list comprehensions and other forms of comprehensions.
---

In this short 10 minute article, you’ll learn what the functional paradigm is in Python. You’ll also learn about list comprehensions.

---

# 📌 Functional Paradigm

In an imperative paradigm, we do things by giving the computer a sequence of tasks and then it executes them. While executing them, it can change states. For example, let’s say we set `A = 5`, then we change the value of `A`. We have variables in the sense that the value inside the variable varies.

In a functional paradigm, we don’t tell the computer what to do but we tell it what stuff is. What the greatest common divisor of a number is, and so on.

Variables cannot vary. Once we set a variable, it stays that way forever. Because of this, functions have no *side effects* in the functional paradigm. A side effect is where the function changes something outside of it. Let’s look at an example:

    a = 3
    def some_func():
    	global a
    	a = 5
    some_func()
    print(a)
    

The output  is 5. In the functional paradigm, changing variables is a big no-no and having functions affect things outside of their scope is also a big no-no. The only thing a function can do is calculate something and return it.

Now you might think "no variables, no side effects? Why is this good?". Good question, gnarly stranger reading this.

If a function is called twice with the same parameters, it’s guaranteed to return the same result. If you’ve learnt about [mathematical functions](/functions-cheat-sheet/), you’ll appreciate this benefit. We call this *referential transparency*. Because functions have no side effects, if we are building a program which computes things, we can speed up the program. If the program knows that `func(2)` equates to `3`, we can store this in a table. This prevents the program from running the same function when we already know the answer.

Typically, in functional programming, we do not use loops. We use recursion. Recursion is a mathematical concept, it means “feeding into itself”. With a recursive function, the function calls itself as a sub-function. Here’s a nice example of a recursive function in Python:

    def factorial_recursive(n):
        # Base case: 1! = 1
        if n == 1:
        	return 1
        # Recursive case: n! = n * (n-1)!
        else:
        	return n * factorial_recursive(n-1)
    

Some programming languages are also **lazy**. This means they don’t compute or do anything until the very last second. If we write some code to perform `2 + 2`, a functional program will only calculate that when we need to use the resultant. We’ll explore laziness in Python soon.

---

# 🌍 How Does Python's Map Work?

To understand map, let’s first look at what iterables are. An iterable is anything we can iterate over. These are lists or arrays, but Python has many different iterables. We can even create our own iterable objects which by implementing magic methods. A magic method is like an API that helps our objects become more Pythonic. We need to implement 2 magic methods to make an object an iterable:

    class Counter: 
    	def __init__(self, low, high):
        	# set class attributes inside the magic method __init__
        	# for “initialise”
        	self.current = low
        	self.high = high
    	def __iter__(self):
        	# first magic method to make this object iterable
        	return self
      	def __next__(self):
        	# second magic method
        	if self.current > self.high:
          		raise StopIteration
        	else:
          		self.current += 1
    		return self.current - 1
    

The first magic method, `__iter__` or dunder iter (double underscore iter) returns the iterative object, we often use this at the start of a loop. Dunder next, `__next__`, returns what the next object is.

Let’s check this out:

    for c in Counter(3, 8):
    	print(c)
    

This will print:

    3
    4
    5
    6
    7
    8
    

In Python, an iterator is an object which only has an `__iter__` magic method. This means that we can access positions in the object, but cannot iterate through the object. Some objects will have the magic method `__next__` and not the `__iter__` magic method, such as *sets* (talked about later in this article). For this article, we’ll assume everything we touch is an iterable object.

Now we know what an iterable object is, let’s go back to the map function.

The map function lets us apply a function to every item in an iterable. We want to apply a function to every item in a list, but know that it’s possible for most iterables. The syntax for map takes 2 inputs, the function to apply and the iterable object.

    map(function, iterable)
    

Say we have a list of numbers like:

    [1, 2, 3, 4, 5]
    

And we want to square every number, we can write code like this:

    x = [1, 2, 3, 4, 5]
    def square(num):
    	return num*num
    print(list(map(square, x)))
    

Functional Python is lazy. If we didn’t include the `list()` the function would store the definition of the iterable, not the list itself. We need to tell Python *“turn this into a list”* for us to use this.

It’s weird to go from non-lazy evaluation to lazy evaluation suddenly in Python. You’ll get used to it if you think more in the functional mindset than an imperative mindset.

Now it’s nice to write a normal function like `square(num)` but it doesn’t look right. Do we have to define a whole function just to use it once in a map? Well, we can define a function in map using a *lambda (anonymous) function.*

---

# 🔑 Lambda Expressions in Python

Lambda functions are a one-line function, used for a short period of time. We often use them with higher order functions along with filter, map, and reduce. This lambda expression squares a number given to it:

    square = lambda x: x * x
    

Now let’s run this:

    >>> square(3)
    9
    

I hear you. “Brandon, where are the arguments? what the heck is this? that looks nothing like a function?”

Well, it’s confusing but can be explained. We’re assigning something to the variable `square`. this part:

    lambda x:
    

Tells Python that this is a lambda function, and the input is called x. Anything after the colon is what we do with the input, and it returns whatever the result of that is.

To simplfy our square program into one line we can do:

    x = [1, 2, 3, 4, 5]
    print(list(map(lambda num: num * num, x)))
    

In a lambda expression, all the arguments go on the left and the stuff we want to do with them go on the right. It gets a little messy, no one can deny that. There’s a certain pleasure in writing code that only other functional programmers can read. Also, it’s super cool to take a function and turn it into a one-liner.

---

# 🔹 Reduce Function in Python

Reduce is a function that applies a given function on an iterable and returns one thing. Normally we’ll perform a computation on a list to reduce it down to one number. Reduce looks like this:

    reduce(function, list)
    

We can (and often will) use lambda expressions as the function.

The product of a list is every single number multiplied together. To program this:

    product = 1
    x = [1, 2, 3, 4]
    for num in x:
    	product = product * num
    

But with reduce we can write:

    from functools import reduce
    product = reduce((lambda x, y: x * y),[1, 2, 3, 4])
    

To get the same product. The code is shorter, and with knowledge of functional programming, it is neater.

---

# 🍳 Filter

The filter function takes an iterable and filters out all the things we don’t want in that iterable.

Filter takes a function and a list. It applies the function to each item in the list and if that function returns True, it does nothing. If it returns False, it removes that item from the list.

The syntax looks like:

    filter(function, list)
    

Let’s see a small example, without filter we’ll write:

    x = range(-5, 5)
    new_list = []
    for num in x:
    	if num < 0:
    		new_list.append(num)
    

With filter, this becomes:

    x = range(-5, 5)
    all_less_than_zero = list(filter(lambda num: num < 0, x))
    

---

# ☁ Higher Order Functions in Python

Higher order functions can take functions as parameters and return functions. An example is:

    def summation(nums):
    	return sum(nums)
    def action(func, numbers):
    	return func(numbers)
    print(action(summation, [1, 2, 3]))
    # Output is 6
    

Or an simple example of the second definition, `return functions`, is:

    def rtnBrandon():
    	return “brandon”
    def rtnJohn():
    	return “john”
    def rtnPerson():
    	age = int(input(“What’s your age?”))
    	if age == 21:
        	return rtnBrandon()
    	else:
        	return rtnJohn()
    

Higher-order functions make non-varying variables easier to work with. We need not store a variable anywhere if all we’re doing is passing data through a long tunnel of functions.

All functions in Python are first-class objects. We define a first-class object as having one or more of these features:

- Created at runtime
- Assigned to a variable or element in a data structure
- Passed as an argument to a function
- Returned as the result of a function

So all functions in Python are first-class and can be used as a higher-order function.

---

# 🎶 Partial Application with Functions

Partial application (also called closures) is weird but is cool. We can call a function without supplying all the arguments it requires. Let’s see this in an example. We want to create a function which takes 2 arguments, a base and an exponent, and returns base to the power of the exponent, like so:

    def power(base, exponent):
    	return base ** exponent
    

Now we want to have a dedicated square function, to work out the square of a number using the power function:

    def square(base):
    	return power(base, 2)
    

This works, but what if we want a cube function? or a function to the power of 4? Can we keep on writing them forever? Well, we could. But programmers are lazy. If we repeatedly do the same thing, it’s a sign that there is a much quicker way to speed things up and that will allow us to not repeat things. We can use partial applications here. Let’s see an example of the square function using a partial application:

    from functools import partial
    square = partial(power, exponent=2)
    print(square(2))
    # output is 4
    

Isn’t that cool! We can call functions which require 2 arguments, using only 1 argument by telling Python what the second argument is.

We can also use a loop, to generate a power function that works from cubed up to powers of 1000.

    from functools import partial
    powers = []
    for x in range(2, 1001):
    	powers.append(partial(power, exponent = x))
    print(powers[0](3))
    # output is 9
    

---

# 🐍 Functional Programming Isn’t Pythonic

You might have noticed, but a lot of the things we want to do in functional programming revolve around lists. Other than the reduce function & partial application, all the functions we have seen generate lists. Guido (the inventor of Python) dislikes functional stuff in Python because Python already has its own way to generate lists.

If we write “import this” into a Python IDLE session, we’ll get:

    >>> import this
    The Zen of Python, by Tim Peters
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren’t special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you’re Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it’s a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let’s do more of those!
    

This is the Zen of Python. It’s a poem about what something being Pythonic means. The part we want to relate to here is:

There should be one — and preferably only one — obvious way to do it.

In Python, map & filter can do the same things as a list comprehension (discussed next). This breaks one rule of the Zen of Python, so these parts of functional programming ‘pythonic’.

Another talking point is Lambda. In Python, a lambda function is a normal function. Lambda is syntactic sugar. Both are equivalent:

    foo = lambda a: 2
    def foo(a):
    	return 2
    

A regular function can do everything a lambda function can, but it doesn’t work the other way around. A lambda function cannot do everything that a regular function can do.

This was a short argument about why functional programming doesn’t fit into the whole Python ecosystem very well. You may have noticed I mentioned list comprehensions earlier, we’ll discuss them now.

---

# 🎓 List Comprehensions

Earlier, I mentioned that anything we could do with map or filter, we could do with a list comprehension. This is the part where we’ll learn about them.

A list comprehension is a way to generate lists in Python. The syntax is:

    [function for item in iterable]
    

So let’s square every number in a list, as an example:

    print([x * x for x in [1, 2, 3, 4]])
    

Okay, so we can see how we can apply a function to every item in a list. How do we go around applying a filter? Well, look at this code from earlier:

    x = range(-5, 5)
    all_less_than_zero = list(filter(lambda num: num < 0, x))
    print(all_less_than_zero)
    

We can convert this into a list comprehension like so:

    x = range(-5, 5)
    all_less_than_zero = [num for num in x if num < 0]
    

List comprehensions support if statements like this. We no longer need to apply a million functions to something to get what you want. If we’re trying to make some kind of list chances are that it’ll look cleaner and easier using a list comprehension.

What if we want to square every number below 0 in a list? Well, with lambda, map and filter we’ll write:

    x = range(-5, 5)
    all_less_than_zero = list(map(lambda num: num * num, list(filter(lambda num: num < 0, x))))
    

This is long and complicated. With a list comprehension it is:

    x = range(-5, 5)
    all_less_than_zero = [num * num for num in x if num < 0]
    

A list comprehension is only good for, well, lists. Map and filter work on any iterable, so what’s up with that? We can use any comprehension for any iterable object we encounter.

---

# 🤔 Comprehensions of Any Iterable

We can generate any iterable using a comprehension. Since Python 2.7, we can even generate a dictionary (hashmap).
```python
# Taken from page 70 chapter 3 of Fluent Python by Luciano Ramalho
DIAL_CODES = [ 
    (86, ‘China’),
    (91, ‘India’),
    (1, ‘United States’),
    (62, ‘Indonesia’),
    (55, ‘Brazil’),
    (92, ‘Pakistan’),
    (880, ‘Bangladesh’),
    (234, ‘Nigeria’),
    (7, ‘Russia’),
    (81, ‘Japan’),
    ]
>>> country_code = {country: code for code, country in DIAL_CODES}
>>> country_code
{’Brazil’: 55, ‘Indonesia’: 62, ‘Pakistan’: 92, ‘Russia’: 7, ‘China’: 86, ‘United States’: 1, ‘Japan’: 81, ‘India’: 91, ‘Nigeria’: 234, ‘Bangladesh’: 880}
>>> {code: country.upper() for country, code in country_code.items() if code < 66}
{1: ‘UNITED STATES’, 7: ‘RUSSIA’, 62: ‘INDONESIA’, 55: ‘BRAZIL’}
```
    

If it’s an iterable, we can generate it. Let’s look at one last example of sets. If you don’t know what a set is, [check out this other article I wrote](/a-primer-on-set-theory/). The TL;DR is:

- Sets are lists of elements, no element is repeated twice in that list
- The order in sets do not matter.

```python
# taken from page 87, chapter 3 of Fluent Python by Luciano Ramalho
>>> from unicodedata import name
>>> {chr(i) for i in range(32, 256) if ‘SIGN’ in name(chr(i), ‘’)}
{’×’, ‘¥’, ‘°’, ‘£’, ‘©’, ‘#’, ‘¬’, ‘%’, ‘µ’, ‘>‘, ‘¤’, ‘±’, ‘¶’, ‘§’, ‘<’, ‘=’, ‘®’, ‘$’, ‘÷’, ‘¢’, ‘+’}
```

You may notice that sets have the same curly braces as dictionaries. Python is smart. It’ll know whether we're writing a dictionary comprehension or a set comprehension based on whether we provide the extra value for the dictionary or not. If you want to learn more about comprehensions, check out this [visual guide](https://treyhunner.com/2015/12/python-list-comprehensions-now-in-color/).

---

# 👋 Conclusion

Functional programming is beautiful and pure. Functional code can be clean, but it can also be messy. You should use what you want to use.