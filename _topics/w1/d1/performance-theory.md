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

P problems are often considered ‘doable problems,’ but improvements of a problem within P are very important. Poster child example: Fast Fourier Transform, used to quickly multiply polynomials, improves O(n^2) to O(n log n). "the most important numerical algorithm of our lifetime.”

Another example: Sorting, improvement from O(n^2) to O(n log n). But different sorting techniques are useful in different contexts. i.e. Mergesort when memory is not an issue and can parallelize, quicksort when do not care about stability.

# Data structures: 
Pick right data structure to suit purposes. Example: For a set of objects, do we want a linked list, a dynamic array? What operations will we need to be done quickly.

Search another important example: Symbol tables, Binary search tree, hash tables, etc.

# Graph Problems: 
Many problems show up as graph problems. Finding minimum spanning trees, max flow/ min cut, shortest paths. Some important algorithms: Depth first and breadth first search, Prim, Dijkstra, Kruskal, Prim, Bellman-Ford.

# RegExp: 
Important for webcrawling and searching through text is regular expressions: What type of strings can and cant be found by regular expressions / nondeterministic finite automaton.

# Random algorithms: 
Overview of some probabilistic methods. Monte Carlo, IsPrime, Quick sort, verifying some output by random selection.


