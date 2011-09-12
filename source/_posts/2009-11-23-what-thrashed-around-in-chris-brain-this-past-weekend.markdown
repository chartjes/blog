--- 
layout: post
title: What Thrashed Around In Chris' Brain This Past Weekend
---
<p>(The blog experiment continues: 1 post every weekday in November and I think I only skipped one, but made up for it with a Saturday post)</p>
<p>
<i>Node.js is something I want to use, but I do not know what for</i><br />
For those who don't know, <a href="http://nodejs.org/">Node</a> is a "toolkit for writing extremely high performance non-blocking event driven network servers in JavaScript".  In other words, it's for writing server-side Javascript with an emphasis on providing concurrency.  Damn you Tim Bray, I cannot avoid seeing concurrency everywhere since you started your <a href="http://www.tbray.org/ongoing/When/200x/2009/09/27/Concur-dot-next">Concur.next</a> series on your blog.  It fascinates me, and I don't even do any kind of work where I need to worry about concurrency.  Not yet anyway.
</p>
<p>
Simon Wilson (someone I follow from the Django community) has a great article explaining why <a href="http://simonwillison.net/2009/Nov/23/node/">Node.js is genuinely exciting</a> to him, and my old CakePHP landsmann Felix shows <a href="http://debuggable.com/posts/streaming-file-uploads-with-node-js:4ac094b2-b6c8-4a7f-bd07-28accbdd56cb">how to handling streaming file uploads in node.js</a>.  Like so many new technologies, Node.js starts out as a solution looking for a problem but as I become more familiar with concurrency it all becomes a little clearer.
</p>
<p>
<i>While <a href='http://www.vim/org">Vim</a> is awesome, don't put up with any crap from it</i><br />
I had been experiencing a problem with Vim.  Well, two problems.  The first big one was weird behaviour involving the <a href="http://www.vim.org/scripts/script.php?script_id=1849">AutoClose</a> plugin.  It would spit out brackets and quotes at the weirdest time, and I found myself doing a lot of unnecessary keystrokes (and toggling in and out of insert mode) to get things done.  So I deleted it.  Enough of that crap.  Same goes with my attempts to use the <a href="http://www.vim.org/scripts/script.php?script_id=69">Project plugin</a>.  I just could not get it to work properly.  DELETED.
</p>
<p>
Vim's ability to be ultracustomizable ALSO makes it easy to dump stuff when you no longer what to use it.  Heck, I even see some stuff in my .vimrc that I am not using any more.  Mappings I did to accomplish some specific tasks.  Those were deleted too.
</p>
<p>
<i>Understanding the concept of callbacks opens your mind to all sorts of possibilities</i><br />
While callbacks are related to my use of Javascript (jQuery uses them to great success) I also find myself digging into the <a href="http://docs.djangoproject.com/en/dev/topics/signals/">documentation in Django on signals</a>, which are callbacks by another name:  functionality that is executed when certain events happen.</p>
<p>Django uses them all over the place, and CakePHP uses them as well.  When I look at the CodeIgniter code that powers <a href="http://www.sportso.com">Sportso</a>, I often ruminate about what programming techniques or design patterns could help me reduce the amount of code that has actually been written.  CodeIgniter doesn't really support callbacks except in the form of allowing you to define custom functions for validation purposes.  It's a start I get.  I wonder what the code would look like if I could define more code that is triggered when specific events happen?  Any time I find myself typing the same block of code over and over again, it is only natural that I seek to reduce how often I need to do it.  
</p>
