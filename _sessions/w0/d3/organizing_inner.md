---
title: Organizing inside Your Source - Best Practices, Separation of Concerns
---

## What & Why?

Some examples to look at:
[bad_code.py]({% include linkmunge.lq %}/bad_code.py)
[less_bad_code.py]({% include linkmunge.lq %}/less_bad_code.py)

## Best practices
Work with one other person to write a list of at least 10 "best practices,"
based on at least three sources.  For each best practice, note whether it is
something you should always, sometimes, or never do.  If sometimes, why only
sometimes?  If never--and there are some old best practices that are now
widely regarded as bad practices--try to understand why in some context they
made sense.  What kinds of factors determine what "best practices" means?

## User interface and object design
Draw and label the parts of two electric fans (the kind you cool yourself
with).  

For the first one, include the minimum number of functional parts--
the simplest possible powered fan, if you were to put one together from minimal
parts. 

For the second one, include things that would make it user-friendly,
something that might be sold in a store.

## Design a class structure
Write down a class hierarchy that reflects the functional and user-friendly
fan parts that you identified in the last part.  What is part of the public
interface for each class?  If you need help getting started, a sensible option
would be to start with a Fan class and create functions the correspond to how
the user would interact with it.  What subclasses to you need to define that
can be put together to make up a Fan object?  Note that you DO NOT need to
write any algorithms or mathematical equations.  For example, you don't need
to figure out how pushing a button (or turning a dial or pulling a chain)
changes the motor speed, but your interface should indicate that that
functionality exists.

[Example of a class diagram](http://web.gccaz.edu/~pbrown2/cis_225/projects/225P_Project_04_Class_Diagram_Auto_Shop.html)

{% comment %}

## older content
## What are coding conventions or best practices?
 - just a conversation, not intended to be exhaustive

## Value and burden of conventions
 - faster development
 - avoid decision fatigue
 - encoded information for the human reader
 - can be tedious/contentious/fail to be universally optimal

## Some topics
 - syntax
    - capitalization vs CamelCase vs pothole_case
    - whitespace
 - naming
    - get/set
    - indicating type
    - to reduce comment burden
 - ordering
    - function arguments
    - variable declaration
    - functions
 - optimizations
    - legibility (good first priority)
    - maintainability (dry principle)
    - algorithmic complexity (as needed)

## OOP
 - structure code the way people think
 - separation of concerns
    - clear interfaces
    - agnostic internals

## Comments from 04/08/15
 - conventions may be institutional or language specific
 - NASA example
 - math has its own set of conventions, that may compete with programmatic concerns
 - best option tends to be audience-specific


## previous notes

organizing by way of syntax choices: capitalization vs CamelCase vs pothole_case,
indentation, arrangement of function arguments, etc.

Value of making these choices consistently: like reading a well-written book.
Authors may each have different voice, but their story-telling style (word choice,
construction, etc) is consistent within a book, often across their work.

Organization by class structure - what to make a class, what to not make a class.
Using functions to make work intellectually bite-sized.  Approaching organization
in a way that minimizes how much you have to worry about at once.

Regular refactoring: not just for optimization, but for organization.

{% endcomment %}
