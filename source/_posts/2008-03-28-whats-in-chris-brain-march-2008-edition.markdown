--- 
layout: post
title: "What's In Chris' Brain: March 2008 Edition"
---
<p>I've got a whole bunch of little things I want to talk about, as opposed to one big topic.  Here we go</p>
<p>
<ul>
<li>You'll see a badge on the right side of my blog announcing that I'm speaking at <a href="http://openwebvancouver.ca">Open Web Vancounver 2008</a>.  If you can make your way up to Vancouver on April 14th and April 15th, please come up and support this conference.</li>
<li>I got an email from someone on the CakePHP mailing list asking me about what sort of setup I have for running my apps.  I have a 256 MB slice <a href="http://www.slicehost.com">with slicehost</a>, and I have ZERO complaints about performance.  I'm running PHP 5.2.5 under fastcgi (I use nginx as my web server), with MySQL on there to power my blog.  In an earlier post I wrote how to create the rewrite rules for CakePHP to work with nginx, so search my archives for that.  I've got Python on there as well for my upcoming Django work, and soon Apache will be on there to act as my app server for Django.
</li>
<li>Wrote my first Python script for work:  it trolls through a bunch of gzipped XML documents, doing some search and replace.  75 lines of pure Python n00bness, built entirely with the help of "Dive Into Python" and google.  I'm sure it could be optimized by some more experienced Pythonistas, but it sure felt good to get the first one done and out of the way.</li>
<li>I've decided to start using <a href="http://twitter.com">twitter</a> again, see how long that lasts</li>
<li>The more I use it, the more powerful I realize jQuery is</li>
<li>Some ruthless refactoring has caused my Code Igniter code to be a bit more CakePHP-like, in that I'm moving stuff into models and out of the controller wherever it makes sense.  That's a good practice no matter what framework you use</li>
<li>As much info as there is out there for using Django (the Django project site, the Django book available online), it sure would be helpful to me to find some sort of Django guru who can help me out with some of the finer points of Django and Python itself.  I'm trying very hard to not write Python code like I was writing PHP, and I feel like some of the finer points are escaping me.</li>
<li>I'm working on moving some old CakePHP code I have that runs on PHP 4 over to PHP 5, and having PHP 4 *and* PHP 5 running on the same server.  Should be an interesting experience</li>
</ul></p>
