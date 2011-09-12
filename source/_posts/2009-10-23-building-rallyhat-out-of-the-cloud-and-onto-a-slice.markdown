--- 
layout: post
title: "Building Rallyhat: Out of the cloud and onto a slice"
---
<p>The fall and winter are really the time of year when I can sink my virtual teeth into side projects.  During the summer I'm too busy playing softball or games in my <a href="http://www.ibl.org">simulation baseball league</a>, so now that both seasons are done or winding down I can take a look at a side project that's been percolating in my brain for several years.  Late last night I pushed an extremely rough and not-completely-finished version of my application, which I call <a href="http://www.rallyhat.com">Rallyhat</a>.</p>
<p>
It's build using the latest official version of <a href="http://www.djangoproject.com">Django</a> (which is 1.1.1 as of this writing) and originally I thought of putting up on <a href="http://code.google.com/appengine/">Google App Engine</a> long-term.  I did, and it was a hacked-up version of the app without the proper registration links working.  When you add in that I was using a patched version of Django in order to just run on there, I decided it would be smarter if I used regular Django.  You know, learn how the damn thing actually works.  And run it on an environment close to what I would expect, which is Apache using mod_python.  I will probably tinker with it to get to work with <a href="http://code.google.com/p/modwsgi/">mod_wsgi</a> as a next step.
</p>
<p>
So, in order to stop procrastinating I decided to put what I actually had working up onto the web for people to see.  Warts and all.
</p>
<p>
The idea for the site is allow people to plan activities that involve them going from one place to another.  Think baseball road trip.  Think pub crawl.  Think anything where you need to go to a bunch of places in sequential order.  Your membership in the site will allow you to save those searches to review later.  I've been toying with allowing members to look at ALL searches made by people, but there might be some privacy issues related to doing that.  You might not want people to know what you're planning. ;)
</p>
<p>
The resulting interface will be slicker, better annotation on the points you've selected, etc.  It's really rough right now so don't think this is the final version or anything. ;)
</p>
<p>
So check it out and play with it.  Don't worry if you break something, hopefully I can learn enough to fix it. ;)
</p>
<p>
In my next post I will share some of the code I was using, sort of mini code-review if you will to make sure I am on the way to writing idiomatic Python (or Javascript in some cases).
</p>
