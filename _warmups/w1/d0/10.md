---
title: SQLite Practice
---

## The Assignment:
Create an SQLite database to hold information about your classmates and the projects they're working on.

A few details that will make sense later: Use two tables called *students* and *projects*.  *students*
should have fields for first/given name, last/family name, github username, and an id number for their
project.  *projects* should have a unique id number that you assign, a title, and a main programming 
language.  Include, at a minimum, the complete information for at least two projects in the class.

## The Background:
An SQLite database is a single file on your computer that provides a flexible way of storing *structured* 
data. Structured, in this context, means you can describe rules for how different types of information
relate and the database will enforce them.  (For this reason, these kinds of databases are called *relational*
databases.)  For example, you can specify that each student has one project,
each project has at least one student, and students and projects must both have names.  Once you have a
database you can *insert* new data, *update* existing data, *alter* the existing structure of the database,
and *select* information to retrieve from the database.  One of the nice things about using a database for
retrieving data is that you can use rules to control what information you get (e.g., I want all projects
that are using Python) and you can do operations on them too (e.g., I want a list of all projects with a
*count* of how many students are working on each one).

## The Approach:
 
 1. Work through the exercises [in this tutorial](http://www.thegeekstuff.com/2012/09/sqlite-command-examples/)
at least until you think you know how to approach the assignment specified above.
 2. One of the great things about SQLite is that you can work with it on the command line as in that tutorial,
or you can work with it programmatically, meaning you can write a program in a large number of different
languages that will do all of the creating, inserting, and selecting.  The SQLite file will still exist on
the hard drive if you want to inspect your data yourself, but that's not strictly necessary.

    Find a guide or tutorial that explains how to work with SQLite in your preferred programming language.  Here are a couple
options we found [for python](http://www.pythoncentral.io/series/python-sqlite-database-tutorial/) and
[for R](http://rstudio-pubs-static.s3.amazonaws.com/8753_a57d3950027541a590c9b40a045accbf.html).  Feel free to look
around for others.


