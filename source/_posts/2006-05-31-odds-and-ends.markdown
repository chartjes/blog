--- 
layout: post
title: Odds and Ends
---
The past few days I've been working on a couple of different things.

1) working on adding in support for Subversion to <a href="http://rephlux.sourceforge.net">Rephlux</a>
2) added in some new stat reports (all in Ruby too) for the <a href="http://www.ibl.org">IBL website</a>
3) ran through the tutorial for the <a href="http://framework.zend.com">Zend Framework</a> and have started making plans for a website using the framework (more details later).

The Rephlux stuff is going slow because, well, the CVS stuff is really tangled up and is in the process of being cleaned by the other developer on the project.  He's going to send me some specs on how it's supposed to work and I'll model my patches for Subversion support on that.

The new stats are making lots of people happy, which is good.  The site runs pretty snappy considering how much work the database is doing to generate those reports.

The Zend Framework looks really good so far, and I shouldn't have any problems using it.  Some stuff is missing but I can build my own for now and replace it as the framework matures.  I'm also going to hold strict to my unit testing practices and create tests for all the models I create.  Gotta eat your own dogfood if you're going to talk about testing.
