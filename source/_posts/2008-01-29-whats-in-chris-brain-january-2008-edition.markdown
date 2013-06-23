--- 
layout: post
title: "What's In Chris' Brain: January 2008 Edition"
---
<p>
Not a lot going on, it's time for a quick round-up post
<ul>
<li>I'm speaking at <a href='http://www.cakefest.org'>CakeFest</a>, so I'm working on my presentation.  Since I'm going to be a combination of slides and actual demonstrations of the Cake console, I'm going to be using <a href="http://meyerweb.com/eric/tools/s5/">S5</a> to run the slideshow, then switching to a terminal and my IDE to show people the results</li>
<li>I've run into a weird bug in working with Cake and Postgres, where the code works okay in PHP 5 + Postgres + OS-X, but erroring out in PHP 4 + Postgres + Linux.  If I could figure out a test to recreate the bug, that would be a good step forward.  In a nutshell, for some reason CakePHP is not determining the correct name of the sequence (it's what Postgres uses when determining auto-incremented ID's for a table) in the PHP 4 + Postgres + Linux environment.  It's very weird and I have no idea what might be happening here.  Given that I can't submit a ticket without a test proving the problem, and then figuring out what code to change, this could cause me some headaches.</li>
<li>I suck at writing screen scrapers, which is what I need to make one of my side projects work</li>
<li>Via the ever-increasingly-useful Miro, I have started watching a presentation on <a href="http://research.sun.com/projects/lively/">the Lively Kernel</a>.  For some more info about it,  check out this post about how <a href="http://bitworking.org/news/290/JavaScript-is-the-new-Smalltalk">Javascript is the new Smalltalk</a></li>
<li>I've been playing around with different themes for this blog, but nothing seems to work as well as my current setup.  Interesting...</li>
<li>I also experimented with adding some more advertising but that got me nothing in the way of revenue.  Maybe I didn't give it enough time or something. My current set of advertisers (thank you very much, guys and gals) make this blog pay for itself, so I consider that a major accomplishment.
</li>
</ul></p>
