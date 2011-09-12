--- 
layout: post
title: Open Source Is Really About Documentation - Twisted vs. Tornado
---
<p>I think I can give you an executive summary of this blog post:  if the documentation for an open source project sucks, nobody but the most hardcore developers will use it.</p>
<p>
What has prompted this incredibly brilliant stating-of-the-obvious?  The reaction by those in the <a href="http://twistedmatrix.com/trac/">Twisted</a> community over Facebook's pre-emptive strike in the non-blocking Python-based web server space by open sourcing a framework they are using internally called <a href="http://www.tornadoweb.org">Tornado</a>.  Why are the Twisted folks getting all twisted (look how funny I am!) up about this?  Like any good Open Source project for people who are interested in Getting Things Done, Tornado is dissing Twisted by basically saying "yeah, we thought about using Twisted but it wasn't easy enough for us to use and we think it sucks".  I'm pretty sure I'm paraphrasing here, but you get the idea.
</p>
<p>
Now, I have looked at Twisted and have come to the following conclusions:
<ul>
<li>It looks awesome</li>
<li>It is built for people who are supposed to understand what they are doing</li>
<li>The documentation sucks</li>
<li>The examples on how to build anything of any significance are, to this developer, non-existant and/or difficult to find without shelling out for a possibly very-outdated book</li>
</ul>
Contrast this with Tornado.  I've looked at Tornado and have come to the following conclusions:
<ul>
<li>It looks awesome</li>
<li>It is built for people who are supposed to understand what they are doing</li>
<li>The documentation is inside the comments on the code which sucks only if you're not into reading the code</li>
<li>It includes a sample application so you can see something other than Hello World</li>
</ul>
</p>
<p>
Am I biased towards Tornado?  You bet.  Why?  Because as hard as I tried, I could not find USEFUL documentation on how to build things using Twisted.  Maybe I didn't use the right search terms.  Maybe I didn't dig down enough links deep on the Twisted site.  Maybe I didn't fully understand the terminology or architecture of Twisted and how they different components speak to each other.
</p>
<p>
I'll tell you this though:  I am not having any such problems with Tornado.  This is coming across as a criticism aimed towards Twisted, and I suppose that's fair.  I've noticed complaints from the Twisted community which really amount to whining.  I understand that attitude totally.  I've been there, when faced with competition that just might be doing a better job then I am doing.  But complaining that Facebook should've simply fixed up Twisted instead of writing their own is not productive.  Productive is understanding that Facebook looking at Twisted and said "this is not for us because *we* don't find it easy enough to use" is a sign that something serious is wrong with Twisted's documentation.   You could have the most awesome non-blocking web server available, but if people with who WANT to use it can't figure out HOW to use it, well, what can you say to that?  Only the most dedicated open source contributors would've done that.  Most will say "meh, I want to do this myself so I understand it" and then Twisted will die an obscure death while Tornado plunges forward gaining mindshare amongst people interested in the type of applications you can build with this technology.  In my opinion, it's all because of the lack of clear, freely available documentation for Twisted.
</p>
<p>
If there is an online source BETTER than the Twisted site, please share the link love in the comments so I can try and do a better comparison of the two at a documentation level.  For someone like me, who is new to Python but old to the idea of web frameworks, I think that would be the fairest comparison.
</p>
