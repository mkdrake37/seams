---
title: Modeling in Code
---

## Choosing the Right Model

### General Questions

 1. What specific problem should be solved by the model?
 2. What specific questions should the model answer?  (How do we want to visualize the results?)
 3. What data set(s) will be used by the model?

### Characteristics?

 4. Is it linear?
 5. Static or dynamic?
 6. Discrete or continuous?
 7. Deterministic or stochastic?

### Evaluation?

 8. How stable is the model? (Is the result reproducible)
 9. How does uncertainty in input affect the output?  
 10. How do we validate the model?
 11. Is the mathematics used to model clear, concise, and understandable?

### Agent Based Models (ABM's)

 12. What is an ABM?
 13. What does it model well?  What does it model poorly?
 14. What would you use an ABM for?

### Exercise:

Recall the [Agent Based Model of Racial Segregation in NYC](https://www.binpress.com/tutorial/introduction-to-agentbased-models-an-implementation-of-schelling-model-in-python/144)

With a partner, answer the following questions and complete the following updates to the model:

 1. How does the program compute an unsatisfied agent?  What does an unsatisfied agent do?  Change the way an unsatisfied agent moves, so that he may only move within a nearby geographic area. Show your work to an instructor.
 2. Incorporate financial status and house prices into the model (so each agent has a certain amount of money and each house costs a certain amount.  Then unsatisfied agents may only move to houses they can afford (remove the previous geographic restriction first).
 3. How could you use real data on house prices and incomes to update this model.  What would you need to do with the data for the model to use it? 
 4. What if after house remain empty for a certain period of time (number of iterations), they can no longer be lived in?  Update the model accordingly.
 5. How would you update the model to change the region to something actually shaped like New York City?  What additional challenges will you have to overcome in the model?  Identify every part of the code that will need to change. 
 6. In what other ways could you make the model more realistic?  What changes to the code will be required for your updates?
