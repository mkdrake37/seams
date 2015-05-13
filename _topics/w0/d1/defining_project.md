---
title: How to Define a Programming Project in Research
---
#1) TB
*“A systems level analysis of different Mycobacterium Tuberculosis strains using functional interaction networks” by Linsay Blows*
 - Compare and contrast the protein interactions within 4 strains of the same bacteria. Try to answer which proteins of tuberculosis are essential for biological functionality, and find connections between different strains.
 
###Questions:
- Overall: How to construct a program that will in someway answer these questions.
- What data is available and how do you interface with the data (for this GenBank, Ensembl, NCBI)?
- What do we do with the uncertainty of the figures that the data provides and how we incorporate it?
 
###Her method:
- “To perform these analyses we first have to construct protein-protein functional interaction networks for each strain, these networks can be used to compare the different strains. Our objective is to try and understand how genetic differences between strains could possibly influence the structure or topology of the functional networks we have produced.”
 
###Implementation questions:
- How do we represent the network in our code?
- Which language/software is appropriate for this project?
- Will this be computationally intensive / need to utilize optimization techniques.
 
#2) ASL
*“Local Features for American Sign Language (ASL) Recognition” -Ali Bakar*
- https://xkcd.com/1425/
- Problem: Want to improve program that turns ASL into text.
 
###Questions one should ask:
- What is the current state of the program and how does the program work?
- What data do we have available?
- When does this program malfunction? Is there a trend to these inaccuracies?
 
###Conclusion:
- “The project employed the ’Scale Invariant Feature Transform’ (SIFT) algorithm to detect, extract and analyse the image local features. The method is preferred because it maintains the invariance property for images with scale change and rotation. It also has a strong adaptation to image deformation and illumination. Moreover, SIFT has good localizing accuracy and computing speed.
- In my project I did some modifications to these images. I pre-computed the key features for each image. Therefore I replaced the image files by keypoint files. Then I reduced the number of keypoints in each file to optimal number which retain the important features.”
 
###Implementation Questions:
- How do you determine where the sign is via edge detection?
- How can we change the input pictures so the algorithm works better?
- What are key features of a particular sign that distinguishes a sign? How do we create that in code.
- How do we test the effectiveness of our changes?
 
#3) Plumes
*“Modelling transport of air pollutants using the Gaussian plume” -Masingita Errol Manganyi*
- Problem: Accurately describe transport of air pollutants under various circumstances.
 
###Questions you should ask:
- What data is available to us? How do we incorporate error?
- Are there models for this problem or a related problem available?
- What are the different factors that contribute?  Are there instances when modeling is particularly difficult?
- What physics are important for us to understand?
 
###Answer: 
- “In this essay, three methods were applied to solve the two dimensional diffusion equation. Its solution, called Gaussian plume model, was derived using Laplace transform, Green’s function and Lax Wendroff scheme methods. The concentration of the plume was calculated using Laplace transform and Lax-Wendroff scheme. In order to compare the analytical solution with the numerical solution, the same values were used in both methods. The results of two methods, Laplace transform and Lax-Wendroff scheme were then plotted.”
 
###Questions:
- What software/data structures are appropriate?
- How do we represent this diffusion pattern in our code?
- What instances to the above models behave poorly under?
- How do we compare analytic and numerical solutions?











##OLD:
- (Software) Engineering: Application of scientific principles toward practical ends. Trying to apply formal methods to all software projects is as bad an idea as trying to apply code-and-fix development to all projects.

- “Treating software as engineering makes clearer the idea that different development goals are appropriate for different projects. When a building is designed, the construction materials must suit the building’s purpose. I can build a large equipment shed to store farming vehicles from thin, uninsulated sheet metal. I wouldn’t build a house the same way. But even though the house is sturdier and warmer, we wouldn’t refer to the shed as being inferior to the house in any way. The shed has been designed appropriately for its intended purpose. If it had been built the same way as a house, we might even criticize it for being “over-engineered”—a judgment that the designers wasted resources in building it and that it actually isn’t well engineered.”

######PRODUCT OBJECTIVES:
- Minimal defects
- Maximum user satisfaction
- Minimal response time
- Good maintainability
- Good extendibility
- High robustness
- High correctness
- How important is each objective for your project?

- “Some projects need to produce software with minimal defects and near-perfect correctness—software for medical equipment, avionics, anti-lock brakes, and so on. Most people would agree that these projects are an appropriate domain for full-blown software engineering. Other projects need to deliver their software with adequate reliability but with low costs and short schedules. Are these properly the domain of software engineering?”

######OTHER CONSIDERATIONS:
- Short schedule
- Predictable delivery date
- Low cost
- Small team size
- Flexibility to make mid-project feature-set changes

Frequent causes of software project failure have to do with requirements problems—requirements that define the wrong system, that are too ambiguous to support detailed implementation, or that change frequently and wreak havoc on the system design.[9] But requirements problems are not new. Back in 1969, Robert Frosch observed that a system could “satisfy the letter of the specification and still not be very satisfactory.”[10]

######More
*Ask good questions! Translate your researchers' questions into questions you can answer and they want answered.*
1.  Initially research questions do not have "obvious" solutions. Requirements in a scientific setting...
2.  SCOPE, REQUIRED INTERFACES: Also deal with questions of what scope to address -- namely, what parts does your
code do explicitly, what parts do you with system tools or libraries.
3.  What will the code be used for? Deal with addressing different parts of project with different tools (e.g.,
munging raw data w/ Python, doing simulation in C++, visualizing output with R).
Talk about thinking in terms of pipeline.
4.  Publication? "Publication" programming - having an approach that you can describe in a publication
that someone else can review / publish.

Paragraphs taken from:
(http://www.stevemcconnell.com/psd/04-senotcs.htm, http://www.stevemcconnell.com/psd/01-dinosaurs.htm)
