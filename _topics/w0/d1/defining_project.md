---
layout: section
slug: defining_project
title: How to Define a Programming Project in Research
---

(Software) Engineering: Application of scientific principles toward practical ends. Trying to apply formal methods to all software projects is as bad an idea as trying to apply code-and-fix development to all projects.

“Treating software as engineering makes clearer the idea that different development goals are appropriate for different projects. When a building is designed, the construction materials must suit the building’s purpose. I can build a large equipment shed to store farming vehicles from thin, uninsulated sheet metal. I wouldn’t build a house the same way. But even though the house is sturdier and warmer, we wouldn’t refer to the shed as being inferior to the house in any way. The shed has been designed appropriately for its intended purpose. If it had been built the same way as a house, we might even criticize it for being “over-engineered”—a judgment that the designers wasted resources in building it and that it actually isn’t well engineered.”

PRODUCT OBJECTIVES:
Minimal defects
Maximum user satisfaction
Minimal response time
Good maintainability
Good extendibility
High robustness
High correctness
→ How important is each objective for your project?

“Some projects need to produce software with minimal defects and near-perfect correctness—software for medical equipment, avionics, anti-lock brakes, and so on. Most people would agree that these projects are an appropriate domain for full-blown software engineering. Other projects need to deliver their software with adequate reliability but with low costs and short schedules. Are these properly the domain of software engineering?”

OTHER CONSIDERATIONS:
Short schedule
Predictable delivery date
Low cost
Small team size
Flexibility to make mid-project feature-set changes

Frequent causes of software project failure have to do with requirements problems—requirements that define the wrong system, that are too ambiguous to support detailed implementation, or that change frequently and wreak havoc on the system design.[9] But requirements problems are not new. Back in 1969, Robert Frosch observed that a system could “satisfy the letter of the specification and still not be very satisfactory.”[10]

Ask good questions! Translate your researchers' questions into questions you can answer and they want answered.
1. Initially research questions do not have "obvious" solutions. Requirements in a scientific setting...
2. SCOPE, REQUIRED INTERFACES: Also deal with questions of what scope to address -- namely, what parts does your
code do explicitly, what parts do you with system tools or libraries.
3. What will the code be used for? Deal with addressing different parts of project with different tools (e.g.,
munging raw data w/ Python, doing simulation in C++, visualizing output with R).
Talk about thinking in terms of pipeline.
4. Publication? "Publication" programming - having an approach that you can describe in a publication
that someone else can review / publish.

Paragraphs taken from:
(http://www.stevemcconnell.com/psd/04-senotcs.htm, http://www.stevemcconnell.com/psd/01-dinosaurs.htm)
