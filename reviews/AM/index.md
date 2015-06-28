---
title: Language Review I
---

FOR ALL QUIZZES: WRITE ALL ANSWERS ON PAPER FIRST.  WHEN WE RE-QUIZ, TYPE ANSWERS TO CODE QUESTIONS INTO THE APPROPRIATE CONSOLE.

## Keywords, Reserved Words and Tokens, and Operators

> ### Quiz
>
>  0. List five reserved words in R.
>  1. List five reserved words in Python.
>  2. List five reserved words in Octave.

In all programming languages, there are certain characters, words, and symbols
that have a fixed meaning and must be used in certain ways.  This is the same as
notation conventions in various mathematical fields.  When we talk about
arithmetic, `+` and `=` have fixed definitions.  If instead we are talking about
algebra, operators can take on different meaning, but saying something is a
group (or field, ring, *etc*.) has a fixed meaning.

In the programming context, these *syntactical* elements are referred to by many
different labels (keywords, reserved words, operators, *etc*.).  Some minor
language specific distinctions aside, they share the same practical definition:
these are the (sequences of) characters that have particular uses in your
code, and you cannot redefine their meaning.

Keep these in mind as we move through the following sections - they show up in
almost all of them.

> ### Re-Quiz

## Variable Declaration

> ### Quiz: Variable Declaration
>
>  0. Declare an integer in R, Python, and Octave
>  1. Declare a sequential data structure (*i.e.*, a collection with items in ordinal positions) in R, Python, and Octave
>  2. Declare a key-value data structure (*i.e.*, a collection with keys mapping to values) in R, Python, and Octave
>  3. Declare a variable derived from other variables.
>  4. Contrast immutable and mutable variables and collections.
{:.quiz}

"Variable" has a similar (*but not identical!*) meaning in programming and mathematics.

They are similar in the sense that we can express relationships between
variables, and transformations of them, and so on, in both perspectives without
having to know particular values.  Of course, to get particular results in
either, we need to know the particular variable value.

"Variable" in programming tends to be bit more expansive than typical use in
mathematics, but in both realms we think of variables as being constrained to a
certain domain - *e.g.*, something might be a "natural" or "complex" scalar (or
vector, matrix, *etc*).  The same is true in programming, and these domains are
called *types*.  When a variable is actually several items of some type gathered
together, this is generally called a *collection*, with specific names for
different types of collections that either have items in particular ordinal
positions (*e.g.*, `array(...)` in *R*) or associated with particular keys (*e.g.*, `dict`s in *Python*).

> ### Re-Quiz: Variable Declaration
{:.re.quiz}

## Function Declaration

> ### Quiz: Function Declaration
>
>  0. Declare a function in R, Python, and Octave
>  1. What does "signature" mean relative to functions?
>  2. Write a function in R, Python, and Octave that returns multiple values.
>  3. Write a function in R, Python, and Octave that has no inputs or outputs, but has a side-effect.
{:.quiz}

Like in mathematics, a *function* is a special kind of variable in programming.
In mathematics, functions represent a transformation from domain to range; the same is true in programming, though functions (or approximate synonyms like *methods*, *definitions*, *procedures*) can often also produce side-effects (*e.g.*, writing a file or drawing a plot), and we call the domain *arguments* and range *returns*.

In programming, we typically use functions as a way to organize a related series of instructions to the computer.  This is similar to how we use functions to represent mechanisms in applied mathematics (modeling).

Like other variables, functions have a *type* defined by the type of the arguments it accepts and the type of its returns.  This type is sometimes called the *signature*.

There are some functions that are *built-in* - these can behave differently from functions you define in your code.

Like other variables, functions may be arguments to other functions.  In
mathematics, this notion appears in composition and with operators (*e.g.*,
operators in physics, summation or product operators).  In programming, this is
often called a *functional* approach, and functions which are supplied as
arguments are often called *lambda* functions.

> ### Re-Quiz: Function Declaration
{:.re.quiz}


## Scope

> ### Quiz: Scope
>
> 0. Running the following Python, what is print out?
>
{% highlight python %}
a = 4

def afun(a):
  print(a)

afun(a)
afun(2)
{% endhighlight %}
>
> 1. Running the following blocks of R, what is print out?
>
{% highlight r %}
a <- 4

afun <- function(a) {
  print(a)
  a <- 7
}

afun(a)
afun(2)
{% endhighlight %}
>
> 2. Running the following blocks of Octave, what is print out?
>
{% highlight octave %}
a = 4

def afun(a):
  print(a)

afun(a)
afun(2)
{% endhighlight %}
>
{:.quiz}

In programming, *scope* is how the computer determines the value of a variable.  If we only ever use unique variable names, then scope is simply a question of how does the computer *find* the variable.  Is it a function argument?  Defined within the function?  Defined outside the function at the same level?  Globally defined?  Your code will need to ensure that the computer can find the appropriate variable.  This happens differently in different languages, so you will need to understand at the general way it happens in one you choose.

This is akin to understanding the definition of variables in applied mathematics problems based on the *context* of the problem.  Are we talking about physics?  Then *c* probably refers to the speed of light, and we can use the mass-energy equivalence in whatever specific problem we are addressing.  Are we solving quadratics?  Then *c* is probably the constant coefficient of a quadratic polynomial, and we can use the quadratic formula.

The overlap in names in that mathematics example (*i.e.*, *c* is both the speed of light and a particular coefficient in a quadratic) highlights another important aspect of scope: when your code re-uses names, how does the computer know which *c* to use?  Like finding the variables, different languages resolve these questions differently, so make sure you know what's happening with yours.

> ### Re-Quiz
{:.re.quiz}

## Logical Operators & Conditionals

> ### Quiz: Logical Operators & Conditionals
>
>  0. What are the operators, keywords, or built-in functions for *and*, *or*, *not*, and *xor* in R, Python, and Octave?
>  1. In the following code blocks, what is print out?
>
{% highlight python %}
def testfun(a):
  if (a == 5):
    print("five alive!")
  elif ((a % 2 != 0) & (a % 3 == 0)):
    print("that's triply odd!")
  else:
    print("even odds are boring!")

testfun(5)
testfun(15)
testfun(2)
{% endhighlight %}
>
{% highlight r %}
a <- 1:10
ifelse(a < 5, "need at least 5", "woohoo!")
{% endhighlight %}
>
{% highlight octave %}
a = 4

if (a % 2 != 0)
  printf("that's odd...\n")
elsif (length(unique(factor(a))) != 1)
  printf("it has multiple prime factors...\n")
else
  printf("boring power!\n")
endif
{% endhighlight %}
>
{:.quiz}

Programming and mathematical logic share a very deep connection.  At a fundamental level, computers are constructed of components called *logic gates* and programming languages ultimately translate to manipulation of the arrangements of these gates.

Beyond all the logical operations under the hood, however, logical operations are a common part of a programmer's toolkit.  Often we want to take different actions depending on how one value compares to another (*e.g.*, is `a < 5`?), and often we want to combine multiple comparisons (*e.g.*, is `a > 0` **and** `a < 5`).

Once we have evaluated a condition as `true` or `false`, we can direct the flow of the program through different branches of action via `if` and `else` keywords.  The details of how to do so varies by language, so make sure you understand how these work for your language of choice.

A final note, though not specific to actual code syntax: a useful way to think about how to direct flow with conditionals is to use *truth tables*.  Truth tables are an enumeration of the possible condition combinations and what you want to happen in response to them.  They also have a side benefit: if your conditionals are too complex, then you will have trouble writing out the tables and know you need to consider a different approach.

> ### Re-Quiz
{:.re.quiz}