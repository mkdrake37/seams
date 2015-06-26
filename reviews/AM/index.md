---
title: Language Review I
---

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
algebra, operators can take on different meaning, but groups (and fields, rings,
*etc*.) have a fixed definition.

In the programming context, these *syntactical* elements are referred to by many
different labels (keywords, reserved words, operators, *etc*.).  While there can
be nuanced distinctions between these concepts, the practical definition is
quite simple: these are the (sequences of) characters that have a fixed meaning
in your code.  *I.e.*, you cannot redefine their meaning.

Keep these in mind as we move through the following sections - they show up in
almost all of them.

> ### Re-Quiz

## Variable Declaration

> ### Quiz: Variable Declaration
>
>  0. Declare an integer in R, Python, and Octave
>  1. Declare a sequential data structure (*i.e.*, a collection with items in ordinal positions) in R, Python, and Octave
>  2. Declare a key-value data structure (*i.e.*, a collection with keys mapping to values) in R, Python, and Octave
>  3. Contrast immutable and mutable variables and collections.
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
positions (*e.g.*, array) or associated with particular keys (*e.g.*, `dict`s).

small exercise

> ### Re-Quiz: Variable Declaration
{:.re.quiz}

## Function Declaration

> ### Quiz: Function Declaration
>
>  0. Declare a function in R, Python, and Octave
>  1. What does "signature" mean relative to functions?
>  2. Write a function in R, Python, and Octave that returns multiple values.

Like in mathematics, a *function* is a special kind of variable in programming.
Functions represent a transformation from inputs to outputs.

There are some functions that are *built-in* - these can behave differently from functions you define in your code.

re-quiz

## Scope

> ### Quiz: Scope
>
> Running the following blocks of Python, what is print out?
>  ...TODO some blocks with variables in different scopes
>
> Running the following blocks of Python, what is print out?
>
> Running the following blocks of Octave, what is print out?

quiz - check knowledge of global vs local scope

re-quiz

## Logical Operators & Conditionals

> ### Quiz: Logical Operators & Conditionals
>
>  0. What are the operators, keywords, or built-in functions for *and*, *or*, *not*, and *xor*?
>  1. In the following Python code, what is print out?
>    ...TODO some blocks with conditional forking and print statements
>  2. In the following R code, what is print out?
>  3. In the following Octave code, what is print out?



quiz - check knowledge of operators, check knowledge of branching (which statement prints?)

and, or, not, xor

if, else, else if, unless

elvis?

ifelse

re-quiz
