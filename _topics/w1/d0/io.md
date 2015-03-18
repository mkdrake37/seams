---
layout: section
title: IO - Why, What, When, Where, and sometimes How
---

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
