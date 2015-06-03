---
title: Performance, in Theory
---

# Overview

For this session, students (perhaps in small groups) will research an algorithm or a particular implementation of an abstract data type. The students will then implement the algorithm in code and then present a short presentation on the algorithm. First begin with one of the lower ranked problems, then move on to a harder one if you have time.

# Goals for Presentation 

Some important parts of the presentation that should be addressed:

1. For algorithms, clearly state the input and output. For an ADT, explcitly state the API.
2. If applicable, mention the naive algorithm/implementation, and how yours improves.
3. Mention any relevant classifications: Recursive? Parallelizable? Greedy? Deterministic?
4. Go through the algorithm/construction. Cut some corners if yours is very involved.
5. At the end, provide a toy problem (ex. a graph with 7 vertices, 2x2 matrix, a few calls to your API) and let us go through the example on our own.
6. Mention some important applications.

# Example selection

The following is a modest collection of algorithms and some data types (but no reference, part of the exercise is finding the relevent information on the internet!). Because of their wide spread importance, they are undoubtably in some Python library and perhaps in the Standard Python Library. Nevertheless, this exercise will be good practice for when you come across an algorithm in a scientific paper that does not provide code, and will also give insight to the uses and limitations.

Do not feel limited to the following examples. If your personal research has led you to a particular algorithm or ADT implementation you wish to know more about, feel free to pick that. Consequently, we will feel free to add or remove. Ssome of the examples are harder to grasp than others, but perhaps not surprisingly, the simplest algorithms tend to have the most amount of applications. If you pick one that seems trivially simple, think about some important uses, extensions, or improvements.

## Some ADT Implementations

1. Own version of stack/queue of Strings: Should implement push, pop, peek, isEmpty all in O(1) time. (*)
2. Weighted disjoint-set of forests for integers: Data type which initializes to n 1-element subsets, and then can union 2 sets and also ask if two elements are in the same subset. Should run both operations in O(log(n)) time. (**)
3. Hash Table + Collision resolution with keys and values as Strings: Should be able to search and insert in amortized O(1) time. (Separate chaining, Open addressing, etc.) (***)
4. Priority Queue heap with Strings: Should be able to insert and delete the max in O(log(n)) time. 

## Some Algorithms

1. Dijkstra: Takes in a file with number of vertices, and weights of any existing edges between them. Efficiently outputs shortest distance from first vertex to the rest of the vertices. (*)
2. Primality Testing: Input an int, outputs a Boolean of whether the int is prime or not. Should be correct an overwhelming majority of the time. (*)
3. A*: Takes in a file with points on a plane (as pairs of a doubles). Outputs shortest path between first vertex and last vertex. (*)
4. Knuth-Morris-Pratt: Given two strings, efficiently outputs indices for the second string being a substring of the first. (**)
5. Newton's Method (**)
6. Needleman–Wunsch algorithm: Given two strings, efficiently outputs the two strings with spaces added such that the difference between the two (where 2 spaces marks a difference) is minimized. Key for protein sequencing. (***)
7. PageRank: How Google determines the most important page. Abstractly, given a directed weighted graph, outputs an 'importance' for each vertex. (****)

# Older:

## Some ADT Implementations

1. Balanced Binary Search Trees (2-3 Trees, Red-Black, Splay, etc.)
2. Hash Table Collision resolution (Separate chaining, Open addressing, etc.)
3. Priority Queue heap (heap, Fibonacci heap, etc.)
4. Tries
5. Disjoint-set forests

## Graph Algorithms

1. A*
2. Dijkstra
3. Floyd-Warshall
4. Kruskal
5. Prim
6. Bellman-Ford
7. PageRank (How Google determines the most important page)

## Linear Algebra Algorithms

1. Csanky's Algoirthm (inverts a matrix)
2. Rank of a Matrix 
3. Singular Value Decomposition
4. LLL-algorithm (finds short near-orthogonal set of vectors in a lattice)

## Other Algorithms

1. Discrete Fast Fourier Transform 
2. Knuth-Morris-Pratt (search for a word in a string)
3. Primality Testing 
4. Diffie-Hellman key exchange
5. Karatsuba and other fast multiplicatoin algorithms


1. Students research and implement algorithms relevent to their research, conduct short presentation
2. Complexity sorting worksheet: Look at this algorithm/data structure.  How fast does it run
3. Reduction exercise: Barber of Accra
4. ProjectEuler Optimization Problems
5. More stuff

http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.204.5875&rep=rep1&type=pdf
http://stackoverflow.com/questions/8024911/project-euler-5-in-python-how-can-i-optimize-my-solution
http://codereview.stackexchange.com/questions/39348/project-euler-problem-12-highly-divisible-triangular-number-python-solution
http://codereview.stackexchange.com/questions/2/project-euler-problem-1-in-python-multiples-of-3-and-5
http://codereview.stackexchange.com/questions/14442/optimizing-code-for-project-euler-problem-14
http://codereview.stackexchange.com/questions/13086/problem-5-on-project-euler
http://www.mathblog.dk/project-euler-18/



~Challenge students to modify interface.
~Evaluate efficiency and quality of interfaces of common software
~Emphasize importance of usability, robustness
Have students exchange long project code and modify each other's code to produce output in various programs (i.e. Excel-like spreadsheet, databases, LaTex), and interface with various libraries, databases provided.
