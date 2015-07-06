---
title: Performance, in Theory
---

# Overview

For this session, students (perhaps in small groups) will research some algorithms. The students will then implement the algorithm in code and then give a short presentation on an algorithm. You will start off with 2 elementary (i.e. super important) algorithms of antiquity, followed by another of your choosing.

# Goals for Presentation 

Some important parts of the presentation that should be addressed:

1. Clearly state the input and output.
2. If applicable, mention the naive algorithm/implementation, and how yours improves.
3. Mention any relevant classifications: Recursive? Parallelizable? Greedy? Deterministic?
4. Go through the algorithm/construction. 
5. Provide a toy problem (ex. a graph with 7 vertices, a string and a substring, ...) and let us go through the example on our own.
6. Mention some important applications.

# Example selection

Below is the list of algorithms and descriptions. Do the first two, then pick a more difficult one, potentially from the list or of your choosing. If your personal research has led you to a particular algorithm you wish to know more about, feel free to pick that, just ask us. Some of the examples are harder to grasp than others, but perhaps not surprisingly, the simplest algorithms tend to have the most amount of applications.


##  Algorithms

The first two you will implement before you go on to a more difficult one:

1. Euclidean Algorithm: Calculates the greatest common divisor of two numbers. Considered the first algorithm ever described.
2. The Sieve of Eratosthenes: Calculates the prime numbers less than n. Perhaps the first number theory algorithm.

Then a single difficult algorithm (you can pick your own if you ask us):

1. Dijkstra: Takes in a file with number of vertices, and weights of any existing edges between them. Efficiently outputs shortest distance from first vertex to the rest of the vertices. Basis for running GoogleMaps.
2. Runge Kutta or any other iterative method for solving ODEs explicitely. Applicable for any physics simulator and many others.
3. Knuth-Morris-Pratt: Given two strings, efficiently outputs indices for the second string being a substring of the first. Essentially, when you type Ctrl-F on a webpage, you run this algorithm.
4. Needleman–Wunsch algorithm: Given two strings, efficiently outputs the two strings with spaces added such that the difference between the two (where 2 spaces marks a difference) is minimized. Sequences proteins, fundamental algorithm in molecular biology.


