--- 
layout: post
title: What's In Chris' Brain -- January 2007 Edition
---
<p>My work week has been spent rebuilding stats that were supposed to be collected by my reporting application.  I was missing a month's worth of data.  Why?  Turns out that a bug fix I made actually introduced a new bug, and was causing silent failures.  Something about me not setting the proper PDO attribute to buffer queries.  My testing didn't reveal the bug, so the first thing I did was change the tests and bingo! it revealed the bug. Silly Chris.  Luckily, I had created a tool a while back to allow me to fix the stats for a specific day, so with a list of dates for which data was missing I set about collecting the data.  Unfortunately, it takes between 5 and 10 minutes per day to hit our 30+ sites that we are collecting data from (probably due to huge record sets and improper indexes) so that meant a minimum of 150 minutes of continuous data grabbing.  Of course, it took longer because I kept testing things, and was tweaking the stats reporting software code (I found out about the magical BETWEEN function in MySQL to use when looking for records in a date range) so it basically took me all week to retrieve the data, make changes to the reporting application and test everything.  Phew.</p>
<p>Now, back to what is in Chris' Brain for January 2007
<ul>
<li>I'm working on the article for <a href=http://hades.phparch.com/artemis/main/>A/R/T, which is <a href="http://phparch.com">php|architect's</a> online article repository.  First draft is done, just waiting to find out from Marco who to send it to and if they like it.</li>
<li>Finished phase one of my work on Mustique Island, a side project I had been doing some PHP work on.  The work isn't online yet but it was interesting to do:  search engine for villas-for-rent on a private island in the Caribbean.  I got to flex my Ajax skills a little with some forms that refreshed without refreshing the page, etc.  Good practice for rallyhat</li>
<li>Thinking about how to modify my presentation for my talk in February.  Have to mix it up a bit, make sure what's in there is still relevant.  Things do change fast, and my work with <a href="http://www.cakephp.org">CakePHP</a> should probably be worked into the presentation as well.</li>
<li>Continue pestering <a href="http://derekmartin.ca">Derek</a> to do his fair share of the work on Zend_Service_Audioscrobbler and write the documentation that we are missing.</li>
<li>Start working on the outline for that Ruby training course (I hope I haven't gotten in over my head)</li>
<li>See if I can't have a working beta of <a href="rallyhat.com">Rallyhat</a> to show people by the end of the month</li>
</ul>
</p>
