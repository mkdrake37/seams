HOWTO CAMS
==========

## Recipe for editing only online

 1. have github account
 2. go to github.com/aims-ghana/seams
 3. use the "fork" button (top right-ish)
 4. ...wait til done
 5. looking at fork, switch to gh-pages branch if not already there (selector box for branch)
 6. navigate through files to target (e.g., README.md in this case)
 7. when viewing target, click edit button (pencil, top left of view panel)
 8. ...make edits
 9. scroll down to bottom of screen
 10. enter useful headline for edits
 11. if more details useful, enter them as well in big text box
 12. commit (directly to gh-pages branch)
 13. click pull request (button to the side of resulting view below button for code (looks like "<>"))
 14. select gh-pages branch in aims-ghana and your repositories, then click buttons to proceed (there are a few, with different names, but all green)
 15. can continue to make updates while waiting for pull to be accepted, and all will be included
 16. once pull accepted, trash fork
 17. repeat as necessary

## More General Developing material

 1. learn [git](http://git-scm.com/documentation "git docs"), [github](https://help.github.com/),
 [github pages](https://help.github.com/categories/github-pages-basics/) (though [start here for from-scratch-diy](https://pages.github.com/)), [jekyll](http://jekyllrb.com/)
 2. CAMS material is organized into sections, with material for each day/session combo.  A workshop
 day generally entails warmup -> topic discussion / small exercises -> in-depth exercise -> individual
 project workshopping from the perspective of that topic.  The folders for the material are
 as follows:
  - `_warmups`: both in-class and background material for daily warmup exercises.  should specify any directions,
  link to any material to download, what people will be expected to "turn in"
  - `_sessions`: both in-class material for the in class discussion of a topic.  should contain / link to any presentation material, exercise downloads, exercise instructions, etc.  presentation notes should go here as well.
  - `_topics`: "textbook" material for each session.  should go beyond in class discussion, and serve as reference material.  some duplication of `_sessions` material may be warranted, but probably not very much
  - `_practice`: detailed guidance for each stage of the long form exercise + discussion of how it relates to
  in-class + reading material
  - `_project`: detailed discussion of particular project milestones + guidance for what students need to
  present at the end of the self-directed work period.

 3. for each of our responsible areas, we need to assemble the above in a fork, then issue a pull request to integrate it into the main repository.  Recommend that we do that in small bites.  We'll develop the material
 in stages, with outlines that get revised / filled in with increasing levels of detail
