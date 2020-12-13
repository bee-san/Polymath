---
title: COMP201 - Software Engineering Revision
slug: comp201-software-engineering-revision
date_published: 2019-01-09T13:58:00.000Z
date_updated: 2019-04-28T11:22:05.000Z
tags: 
  - "University"
draft: true
excerpt: COMP201 Blog post featuring all slides that belong to the questions in the exam.
---

Answers to mock test [here](https://drive.google.com/file/d/1xR7zNu9_GgLheD6g9actk8HMNcw8BR55/view?usp=sharing) provided by [James Saeed](https://www.linkedin.com/in/james-s-320525127/). For my answers to the mock test, find them [here](https://drive.google.com/file/d/1Q4QhNFwCt17aW2Tg1tJZj77hlVLXIeXo/view?usp=sharing):

Hey all! You know that list of questions that'll be on the exam? Someone has organised by how many there are as well as what lecture slides they are:

Topic | Questions | Slides
Nets, Petri nets | 6Q | 8 - 10
Java programming (Private scope, Extends, dynamic binding) | 5Q | 17/19
Use cases | 5Q | 17
Security, Including Bell-laPudla | 5Q | 6
Testing | 5Q | 22-24
Functional/Non-functional requirements | 4Q | 4
Class diagram | 4Q | 19/20
Formal specification and ASML | 2Q | 11/12
Cohesion & coupling | 2Q | 2/4/6/7/9/10-12/14/17
UML Diagrams | 2Q | 18-21
Flow graphs & Testing | 2Q | 7
Interaction question | 2Q | 21
Project management | 2Q | 25
Methodology (Waterfall, incremental) | 2Q | 2
Code estimation | 1Q | 26
State charts| 1Q | 7
OO design inheritance & encapsulation | 1Q | 17

I ordered them by the lecture slide numbers instead of how many questions:

Topic | Questions | Slides
Cohesion & coupling | 2Q | 2/4/6/7/9/10-12/14/17
Methodology (Waterfall, incremental) | 2Q | 2
Functional/Non-functional requirements | 4Q | 4
Security, Including Bell-laPudla | 5Q | 6
Flow graphs & Testing | 2Q | 7
State charts| 1Q | 7
Nets, Petri nets | 6Q | 8 - 10
Formal specification and ASML | 2Q | 11/12
Use cases | 5Q | 17
OO design inheritance & encapsulation | 1Q | 17
Java programming (Private scope, Extends, dynamic binding) | 5Q | 17/19
Class diagram | 4Q | 19/20
UML Diagrams | 2Q | 18-21
Interaction question | 2Q | 21
Testing | 5Q | 22-24
Project management | 2Q | 25
Code estimation | 1Q | 26

This blog post features all lecture slides mentioned above. Enjoy ✨

# Unit testing

Individual components are tested
Module testing
Related collections of dependent components are tested
Sub-system testing (merges with system testing)
Modules are integrated into sub-systems and tested. The focus here should be on interface testing
System testing
Testing of the system as a whole. Testing of emergent properties
Acceptance testing
Testing with customer data to check that it is acceptable

# What is a requirement?

It may range from a high-level abstract statement of a service or of a system constraint to a detailed mathematical functional specification
This is inevitable as requirements may serve a dual function
May be the basis for a bid for a contract - therefore must be open to interpretation
May be the basis for the contract itself - therefore must be defined in detail
Both of these statements may be called requirements

# Types of requirements

User requirements
Statements in natural language plus diagrams of the services the system provides and its operational constraints. Written for customers
System requirements
A structured document setting out detailed descriptions of the system services. Written as a contract between client and contractor
Software specification
A detailed software description which can serve as a basis for a design or implementation. Written for developers

# Functional and non functional requirements

Functional requirements
Statements of services the system should provide, how the system should react to particular inputs and how the system should behave in particular situations
Non-functional requirements
constraints on the services or functions offered by the system such as timing constraints, constraints on the development process, standards, etc. Usually defined on the system as a whole
Domain requirements
Requirements that come from the application domain of the system and that reflect characteristics of that domain

# Requirements imprecision

Problems arise when requirements are not precisely stated
Ambiguous requirements may be interpreted in different ways by developers and users
Consider the term ‘recover password’ from previous slide..
User intention – mechanism which allows the user to view the password after going through an authentication procedure
Developer interpretation – allowing the user to reset their password so that it can be set again (e.g. using email link)
Before development is to commence requirements should be defined as precisely as possible

# guidelines for writing requirements

Invent a standard format and use it for all requirements
Use language in a consistent way. Use
shall for mandatory requirements (that must be supported),
should for desirable requirements (that are not essential).
See RFC 2119
Use text highlighting to identify key parts of the requirement
Avoid the use of computer jargon
Try and make documents self contained (e.g. include glossaries and complete examples)

A feasibility study decides whether or not the proposed system is worthwhile.

There are two types of interview
Closed interviews where a pre-defined set of questions are answered.
Open interviews where there is no pre-defined agenda and a range of issues are explored with stakeholders.

# Security

Broken down into 4 main issues
Confidentiality
Integrity
Authentication and Authorization
Non-repudiation
One auxiliary issue
Availability  (Performance security)

Usually two main options
Encryption	(hard security)
Permissions	(soft security)
Data must be kept secure
In storage (final or intermediary)
On the wire or wireless link
For as long as reasonably possible

Messages or data must not be modifiable without
Knowledge of the change
Integrity approaches
CRC Checking (no good, easy to forge check value)
Hash value over data, similar problem to CRC
Hash value over data + secret value
Key distribution problem
Hash value encrypted using asymmetric cipher
Best approach to date

Authentication
Who are you?
Authorization
What are you allowed to do?
Techniques
Usernames, Passwords, hardware (cards, dongles), Biometrics
Often first point of attack

May require
Trusted broker, third party
Funding in Escrow
Non repudiation is built on
Authentication
Integrity
Recording and time stamping
Broker style services

9s terminology not always useful
Imagine a computer system
Three 9s available but unavailability spread as 78 seconds per day
Or Five 9s available, failing once every 10 years for 50 minutes
So ideally to need specify
Worst case scenarios
Worst case delay as well as down time
How the system can degrade gracefully

Security is very dependent on knowledge of activity (audits and logs)
Standard log (records all logins/logouts, database access requests)
Failed login log (records all failed logins)
Unusual activity log (high volume transactions on account)
Alert log (failed logins for top level clearance users)
Alerts
Unusual activity can be used to alert operators, suspend accounts etc.

# Belle-LaPadula Model

All items given security clearance level
Top-Secret (4), Secret(3), Sensitive(2), Unclassified
no read-up
A subject cannot read a document above their clearance level
If I am cleared to level 2, I cannot read a level 3 or 4 document
no write-down
A document cannot be copied/included with another document with a lower security clearance
So if I want to add a top secret to a sensitive document the result will be a top secret document
If my classification is 2, I cannot produce an unclassified document
Trusted subjects
Can write documents down
Must be shown trustworthy with regard to the security policy

Ideally kept as open as possible to allow for
Upgrading of encryption algorithms and protocols
Security policy
Shredding documents
Secure disposal
Password reset protocols
Security training
Security audits
Standards compliance
Payment Card Industry Data Security Standard

# System Models

User requirements must be written in such a way that non-technical experts can understand them, e.g., by using natural language
Detailed system requirements may be expressed in a more technical way however
One widely used technique is to document the system specification as a set of system models
These are graphical representations which describe business processes and the system to be developed
They are an important bridge between the analysis and design processes

Data Flow Diagrams track and document how the data associated with a process is helpful to develop an overall understanding of the system
Data flow diagrams may also be used in showing the data exchange between a system and other systems in its environment

# Data flow diagrams

Data Flow Diagrams track and document how the data associated with a process is helpful to develop an overall understanding of the system

Data flow diagrams may also be used in showing the data exchange between a system and other systems in its environment

Data Flow Diagrams have an advantage in that they are simple and intuitive and can thus be shown to users who can help in validating the analysis

Developing data flow diagrams is usually a top-down process 

We begin by evaluating the overall process we wish to model before considering sub-processes

Data flow diagrams show a functional perspective where each transformation represents a single function or process which is particularly useful during requirements analysis since it shows end-to-end processing

DPD context diagram
![](/content/images/2019/01/image-114.png)![](/content/images/2019/01/image-115.png)level 0 DFD![](/content/images/2019/01/image-116.png)Level 1 DFD
# Statechart Diagrams

Statechart Diagrams (or State machine models ) show the behaviour of the system in response to external and internal events

They show the system’s responses to stimuli (the event-action paradigm) so are often used for modelling real-time systems

Statechart diagrams show system states as nodes and events as arcs between these nodes. When an event occurs, the system moves from one state to another

Statecharts are an integral part of the Unified Modeling Language (UML)

An initial state is denoted by a solid circle and is optional (sometimes the system will start in different places and thus the initial state should be omitted). 

If required, a final state can also be used; this is denoted by a solid circle with a ring around it.
![](/content/images/2019/01/image-118.png)
We use a level of abstraction so that we can observe the essential behaviour of the system we want to model. 

Rounded rectangles are used for states. Each state contains two components, the state name and a brief description of the action performed in that state (see next slide).
![](/content/images/2019/01/image-119.png)
Statecharts also allow the decomposition of a model into sub-models (see figure on next slide).

A brief description of the actions is included following the ‘do’ in each state (the word “do” is optional).

Can be complemented by tables describing the states and the stimuli.
![](/content/images/2019/01/image-120.png)
The label on an arc can denote the method called to move from one state to the next (the event).

A guard is used to ensure that the system only moves from one state to the other if the expression is satisfied.

A state can contain a subdiagram within it (also called a composite state). This is useful for example when we wish to model a subsystem or substates.

On the next slide, we can see all these elements of a UML statechart diagram
![](/content/images/2019/01/image-121.png)![](/content/images/2019/01/image-122.png)
Often have an Idle state where the process is not active

All states need some exit (no deadlock, even in error conditions)

Use multiple state charts to keep the design simple

Do NOT need to have a state chart as sub state of other state chart

System can be described by multiple state machines running concurrently

# Finite State Automata                 

 Finite State Machines (FSM), also known as Finite State Automata (FSA) are models of the behaviours of a system or a complex object, with a limited number of defined conditions or modes, where mode transitions change with circumstance.
![](/content/images/2019/01/image-125.png)
AAAAAAA, ABBA - any combination of A's and B's.

 A model of computation consisting of

a set of states, 

a start (initial) state, 

an input alphabet, and 

a transition function that maps input symbols 

	and current states to a next state

You may recall finite state

	machines (or automata)

	from COMP209.

Computation begins in the start state with an input string. It changes to new states depending on the transition function. 

states define behaviour and may produce actions 

state transitions are movement from one state to another 

rules or conditions must be met to allow a state transition

input events are either externally 

	or internally generated, which 

	may possibly trigger rules and 

	lead to state transitions.

A model is an abstract system view. Complementary types of model provide different system information.

Context models show the position of a system in its environment with other systems and processes.

Data flow models may be used to model the data processing in a system.

State machine models model the system’s behaviour in response to internal or external events

Computation begins in the start state with an input string. It changes to new states depending on the transition function. 

states define behaviour and may produce actions 

state transitions are movement from one state to another 

rules or conditions must be met to allow a state transition

input events are either externally 

	or internally generated, which 

	may possibly trigger rules and 

	lead to state transitions.

There are many variants, for instance, 

machines having actions (outputs) associated with transitions (Mealy machine) or states (Moore machine), 

multiple start states, 

transitions conditioned on no input symbol (a null) or more than one transition for a given symbol and state (nondeterministic finite state machine), 

one or more states designated as accepting states (recognizer), etc.

Finite state automata are like computers in that they receive input and process the input by changing states. 

The only output that we have seen finite automata produce so far is a yes/no at the end of processing. 

We will now look at two models of finite automata that produce more output than a yes/no. 

Basically a Moore machine is just a FSA with two extra attributes. 

1. It has TWO alphabets, an input and output alphabet. 
2. It has an output letter associated with each state. The machine writes the appropriate output letter as it enters each state. 

![](/content/images/2019/01/image-128.png)![](/content/images/2019/01/image-129.png)![](/content/images/2019/01/image-130.png)![](/content/images/2019/01/image-131.png)
Mealy machines are complete in the sense that there is a transition for each character in the input alphabet leaving every state. 

There are no accept states in a Mealy machine because it is not a language recogniser, it is an output producer. Its output will be the same length as its input. 

# Petri Nets

Petri Nets were developed originally by Carl Adam Petri (when he was 12), and were the subject of his dissertation in 1962. 

Originally to model chemical reactions

Since then, Petri Nets and their concepts have been extended, developed, and applied in a variety of areas.

While the mathematical properties of Petri Nets are interesting and useful, the beginner will find that a good approach is to learn to model systems by constructing them graphically.
![](/content/images/2019/01/image-132.png)![](/content/images/2019/01/image-133.png)![](/content/images/2019/01/image-134.png)![](/content/images/2019/01/image-135.png)![](/content/images/2019/01/image-136.png)![](/content/images/2019/01/image-137.png)![](/content/images/2019/01/image-138.png)![](/content/images/2019/01/image-139.png)![](/content/images/2019/01/image-140.png)![](/content/images/2019/01/image-141.png)![](/content/images/2019/01/image-144.png)![](/content/images/2019/01/image-145.png)![](/content/images/2019/01/image-146.png)![](/content/images/2019/01/image-147.png)![](/content/images/2019/01/image-148.png)![](/content/images/2019/01/image-149.png)![](/content/images/2019/01/image-150.png)![](/content/images/2019/01/image-151.png)![](/content/images/2019/01/image-152.png)![](/content/images/2019/01/image-153.png)![](/content/images/2019/01/image-154.png)![](/content/images/2019/01/image-155.png)![](/content/images/2019/01/image-156.png)![](/content/images/2019/01/image-157.png)![](/content/images/2019/01/image-158.png)![](/content/images/2019/01/image-159.png)![](/content/images/2019/01/image-160.png)![](/content/images/2019/01/image-161.png)![](/content/images/2019/01/image-162.png)
TODO lecture 10
![](/content/images/2019/01/image-163.png)![](/content/images/2019/01/image-164.png)![](/content/images/2019/01/image-165.png)![](/content/images/2019/01/image-166.png)![](/content/images/2019/01/image-167.png)![](/content/images/2019/01/image-168.png)![](/content/images/2019/01/image-169.png)![](/content/images/2019/01/image-170.png)![](/content/images/2019/01/image-171.png)![](/content/images/2019/01/image-172.png)![](/content/images/2019/01/image-173.png)![](/content/images/2019/01/image-174.png)![](/content/images/2019/01/image-175.png)![](/content/images/2019/01/image-176.png)![](/content/images/2019/01/image-177.png)![](/content/images/2019/01/image-178.png)![](/content/images/2019/01/image-179.png)![](/content/images/2019/01/image-180.png)![](/content/images/2019/01/image-181.png)![](/content/images/2019/01/image-182.png)![](/content/images/2019/01/image-183.png)![](/content/images/2019/01/image-184.png)![](/content/images/2019/01/image-185.png)![](/content/images/2019/01/image-186.png)![](/content/images/2019/01/image-187.png)
# Formal Specification
![](/content/images/2019/01/image-188.png)![](/content/images/2019/01/image-189.png)![](/content/images/2019/01/image-190.png)![](/content/images/2019/01/image-191.png)![](/content/images/2019/01/image-192.png)![](/content/images/2019/01/image-193.png)![](/content/images/2019/01/image-194.png)![](/content/images/2019/01/image-195.png)![](/content/images/2019/01/image-196.png)![](/content/images/2019/01/image-197.png)![](/content/images/2019/01/image-198.png)![](/content/images/2019/01/image-199.png)![](/content/images/2019/01/image-200.png)![](/content/images/2019/01/image-201.png)![](/content/images/2019/01/image-202.png)![](/content/images/2019/01/image-203.png)![](/content/images/2019/01/image-204.png)![](/content/images/2019/01/image-205.png)![](/content/images/2019/01/image-206.png)![](/content/images/2019/01/image-207.png)![](/content/images/2019/01/image-208.png)![](/content/images/2019/01/image-209.png)![](/content/images/2019/01/image-210.png)![](/content/images/2019/01/image-211.png)![](/content/images/2019/01/image-212.png)![](/content/images/2019/01/image-213.png)![](/content/images/2019/01/image-214.png)![](/content/images/2019/01/image-215.png)![](/content/images/2019/01/image-216.png)![](/content/images/2019/01/image-217.png)![](/content/images/2019/01/image-218.png)![](/content/images/2019/01/image-219.png)![](/content/images/2019/01/image-220.png)![](/content/images/2019/01/image-221.png)![](/content/images/2019/01/image-222.png)![](/content/images/2019/01/image-223.png)![](/content/images/2019/01/image-224.png)![](/content/images/2019/01/image-225.png)![](/content/images/2019/01/image-226.png)![](/content/images/2019/01/image-227.png)![](/content/images/2019/01/image-228.png)
 We're going to skip a bunch of slides now because the questions skp slides, but I'm going to include the stuff that looks important.
![](/content/images/2019/01/image-229.png)![](/content/images/2019/01/image-230.png)![](/content/images/2019/01/image-231.png)![](/content/images/2019/01/image-232.png)
# Use cases
![](/content/images/2019/01/image-233.png)![](/content/images/2019/01/image-234.png)![](/content/images/2019/01/image-235.png)![](/content/images/2019/01/image-236.png)![](/content/images/2019/01/image-237.png)![](/content/images/2019/01/image-238.png)![](/content/images/2019/01/image-239.png)![](/content/images/2019/01/image-240.png)![](/content/images/2019/01/image-241.png)![](/content/images/2019/01/image-242.png)![](/content/images/2019/01/image-243.png)![](/content/images/2019/01/image-244.png)![](/content/images/2019/01/image-245.png)![](/content/images/2019/01/image-246.png)![](/content/images/2019/01/image-247.png)![](/content/images/2019/01/image-248.png)![](/content/images/2019/01/image-249.png)![](/content/images/2019/01/image-250.png)![](/content/images/2019/01/image-251.png)![](/content/images/2019/01/image-252.png)![](/content/images/2019/01/image-253.png)![](/content/images/2019/01/image-254.png)![](/content/images/2019/01/image-255.png)![](/content/images/2019/01/image-256.png)![](/content/images/2019/01/image-257.png)![](/content/images/2019/01/image-258.png)![](/content/images/2019/01/image-259.png)![](/content/images/2019/01/image-260.png)![](/content/images/2019/01/image-261.png)![](/content/images/2019/01/image-262.png)
# UML
![](/content/images/2019/01/image-263.png)![](/content/images/2019/01/image-264.png)![](/content/images/2019/01/image-265.png)![](/content/images/2019/01/image-266.png)![](/content/images/2019/01/image-267.png)![](/content/images/2019/01/image-268.png)![](/content/images/2019/01/image-269.png)![](/content/images/2019/01/image-270.png)![](/content/images/2019/01/image-271.png)![](/content/images/2019/01/image-272.png)![](/content/images/2019/01/image-273.png)![](/content/images/2019/01/image-274.png)![](/content/images/2019/01/image-275.png)![](/content/images/2019/01/image-276.png)![](/content/images/2019/01/image-277.png)![](/content/images/2019/01/image-278.png)![](/content/images/2019/01/image-279.png)![](/content/images/2019/01/image-280.png)![](/content/images/2019/01/image-281.png)![](/content/images/2019/01/image-282.png)![](/content/images/2019/01/image-283.png)![](/content/images/2019/01/image-284.png)![](/content/images/2019/01/image-285.png)![](/content/images/2019/01/image-286.png)![](/content/images/2019/01/image-287.png)![](/content/images/2019/01/image-288.png)![](/content/images/2019/01/image-289.png)![](/content/images/2019/01/image-290.png)![](/content/images/2019/01/image-291.png)![](/content/images/2019/01/image-292.png)![](/content/images/2019/01/image-293.png)![](/content/images/2019/01/image-294.png)![](/content/images/2019/01/image-295.png)![](/content/images/2019/01/image-296.png)![](/content/images/2019/01/image-297.png)![](/content/images/2019/01/image-298.png)![](/content/images/2019/01/image-299.png)![](/content/images/2019/01/image-300.png)![](/content/images/2019/01/image-301.png)![](/content/images/2019/01/image-302.png)![](/content/images/2019/01/image-303.png)![](/content/images/2019/01/image-305.png)![](/content/images/2019/01/image-306.png)![](/content/images/2019/01/image-307.png)![](/content/images/2019/01/image-308.png)![](/content/images/2019/01/image-309.png)![](/content/images/2019/01/image-310.png)![](/content/images/2019/01/image-311.png)![](/content/images/2019/01/image-312.png)![](/content/images/2019/01/image-313.png)![](/content/images/2019/01/image-314.png)![](/content/images/2019/01/image-315.png)![](/content/images/2019/01/image-316.png)![](/content/images/2019/01/image-317.png)![](/content/images/2019/01/image-318.png)![](/content/images/2019/01/image-319.png)![](/content/images/2019/01/image-320.png)![](/content/images/2019/01/image-321.png)![](/content/images/2019/01/image-322.png)![](/content/images/2019/01/image-323.png)![](/content/images/2019/01/image-324.png)![](/content/images/2019/01/image-325.png)![](/content/images/2019/01/image-326.png)![](/content/images/2019/01/image-327.png)![](/content/images/2019/01/image-328.png)![](/content/images/2019/01/image-329.png)![](/content/images/2019/01/image-330.png)![](/content/images/2019/01/image-331.png)![](/content/images/2019/01/image-332.png)![](/content/images/2019/01/image-333.png)![](/content/images/2019/01/image-334.png)![](/content/images/2019/01/image-335.png)![](/content/images/2019/01/image-336.png)![](/content/images/2019/01/image-337.png)![](/content/images/2019/01/image-338.png)![](/content/images/2019/01/image-339.png)![](/content/images/2019/01/image-340.png)![](/content/images/2019/01/image-341.png)![](/content/images/2019/01/image-342.png)![](/content/images/2019/01/image-343.png)![](/content/images/2019/01/image-344.png)![](/content/images/2019/01/image-345.png)![](/content/images/2019/01/image-346.png)![](/content/images/2019/01/image-347.png)![](/content/images/2019/01/image-348.png)![](/content/images/2019/01/image-349.png)![](/content/images/2019/01/image-350.png)![](/content/images/2019/01/image-351.png)![](/content/images/2019/01/image-352.png)![](/content/images/2019/01/image-353.png)![](/content/images/2019/01/image-354.png)![](/content/images/2019/01/image-355.png)![](/content/images/2019/01/image-356.png)![](/content/images/2019/01/image-357.png)![](/content/images/2019/01/image-358.png)![](/content/images/2019/01/image-359.png)![](/content/images/2019/01/image-360.png)![](/content/images/2019/01/image-361.png)![](/content/images/2019/01/image-362.png)![](/content/images/2019/01/image-363.png)![](/content/images/2019/01/image-364.png)
### Verifaction and validation
![](/content/images/2019/01/image-365.png)![](/content/images/2019/01/image-366.png)![](/content/images/2019/01/image-367.png)![](/content/images/2019/01/image-368.png)![](/content/images/2019/01/image-369.png)![](/content/images/2019/01/image-370.png)![](/content/images/2019/01/image-371.png)![](/content/images/2019/01/image-372.png)![](/content/images/2019/01/image-373.png)![](/content/images/2019/01/image-374.png)![](/content/images/2019/01/image-375.png)![](/content/images/2019/01/image-376.png)![](/content/images/2019/01/image-377.png)![](/content/images/2019/01/image-378.png)![](/content/images/2019/01/image-379.png)![](/content/images/2019/01/image-380.png)c![](/content/images/2019/01/image-381.png)![](/content/images/2019/01/image-382.png)![](/content/images/2019/01/image-383.png)![](/content/images/2019/01/image-384.png)![](/content/images/2019/01/image-385.png)![](/content/images/2019/01/image-386.png)![](/content/images/2019/01/image-387.png)![](/content/images/2019/01/image-388.png)![](/content/images/2019/01/image-389.png)![](/content/images/2019/01/image-390.png)![](/content/images/2019/01/image-391.png)![](/content/images/2019/01/image-393.png)![](/content/images/2019/01/image-394.png)![](/content/images/2019/01/image-395.png)![](/content/images/2019/01/image-396.png)![](/content/images/2019/01/image-397.png)![](/content/images/2019/01/image-398.png)![](/content/images/2019/01/image-399.png)![](/content/images/2019/01/image-400.png)![](/content/images/2019/01/image-401.png)![](/content/images/2019/01/image-402.png)![](/content/images/2019/01/image-403.png)![](/content/images/2019/01/image-404.png)![](/content/images/2019/01/image-405.png)![](/content/images/2019/01/image-406.png)![](/content/images/2019/01/image-407.png)![](/content/images/2019/01/image-408.png)![](/content/images/2019/01/image-409.png)![](/content/images/2019/01/image-410.png)![](/content/images/2019/01/image-411.png)![](/content/images/2019/01/image-412.png)![](/content/images/2019/01/image-413.png)![](/content/images/2019/01/image-414.png)![](/content/images/2019/01/image-415.png)![](/content/images/2019/01/image-416.png)![](/content/images/2019/01/image-417.png)![](/content/images/2019/01/image-418.png)![](/content/images/2019/01/image-419.png)![](/content/images/2019/01/image-420.png)![](/content/images/2019/01/image-421.png)![](/content/images/2019/01/image-422.png)![](/content/images/2019/01/image-423.png)![](/content/images/2019/01/image-424.png)![](/content/images/2019/01/image-425.png)![](/content/images/2019/01/image-426.png)![](/content/images/2019/01/image-427.png)![](/content/images/2019/01/image-428.png)![](/content/images/2019/01/image-429.png)![](/content/images/2019/01/image-430.png)![](/content/images/2019/01/image-431.png)![](/content/images/2019/01/image-432.png)![](/content/images/2019/01/image-433.png)![](/content/images/2019/01/image-434.png)![](/content/images/2019/01/image-435.png)![](/content/images/2019/01/image-436.png)![](/content/images/2019/01/image-437.png)![](/content/images/2019/01/image-438.png)![](/content/images/2019/01/image-439.png)![](/content/images/2019/01/image-440.png)![](/content/images/2019/01/image-441.png)![](/content/images/2019/01/image-442.png)![](/content/images/2019/01/image-443.png)![](/content/images/2019/01/image-445.png)![](/content/images/2019/01/image-446.png)![](/content/images/2019/01/image-447.png)![](/content/images/2019/01/image-448.png)![](/content/images/2019/01/image-449.png)![](/content/images/2019/01/image-450.png)![](/content/images/2019/01/image-451.png)![](/content/images/2019/01/image-452.png)![](/content/images/2019/01/image-453.png)![](/content/images/2019/01/image-454.png)![](/content/images/2019/01/image-455.png)![](/content/images/2019/01/image-456.png)![](/content/images/2019/01/image-457.png)![](/content/images/2019/01/image-458.png)![](/content/images/2019/01/image-459.png)![](/content/images/2019/01/image-460.png)![](/content/images/2019/01/image-461.png)![](/content/images/2019/01/image-462.png)![](/content/images/2019/01/image-463.png)![](/content/images/2019/01/image-464.png)![](/content/images/2019/01/image-465.png)![](/content/images/2019/01/image-466.png)![](/content/images/2019/01/image-467.png)![](/content/images/2019/01/image-468.png)![](/content/images/2019/01/image-469.png)![](/content/images/2019/01/image-470.png)![](/content/images/2019/01/image-471.png)![](/content/images/2019/01/image-472.png)![](/content/images/2019/01/image-473.png)![](/content/images/2019/01/image-474.png)![](/content/images/2019/01/image-475.png)![](/content/images/2019/01/image-476.png)![](/content/images/2019/01/image-477.png)![](/content/images/2019/01/image-478.png)![](/content/images/2019/01/image-479.png)![](/content/images/2019/01/image-480.png)![](/content/images/2019/01/image-481.png)![](/content/images/2019/01/image-482.png)![](/content/images/2019/01/image-483.png)![](/content/images/2019/01/image-484.png)![](/content/images/2019/01/image-485.png)![](/content/images/2019/01/image-486.png)![](/content/images/2019/01/image-487.png)![](/content/images/2019/01/image-488.png)![](/content/images/2019/01/image-489.png)![](/content/images/2019/01/image-490.png)![](/content/images/2019/01/image-491.png)![](/content/images/2019/01/image-492.png)![](/content/images/2019/01/image-493.png)![](/content/images/2019/01/image-494.png)![](/content/images/2019/01/image-495.png)![](/content/images/2019/01/image-496.png)![](/content/images/2019/01/image-497.png)![](/content/images/2019/01/image-498.png)![](/content/images/2019/01/image-499.png)![](/content/images/2019/01/image-500.png)![](/content/images/2019/01/image-501.png)![](/content/images/2019/01/image-502.png)![](/content/images/2019/01/image-503.png)
