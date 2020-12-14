---
title: Timsort — the fastest sorting algorithm you’ve never heard of
slug: timsort
date_published: 2019-01-11T16:00:00.000Z
date: 2019-10-10T16:17:20.000Z
tags: 
    - Computer Science
    - Popular
excerpt:  A very fast , O(n log n), stable sorting algorithm built for the real world — not constructed in academia.
---

Timsort: A very fast , O(n log n), stable sorting algorithm built for the real world — not constructed in academia.
![](https://cdn-images-1.medium.com/max/600/0*kZKyCrzT9YvXBtT9.jpg)Image of Tim Peter from [here](https://www.youtube.com/watch?v=1wAOy88WxmY)
Timsort is a sorting algorithm that is efficient for real-world data and not created in an academic laboratory. Tim Peters created Timsort for the Python programming language in 2001. Timsort first analyses the list it is trying to sort and then chooses an approach based on the analysis of the list.

Since the algorithm has been invented it has been used as the default sorting algorithm in Python, [Java](https://bugs.java.com/bugdatabase/view_bug.do?bug_id=6804124), the [Android ](http://www.kiwidoc.com/java/l/x/android/android/5/p/java.util/c/TimSort)Platform, and in GNU Octave.

Timsort’s [big O notation](https://skerritt.blog/big-o/) is O(n log n). To learn about Big O notation, read [this](https://skerritt.blog/big-o/).
![](https://cdn-images-1.medium.com/max/800/1*1CkG3c4mZGswDShAV9eHbQ.png)From [here](http://bigocheatsheet.com/)
Timsort’s sorting time is the same as Mergesort, which is faster than most of the other sorts you might know. Timsort actually makes use of Insertion sort and Mergesort, as you’ll see soon.

Peters designed Timsort to use already-ordered elements that exist in most real-world data sets. It calls these already-ordered elements “natural runs”. It iterates over the data collecting the elements into runs and simultaneously merging those runs together into one.

---

### **The array has fewer than 64 elements in it**

If the array we are trying to sort has fewer than 64 elements in it, Timsort will execute an insertion sort.

An insertion sort is a simple sort which is most effective on small lists. It is quite slow at larger lists, but very fast with small lists. The idea of an insertion sort is as follows:

- Look at elements one by one
- Build up sorted list by inserting the element at the correct location

![](https://cdn-images-1.medium.com/max/800/1*3bMtqGONwfRvPMvVf8zfJQ.png)Image taken by me, from my website [skerritt.tech](https://skerritt.tech)
In this instance we are inserting the newly sorted elements into a new sub-array, which starts at the start of the array.

Here’s a gif showing insertion sort:
![](https://cdn-images-1.medium.com/max/800/0*I8VlK7-Zh-2btQP4.gif)Taken from [here](https://upload.wikimedia.org/wikipedia/commons/9/9c/Insertion-sort-example.gif)
---

### **More about runs**

If the list is larger than 64 elements than the algorithm will make a first pass through the list looking for parts that are strictly increasing or decreasing. If the part is decreasing, it will reverse that part.

So if the run is decreasing, it’ll look like this (where the run is in bold):
![](https://cdn-images-1.medium.com/max/800/1*LWJSZ8DHZ2DNF8aeVyGpig.png)Image from my website, [skerritt.tech](https://skerritt.tech/)
If not decreasing, it’ll look like this:
![](https://cdn-images-1.medium.com/max/800/1*r96puBtKKiF6-Rj3DKjOUA.png)Image from my website, [skerritt.tech](https://skerritt.tech/)
The minrun is a size which is determined based on the size of the array. The algorithm selects it so that most runs in a random array are, or become minrun, in length. Merging 2 arrays is more efficient when the number of runs is equal to, or slightly less than, a power of two. Timsort chooses minrun to try to ensure this efficiency, by making sure minrun is equal to or less than a power of two.

The algorithm chooses minrun from the range 32 to 64 inclusive. It chooses minrun such that the length of the original array, when divided by minrun, is equal to or slightly less than a power of two.

If the length of the run is less than minrun, you calculate the length of that run away from minrun. Using this new number, you grab that many items ahead of the run and perform an insertion sort to create a new run.

So if minrun is 63 and the length of the run is 33, you do 63–33 = 30. You then grab 30 elements from in front of the end of the run, so this is 30 items from run[33] and then perform an insertion sort to create a new run.

After this part has completed we should now have a bunch of sorted runs in a list.

---

### **Merging**

[https://giphy.com/gifs/dragon-ball-z-dbz-UfaSEmvHQtrEI](https://giphy.com/gifs/dragon-ball-z-dbz-UfaSEmvHQtrEI)

Timsort now performs mergesort to merge the runs together. However, Timsort makes sure to maintain stability and merge balance whilst merge sorting.

To maintain stability we should not exchange 2 numbers of equal value. This not only keeps their original positions in the list but enables the algorithm to be faster. We will shortly discuss the merge balance.

As Timsort finds runs, it adds them to a stack. A simple stack would look like this:
![](https://cdn-images-1.medium.com/max/800/1*sJ4GSPsTvUdIYQIR2pbKig.png)Image from my website, [skerritt.tech](https://skerritt.tech/)
Imagine a stack of plates. You cannot take plates from the bottom, so you have to take them from the top. The same is true about a stack.

Timsort tries to balance two competing needs when mergesort runs. On one hand, we would like to delay merging as long as possible in order to exploit patterns that may come up later. But we would like even more to do the merging as soon as possible to exploit the run that the run just found is still high in the memory hierarchy. We also can’t delay merging “too long” because it consumes memory to remember the runs that are still unmerged, and the stack has a fixed size.

To make sure we have this compromise, Timsort keeps track of the three most recent items on the stack and creates two laws that must hold true of those items:

1. A > B + C

2. B > C

Where A, B and C are the three most recent items on the stack.

In the words of Tim Peters himself:

> *What turned out to be a good compromise maintains two invariants on the stack entries, where A, B and C are the lengths of the three righmost not-yet merged slices*

Usually, merging adjacent runs of different lengths in place is hard. What makes it even harder is that we have to maintain stability. To get around this, Timsort sets aside temporary memory. It places the smaller (calling both runs A and B) of the two runs into that temporary memory.

---

### **Galloping**

[https://giphy.com/gifs/horse-riding-yNldIEA9XD7TW](https://giphy.com/gifs/horse-riding-yNldIEA9XD7TW)

While Timsort is merging A and B, it notices that one run has been “winning” many times in a row. If it turned out that the run A consisted of entirely smaller numbers than the run B then the run A would end up back in its original place. Merging the two runs would involve a lot of work to achieve nothing.

More often than not, data will have some preexisting internal structure. Timsort assumes that if a lot of run A’s values are lower than run B’s values, then it is likely that A will continue to have smaller values than B.
![](/content/images/2019/01/image-505.png)
Image of 2 example runs, A and B. Runs have to be strictly increasing or decreasing, hence why these numbers were picked.

Timsort will then enter galloping mode. Instead of checking A[0] and B[0] against each other, Timsort performs a binary search for the appropriate position of b[0] in a[0]. This way, Timsort can move a whole section of A into place. Then Timsort searches for the appropriate location of A[0] in B. Timsort will then move a whole section of B can at once, and into place.

Let’s see this in action. Timsort checks B[0] (which is 5) and using a binary search it looks for the correct location in A.

Well, B[0] belongs at the back of the list of A. Now Timsort checks for A[0] (which is 1) in the correct location of B. So we’re looking to see where the number 1 goes. This number goes at the start of B. We now know that B belongs at the end of A and A belongs at the start of B.

It turns out, this operation is not worth it if the appropriate location for B[0] is very close to the beginning of A (or vice versa). so gallop mode quickly exits if it isn’t paying off. Additionally, Timsort takes note and makes it harder to enter gallop mode later by increasing the number of consecutive A-only or B-only wins required to enter. If gallop mode is paying off, Timsort makes it easier to reenter.

In short, Timsort does 2 things incredibly well:

- Great performance on arrays with preexisting internal structure
- Being able to maintain a stable sort

Previously, in order to achieve a stable sort, you’d have to zip the  items in your list up with integers, and sort it as an array of tuples.

---

### **Code**

If you’re not interested in the code, feel free to skip this part. There’s some more information below this section.

The source code below is based on mine and Nanda Javarma’s work. The source code is not complete, nor is it similar to Python’s offical sorted() source code. This is just a dumbed-down Timsort I implemented to get a general feel of Timsort. If you want to see Timsort’s original source code in all its glory, check it out [here](https://github.com/python/cpython/blob/master/Objects/listobject.c). Timsort is offically implemented in C, not Python.

Timsort is actually built right into Python, so this code only serves as an explainer. To use Timsort simply write:

    list.sort()

Or

    sorted(list)

If you want to master how Timsort works and get a feel for it, I highly suggest you try to implement it yourself!

This article is based on Tim Peters’ original introduction to Timsort, found [here](https://bugs.python.org/file4451/timsort.txt).

---

Hey 👋 Want to subscribe to my blog and stay up to date with posts similar to this one? Subscribe to my email list below. I won't spam you. I will only send you posts similar to this one 😊✨

# Like this article? 🔥

Sign up and get more content like this 😁✨

Subscribe

We won't send you spam. Unsubscribe at any time.
[Powered By ConvertKit](https://convertkit.com/?utm_source=dynamic&amp;utm_medium=referral&amp;utm_campaign=poweredby&amp;utm_content=form)
.formkit-form[data-uid="4028200a82"] *{font-family:"Helvetica Neue",Helvetica,Arial,Verdana,sans-serif;box-sizing:border-box;}.formkit-form[data-uid="4028200a82"]{-webkit-font-smoothing:antialiased;-moz-osx-font-smoothing:grayscale;}.formkit-form[data-uid="4028200a82"] legend{border:none;font-size:inherit;margin-bottom:10px;padding:0;position:relative;display:table;}.formkit-form[data-uid="4028200a82"] fieldset{border:0;padding:0.01em 0 0 0;margin:0;min-width:0;}.formkit-form[data-uid="4028200a82"] body:not(:-moz-handler-blocked) fieldset{display:table-cell;}.formkit-form[data-uid="4028200a82"] h1,.formkit-form[data-uid="4028200a82"] h2,.formkit-form[data-uid="4028200a82"] h3,.formkit-form[data-uid="4028200a82"] h4,.formkit-form[data-uid="4028200a82"] h5,.formkit-form[data-uid="4028200a82"] h6{color:inherit;font-size:inherit;font-weight:inherit;}.formkit-form[data-uid="4028200a82"] p{color:inherit;font-size:inherit;font-weight:inherit;}.formkit-form[data-uid="4028200a82"][data-format="modal"]{display:none;}.formkit-form[data-uid="4028200a82"][data-format="slide in"]{display:none;}.formkit-form[data-uid="4028200a82"] .formkit-input,.formkit-form[data-uid="4028200a82"] .formkit-select,.formkit-form[data-uid="4028200a82"] .formkit-checkboxes{width:100%;}.formkit-form[data-uid="4028200a82"] .formkit-button,.formkit-form[data-uid="4028200a82"] .formkit-submit{border:0;border-radius:5px;color:#ffffff;cursor:pointer;display:inline-block;text-align:center;font-size:15px;font-weight:500;cursor:pointer;margin-bottom:15px;overflow:hidden;padding:0;position:relative;vertical-align:middle;}.formkit-form[data-uid="4028200a82"] .formkit-button:hover,.formkit-form[data-uid="4028200a82"] .formkit-submit:hover,.formkit-form[data-uid="4028200a82"] .formkit-button:focus,.formkit-form[data-uid="4028200a82"] .formkit-submit:focus{outline:none;}.formkit-form[data-uid="4028200a82"] .formkit-button:hover > span,.formkit-form[data-uid="4028200a82"] .formkit-submit:hover > span,.formkit-form[data-uid="4028200a82"] .formkit-button:focus > span,.formkit-form[data-uid="4028200a82"] .formkit-submit:focus > span{background-color:rgba(0,0,0,0.1);}.formkit-form[data-uid="4028200a82"] .formkit-button > span,.formkit-form[data-uid="4028200a82"] .formkit-submit > span{display:block;-webkit-transition:all 300ms ease-in-out;transition:all 300ms ease-in-out;padding:12px 24px;}.formkit-form[data-uid="4028200a82"] .formkit-input{background:#ffffff;font-size:15px;padding:12px;border:1px solid #e3e3e3;-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;line-height:1.4;margin:0;-webkit-transition:border-color ease-out 300ms;transition:border-color ease-out 300ms;}.formkit-form[data-uid="4028200a82"] .formkit-input:focus{outline:none;border-color:#1677be;-webkit-transition:border-color ease 300ms;transition:border-color ease 300ms;}.formkit-form[data-uid="4028200a82"] .formkit-input::-webkit-input-placeholder{color:#848585;}.formkit-form[data-uid="4028200a82"] .formkit-input::-moz-placeholder{color:#848585;}.formkit-form[data-uid="4028200a82"] .formkit-input:-ms-input-placeholder{color:#848585;}.formkit-form[data-uid="4028200a82"] .formkit-input::placeholder{color:#848585;}.formkit-form[data-uid="4028200a82"] [data-group="dropdown"]{position:relative;display:inline-block;width:100%;}.formkit-form[data-uid="4028200a82"] [data-group="dropdown"]::before{content:"";top:calc(50% - 2.5px);right:10px;position:absolute;pointer-events:none;border-color:#4f4f4f transparent transparent transparent;border-style:solid;border-width:6px 6px 0 6px;height:0;width:0;z-index:999;}.formkit-form[data-uid="4028200a82"] [data-group="dropdown"] select{height:auto;width:100%;cursor:pointer;color:#333333;line-height:1.4;margin-bottom:0;padding:0 6px;-webkit-appearance:none;-moz-appearance:none;appearance:none;font-size:15px;padding:12px;padding-right:25px;border:1px solid #e3e3e3;background:#ffffff;}.formkit-form[data-uid="4028200a82"] [data-group="dropdown"] select:focus{outline:none;}.formkit-form[data-uid="4028200a82"] [data-group="checkboxes"]{text-align:left;margin:0;}.formkit-form[data-uid="4028200a82"] [data-group="checkboxes"] [data-group="checkbox"]{margin-bottom:10px;}.formkit-form[data-uid="4028200a82"] [data-group="checkboxes"] [data-group="checkbox"] *{cursor:pointer;}.formkit-form[data-uid="4028200a82"] [data-group="checkboxes"] [data-group="checkbox"]:last-of-type{margin-bottom:0;}.formkit-form[data-uid="4028200a82"] [data-group="checkboxes"] [data-group="checkbox"] input[type="checkbox"]{display:none;}.formkit-form[data-uid="4028200a82"] [data-group="checkboxes"] [data-group="checkbox"] input[type="checkbox"] + label::after{content:none;}.formkit-form[data-uid="4028200a82"] [data-group="checkboxes"] [data-group="checkbox"] input[type="checkbox"]:checked + label::after{border-color:#ffffff;content:"";}.formkit-form[data-uid="4028200a82"] [data-group="checkboxes"] [data-group="checkbox"] input[type="checkbox"]:checked + label::before{background:#10bf7a;border-color:#10bf7a;}.formkit-form[data-uid="4028200a82"] [data-group="checkboxes"] [data-group="checkbox"] label{position:relative;display:inline-block;padding-left:28px;}.formkit-form[data-uid="4028200a82"] [data-group="checkboxes"] [data-group="checkbox"] label::before,.formkit-form[data-uid="4028200a82"] [data-group="checkboxes"] [data-group="checkbox"] label::after{position:absolute;content:"";display:inline-block;}.formkit-form[data-uid="4028200a82"] [data-group="checkboxes"] [data-group="checkbox"] label::before{height:16px;width:16px;border:1px solid #e3e3e3;background:#ffffff;left:0px;top:3px;}.formkit-form[data-uid="4028200a82"] [data-group="checkboxes"] [data-group="checkbox"] label::after{height:4px;width:8px;border-left:2px solid #4d4d4d;border-bottom:2px solid #4d4d4d;-webkit-transform:rotate(-45deg);-ms-transform:rotate(-45deg);transform:rotate(-45deg);left:4px;top:8px;}.formkit-form[data-uid="4028200a82"] .formkit-alert{background:#f9fafb;border:1px solid #e3e3e3;border-radius:5px;-webkit-flex:1 0 auto;-ms-flex:1 0 auto;flex:1 0 auto;list-style:none;margin:25px auto;padding:12px;text-align:center;width:100%;}.formkit-form[data-uid="4028200a82"] .formkit-alert:empty{display:none;}.formkit-form[data-uid="4028200a82"] .formkit-alert-success{background:#d3fbeb;border-color:#10bf7a;color:#0c905c;}.formkit-form[data-uid="4028200a82"] .formkit-alert-error{background:#fde8e2;border-color:#f2643b;color:#ea4110;}.formkit-form[data-uid="4028200a82"] .formkit-spinner{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;height:0px;width:0px;margin:0 auto;position:absolute;top:0;left:0;right:0;width:0px;overflow:hidden;text-align:center;-webkit-transition:all 300ms ease-in-out;transition:all 300ms ease-in-out;}.formkit-form[data-uid="4028200a82"] .formkit-spinner > div{margin:auto;width:12px;height:12px;background-color:#fff;opacity:0.3;border-radius:100%;display:inline-block;-webkit-animation:formkit-bouncedelay-formkit-form-data-uid-4028200a82- 1.4s infinite ease-in-out both;animation:formkit-bouncedelay-formkit-form-data-uid-4028200a82- 1.4s infinite ease-in-out both;}.formkit-form[data-uid="4028200a82"] .formkit-spinner > div:nth-child(1){-webkit-animation-delay:-0.32s;animation-delay:-0.32s;}.formkit-form[data-uid="4028200a82"] .formkit-spinner > div:nth-child(2){-webkit-animation-delay:-0.16s;animation-delay:-0.16s;}.formkit-form[data-uid="4028200a82"] .formkit-submit[data-active] .formkit-spinner{opacity:1;height:100%;width:50px;}.formkit-form[data-uid="4028200a82"] .formkit-submit[data-active] .formkit-spinner ~ span{opacity:0;}@-webkit-keyframes formkit-bouncedelay-formkit-form-data-uid-4028200a82-{0%,80%,100%{-webkit-transform:scale(0);-ms-transform:scale(0);transform:scale(0);}40%{-webkit-transform:scale(1);-ms-transform:scale(1);transform:scale(1);}}@keyframes formkit-bouncedelay-formkit-form-data-uid-4028200a82-{0%,80%,100%{-webkit-transform:scale(0);-ms-transform:scale(0);transform:scale(0);}40%{-webkit-transform:scale(1);-ms-transform:scale(1);transform:scale(1);}} .formkit-form[data-uid="4028200a82"]{border:1px solid #e3e3e3;max-width:700px;position:relative;}.formkit-form[data-uid="4028200a82"] .formkit-background{width:100%;height:100%;position:absolute;top:0;left:0;background-size:cover;background-position:center;opacity:0.3;z-index:1;}.formkit-form[data-uid="4028200a82"] [data-style="minimal"]{padding:20px;width:100%;z-index:2;position:relative;}.formkit-form[data-uid="4028200a82"] .formkit-header{margin:0 0 27px 0;text-align:center;}.formkit-form[data-uid="4028200a82"] .formkit-subheader{margin:18px 0;text-align:center;}.formkit-form[data-uid="4028200a82"] .formkit-guarantee{font-size:13px;margin:10px 0 15px 0;text-align:center;}.formkit-form[data-uid="4028200a82"] .formkit-guarantee > p{margin:0;}.formkit-form[data-uid="4028200a82"] .formkit-powered-by{color:#7d7d7d;display:block;font-size:12px;margin:10px 0 0 0;text-align:center;}.formkit-form[data-uid="4028200a82"] .formkit-powered-by[data-active="false"]{opacity:0.5;}.formkit-form[data-uid="4028200a82"] .formkit-fields{display:-webkit-box;display:-webkit-flex;display:-ms-flexbox;display:flex;-webkit-flex-wrap:wrap;-ms-flex-wrap:wrap;flex-wrap:wrap;margin:25px auto 0 auto;}.formkit-form[data-uid="4028200a82"] .formkit-field{min-width:220px;}.formkit-form[data-uid="4028200a82"] .formkit-field,.formkit-form[data-uid="4028200a82"] .formkit-submit{margin:0 0 15px 0;-webkit-flex:1 0 100%;-ms-flex:1 0 100%;flex:1 0 100%;}.formkit-form[data-uid="4028200a82"][min-width~="600"] [data-style="minimal"]{padding:40px;}.formkit-form[data-uid="4028200a82"][min-width~="600"] .formkit-fields[data-stacked="false"]{margin-left:-5px;margin-right:-5px;}.formkit-form[data-uid="4028200a82"][min-width~="600"] .formkit-fields[data-stacked="false"] .formkit-field,.formkit-form[data-uid="4028200a82"][min-width~="600"] .formkit-fields[data-stacked="false"] .formkit-submit{margin:0 5px 15px 5px;}.formkit-form[data-uid="4028200a82"][min-width~="600"] .formkit-fields[data-stacked="false"] .formkit-field{-webkit-flex:100 1 auto;-ms-flex:100 1 auto;flex:100 1 auto;}.formkit-form[data-uid="4028200a82"][min-width~="600"] .formkit-fields[data-stacked="false"] .formkit-submit{-webkit-flex:1 1 auto;-ms-flex:1 1 auto;flex:1 1 auto;} 
If you're feeling extra generous, I have a [PayPal ](https://www.paypal.me/BrandonSkerritt) and even a [Patreon](https://www.patreon.com/user?u=15993188). I'm  a university student who writes these blogs in their spare time. This blog is my full time job, so any and all donations are appreciated!
