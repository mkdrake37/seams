---
title: Clean Up Some Rough Code
---

In this exercise, we are working with a script, [aggregate_rural_and_urban.py]({% include linkmunge.lq %}/aggregate_rural_and_urban.py), that receives an input file ([all_cases.csv]({%include linkmunge.lq%}/all_cases.csv)).  The input file contains location-stratified disease time series data, and aggregates the disease incidence based on whether the
location was rural or urban.

You will be making multiple changes to the code in the task outlined below.  Each time you make a
substantial change, verify that you have not changed the program output, and once you have done so, commit your changes to the repository you [set up earlier]({% include url.lq %}/organizing-outer/practice/).

## The Exercise:

  1. Read through, understand, and add comments to the code explaining what various parts do.  If you do not understand a line, investigate it by experimenting, checking python references, and talking to others.
  2. If there anything simple that can be done to make the code more readable or manageable, go ahead and do that: *e.g.*, rename variables or reducing the use of [*magic* numbers](https://en.wikipedia.org/wiki/Magic_number_(programming)#Unnamed_numerical_constants).
  3. Break the code up into functional units, and then turn those units into functions.
  4. Write a class that can represent the input data in a useful way.  Create a parser
function in the class that takes a line of text from the file and returns structured
data that is useful and easy to understand.
