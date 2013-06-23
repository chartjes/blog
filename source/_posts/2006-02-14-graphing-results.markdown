--- 
date: 2006-02-24
author: Chris Hartjes
layout: post
title: Graphing Results
---
As I've been pecking away at my article for php|architect (up to 1700 words now) I realized I need to add a section about user tracking for your application.  Here at work I've been introduced to a powerfull tool called <a href="http://www.cacti.net">Cacti</a>, which uses something called <a href="http://people.ee.ethz.ch/~oetiker/webtools/rrdtool/">RRDTool</a> in order to generate nice graphs of, well, just about anything.

In my case I've been learning how to use it in order to do some user tracking not only for our <a href="http://www.tunerfriends.com">TunerFriends</a> site, but for a <a href="http://www.autoforums.com">new site that is launching tomorrow</a>.

If there is one complaint I have of Cacti is that, well, the user-supplied documentation sucks.  For real answers you have to go to their forums.  I got a lot of help, more than you would think a n00b would get from  your typical open source crowd.  It's pretty good though...lets us graph all sorts of things.  Basically, I can write PHP scripts that hit our databases, grabbing a bunch of numbers and then tell Cacti to create graphs based on that output.  Pretty simple stuff and it saves me the toruble of writing my own (which I despise, having done it many times).
