---
title: Organizing inside Your Source - Best Practices, Separation of Concerns
---

## Instructions from aggregate_rural_and_urban.py:

This script takes an input file ("all_cases.csv") that contains location-stratified
disease time series data, and aggregates the disease incidence based on whether the
location was rural or urban.

You will be making multiple changes to the code below.  Each time you make a 
substantial change, verify that you have not changed the output from the program.

The Exercise:

1) Read through, understand, and annotate the code.  If you do not understand a line,
investigate it by experimenting, checking python references, and talking to others.

2) If there anything simple that can be done to make the code more readable or
manageable, go ahead and do that--things like renaming variables or reducing the use
of "magical" numbers.

3) Break the code up into functional units, and then turn those units into functions.

4) Write a class that can represent the input data in a useful way.  Create a parser
function in the class that takes a line of text from the file and returns structured
data that is useful and easy to understand.
