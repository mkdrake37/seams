---
layout: section
title: How to Verify and Validate Research Code as You Work
---


##Warmup discussion:

 - Validation v. Verification
 - How to test "correctness."
 - Why allow user error v. Writing highly detailed API?

##Testing:

##Before you compile:
 - Documentation within code
 - Debugging with IDE
 - Throwing exceptions
 - Testing by hand
 - Incorporating test code
 - Testing for codes involving random variables (e.g. Dependency injection, delegation)

##After Compiling
 - Edge Cases
 - Devising Tests

##Test driven development
 - Core principles: only write code if it is used to pass previously failed test, eliminate duplication
 - how to "black box" components of code, while still compiling
 - how to phrase a coding project as a series of tests
 - coding cycle: devise test, write code to pass test, clean up, repeat
 - Kent beck reference



##Review Excercises
 - Hand students code known to have flaws, ask them to find flaws
 - Exchange code and test/debug
 - Evaluate third party software


##Ex.1 Hand off codes with model bug, they write tests

(Potential contest: which team can find flaw first)

-(easy) weather calculations: Solution: pV = nRT, code not prepared for T = 0

-(hard)”elevator” problem phrased as bus route problem (delivering fans to stadiums): Solution: not all bus stops are actually reachable in given model

-more examples (e.g. Taylor series not converging on given input): http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.204.5875&rep=rep1&type=pdf

##Ex. 2 Students exchange code and write tests

-students may hand off any of their previous work for testing, as long as it is reasonably sophisticated. -students take ~15 minutes to write good APIs as needed. No verbal discussion with tester allowed -tester writes code for testing and writes short report


##Ex. 3 Students given code with bugs and apply new debugging techniques

Testing vs validation vs debugging.

Testing as a way to translate "this code does..." into formal description.  Thinking
with the end product in mind.

Debugging approaches.  Particularly, using IDE in browse mode.

Validating inputs - again, as a way of describe what code does.  Validation can
be thought of as documenting input parameters for a function.

How to have testing code integrated in source and not interfere w/ running.

All this in research setting, when outcomes often not explicitly specified.  How
to do testing given stochastic components.
