---
title: Building a Stadium for Football Exercises
instructor: cabp
---

In this practical, we will apply ideas from the morning discussing.  Particularly, we will create workspaces for the rest of the afternoon practicals ([see the full list here](practice/)) by:

 0. reviewing the projects,
 1. creating places for them in the filesystem,
 2. creating repositories for each of them,
 3. attaching the repositories to the filesystem, and
 4. stubbing out files / templates for those exercises

Got your list?  Time to hit the keys!

The last piece of specific guidance is that you check-in with a **peer** and an **instructor** after each step, and **demand critical feedback**: DO NOT SETTLE FOR "LOOKS GOOD!"

We recommend that you try out the full list for *one* of the practicals first, so that you can be certain to get feedback on the whole process during this time.  The rest of this page provides some loose suggestions on how to attack those tasks.

## REVIEWING

For each step, first think a moment about what we discussed in the morning and answer some of the questions that came up and what you learned from the exercises.  At the highest level, the question is **always**: "what is the task and how should I organize towards solving it?"  Often, that's hard to tell at first, but we can typically break it down:

 - Does the project have data?  If so: What is your data?  How are you going to handle it?  Where does it "want" to be?  Who else needs to access it?  Is there more coming in?  What's your plan for *provenance*, if you need to modify the raw data?  Will you want to test code on its schema or small portions of it (hint: *yes*)?
 - Likewise, what's your plan for your results?
 - Someone will be seeing your code -- *e.g.*, the source directly when reviewing your work, importing it into their own as a library, interacting with it as a tool -- how are you going to get the product to them?
 - Which languages or other tools are you using?  What are the conventions for them?  Do you need to control those to particular versions?
 - How many people will be working with the code?  How are you going to manage that process towards successful collaboration?

That's far from a comprehensive list - but try going through it for each of the other practicals, and **write down** a quick answer for the ones that seem to apply.

## FILESYSTEM

Everyone has experienced the cluttered desktop (either personal or via a co-worker).  The clutter makes finding anything difficult, and its particularly confusing for people that didn't make that mess.

There is an easy and simple way to start to address this problem: make a projects folder.
In that folder, make another folder for each project.  Whenever you work on a project, only work in its folder.

That last part is easier said than done, but if you haven't started with one place to work, you *definitely* won't end up working in one place.

Sometimes you data that belongs with one project, sometimes with many.  

## Rough Outline for Long Exercise

 - select tools for the job: based on problem, skill set, goals - ensure those
 tools are available, configured correctly.  
 - set up repository
 - layout parts w/in filesystem/repo: folders/files for:
   * data
   * sources (partitioned by language, task)
   * testing work
   * top level scripts
   * any configuration items
   * intermediate results
   * plots / visualization
   * publication / lit items
 - select what to have in / out of repository
 - layout project tasks as issues
 - stub out code source files

Small group review focused on discussing:
 - what are the one-click / one-command items setup?
 - how does the organization support those? support portability? support
 working locally?
 - can other people look at the filesystem and "just get it"?
 - options for review: have people swap workstations, look at others organization for
 5 minutes, then try to explain it to group, and have actual owner explain any missed
 points.  from that, actual owner will have items to fix.  Also have people list a
 few items from other approaches that they wished they had done.
