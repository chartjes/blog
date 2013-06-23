--- 
layout: post
title: Got That Olde Thyme TDD Religion
---
<p>
This week has been kicking my ass in terms of work.  I've started a project at work which is a bit of a rush job (my boss forgot I was at PHP Quebec last week when taking into account the schedule) and I decided that there was no time like the present to start doing things right and start practicing Test Driven Development, or Behaviour Driven Development.
</p>
<p>
See, this is much harder to do if you inherit some legacy code.  Also, as I've discovered, Code Igniter is making it difficult to actually write some useful unit tests.  The built-in testing tools are terrible (this is not the first time nor the last time I've said this) so I am unsure how to approach this.  Let me know in the comments of tools you've used to help with this in the PHP world.
</p>
<p>
This new app I'm building using CakePHP, because (a) I'm more familiar with is given the time constraints for the project and (b) it allows me the granular caching that I want.  I did consider using Zend Framework for this but time was the enemy.  CakePHP is a project that has a culture of testing, and I've been using Cake's <a href="http://debuggable.com/posts/running-tests-from-the-commandline-in-cakephp:4821f908-da38-4987-909a-25c74834cda3">CLI test runner</a>.  Yes, I know that Zend Framework has the testing culture too, as I remember all the fun I had writing tests for Zend_Service_Audioscrobbler.  If you take one thing from this blog post, it's this:  DO NOT USE A FRAMEWORK WITHOUT A CULTURE OF TESTING.  You will regret it when you are spending tons of time fixing bugs you should've found through unit and functional testing.
</p><p>
In my first week of doing TDD I've noticed a subtle change.  I'm planning things more.  Deciding the output of functions before I actually write them.  I'm only creating the functionality I need instead of stubbing out all the functionality I think I'm going to need.  I'm looking for ways to run my tests from inside the One True Editor.  All of this must be good, right?
</p>
<p>
PHP does not have a culture of testing at it's core like Ruby and Python do.  I point you at <a href="http://gilesbowkett.blogspot.com/">Giles Bowkett</a> and some of the awesome blog posts he's done about TDD and Ruby.   Search that blog and READ THOSE POSTS.  You will not regret it.Python has the same culture of testing (<a href="http://docs.python.org/library/doctest.html">doctest</a> is one tool for that), and I don't know how PHP can get there.  Maybe it will never get there because I hazard a guess that most people who use PHP couldn't give two flying fucks about writing tests.  Until that changes (meaning all the cool kids of PHP start writing tests) then TDD will continue to simply result in blank stares in the PHP community.
</p>
<p>
So I think what TDD is really supposed to do is NOT find bugs.  Finding bugs is a side-effect of the process.  What it does (at least it did for me) is force you to build you code in such a way that it can be modular and testable.  I found myself adding in switches to put functionality into test mode, so that I could load test fixtures instead of hitting a webservice to get my data.  You tell me:  is that good or bad?
</p>
<p>
Now I know I haven't been doing TDD long enough to call myself an expert, but I feel I really need to give it the time and effort that it deserves.  This project is the perfect (pardon the pun) testing ground for putting some TDD principles into practice.</p>
