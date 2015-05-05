---
layout: section
title: Organizing inside Your Source - Best Practices, Separation of Concerns
---

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
