---
title: Performance, in Theory
---

# Overall question: 
Which problems are difficult to solve and which are easy.
This concept is above hardware: Moore’s law does not make difficult problems easy. Rather, some problems are intrinsically more difficult (probably).

Growth: Any problem is easy on a small scale. The issue is how the problem scales.

Class P (polynomial time): An algorithm is solvable in polynomial time if the number of steps require to complete algorithm for a given input is bounded by n^k for some integer k, where n is the amount of input.

Class NP (nondeterministic polynomial time): Set of decision problems where the affirmative answers have polynomial time verifiable proofs.

Example:  Does a set of numbers have a subset which sums to zero? For the set {-3,7,10,-4,1}, it is easy to check that {-3,7,4} works, but finding this set is thought to be hard. This is an NP problem, and shown just to be as hard as any other NP problem (called NP-Hard). This is thought not to be a P problem.

Important, difficult problems: Are all NP problems actually in P?

This is the overarching question to what problems can be solved quickly: P problems are often considered ‘doable problems,’ but improvements of a problem within P are very important. Poster child example: Fast Fourier Transform, used to quickly multiply polynomials, improves O(n^2) to O(n log n). 

Another example: Sorting, improvement from O(n^2) to O(n log n). But different sorting techniques are useful in different contexts. i.e. Mergesort when memory is not an issue and can parallelize, quicksort when do not care about stability.



# Data structures: 
Picking the right data structure to suit purposes. During the day, we will focus on example problems and consider what would be the good solutions given the data structures. Some will be using the data structures (ex. how do you find if a linked list has a loop?) to what would be a good data structure for our problem (ex. given a set of fixed points in the plane, which point is closest to a given moveable point?) This section will go by fast if you are not well acquianted with the data structures beforehand. It would be good to know the operations, the speed for some implementations, and an understanding of how it is implemented for the following:

1. Array
2. List/Dynamic Array
3. Stack/Queue/Deque
4. Dict/ Symbol Table
5. Priority Queue
6. Set/Multiset

Some resources:

https://wiki.python.org/moin/TimeComplexity

http://bigocheatsheet.com/

https://docs.python.org/2/tutorial/datastructures.html

https://wiki.python.org/moin/TimeComplexity

http://dtkachenko.blogspot.com/2011/11/data-structures-and-algorithms-when-to.html

http://www.idevelopment.info/data/Programming/data_structures/overview/Data_Structures_Algorithms_Introduction.shtml

http://www.careerride.com/Data-Structure-Interview-Questions.aspx

# Dynamic Programming/ Memoization

Essentially 'divide-and-conquer' strategies to problems. Simple but very powerful.

Ex. Tower of Hanoi Puzzle: http://en.wikipedia.org/wiki/Tower_of_Hanoi

Resources

https://www.topcoder.com/community/data-science/data-science-tutorials/dynamic-programming-from-novice-to-advanced/

http://www.codechef.com/wiki/tutorial-dynamic-programming

A sample problem: https://projecteuler.net/problem=81

# Sorting

Sorting is important problem both as a key part to other algorithms and an important standalone question. We will review some sorting algorithms (Quicksort, Mergesort, etc.) and work example problems where they play a key part.

Ex. Given a set of numbers, can you find a pair that sums to 0? Naive is O(n^2), with sorting O(n log(n))

Ex. Given a set of numbers, can you find a triples that sums to 0? Naive is O(N^3), with sorting O(n^2 log(n))

Resources: 
https://www.cs.cmu.edu/~adamchik/15-121/lectures/Sorting%20Algorithms/sorting.html

# Graph Problems: 
Many problems show up as graph problems. Finding minimum spanning trees, max flow / min cut, shortest paths. Some important algorithms, some of which we will go over: Depth first and breadth first search, Prim, Dijkstra, Kruskal, Prim, Bellman-Ford. During the day we will go through some interesting problems with graph representations and use some of the above algorithms to solve them. Some examples might be: Seam Carving pictures for photo editing, finding the your way out of a maze, etc.

# RegExp: 
Important for webcrawling and searching through text is regular expressions: What type of strings can and cant be found by regular expressions / nondeterministic finite automaton. We will go over some uses.

http://infolab.stanford.edu/~ullman/focs/ch10.pdf

Good overview of theory, last bit about NFA: https://courses.engr.illinois.edu/cs373/fa2010/lectures/lect06.pdf

optimizing: http://blog.codinghorror.com/regex-performance/

https://docs.python.org/2/howto/regex.html#regex-howto

https://docs.python.org/2/library/re.html

https://projecteuler.net/problem=89

# Parallelizing
Some problems can take advantage of multiple processors. Although distinct from the idea of P vs NP, this concept can quickly make a problem more manageable. Throughout we will keep an eye on when parallelization is possible, and bring up some very important instances.

Resources:
http://scottsievert.github.io/blog/2014/07/30/simple-python-parallelism/

https://www.binpress.com/tutorial/simple-python-parallelism/121

# Random algorithms: 
Overview of some probabilistic methods. Monte Carlo, IsPrime, Quick sort, verifying some output by random selection.


