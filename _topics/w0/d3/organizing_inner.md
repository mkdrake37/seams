---
title: Organizing inside Your Source - Best Practices, Separation of Concerns
---

## Guido's Style Guide for Python Code
https://www.python.org/dev/peps/pep-0008/

## Structuring Your Project
http://docs.python-guide.org/en/latest/writing/structure/

## Why are spaces preferred over tabs as indentation?
http://www.reddit.com/r/learnpython/comments/34dpn4/why_are_spaces_preferred_over_tabs_as_indentation/

## How can I implement classes in my code? (chess)
http://www.reddit.com/r/learnpython/comments/34eos6/how_can_i_implement_classes_in_my_code_chess/

## Function interface design
From http://www.greenteapress.com/thinkpython/html/thinkpython005.html
######################################################################
4.6  Interface design

The next step is to write circle, which takes a radius, r, as a parameter. Here is a simple solution that uses polygon to draw a 50-sided polygon:

def circle(t, r):
    circumference = 2 * math.pi * r
    n = 50
    length = circumference / n
    polygon(t, n, length)

The first line computes the circumference of a circle with radius r using the formula 2 π r. Since we use math.pi, we have to import math. By convention, import statements are usually at the beginning of the script.

n is the number of line segments in our approximation of a circle, so length is the length of each segment. Thus, polygon draws a 50-sides polygon that approximates a circle with radius r.

One limitation of this solution is that n is a constant, which means that for very big circles, the line segments are too long, and for small circles, we waste time drawing very small segments. One solution would be to generalize the function by taking n as a parameter. This would give the user (whoever calls circle) more control, but the interface would be less clean.

The interface of a function is a summary of how it is used: what are the parameters? What does the function do? And what is the return value? An interface is “clean” if it is “as simple as possible, but not simpler. (Einstein)”

In this example, r belongs in the interface because it specifies the circle to be drawn. n is less appropriate because it pertains to the details of how the circle should be rendered.

Rather than clutter up the interface, it is better to choose an appropriate value of n depending on circumference:

def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 1
    length = circumference / n
    polygon(t, n, length)

Now the number of segments is (approximately) circumference/3, so the length of each segment is (approximately) 3, which is small enough that the circles look good, but big enough to be efficient, and appropriate for any size circle.
######################################################################
