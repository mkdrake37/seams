---
title: Modeling in Code
---

## Choosing the Right Model

 1. What specific problem should be solved by the model?  What specific questions should the model answer?  
 2. How do we want to visualize the results?
 3. What data set(s) will be used by the model?
 4. What are the characterstics of the model?
   * Is it linear?
   * Static or dynamic?
   * Discrete or continuous?
   * Deterministic or stochastic?
 5. How does uncertainty in input affect the output? How stable is the model? (Is the result reproducible)
 6. How can we validate the model?
 7. Is the mathematics used to model clear, concise, and understandable?

### Agent Based Models (ABM's)

 12. What is an ABM?
 13. What does it model well?  What does it model poorly?
 14. What would you use an ABM for?

### Exercise:

Recall the [Agent Based Model of Racial Segregation in NYC](https://www.binpress.com/tutorial/introduction-to-agentbased-models-an-implementation-of-schelling-model-in-python/144)

Quiz: 

 1. What is schelling.agents?  What is its length?
 2. What is the topology of the model?  How could you make it more realistic?  How would you make this change in the code?  What else would this require? 
 3. How can you decide how many iterations to run to ensure the model is effective?  What line of code hints at this answer?  How could you change the code so that a number of iterations is not required, but instead the model stops when most people stop moving (are no longer unsatisfied)?
 4. How does the program compute an unsatisfied agent?  What does an unsatisfied agent do?  

With a partner, answer the following questions and complete the following updates to the model:
 
 1. Run Schelling with 3 colors instead of 2.  What happens at 80% Similarity Threshhold?  How can you explain this?  What does this tell you about your model?
 2. Change the way an unsatisfied agent moves, so that he may only move within a nearby geographic area. Show your work to an instructor.
 3. Incorporate financial status and house prices into the model (so each agent has a certain amount of money and each house costs a certain amount.  Then unsatisfied agents may only move to houses they can afford (remove the previous geographic restriction first).
 4. How could you use real data on house prices and incomes to update this model.  What would you need to do with the data for the model to use it? 
 5. What if after house remain empty for a certain period of time (number of iterations), they can no longer be lived in?  Update the model accordingly.
 6. How would you update the model to change the region to something actually shaped like New York City?  What additional challenges will you have to overcome in the model?  Identify every part of the code that will need to change. 
 7. In what other ways could you make the model more realistic?  What changes to the code will be required for your updates?
