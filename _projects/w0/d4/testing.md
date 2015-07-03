---
title: How to Verify and Validate Research Code as You Work
---
During this time, we will identify capabilities you will need to provide in your
project and write tests for your *future* code.

Emphasis on *future*: write the tests for what will be accomplished first, then
the code.

First, write down some tests on paper.  You should be able to use your diagram
from [yesterday](project/organizing-inner/) to identify the parts that you are
concerned about, and the relationships or interactions between them you need to
consider.

Once, you have written down some tests on paper, translate an easy one (and one
that you think you know how to satisfy) to code.  If you're having trouble,
consult your project advisor for assistance.

Once you have a your simplest test down, try to satisfy it by writing project
code.

Then: Repeat!

As always, you should keep track of your progress with version control.  Your basic cycle should be:

 1. write a test that *fails*
 2. `git add` + `git commit` + `git push` test
 3. write code that satisfies test
 4. `git add` + `git commit` + `git push` code
 5. return to start