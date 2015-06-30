---
title: How to Define a Programming Project in Research
---

##Part 1: Research and the Research Problem

What is **research**?  

What is research in software engineering?

What is the **scientific method**?  

Where does software engineering play a role in the scientific method?

What makes a good **research problem**?

How do you break down a research problem into subproblems? (*Part:Whole, History, Use*)

####Develop a Research Problem

As a group, answer the following questions, and present a research problem based on your topic.

* Is this a research problem?  If not, can you turn it into a research problem?  
* What sort of data do you expect to use?  How do you expect the quality of data to vary?  How do you expect to use code in your research?
* What subproblems might arise?  How could you appropriately limit the scope of the problem?

1. A study to compare the results in school history exams for 16-year-olds throughout Europe between 1970 and 1980.
2. The impact of local tax and exaction policies on the Maghreb commercial office sector.
3. The relationship between temperature, humidity and air movement in the cooling effect of sweating on the human skin.
4. The effects of using glass of different thickness and qualities in single, double and triple glazing.
5. What factors must be evaluated and what is their relative importance in constructing a formula for allotting grants to university students in Egypt.
6. Whether the advantages of foreign borrowing by Third World countries outweigh the disadvantages.

####Evaluating a research proposal.  

[Read pg 24-25 here, then answer questions 1-7](https://www.nyu.edu/classes/bkg/methods/010072.pdf)


##Part 2: Problems from Past Theses

####**TB**
*“A systems level analysis of different Mycobacterium Tuberculosis strains using functional interaction networks” by Linsay Blows*
 - Compare and contrast the protein interactions within 4 strains of the same bacteria. Try to answer which proteins of tuberculosis are essential for biological functionality, and find connections between different strains.
 
######Questions:
- Overall: How to construct a program that will in someway answer these questions.
- What data is available and how do you interface with the data (for this GenBank, Ensembl, NCBI)?
- What do we do with the uncertainty of the figures that the data provides and how we incorporate it?
 
######Her method:
- “To perform these analyses we first have to construct protein-protein functional interaction networks for each strain, these networks can be used to compare the different strains. Our objective is to try and understand how genetic differences between strains could possibly influence the structure or topology of the functional networks we have produced.”
 
######Implementation questions:
- How do we represent the network in our code?
- Which language/software is appropriate for this project?
- Will this be computationally intensive / need to utilize optimization techniques.
 
####**ASL**
*“Local Features for American Sign Language (ASL) Recognition” -Ali Bakar*
- https://xkcd.com/1425/
- Problem: Want to improve program that turns ASL into text.
 
######Questions one should ask:
- What is the current state of the program and how does the program work?
- What data do we have available?
- When does this program malfunction? Is there a trend to these inaccuracies?
 
######Conclusion:
- “The project employed the ’Scale Invariant Feature Transform’ (SIFT) algorithm to detect, extract and analyse the image local features. The method is preferred because it maintains the invariance property for images with scale change and rotation. It also has a strong adaptation to image deformation and illumination. Moreover, SIFT has good localizing accuracy and computing speed.
- In my project I did some modifications to these images. I pre-computed the key features for each image. Therefore I replaced the image files by keypoint files. Then I reduced the number of keypoints in each file to optimal number which retain the important features.”
 
######Implementation Questions:
- How do you determine where the sign is via edge detection?
- How can we change the input pictures so the algorithm works better?
- What are key features of a particular sign that distinguishes a sign? How do we create that in code.
- How do we test the effectiveness of our changes?
 
####**Plumes**
*“Modelling transport of air pollutants using the Gaussian plume” -Masingita Errol Manganyi*
- Problem: Accurately describe transport of air pollutants under various circumstances.
 
######Questions you should ask:
- What data is available to us? How do we incorporate error?
- Are there models for this problem or a related problem available?
- What are the different factors that contribute?  Are there instances when modeling is particularly difficult?
- What physics are important for us to understand?
 
######Answer: 
- “In this essay, three methods were applied to solve the two dimensional diffusion equation. Its solution, called Gaussian plume model, was derived using Laplace transform, Green’s function and Lax Wendroff scheme methods. The concentration of the plume was calculated using Laplace transform and Lax-Wendroff scheme. In order to compare the analytical solution with the numerical solution, the same values were used in both methods. The results of two methods, Laplace transform and Lax-Wendroff scheme were then plotted.”
 
######Questions:
- What software/data structures are appropriate?
- How do we represent this diffusion pattern in our code?
- What instances to the above models behave poorly under?
- How do we compare analytic and numerical solutions?
