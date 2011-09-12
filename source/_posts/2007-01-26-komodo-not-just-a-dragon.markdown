--- 
layout: post
title: Komodo - not just a dragon
---
<p>
I've tried all sorts of editors in my time:  emacs, vim, Eclipse, Zend Studio.  After I got into Ruby on Rails, I bought a copy of TextMate to be my main editor.  But that's all it is, an editor.   In the Rails world, lightweight tools are preferred.  I'm a big believer in lightweight tools, because I *hate* when my system gets lagged down because of the number of apps I'm running at once.  However, I've noticed that there really isn't much out there in the way of a full IDE for Rails, with debugging tools, etc.  I really like the TextMate + Cyberduck combo I've been using at work for my PHP work and using TextMate for all my Ruby work.  But I feel like a debugger is something that is missing.  Maybe that's in the works or exists already, I just haven't run into it.
</p>
<p>
For PHP I really liked Zend Studio, but it was pretty expensive for just one developer to buy...and my company seems reluctant to fork out the cash to buy me a copy.  The other PHP developer at work is old skool, using vim.  So, I'd been getting along just fine with TextMate...but was starting to feel the pinch of not having a debugger (and some integrated version control would be nice) for the PHP work.  A step-through debugger would've been a HUGE help as I was building out my Sportsticker feed parser.  I got so used to using var_dump and print statements at certain points to see what was going on, that I totally forgot about using debuggers and setting break points, and the joy that can come from putting your app through it's paces via a step-through debugger.  Work smarter Chris, not harder. :)
</p>
<p>
Now, one of the fine folks who is putting together the <a href="http://vancouver.php.net">Vancouver PHP Conference 2007</a> is Shane Caraveo, who is a lead developer for <a href="http://www.activestate.com">ActiveState</a>, the company that makes the Komodo IDE.  While exchanging some emails with him (thanking him for the reimbursement cheque for my flight to Vancouver amongst other things) I sort of jokingly mentioned that I thought it would be a nice perk for giving the talk at the conference if I could get a copy of Komodo from them, because I felt that I would have to buy a copy of it with my own money if I wanted a copy.  Next thing I new, I got an email from someone at ActiveState with a link to a downloadable copy of Komodo IDE 4.0 (the latest) and a license for it.  Awesome!
</p>
<p>
One of the blogs I read is <a href="http://www.litfuel.net/plush/">Jim Plush's</a> (I heard him on the sadly silent Pro-PHP podcast), and he was <a href="http://www.litfuel.net/plush/?postid=160">raving about Komodo</a> because, like me, he uses a MacBook and there is no Intel version of Zend Studio Server.  He even provided a nice link to someone else instructions on how to get the <a href="http://www.sysarchitects.com/node/22">PHP debugger up and running</a>.
</p>
<p>
Undaunted, I set things up and bingo!  It works like a charm.  Just as a test, I decided to try the step-through debugger on my reporting system I wrote in CakePHP and got a glimpse into the heart of CakePHP just to do a simple request.  On Monday I'm going to configure PHP on my development server at work to have support for <a href="http://www.xdebug.org">XDebug</a> built into it so I can use the step-through debugger there as well.  It will help me track down some stupid mistakes I made with the Sportsticker code that took me a long time to figure out.
</p>
<p>
Until you've used one of these debuggers for a while, you don't understand how powerful they really are.  Thanks again to Shane for hooking me up with a copy!  I owe you a beer or two while in Vancouver...
</p>
