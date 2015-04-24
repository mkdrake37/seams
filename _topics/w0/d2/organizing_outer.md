---
layout: section
title: Organizing Your Workspace
instructor: cabp
---

## Overview

You have a [rough](topic/defining-project/) [project](session/defining-project/) [definition](project/defining-project/).  Now what?

You don't know exactly what the final product looks like, or how you are going to get there, but like every good researcher you want to *follow the scientific method*, *accomplish research effectively*, and *share that work with the community*.

You can help yourself and your collaborators meet these goals by choosing and organizing your tools and workspace effectively.

## Deal With the Fact That You Don't Know!

## Think in Terms of the **Product**

motivate remaining points in terms of what a scientist wants, namely "software"
(*e.g.*, the combination of scripts, analysis code, data management, reference management, external tools devoted to addressing a particular research question / area) that is:

 - easy to use correctly
 - easy to validate (*i.e.*, does what intends) and verify (*i.e.*, produces something
   can be compared to empirical measurements)
 - easy to know when using incorrectly + what to do differently
 - easy to understand, both as a whole and individual parts
 - plausible to deploy in other settings (*e.g.*, distributed computation, GUI tool for non-technical users)
 - generalizable (*e.g.*, different dataset / context)

## Think in Terms of the **Process**

motivate remaining points in terms of how a scientist works.  Organization should
support:

 - shifting data (new data, updates to existing data, changes to schema)
 - effective collaboration with people in different roles (*e.g.*, theoreticians, modelers, field scientists)
 - portability
 - publication (results *as well as recipe*)
 - subsequent extension

## Filesystem + Version Control

### Basic Layout

 - Follow a template

### What to Do About Data?

 - [Data Management Discussion](http://mariovalle.name/sdm/scientific-data-management.html)
 - [Boston University Discussion](http://www.bu.edu/datamanagement/outline/elements/) - good surrounding context discussion as well
 - [Discussion of Long vs Short Form Data](http://seananderson.ca/2013/10/19/reshape.html), and from `reshape2` package author
 - [J. Stat. Soft. article discussing](http://www.jstatsoft.org/v21/i12)
 - [SO: Why Use SQL Database?](http://stackoverflow.com/questions/2900324/why-use-sql-database)
 - [UK Data Archive](http://www.data-archive.ac.uk/media/2894/managingsharing.pdf) - good general read, but certain specific sections pertinent to how to organize / save yours

### Version Control

 - [SO: Why Should I Use Version Control?](http://stackoverflow.com/questions/1408450/why-should-i-use-version-control) and [Academia SE: Why Use VC for Writing a Paper?](http://academia.stackexchange.com/questions/5277/why-use-version-control-systems-for-writing-a-paper)
 - [Biomed Central Blog](http://blogs.biomedcentral.com/bmcblog/2013/02/28/version-control-for-scientific-research/) - several links to other publications on value of version control in science, including:
 - [ArXiV description](http://arxiv.org/pdf/1210.0530.pdf)
 - [PLoS Computational Biology](http://dx.doi.org/10.1371/journal.pcbi.1003285)
 - [Assorted Reddit Discussions](http://www.reddit.com/r/programming/search?q=why+version+control&restrict_sr=on)



 - what kind of bits will be in a project?
   * data, possibly in several formats
   * analysis, possibly in several languages
   * visualization, possibly in several languages
   * outputs, possibly in several formats (flat files, images, *etc.*)
   * reference material
   * documentation
   * meta-data, *e.g.* configuration for tools
 - what kind of particular bits need to be on the computer, but not specifically part of the project?
   * compilers / interpreters
   * libraries (*e.g.*, `R` packages, `python` modules)
   * support tools (*e.g.*, `git`)
 - which bits go in the repository?
   * are there controls on the data (*e.g.*, is it human subjects data? private business data)?
   * which outputs belong in the repository? intermediate vs. final steps.  artefacts that take substantial time to build
   * what configuration files are local vs. general?
   * how are dependencies handled?
 - how do you organize the pieces of the project in a way that addresses these needs and permits both collaborative + local work.  Always online is great (in principle) for collaboration, but can preclude work unless quality internet connection present.  Also
 trade off problems of making bad changes easily / with low visibility vs dealing with integrating local work

## Operating System Tools

 - searching tools: `grep`, `ls` and regular expressions
 - transforming tools: `sed`, `awk`
 - writing with `>`, `>>`
 - directing data into other commands: `|`, `<<`
 - manipulating files: `rm`, `cp`, `mv`
 - environment variables
 - command line scripts (*e.g.*, `bash`)
 - scripts for other tools (*e.g.*, pbs)
 - where do I find help / documentation?

## Coding Tools

### Editors

 - [Overview of Text Editors](http://en.wikipedia.org/wiki/Comparison_of_text_editors) - what comes across as important?
 - Instructor Preferences:
   * Carl: Atom, PyCharm, RStudio, Eclipse
   * Ethan:
   * Tom:
   * Marjie:
   * Nicky:

### IDE Organization Tools

 - [RStudio IDE Project](https://support.rstudio.com/hc/en-us/articles/200526207-Using-Projects)
 - [PyCharm IDE Project](https://www.jetbrains.com/pycharm/help/project.html)

 - editor
   * bare minimum: plain text
   * next priority: syntax highlighting
   * next priority: syntax / logic / type checking (*i.e.*, static analysis)
   * higher level priorities: integration with other tools (*e.g.*, version control, worksheet mode / consoles / graphics display, library + package management)
 - compiler / interpreter
 - optional: build tools, dependency management
 - static analysis tools: linters, code beautifiers, etc

## Publication

 - goal of our work as scientists is to create useful knowledge (*useful* may be defined on a very long time scale).  knowledge doesn't exist if people don't have access to it,
 and it's not useful if they can't engage with it given access
 - one foundation of scientific way of knowing is replicability: I describe *recipe* that leads to *results*, you can follow recipe and attain the same results
 - sometimes that description is hard: *e.g.*, we forget to include items that seem trivial to us, but are critical to people new to this area
 - code details are often hard



How to organize various parts of a project.

Separating data / configuration elements into their own area.

Organizing code by scripts, analysis source, visualization source, etc.

Pipelining in publication (e.g., Rweave).

tools: version control + IDEs + data viewers.
