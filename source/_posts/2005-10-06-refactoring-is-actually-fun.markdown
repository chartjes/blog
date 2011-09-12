--- 
layout: post
title: Refactoring is actually fun
author: Chris Hartjes
date: 2005-10-06
---
No, really.

If you look at my <a href="http://www.littlehart.net/attheballpark">other blog</a>, you will notice that I'm the commissioner of the league.  There's a weekly newsletter that goes out to the league, with results and other info of interest to the league.

I've been Commish since the middle of the 2000 season and I was stunned to see that the newsletter was being compiled by hand (shudder), and that was the most difficult part of the job.  So, I quickly wrote a bunch of PHP scripts to collect the raw info needed to do the newsletter and then munge it all into the format it needs.  I'd show you guys the app, but it's password protected and the security is pretty much non-existent.

Which brings me back to the topic at hand.  We're going to be redesigning the <a href="http://www.ibl.org">Internet Baseball League's website</a> to make it more CMS-like and have our webguru stop putting things in by hand.  Part of the work is moving my code from where it lives right now (under my own littlehart.net domain) to be part of the new site.

Right now I'm using my own DB abtraction layer, but since I'm going to be using PEAR::DB for the new site I might as well go back into my existing code and refactor it to use that code.  Plus fix the ugly-looking interface.  

I'm probably the only person out there who enjoys going back and fixing his old programming mistakes...
