
title: Language Review II
---

## Loop Constructs

> ### Quiz
>
>  0. For the following `for` loops, which values does `i` take on inside the loop?
>    0. for i in range(2,5): print i
>    1. for (i in 1:4) {print(i)}
>    2. for i = [1,3;2,4] i endfor
>  1. How many times is the code inside these while loop executed? In each case, what is the final value of j?
>    0. i = -1; j = 7;
>       while (j+i < 100):
>           j += j + (-1)**j -1
>           print j
>    1. i = 4; j = 1;
>       while(i>1) { 
>           j = j*i; i = i-1;
>       }
>    2. fib = [1 1 1 1 1];
>       i = 3;
>       while (i <= 6)
>         fib (i) = fib (i-1) + fib (i-2);
>         i++;
>       endwhile
>  2. What list results from each of the expressions below?
>    0. [i*i for i in range(5) if i%2==1]
>    1. sapply(2:5, factorial)
>    2. x=1:10; (x.^2)(mod(x,2)==0)
opening about why looping useful

## `for` and `while` loops
In a sense, for loops are while loops with explicit constraits about some list you are iterating through.
Why bother with for loops at all?

In many cases, sensible constraints result in safer code.  In this case, bugs in while loops are more common
than bugs in for loops.  While loops must be initialized and incremented correctly, and must have a properly
specified condition for exit.  These three parts are generally specified on three separate lines of code, which
can be accidentally deleted or modified, thereby corrupting the loop.  For loops can also fail to start or exit,
but this is much less common because it is usually obvious if you are trying to iterate through an empty list,
or if you are modifiying the container you are iterating through in the loop.  (Hint: NEVER do that.)
incremented correctly, they may never exit

In general, prefer for loops unless it is impractical to use one.  Generally, it is appropriate to use a while
loop when the number of times you need to repeat a block of code is not known to the program.  Occasionally,
while loops may make code clearer than using clever tricks (programmatic or mathematical) to figure out how
many times a loop needs to execute.  An example is reading in a file, line by line.  You could query the OS
to find out how many lines are in the file and then iterate through it using a for loop, but it is usually
more efficient and less complicated to use a while loop.  In this particular case, Python provides a useful
idiom `for line in file('filename')`, so we do not have to resort to a while loop.

## comprehensions
Comprehensions (and their equivalent in non-Python languages) are concise ways of expressing how to convert
one list of things into another.  Very often, that's all we're doing with a loop, but loops tend to take up
more space and may be slower because the interpreter can sometimes be more clever about comprehensions.

Something about functional programming?

map-reduce-filter

re-quiz

## Using Other Code
### Quiz
    0. Python: What is the syntax to load a library?
    1. Python: What do you do if you want to load a library you wrote?
    2. R: What is the syntax to load a library?
    3. R: What is the syntax to run a separate R script at a particular point in your script.
    4. Octave: What is the syntax to load a library?

In most languages it is possible--and sometimes problematic--to have variables and/or functions that share the same
name in two different places.  Names sometimes get reused, particularly simple ones like `i` and `max`.  A simple
example is nested loops.  We so often use `i` as a loop iterator, that it can be easy to write code like this:

for i in [1,2,3]:
    for i in [10,20,30]:
        ...

Although code like this will run in some languages, it is a bad practice because the intent may be misinterpreted by
readers.  Choose a different name for interator in nested loops.

Loading packages may also result in name collisions, and those can be harder to avoid.  In R, for example, a library
called `plotter` might implement a `plot()` function.  Since `plot` is also the name of a base function, what happens 
when `plot()` is called changes when plotter is loaded.  If we still want to call the base package verison of `plot()`,
we need to prepend the function call with a namespace, e.g. `base::plot()`.  In order to avoid ambiguity for readers,
it might also be a good idea to call the other function explicitly as `plotter::plot()`.

Python handles namespaces somewhat more carefully.  The simplest way of loading a library ("module" in Python parlance),
`import plotter`, preserves your namespace.  To access the new plot function here, we would call `plotter.plot()`.  If
you are not concerned with namespace collisions, you can instead use `from plotter import *`, which will import all of
plotter's members, overwriting previously defined variables and functions.  There is no way to access the old
definitions in Python.

In very short programs, it may not be necessary to bother with explicit namespaces.  As software becomes more
complicated, however, it becomes increasingly likely that names will be reused.  In order to maintain readability, and
avoid bugs, as your project grows, consider creating your own libraries (== modules == packages) so that
conceptually-related code is bundled together in its own namespace.


finding packages, finding documentation on packages

re-quiz

## Classes
How we interact with an object, in real life and programming, depends on what type thing that object is.  It does not make
sense to divide words or to spell-check numbers, for example.  In programming, we define how a variable can be interacted
with and what attributes it has by defining a *class*.  In some languages, including Python, everything is an object,
which is the same as saying that everything is an instance of some class.  Classes are a useful way to get away from the
1's and 0's that computers work with because they allow us to work with arbitrarily sophisticated abstractions: a variable
can represent a traffic collision, a connection to a server, or a person.  A class can also be an extension of another. An
athlete object, for example, could have all of the attributes of a person, but also have a team affiliation and performance
statistics.

Classes are also useful because they allow encapsulation.  Within a class, attributes and functions can be either public or
private.  Private things can only be directly accessed or modified within the class, whereas public things are available
anywhere.  To illustrate this, let's consider a polygon class in Python:

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



discuss using `list(...)` as a data object in R

## IO and Visualization

? using console / REPL mode

invoke interpreters + script from OS commandline

reading structured files (csv, json)

arbitrary, sequential line reading

writing structured files

plotting / writing images
