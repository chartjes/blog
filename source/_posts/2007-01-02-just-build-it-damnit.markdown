--- 
layout: post
title: Just Build It, Damnit!
---
<p>There was a posting on the <a href="http://cakephp.org">CakePHP</a> mailing list today from someone asking for sources of advice on "starting big applications".  Having gone through this at my previous job, I posted the following response:
<br />
<blockquote>
Just to inject some sanity into what should be a very interesting
thread, I urge anyone building an application to simply BUILD IT and
worry about the profiling / benchmarking for AFTER you've built it.
Trust me when I say this:  no application of any significant size
survives long enough to be scaled past it's original intent without
wholesale architectural changes.  You *WILL* be rewriting things, you
*WILL* be rethinking how your application is organized.  Like Death
and taxes, it is inevitable.  But you can worry about it later.

I say this as someone who has been through the "let's build something
massive" process, only to see it fail horribly due to all sorts of
preconceptions at design time that resulted in major rewrites that no
benchmarking would've helped.  We didn't know what the bottlenecks
were until we actually saw them get hit, and then we set about
rewriting the bottlenecks.  A little slipshod for sure, but there were
many things that happened that we could not have anticipated when we
were building it.

If your site is so busy that you need to do benchmarking and other
refactoring work, then you have accomplished more than 99% of other
websites out there and deserve a round of applause.  Until then, Just
Build Something, Damnit and worry about fixing any performance issues
later.

Before everyone jumps on me, please understand that I am saying this
out of experience.  Yes, there are certain things you can do in terms
of building a cache-friendly app, or configuring a web server for
optimal use but those are so application-specific I hesitate to
recommend those things until you actually know what you need.  Premature
optimization lies on the path to developer madness.

You won't know what challenges your application will face until people
other than you are actually using it. ;)

Hope that helps.
</blockquote>

</p><p>My new mantra for programming in 2007 is Just Build It, Damnit!  I've been procrastinating too much on several personal projects so it's time to put my money where my mouth is.</p>
