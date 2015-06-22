---
title: IO - Why, What, When, Where, and sometimes How
---

## Communicating with the outside world
 - examples?

## Important context
 - interactive, human user?
 - quick and dirty?
 - need for speed?
 - rigid specification?

## The options
 - STDIO
 - ad hoc text
 - csv, tab, etc.
 - HTML, XML, JSON, etc.
 - binary
 - database
 - specialized file formats (e.g., tiff, hdf5, docx)

 Spend 10 minutes researching one of the following topics (to be assigned):
 1) What are standard out and standard error?  What's the difference, and how 
 do you write to them on the command line and in [your language here].
 2) What is a markup language, and what are some examples?  What advantages
 and disadvantages do markup languages have over simple text?
 3) In your own words, what is database normalization?  What's the point?
 4) Choose a specialized file format, explain when it should be used,
 and what advantage it has over plain text.  

## Parsers
 - existing, established
 - making your own (use the standard, write tests, be fastidious)

Making choices about input formats: raw text, structured text (e.g., csv),
binary, databases.

What should be input?  Obviously empirical data - slightly less obvious
simulation parameters, even less obvious analysis configuration parameters.
However, often very valuable to be able to have configuration of setup / results
as an input.  Importance of random seed as input.

Making choices about output.  Checkpointing.  Value of checkpointing to debugging,
but also scaling up to supercomputer approaches, use in alternative analysis /
visualization streams or handing off to other researchers.  What to save as
interim results.

What to save as "final" results, and how to save it.  Value of having simulation
outputs AND separate visualization, not just final plots.
