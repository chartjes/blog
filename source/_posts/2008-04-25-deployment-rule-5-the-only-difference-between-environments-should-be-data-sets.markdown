--- 
layout: post
title: "Deployment Rule #5: The only difference between environments should be data sets"
---
<p>One of the 6 "rules" I came up with for my talk on application deployment at <a href="http://www.openwebvancouver.ca">Open Web Vancouver</a> was that the only difference between your development environment and your production environment should be data sets.  My friend Juan, who works as the software architect at the adult dating site I used to work for, talked with me via IM about how that rule isn't always true.
</p>
<p>
A little background on this is necessary.  They are still using the same development setup today that was in place when I was there, in that they have given each developer a server that uses jails (this is a FreeBSD thing) to simulate having all the servers they would have in production.  A great solution, one that is still great today.  It made writing architecture-specific code (i.e. testing that an application server could talk to a queue processing server for a specific task) very simple.  So, in this case I believe that they had a development environment that matches production as closely as you can get.
</p>
<p>
But then Juan mentioned that they are using <a href="http://www.zend.com/en/products/platform/">Zend Platform</a> on their production servers, and it wasn't possible to give everyone a copy of Zend Platform on their development servers due to licensing.  While Zend Platform is a great product, well, you've just introduced an extra variable into your application development and deployment process.  Now, your development environment will never be the same as production and you are increasing the likelihood that you will encounter "production-only" bugs, which are the hardest to solve.
</p>
<p>I have great respect for Juan (he's near the top of my list of the smartest developers I've worked with), but rule #5 still the best one to follow.  While you gain from using something like Zend Platform in production because of all the extras you get, you end up with a development environment very far from what is using in production. Just make sure that you understand the implications of that decision.
</p>
<p>
Also, there is something else hidden inside rule #5.  If you have differences between environments, make sure you understand what those differences are and take steps to minimize their impact.  For example, I run Apache2 + PHP 5.2.5 compiled from source + Postgres 8.25 from a package for OS-X & MySQL 5.0.45  from a package for OS-X on my laptop, which is my main development environment.  On my VPS (which hosts this blog) I'm running Nginx + PHP 5.2.5 modified under Gentoo with USE flags + MySQL 5.0.54 under Gentoo.  So, that means I'm running mod_php on my dev, but using FastCGI on my "production".
</p>
<p>
Has this been a problem?  Nothing yet *but* if I ever got serious about running something other than my blog I would definitely consider configuring my VPS to use Apache 2 and PHP with the same configuration options as I have in dev, so that I have consistency in environments.  Django is recommending Apache + mod_python so I may be doing this sooner rather than later.
</p>
<p>
So, remember, the goal is to have your dev and production environments the same.  But if you can't have the same, you better be damn sure you understand what the differences are so you don't end up saying stuff like <a href="http://www.littlehart.net/workz-for-me-u-must-b-dum.jpg">this</a>.
</p>
