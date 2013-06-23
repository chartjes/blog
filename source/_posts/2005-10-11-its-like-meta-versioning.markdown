--- 
layout: post
title: It's like meta-versioning
date: 2005-10-05
author: Chris Hartjes
---
<a href="http://slash7.com">Amy Hoy</a> has a posting up at her blog about her efforts in <a href="http://www.slash7.com/articles/2005/10/09/super-customizing-typo-svk-more">hax0ring at Typo so her blog can be all pretty-like</a>.  In it she mentions using something called <a href="http://svk.elixus.org">SVK</a>, which is "decentralized version controls system" that uses some elements of <a href="http://subversion.tigris.org">Subversion</a>.

Now, I messaged Amy when I got into work and asked her what the big deal was, because I took a look at it last night and couldn't see what the advantage was.  Of course, I was sleep deprived from three days of the baby waking up 3 times a night.  Amy explained it to me thusly:

1) you check out the code you wish to hack using SVK
2) any changes you make to it, when committed, remain only in <strong>your</strong> copy of the repository
3) when you do an update of your repository, any changes made upstream appear in <strong>your</strong> copy of the repository

As soon as she explained it, the light bulb went on.  I <strong>immediately</strong> understood why that was a good thing.  To take it even further, this technique could be used at work when the time came for us to reboot the templating of the site effort.  The templaters could work on their own stuff, committing their changes locally and then pulilng down updates the maintenance team was doing.

I've installed SVK on my iBook and going to fool around with it for a while to see if I can work with it.
