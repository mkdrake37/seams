HOWTO CAMS
==========

## Developing material

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
