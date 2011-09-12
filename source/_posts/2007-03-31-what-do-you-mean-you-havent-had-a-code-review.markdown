--- 
layout: post
title: What Do You Mean You Haven't Had A Code Review?!?
---
<p>As I finish up week 3 at my new job, I have had more code reviews in 3 weeks than I have had in my last 5 years of work.  This is no lie.</p>
<p>
Right now, a code review consists of me either sitting right next to my boss looking at my code on a big monitor or talking via Skype while I am connected to a gotomeeting.com session he is hosting.  Either way, he is in the driver's seat and we go through my code, refactoring things and discussing the original goals of whatever it was I was supposed to be doing.  When we're done, he commits the changes back into our <a href="http://subversion.tigris.org">svn</a> repository, and I'm left to go back and test everything we've changed.
</p>
<p>
So far, to be honest, the reviews have been just fine.  What I'm lacking right now is elegance in the code.  My boss likes to joke about making metrosexual code, but what he's really after is code that is elegant, readable, and as simple as possible.  I find that while my code is getting the job done properly, it could be more elegant as I learn (and in some cases relearn) some of the finer points of design and move towards a more OOP-style of thinking instead of the mishmash of OOP and functional I seem to gravitate towards.
</p>
<p>
Things like returning objects (so that we can chain things as needed), and dumping nested ifs for the sake of readability.  Above all though, he's encouraging me to think about what I'm doing instead of just banging out the code.  Nobody I know gets paid per line of code, and my boss is not some dimwitted pointy-haired-boss who is impressed by the volume of my output as opposed to the quality of what I'm doing.  For the IPTV project I'm working on, the code HAS to be bulletproof and HAS to be able to run unattended as I won't be able to log into the server to hack things on the fly.  I've got a healthy enough level of self-esteem that I am able to take these code reviews not as criticism (which they are not, but would be if I was thin-skinned or had too much ego invested in my code) but as an invaluable opportunity to go back and fix assumptions, drill the manta of elegant code into my programmer's brain, and unlearn bad habits from years of essentially unsupervised programming.  Ouch, kind of hurts to read that now that I've typed it.  
</p>
<p>
Code reviews and unit testing are probably the two things developers try to avoid as much as they can.  Don't be scared of either one.  You will not believe how much you can benefit from a code review, xtreme programming-style, with a developer who knows what he's doing.
</p>
