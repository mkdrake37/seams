---
layout: section
title: How to Verify and Validate Research Code as You Work
---
##References on software testing:

##An introduction to software testing:

http://agile.csc.ncsu.edu/SEMaterials/BlackBox.pdf

##A general guide to testing in Python:

http://docs.python-guide.org/en/latest/writing/tests/

##A guide to PyUnit:

http://www.drdobbs.com/testing/unit-testing-with-python/240165163

##A guide to pycharm:

https://www.jetbrains.com/pycharm/quickstart/

##Debugging in Pycharm

https://www.jetbrains.com/pycharm/help/running-and-debugging.html

https://www.jetbrains.com/pycharm/help/python-debugger.html

https://www.jetbrains.com/pycharm/help/using-debug-console.html

https://www.jetbrains.com/pycharm/help/stepping-through-the-program.html

##A guide to debugging in Rstudio:

 https://support.rstudio.com/hc/en-us/articles/205612627-Debugging-with-RStudio

##Thoughts on input validation:

http://www.ibm.com/developerworks/library/l-sp2/

##Some tests for randomness:

http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.156.7149&rep=rep1&type=pdf





##Warmup discussion:

 - Validation v. Verification
 - How to test "correctness."
 - Why allow user error v. Writing highly detailed API? 
 
##Exercise: Debugging the national team's football game
 - Ghana lost: What went wrong?
 - List possible reasons for failure
 - What are some test scenarios/cases to confirm above reasons?

##Testing:

##Before you compile:
 - Documentation within code
 - Throwing exceptions
 - Testing by hand
 - Incorporating test code 
 - Testing for codes involving random variables (e.g. Dependency injection, delegation)

##Debugging with an IDE
##Break points
 - Types of break point (regular, conditional, temporary) and when to use
 - Identifying suspects in misbehaving code (where to add break points)
 - What are some flaws with the break point system?
 - (Some break point drills)
 
##Other IDE techniques
 - Using incremental evaluation to look inside variables
 - Query based debugging: https://www.cs.ucsb.edu/~urs/oocsb/papers/oopsla97.pdf
 - Dynamic Query based debugging: https://www.cs.purdue.edu/homes/xyzhang/fall07/Papers/query-debugging.pdf

##After Compiling
 - Edge Cases
 - Devising Tests
 - exercises 1 and 2 below



##Test driven development
 - Core principles: only write code if it is used to pass previously failed test, eliminate duplication
 - how to "black box" components of code, while still compiling 
 - how to phrase a coding project as a series of tests
 - coding cycle: devise test, write code to pass test, clean up, repeat
 - Kent beck reference

## Developing tests/test driven development Problem (project Euler problem 4):
 - Read/understand problem 4 (palindromic numbers)
 - Identify problems this code will need to solve
 - Develop test for each function involved. 
 - Scenario: you are a teacher. your students have been assigned to write code that can solve all of the above problems listed (everything necessary for problem 4)
 - over 100 students in class. Write code to grade their assignments. 


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
