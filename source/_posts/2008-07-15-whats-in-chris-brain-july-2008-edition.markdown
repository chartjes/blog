--- 
layout: post
title: What's In Chris' Brain, July 2008 Edition
---
<p>The summer is always the worst for me in terms of blogging.  That's when I have to run my team in the <a href="http://www.ibl.org">IBL</a>, play slo-pitch (or softball for my American readers) at least once a week, do side-jobs to help pay the bills, and spend time with the family.  Phew.  So, that leaves little time for the types of activities that lead to good blogging.  But never fear, I will continue to dispense what wisdom I can from here.  So, here's some of the things I've been thinking about.
</p>
<h2>Closures and lambdas coming to PHP</h2>
<p>
Via twitter I found out that PHP 5.3 is going to have <a href="http://wiki.php.net/rfc/closures">lambdas and closures</a>.  I suggest you google around for a better explanation of what they are, but they are an incredibly powerful tool.  If you do any <a href="http://www.rubyonrails.org">Ruby on Rails</a> work, you end up using them.  If you use <a href="http://jquery.com">jQuery</a>, you end up using them.  I had a conversation in twitter with <a href="http://travisswicegood.com">Mr. Git Book</a> about this, where he accused me of being a "closure hater".  Believe me, I'm not a hater of that particular programming construct.  I simple expressed my feelings that given how horribly some PHP programmers abused OOP concepts, I imagine the same things happening with lambdas and closures.  Please prove me wrong.
</p>
<h2>Where The Hell Are The Easy Layout Editing Tools For Non-Designers?!?</h2>
<p>I have a side job where I am taking an existing app and converting if over to <a href="http://cakephp.org">CakePHP</a>, but preserving the look and feel.  What this poor designer-challenged programmer needs is a tool that will take that existing HTML and let me edit it in a fairly intuitive way so I can fix the so-many-damn-tables-I-want-to-bleach-my-eyes layout that exists.  Can nobody help me with this?  Sheesh.  I don't want to burn up my billable hours fucking around with layouts.</p>
<h2>The Framework Jihad</h2>
<p>I need a "Framework Jihad" t-shirt.  Size 2XLT, please.</p>
<p>Yes, the arguments about frameworks will just not go away.  Which one is best?!?  Why should you even use a framework?!?!  And the more it goes on, the more ambivalent I feel about it.  I cannot think of the last time I wrote a PHP script that was NOT part of a framework.  Hell, even my Python programming has been 75% Django and 25% straight Python, but that's only to do things like loading up databases with info from a CSV file.  But here's what I think:  the Framework Jihad is winning.</p>
<p>
If you substitute "modularized code with standardized API" for "framework", would that make people feel better?  I use frameworks because so much of the infrastructure code is stuff I DO NOT WANT TO WRITE ANY MORE.  After 10 years of doing this, it's time I stopped reinventing things.  My old motto of "just build it, damnit!" requires a structure around your application to let you quickly build something. To me, that means a framework that has taken care of database access and application flow and templating.
</p>
<p>The number one complaint about frameworks appears to be that they are slow and have all sorts of overhead.  Fair enough, but I tell you what:  I'll worry about scaling when I, you know, have something to worry about.  If I get to the point where I have to worry about scaling, then I have done very well indeed.  Despite our desires, not everyone can create a Flickr or Twitter.  They are the lucky ones.  The rest of us should shut up and just build something.</p>
<p>It's just too easy to dismiss the Framework Jihad as irrelevant.  Like many things in life, dismiss it at your own peril.</p>
