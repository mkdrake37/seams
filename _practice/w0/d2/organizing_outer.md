---
title: Building a Stadium for Football Exercises
instructor: carl
---

In this practical, we will apply ideas from the morning discussing.  Particularly, we will create workspaces for the rest of the afternoon practicals ([see the full list here]({% include url.lq %}practice/)) by:

 0. reviewing the projects,
 1. creating places for them in the filesystem,
 2. creating repositories for each of them,
 3. attaching the repositories to the filesystem, and
 4. stubbing out files / templates for those exercises

Got your list?  Time to hit the keys!

The last piece of specific guidance is that you check-in with a **peer** and an **instructor** after each step, and **demand critical feedback** on what you did: DO NOT SETTLE FOR "LOOKS GOOD!"

We recommend that you try out the full list for *one* of the practicals first, so that you can be certain to get feedback on the whole process during this time.  Also, you may discover some approaches in the last step which help with the earlier ones.  The rest of this page provides some loose suggestions on how to attack those tasks.

## REVIEWING

For each step, first think a moment about what we discussed in the morning and answer some of the questions that came up and what you learned from the exercises.  At the highest level, the question is **always**: "what I am trying to accomplish and how should I organize towards that?"  Often, that's hard to tell at first, but we can typically break it down:

 - Does the project have data?  If so: What is your data?  How are you going to handle it?  Where does it "want" to be?  Who else needs to access it?  Is there more coming in?  What's your plan for *provenance*, if you need to modify the raw data?  Will you want to test code on its schema or small portions of it (hint: *yes*)?
 - Likewise, what's your plan for your results?
 - Someone will be seeing your code -- *e.g.*, the source directly when reviewing your work, importing it into their own as a library, interacting with it as a tool -- how are you going to get the product to them?
 - Which languages or other tools are you using?  What are the conventions for them?  Do you need to control those to particular versions?
 - How many people will be working with the code?  How are you going to manage that process towards successful collaboration?

That's far from a comprehensive list - but try going through it for each of the other practicals, and **write down** a quick answer for the ones that seem to apply.

## FILESYSTEM

Everyone has experienced the cluttered desktop (either personal or via a co-worker).  The clutter makes finding anything difficult, and its really confusing for people that didn't make that mess.

There is an easy and simple way to *start* to address this problem: make a projects folder.
In that folder, make another folder for each project.  Whenever you work on a project, only work in its folder.  If you work only in that folder (or sub-folders within it), you will always know where to look for work related to that project.

Working in single directory is easier said than done, but if you haven't started with one place to work, you *definitely* won't end up working in one place.

Another simple but overlooked practice is naming.  Which is more useful: `project1/` or `cams_testing_exercise`?  Don't worry about getting the perfect name, but spend a least a few thoughts on picking a descriptive one.

One last note: sometimes you have materials or tools that are used across multiple projects.  That's typically a good sign.  Like your projects, you want to keep these in one place, alongside your other work.  You can let a particular project see these materials like they are in the project's directory using symbolic links.

## VERSION CONTROL

The point of version control is to have a definitive copy of what you're working on, and how it came to be that way.  It should make it easy to work with a team, as well as on your own.  It can also naturally integrate with sharing your work.

Version control concerns *repositories*, one for each project in version control.  It is natural to have these repositories mirror the project folders you set up.  But there are a few additional concerns:

 - what actually goes into version control, and what remains just local?
 - how does your team use the master repository?  is one person responsible for commits, or can anyone make changes?
 - since you won't want to put everything in the repository, how do you manage sharing what *doesn't* go in it?

## USING TEMPLATES

Do you want other people to use what you develop?  Then you need to make it easy for them to get.  Today, that means accessible via major code-distribution sites like *CRAN*, and also able to be managed via the languages package management system.

That means your work needs to have a particular structure, often a somewhat peculiar one that meets lots of confusing rules.  Templates take care of the rules for you (or at least, go a long way towards doing so), meaning you can focus on what you actually want people to get.