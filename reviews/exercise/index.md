---
title: Language In-depth Exercise
---

Using the syntax and concepts we reviewed this morning, you will write code to accomplish a series of tasks.  You should complete the tasks in the order provided, in whichever language you prefer.  You may use any library to assist you.  For the tasks there is at least one piece of missing information about what to do; you will need to decide for yourself what to do.

The tasks are:

1. given an area, calculate the side length of the following figures with that area:
 - square
 - equilateral triangle
 - circle
 - golden ratio rectangle
2. given an area, shape type (see below), and origin, draw the appropriate, solid black shape in the location
3. given an input file of a series of areas, types, locations, and fill colors (see below for schema), draw all the shapes in the corresponding locations
4. produce code that can be invoked from the command line, receiving an input file name and output file name, that will read in the input file and save your figure to requested output, *e.g.*:

{% highlight bash %}
location uname$ ./MYCOMMAND SOMEINPUT.csv SOMEOUTPUT.png
{% endhighlight %}

The shapes will be specified by strings:
 - square = "SQUARE"
 - equilateral triangle = "TRIANGLE"
 - circle = "CIRCLE"
 - golden ratio rectangle = "RECTANGLE"

The colors will also be specified by strings, with the following set of colors: "red", "orange", "yellow", "green", "blue", "violet"

The input files will be `csv`s, formatted like:

```
16.0, "SQUARE", "red", 0.0, 0.0
5.0, "CIRCLE", "blue", 10.0, 10.0
10.0, "RECTANGLE", "yellow", -5.0, 5.0
```

which corresponds to a request for three shapes, with a red square first, drawn at the normal origin, and so on for the remaining rows.
