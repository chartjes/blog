--- 
layout: post
title: Cake and AJAX
---
Success!  I did manage to get the sortable grid working for the stats reporting system.  It was my first real example of creating an AJAX component for a work project.  It took me quite a while to figure some of the trickier things out.  I did use <a href=http://www.crackajax.net/grid.php>this excellent tutorial</a> to show me a basic example of implementing a sortable grid backed by data pulled from a SQL database.  After that, I found Graham Bird's excellent tutorial on <a href=http://grahambird.co.uk/cake/tutorials/ajax.php>creating an AJAX sortable task list with Cake</a>

Now, what I did was a little more complicated because not only did I have to sort by the header columns in the table, I also had date ranges selected via a form *and* categories selectable via a form to take into consideration.

I can say this:  the AJAX helper functions for CakePHP are just fantastic and spared me from having to figure out all this stuff on my own.  I did have to create some stuff by hand in order to build the following little snipper:

body onLoad = "new Ajax.Updater('hiddenDIV','/verticalscope_stats/reports/getusers/site_name/99', {asynchronous:true, evalScripts:true, requestHeaders:['X-Update', 'hiddenDIV']}) }, false);"


Yikes.  Not the kind of stuff I want to be building by hand if I can avoid it.  Now, the Cake AJAX helpers use scriptaculous and prototype as the base for their actions.  I found a post in the wiki for Cake complaining about the large size of those two helper libraries, and they do have a point.

The post also turned me on to <a href="http://jquery.com">jQuery</a> , which describes itself as "... a Javascript library that takes this motto to heart: Writing Javascript code should be fun. jQuery acheives this goal by taking common, repetitive, tasks, stripping out all the unnecessary markup, and leaving them short, smart and understandable."

I have an idea to try and see if I can take a stab at creating my own Cake helper that uses jQuery instead of the awesome-but-quite-large scriptaculous+prototype combo for the AJAX stuff.

I plan on creating a tutorial on the stuff I did (specifically for implementing a sortable grid in CakePHP) in the next week or so.  It would be nice to share all the stuff I did. :)
