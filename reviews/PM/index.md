---
title: Language Review II
---

## Loop Constructs

> ### Quiz
>
>  0. For the following `for` loops, which values does `i` take on inside the loop?
>     0. `for i in range(2,5): print i`{:.language-python}
>     1. `for (i in 1:4) print(i)`
>     2. `for i = [1,3;2,4] i endfor`
>
>  1. How many times is the code inside these while loop executed? In each case, what is the final value of j?
{% highlight python %}
i = -1; j = 7;
while (j+i < 100):
  j += j + (-1)**j -1
  print j
{% endhighlight %}
{% highlight r %}
i = 4; j = 1;
while(i>1) {
  j = j*i; i = i-1;
}
{% endhighlight %}
{% highlight octave %}
fib = [1 1 1 1 1];
i = 3;
while (i <= 6)
  fib (i) = fib (i-1) + fib (i-2);
  i++;
endwhile
{% endhighlight %}
>  2. What list results from each of the expressions below?
>    0. `[i*i for i in range(5) if i%2==1]`
>    1. `sapply(2:5, factorial)`
>    2. `x=1:10; (x.^2)(mod(x,2)==0)`


One of the fundamental tasks we wish to simplify with programs is repeating tasks.  Loop constructs allow us to do that.

### `for` and `while` loops
In a sense, `for` loops are `while` loops with explicit constraints on the iteration - *i.e.*, particular start, end, and steps.  That can be accomplished in `while` loops as well, so why bother with `for` loops at all?

In many cases, sensible constraints result in safer code, so we should expect
more errors in `while` loops: they must be initialized and incremented
correctly, and must have a properly specified condition for exit.  These three
parts are generally specified on three separate lines of code, which can be
accidentally deleted or modified, thereby corrupting the loop.  Similar
challenges apply to `for` loops, but this is much less common because it is
usually obvious if you are trying to iterate through an empty list, or if you
are modifying the container you are iterating through in the loop.  (Hint:
NEVER do that.) incremented correctly, they may never exit

In general, prefer for loops unless it is impractical to use one.  Generally, it
is appropriate to use a while loop when the number of times you need to repeat a
block of code is not known to the program.  Occasionally, while loops may make
code clearer than using clever tricks (programmatic or mathematical) to figure
out how many times a loop needs to execute.  An example is reading in a file,
line by line.  You could query the OS to find out how many lines are in the file
and then iterate through it using a for loop, but it is usually more efficient
and less complicated to use a while loop.  In this particular case, Python
provides a useful idiom `for line in file('filename')`, so we do not have to
resort to a while loop.

### Map-Filter-Reduce Paradigm: Comprehensions and `apply` family functions

Often in `for` loops, what we do is for each element is one or more of the following:

  - check if the element meets some criteria (e.g., is it greater than 0?)
  - transform the element into a new value (e.g., convert temperature from Fahrenheit to Celsius)
  - combine the elements into some aggregate result (e.g., find maximum value)

These tasks are part of Map-Filter-Reduce paradigm: we *map* the elements to new ones, we *filter* 
(either before or after mapping) to get the subset we care about, and we *reduce* the remaining 
transformed elements from many into a single result by combining them.

In python there are functions called `map`, `filter`, and `reduce` that do these things, although 
mapping and filtering can also be done with comprehensions like the one in the quiz.  

Comprehensions (and their equivalent in non-Python languages) are concise ways of expressing how to convert
one list of things into another.  Very often, that's all we're doing with a loop, but loops tend to take up
more space and may be slower because the interpreter can sometimes be more clever about comprehensions. In
general, if you are applying an already-defined function to each element, you might prefer `map`, but if 
you are instead doing some operation or lookup in another data structure, a comprehension may be 
more concise. Some common reduce operations like `max` and `sum` are provided as built-in
functions, but `reduce` will apply an arbitrary function.

R and Octave will often do element-wise operations when you apply a function or an operation to
a list-like variable. This is a kind of built-in map behavior.

In R:
> c(1,2,3,4)*2
[1] 2 4 6 8

In Octave:
octave:35> cos([1 2 3 4])
ans =

   0.54030  -0.41615  -0.98999  -0.65364

More generally in R, the `apply` family of functions (apply, mapply, tapply, sapply) allow you to
apply functions to a variety of data structures.

> ### Re-Quiz

## Using Other Code

> ### Quiz
>
>    0. Python: What is the syntax to load a library?
>    1. Python: What do you do if you want to load a library you wrote?
>    2. R: What is the syntax to load a library?
>    3. R: What is the syntax to run a separate R script at a particular point in your script.
>    4. Octave: What is the syntax to load a library?

In most languages it is possible--and sometimes problematic--to have variables and/or functions that share the same
name in two different places.  Names sometimes get reused, particularly simple ones like `i` and `max`.  A simple
example is nested loops.  We so often use `i` as a loop iterator, that it can be easy to write code like this:

{% highlight python %}
for i in [1,2,3]:
    for i in [10,20,30]:
        ...
{% endhighlight %}

Although code like this will run in some languages, it is a bad practice because the intent may be misinterpreted by
readers.  Choose a different name for iterators in nested loops.

Loading packages may also result in name collisions, and those can be harder to
avoid.  In *R*, for example, a library called `plotter` might implement a
`plot(...)` function.  Since `plot` is also the name of a base function, loading
`plotter` changes what happens when you invoke `plot(...)`.  If we still want to
call the base package verison of `plot()`, we need to prepend the function call
with a namespace, *i.e.* `base::plot()`.  In order to avoid ambiguity for
readers, it might also be a good idea to call the other function explicitly as
`plotter::plot()`.

Python handles namespaces more carefully.  The simplest way of loading a library
(*module* in Python parlance), `import plotter`, preserves your namespace.  To
access the new plot function here, we would call `plotter.plot()`.  If you are
not concerned with namespace collisions, you can instead use `from plotter
import *`, which will import all of plotter's members, overwriting previously
defined variables and functions.  There is no way to access the old definitions
in Python.

In very short programs, it may not be necessary to bother with explicit
namespaces.  As software becomes more complicated, however, it becomes
increasingly likely that names will be reused.  In order to maintain
readability, and avoid bugs, as your project grows, consider creating your own
libraries (== modules == packages) so that conceptually-related code is bundled
together in its own namespace.

> ### Re-Quiz

## Classes

How we interact with an object, in real life and programming, depends on what
type thing that object is.  It does not make sense to divide words or to
spell-check numbers, for example.  In programming, we define how a variable can
be interacted with and what attributes it has by defining a *class*.  In some
languages, including Python, everything is an object, which is the same as
saying that everything is an instance of some class.  Classes are a useful way
to get away from the 1's and 0's that computers work with because they allow us
to work with arbitrarily sophisticated abstractions: a variable can represent a
traffic collision, a connection to a server, or a person.  A class can also be
an extension of another. An athlete object, for example, could have all of the
attributes of a person, but also have a team affiliation and performance
statistics.

Classes are also useful because they allow encapsulation.  Within a class,
attributes and functions can be either public or private.  Private things can
only be directly accessed or modified within the class, whereas public things
are available anywhere.  To illustrate this, let's consider a polygon class in
Python:

{% highlight python %}
class Polygon:
    'Base class for regular polygons'

    def __init__(sides, side_length):
        self.sides = sides
        self.side_length = side_length
        self.perimeter = sides*side_length

    def get_sides():
        return sides

    def set_sides(n):
        self.sides = n
        self.perimeter = self.sides*self.side_length

    def get_side_length():
        return side_length

    def set_side_length(length):
        self.side_length = length
        self.perimeter = self.sides*self.side_length

    def get_perimeter():
        return perimeter
{% endhighlight %}

*R* also supports defining classes.  However, *R* emphasizes numerics and functional programming much 
more than general purpose programming, and as such its class syntax is clunkier.

## IO and Visualization

> ### Quiz: IO and Visualization
>
>  0.  What are the OS terminal commands for R, Python, and Octave?
>  1.  When R, Python, and Octave scripts are invoked from the command line, how are the arguments available within the scripts?
>  2.  What are the standard libraries / commands to read `csv` and `json` files in R, Python, and Octave?
>  3.  Given an ordered series of (*x*, *y*), write the code to plot them as points in R, Python, Octave.
>  4.  Repeat previous as lines.

As researchers, we should hope to test our work against empirical data, meaning we need to know how to
get this data into and out of our programs for use.  This data may be stored in many formats, but some 
of the simplest are `csv` and `json`.

In Python: csv, json modules
In R     : read.csv(), rjson package
in Octave: csvread(), JSONlab

When working with large amounts of data, we often cannot use GUI tools (like Rstudio or PyCharm) because 
these tools are focused on interaction, rather than data processing, which means they have too much 
overhead.  They are also not supported for use on supercomputers.  In these cases, we can create and test 
our scripts in those tools, but to actually use them on our data, we must do so from a command line interface.

There are a few ways to do that, but during the workshop we will encourage you to write your scripts so 
they may be run directly, which means you need to put the appropriate bash directive at the front of the 
script and make them executable.

Finally, when applying our ideas, we will often need to visualize results to understand our systems, and 
ultimately we should plan to provide visualizations to communicate our results.  This is typically 
accomplished with plots.

In Python: matplotlib, plotly, ggplot, bokeh
In R     : plot() and built-in ploting functions, ggplot2, other specialized libraries
in Octave: plot() and associated functions

> ### Re-Quiz
