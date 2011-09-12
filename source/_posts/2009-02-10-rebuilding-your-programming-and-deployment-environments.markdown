--- 
layout: post
title: Rebuilding Your Programming And Deployment Environments
---
<p>As I get closer to giving my deployment talk at the <a href="http://conf.phpquebec.com/en/">2009 PHP Quebec Conference</a> (you're going, right?) I've been paying close attention to what sort of things people have been doing in terms of best practices and actual application deployment.  Looking at some of these things, I realize how lax I've gotten lately.  Is it the crushing ennui of ongoing, incremental programming by a lone developer for his employer?  I'm being sarcastic (obviously) but the more I think about HOW I've been doing the development work the more I realize that I need to refocus.  
</p>
<p>
So, my programming environment appears somewhat sane to me.  I write my code using <a href="http://www.vim.org">the One True Editor(tm)</a> on my laptop, where I've installed PHP, Python and Perl.  Since I work with both MySQL and Postgres, they are both on my laptop as well.  Is it any wonder I've crammed my MacBook with 4 GB of RAM?  I typically have a few Terminal.app instances running and a couple of <a href="http://code.google.com/p/mavcim">MacVim</a> instances.  I find that I use <a href="http://www.sequelpro.com/">Sequel Pro</a> and <a href="http://www.pgadmin.org/">pgAdmin III</a> a lot, as all that work with sports data requires large queries that I have to tweak little by little.
</p>
<p>
I also have found a powerful tool that I always ignored, but has been a godsend for development work.  What do you do when you have a large data set that your application needs to work against and it is totally impractical to copy it locally?  SSH tunneling to the rescue! 
<pre>
ssh -fNg -L3308:localhost:3306 notchris@rangers.xmlteam.com
</pre>
That creates a tunnel to the MySQL server on one of our production machines (we name them after NHL teams), which I then can access by making a MySQL connection on port 3308.   Very simple and VERY effective.  I can't believe I had forgotten about this.  This technique works well when using something like Sequel Pro, and we had an SQL consultant in who connected the same way.
</p>
<p>
But now we're onto the toughest part of tearing down and rebuilding.  As our products (both the web ones and our main project, a Perl-based data-fetching-and-parse-into-a-db application) get more complicated it becomes obvious to me that my suspicions about there not being enough testing in place are unfortunately coming true.  So now is the time where this lone developer has to start thinking like he is part of a team and push forward with a new strategy, <a href="http://en.wikipedia.org/wiki/Test_driven_development">TDD</a>.
</p>
<p>
I'm positive I've talked about this before on this very blog.  Code Igniter's testing absolutely sucks out of the box.  Luckily I have my CI-to-<a href="http://www.phpunit.de/">PHPUnit</a> bridge.  <a href="http://sebastian-bergmann.de/">Sebastian</a>, I owe you a bunch of alcoholic-beverages-of-your-choice when I run into you in Montreal in March for all you've done with PHPUnit.  So now I begin the incredibly daunting task of shoehorning in tests for an application that doesn't have any.  But that's not where the problem starts.
</p>
<p>
See, I'm having problems deciding WHAT to test.  Let's take a look at one project for example.  We have <a href="http://www.sportsdb.org/sd/sportscaster">self-hosted web service</a> that we released under the  GPL that we not only use ourselves for some clients but also use it to troubleshoot things as well.  In terms of writing tests, I believe the best way to approach this is to write tests that speak directly to the Sportscaster "engine" using a known set of parameters and ensure that the output we get back matches what we expect.  Is unit testing overkill for this?  Very hard to say because we have an HTML front end that talks to a "gateway" that talks to an "engine".  I'm not the one who architected this, but I do have to make sure that it works properly.  In this case I believe that  "your tests should verify your application is outputting what you expect it to" is the best approach.  Comments about this are totally welcome.
</p>
<p>
For another project, I tried something that <a href="http://sebastian-bergmann.de/archives/631-Integrating-PHPUnit-with-Selenium.html">integrated Selenium with PHPUnit</a>, but it was so slow as to be totally useless.  <a href="http://www.sportso.com">Sportso</a> is a very visual application, one that is written in PHP an talks to an <a href="http://exist.sourceforge.net">XML database</a>, but presentation is really the key here.  Sure, we need to make sure that we're placing the right data into our XML documents but that part of the application is solid.  In this case, I wish to have tests that simulate a user clicking around the application and using it.  Then I can compare output again and make sure that things are showing up when and where I expect them to.  I'm thinking the PHPUnit-Selenium bridge is a bad idea, and that I should instead just focus on Selenium.  Again, comments on how to best approach this are also welcome.  I cannot believe that Selenium is really this slow, so there must be something I am doing wrong.
</p>
<p>
Also, I've thought about continuous integration.  This <a href="http://timothyfitz.wordpress.com/2009/02/10/continuous-deployment-at-imvu-doing-the-impossible-fifty-times-a-day/">incredibly inspiring post about continuous deployment</a> has me really thinking hard about how my changes actually get pushed up out of dev to production.  We don't have the resources to use a cluster of machines that IMVU appears to have, but when you think of the infrastructure and (more importantly) the practices in place, you just have to be in awe of it all.  Just the *scale* of it is inspiring.  If they can do this, I can certainly implement a very effective subset of this.  There is really no reason other than laziness on my part to not do it.  Harsh reality, to be sure.
</p>
<p>
But the real problem is the political game that you inevitably end up fighting over bring in what is usually a very radical concept:  a commitment to testing as part of the development process.  Especially when the developers are severely outnumbered.  A lot of people seem to have a pathological fear of automated testing, saying things like "we can just quickly test it by hand".  Then when you see the errors being reported by users of your products, you can't help but wonder "could we have caught this earlier?"  Unless it's a very obscure error involving a race condition or something, of course the answer is YES.
</p>
<p>
I read a post from one of the main developers at justin.tv talking about why he felt <a href="http://abstractstuff.livejournal.com/60388.html">unit testing is useless</a>.  While he is entitled to his opinion  I can't help but think that he really is doing TDD, but he just refuses to acknowledge it.  Yes, ultimately, your users are the only ones who can tell you if your application is spitting out errors.  But if you aren't doing any rigourous testing of stuff BEFORE your users see it, I think you are taking chances with your business.  My company is small (just 7 of us) so I'm so close to most aspects of the business I can really see the impact of certain decisions on the bottom line of the company.  It's not about finding bugs, which is what is being claimed by the justin.tv folks never happens with unit testing.  It's about making sure those bugs never happen in the first place.
</p>
<p>
I have to say that I've never really delved into the world of post-deployment monitoring, so maybe I should start asking a few more questions of people who deal with that sort of thing.  Again, the key is to make it automated and have it report when it finds things that are wrong.  We have a very good nagios infrastructure at work that alerts us to problems with not only servers being down, but stale and/or missing data for our customers.  I guess the next logical step is figuring out ways to look at those mountain of server logs and making sense of the errors?  Definitely something to think about the next time I get stuck on some programming problem at work and need a change of pace.
</p><p>
I know I've been rambling a bit here, so let me pull some of this stuff back together to make it more cohesive:
<ul>
<li>SSH tunneling to access resources that you cannot easily put a snapshot of into your work environment.  I recommend read-only access if you can do it, because if you need to do updates or deletes you should always work off a local copy</li>
<li>TDD is a powerful yet still controversial tool that too many developers are still ignoring (including me, but it's not too late to save myself!)</li>
<li>Automation is the key to really taking advantage of what you gain by going with TDD</li>
<li>You need tools in place after deployment to see if your changes have had the desired effect</li>
</ul>
</p>
<p>
As always, bombard me in the comments with your thoughts and experiences with these types of scenarios.  I hope I don't get too many <a href="http://www.urbandictionary.com/define.php?term=tl%3Bdr">tl;dr</a> responses.
</p>
