--- 
layout: post
title: Is There A More Practical Approach To TDD?
---
<p>One of the things I (foolishly perhaps) promised myself when I started up a new project at work was that I was going to use Test Driven Development (or TDD for short).  I advocated using a <a href="http://framework.zend.com">web application framework that supports good testing practices</a> and discussed how it would be beneficial when trying to track down and solve bugs to have a set of tests.  I ran through the impact of my horrible decision to use a framework without a good culture of testing in a previous project:  fixing things became tedious as I could not run automated tests to verify that things were working properly.
</p>
<p>But a funny thing has happened while building the new application.  Sadly, there are no automated tests, and the question I've been asking myself is "other than being lazy as hell, why did you not write tests?".  The answer I seem to have come up with (or justified is probably the better word) is "I don't see anything complicated in what I'm doing that I need to write a test for."  Before you dismiss my thoughts on this, consider the architecture of what I've built:
</p><p>
We have a backend consisting of MySQL with two distinct databases on it:  one containing raw stats for sporting events, the other summarized records about fantasy points accumulated by players.  My thought was to make the database do all the work of crunching the numbers for me as a daily cron job and then the web front end only needs to do reads.  With proper indexing of the tables, performance is at an acceptable level with a full season's set of test data.  Sounds like a pretty decent strategy to me.
</p>
<p>
The scripts that collect the raw data and pre-calculate fantasy point totals are written in Python.  The web site that displays the fantasy points info was done with Zend Framework.  So what sort of tests should I have written for this.  I've come around to the idea that you should write tests for things that are non-trivial.  Then you get into the problem of deciding what is non-trivial:
<ul>
<li>Verify that point totals are being calculated correctly</li>
<li>Verify that when players are assigned to teams in our admin panel they actually end up, you know, being on the proper team</li>
</ul>
Every else seems to me to be, well, not worth testing.  Make sure teams are sorted in order of total fantasy points?  Database does that for me.  Make sure list of players for a specific team contain expected players for a team?  Um, database does that for me(?).  I can verify that players are properly changing teams in the admin panel by hand.  Of course, I shouldn't be testing things by hand, but I'm wondering if I'm either missing the point or have stumbled upon something here.
</p>
<p>
<b>Am</b> I missing something here?  Am I doing it wrong? I do believe I need some tests, but only for the things that are not super-obvious.  I'd appreciate people's thoughts on this.  Maybe I just need someone else to look at it the app as a whole and say "we should be testing for the following things".  The curse of the lone programmer maybe?
</p>
