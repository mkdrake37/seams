---
layout: section
title: Interfaces
---

How to have an "interface" to your code.

Making your code a library / package / command line tool / etc.

What makes a good interface?  A bad interface?

## Definition/Reason

Interfaces: Contracts between two objects, whether between two chunks of codes or between a user and software.
Analogy: If a software project were an organism and libraries/packages are organs, then an interface would be how different organs interact with each other. "To get blood, call ReceiveBlood()."

Some specifics: Difference from abstract class: Abstract class is a block of code that implements these functions and then has a contract for how other code will interact. Interfaces are contracts that any block of code can satisfy. Analogy: An abstract class would be a heart. But anything that pumps blood is an interface.
In Python, these are not seperated. Anything that pumps blood is a heart.

Interfaces are necessary to create modular code.

## Good vs. Bad

Good qualities:
-Obscure intracacies of code
-Provide clear limitations (input/output)
-Bug-free
Bad qualities:
-Overly detailed
-Unclear
-Crashes/Slow
