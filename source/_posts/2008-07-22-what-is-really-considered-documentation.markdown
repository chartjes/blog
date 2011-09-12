--- 
layout: post
title: What Is Really Considered Documentation?
---
<p>
I struggled to come up with a good name for this blog post, and have totally failed, but give this article a chance.  Or maybe you're here by accident thanks to a weird google search.  
</p>
<p>As a committed user of open source technologies, the difference between me using something and not using something is the documentation.  Is there documentation for it?  Is it easy to find?  Does it answer my questions?  Is there someone I can call an idiot if I disagree with the level of documentation?  These are all very important questions.
</p>
<p>My involvement with <a href="http://cakephp.org">CakePHP</a> has opened my eyes in terms of what people consider documentation.  Me, I'm the type who learns from examples that come with explanations.  While API documentation is great, it only becomes useful to me once *I* can figure out how to do something useful with this new technology.  I see people on the mailing list for Cake asking for the source code to a sample application, which I immediately file away in my head as "looking for answer to their homework", and move on.  Maybe that's unfair, but it's more a reflection of the fact that I tend not to learn anything from having the source code for an application.  I learn by getting in there and DOING SOMETHING and figuring out why this goddamn thing is not behaving properly and who do I know who can help me with this problem etc.  Learning by mooching, I call it.
</p>
<p>
So, back to CakePHP.  CakePHP had acquired the reputation that the documentation for it sucked.  While I did not share that opinion, I can see why people say that.  Because most coders are lazy.  Seriously.  They want solutions handed to them in a form that they can just drop into their application and then get onto the next problem.  There are definitely times when I wish someone else could just write this goddamn "alter the football game stats form dynamically via Ajax and send the results to the XML database" code for me.  Inevitably, I build the code up from an example stolen via Google into something that both works and that I understand fully.  However, most of the time I am content to figure stuff out on my own and ask for help only when stuck.  I'm not lazy, but maybe I'm suffering from a bit of the <a href="http://en.wikipedia.org/wiki/Lake_Wobegon_effect">Lake Woebegon effect</a>.
</p>
<p>So, things are much better in terms of documentation for CakePHP.  Whereas we used to have a manual that only covered 1.1, we now have the amazing <a href="http://book.cakephp.org">CakePHP cookbook</a> that covers both 1.1 and 1.2.  If that's not enough, well, you might actually have to do a little thing I like to call "research".  This gets us to the point of this blog posting.  Sometimes you have to stop being lazy and actually think about where you could find an answer.
</p>
<p>
There are no shortage of blogs that talk about CakePHP.  Some of them are even good.  Maybe you like the code examples I put up here.  People seem to like them enough to comment, so maybe I'm doing something right.  Google is your friend to track down blogs that have exactly the type of information that you need:  small examples with explanations about how they work.
</p>
<p>
The CakePHP mailing list is done via Google Groups, so all those posts where I make fun of people for no reason other than my poor self-esteem can be found with a few keywords.  But there are a lot of great tips on how to accomplish things using Cake, so a search of the google group will find lots of good information.
</p>
<p>
The <a href="http://bakery.cakephp.org">Bakery</a> is another good source of CakePHP info, consisting of all sorts of small articles along with comments.  It has a search function as well, but could easily be considered YACB (Yet Another Cake Blog).  Again, perfect for people with the same learning style as me:  short examples with explanations of how it was done.
</p>
<p>
Finally, we come to one of the more unorthodox documentation sources:  the unit tests for CakePHP.  CakePHP has some really good unit test coverage, although I sometimes wonder if you can really say that a piece of code works properly if it passes all the unit tests associated with it.  This is by no means a phenomenon limited to CakePHP, it happens everywhere there are unit tests.  Sometimes you can't figure out a test that makes something break.  It happens, so please do not misinterpret my thoughts on this.  Unit tests are good, and the amount of tests that CakePHP has in place is awesome and perfect example of a cohesive development team.  Automated testing is a goal worth striving for, don't let anyone else tell you otherwise.  I'm in the early phases of automated testing for a work project on the integration side of things because I'm tired of always running through the same damn tests by hand all the time to make sure something that I wrote didn't break things.  Tips on what good browser-based solutions are out there would be appreciated.  Other than telling me to use Selenium.  A solution that is tailored to the <a href="http://codeigniter.com">framework I have been forced to use</a> would be even better.
</p>
<p>
Okay, back on topic.  Since the unit tests cover so much of what CakePHP can do, what better way to see examples of how to actual do things?  My work on fiddling around with new console functionality showed me that I had no idea of how to create unit tests for my console work.  That led to discussions with people on the best way to do testing of console functionality.  Which leads to changes in the console code itself to make it easier to test certain things.  But at least when I'm ready to get back to doing that console work I can see if doing testing for it has become easier.
</p>
<p>
So, having been told all the stuff above, how can anyone who is not simply lazy say that the documentation for CakePHP sucks?!?
</p> 
