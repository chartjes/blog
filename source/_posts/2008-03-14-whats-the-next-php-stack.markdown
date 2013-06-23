--- 
layout: post
title: What's The Next PHP Stack?
---
<p>Most developers who have worked with PHP for any significant period of time have heard of the LAMP application stack.  <b>L</b>inux, <b>A</b>pache, <b>M</b>ySQL and <b>P</b>HP.  This is probably the most common PHP application configuration out there, and I've been giving application stacks a lot of thought these days for a variety of reasons.  First of all, I'm giving a talk on application deployment at <a href="http://www.openwebvancouver.ca">Open Web Vancouver</a>, and the stack plays a big role in that.  Secondly, I'm always looking at new technologies and trying to figure out where they might fit in.</p>
<p>
Thirdly, there seems to be a trend towards providing "drop-in-place" PHP stacks for developers trying to figure out things locally.  I'm talking about things like <a href="http://www.mamp.info/">MAMP</a> and <a href="http://www.wampserver.com/en/">Wampserver</a>.</p>
<p>
So the next thing I've been wondering about is about what future PHP stacks will look like, at least on the open source side of things.  Have we gotten to the point where this is as good as it gets?  I know for my own personal stuff, I've started moving away from the AMP part of LAMP, instead using Postgres for database stuff and nginx as my webserver.  So, what is that now?  LNPP?  That doesn't roll off the tongue as nicely as LAMP.
</p>
<p>
Also, are we limiting ourselves in the description of a stack by just going with PHP as part of LAMP?  With the rise of Javascript on the client-side and the increasing use of frameworks by developers (I'm *not* getting into that MVC argument again) do they need to be considered as part of the stack now?
</p>
<p>
So, my question to my readers is this:  what do you see as the future stack for PHP?  Is LAMP the combination likely to continue to see the most usage?  To spark things off, here are some of the PHP stacks I've been working with lately:
<ul>
<li>CakePHP + PHP + Apache2 + Postgres + Gentoo Linux</li>
<li>jQuery + Code Igniter + PHP + Apache2 + (<a href="http://exist.sourceforge.net/">eXist</a> + Postgres) + Debian Linux</li>
<li>jQuery + CakePHP + PHP + MySQL + nginx + Gentoo Linux</li>
</ul>
</p>
<p>
Let me know your thoughts about the PHP application stack in the comments.  I mean, are we going to see something like an application server for PHP (like Mongrel for Ruby folks) or is mod_php or FastCGI (for the nginx + lighttpd folks) as good as it's gonna get?
</p>
