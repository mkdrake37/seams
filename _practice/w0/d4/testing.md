---
layout: section
title: How to Verify and Validate Research Code as You Work
---

Ex.1 Hand off codes with model bug, they write tests
(Potential contest: which team can find flaw first)

-(easy) weather calculations:
Solution: pV  = nRT, code not prepared for T = 0

-(hard)"elevator" problem phrased as bus route problem (delivering fans to stadiums):
Solution: not all bus stops are actually reachable in given model

-more examples (e.g. Taylor series not converging on given input):
http://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.204.5875&rep=rep1&type=pdf

Ex. 2 students exchange code and write tests
-students may hand off any of their previous work for testing, as long as it is reasonably sophisticated. 
-students take ~15 minutes to write good APIs as needed. No verbal discussion with tester allowed
-tester writes code for testing and writes short report

Ex. 3 Students given code with bugs and apply new debugging techniques 







Assess how effective code is.  Specifically:
~Edge Cases
~Unexpected inputs (i.e. prob>1, prob<0)
~Actual results (comparison)
~Error stats
~Proper use of exceptions

Two tasks: (1) Have students assess and correct provided code.  (2) Students have already created code which performs specific tasks.  We'll ask them to test the quality of this code by testing edge cases (e.g. Manchester United defeats Ghana) and comparing to (newly provided) data.
