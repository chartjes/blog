---
layout: post
title: Component Architecture -- Why Are You Not Doing This?!?
---
Welcome to my last post of the
[Ideas of March](http://shiflett.org/blog/2011/mar/ideas-of-march)
series. It's been awesome stretching out the brain and putting more
long-form thoughts in to blogposts. I hope I've spurred other
people on into doing more research and thinking about the stuff
they do as a developer. It's very easy to fall into a rut and get
comfortable, shunning new ideas and new techniques.

I discovered an awesome presentation by my new favourite PHP
developer, [Stuart Herbert](http://blog.stuartherbert.com/). Pardon
the salty language, but how the FUCK did I not know about this guy
before?!? I found out about him from this awesome presentation he
gave at the PHP UK Conference about
[Beyond Frameworks](http://blog.stuartherbert.com/php/2011/03/20/following-up-my-beyond-frameworks-talk/).
Talks about real-world situations always resonate a lot better with
me than a presentation about out cool some new piece of tech is
without presenting a compelling reason to use it. Not to pick on
the NoSQL guys, but please show those of us not as smart as you why
we really need it. Here's a good example of what I like to see: a
blog post from MongoDB-internals-developer-turned-web-developer
Mike Dirolf and his
[perspective on MongoDB](http://dirolf.com/2011/03/28/new-perspective-on-mongodb.html)
is a great example of providing reasons behind someone's use of a
particular technology. Enough of that, I'm drifting off topic.
Again.

Stuart's presentation was all kinds of awesome because it examined
a problem that many people have (that their applications end up
being held hostage by their framework choice), showed an example of
a real problem (their own infrastructure as it crept through
several iterations), and then provided a real solution (reduce the
dependence on the framework itself by creating reusable
components). By sheer coincidence, this is the sort of things I had
been contemplating doing while still working for
[XML Team Solutions](http://www.xmlteam.com) but in a slightly
different form. The brilliance was the leveraging of PEAR to be a
keep part of it.

When do you need to start thinking about a component architecture?
When you find yourself reimplementing the same thing for different
applications. At XML Team, there were hints that this needed to be
done. Requests to allow users of one application be allowed to use
their authentication credentials on another. A desire to refactor a
web service plus web GUI in order to simplify the internals because
we were mixing up theming with the web service stuff. Add to it a
dash that I was relying too heavily on framework tools that might
make it tough to do things like add an IOS application for clients,
and I realized that there were some serious architectural changes
on the horizon that some people really wanted to ignore.

But here's the really tricky part (and I'd love for Stuart to
follow-up on this) about the decision: how do you decide what stuff
can be extracted out and built into a component? Without a clear
method for figuring this out, there will be no movement in that
direction. The main reason is what I like to call the Precious
Snowflake Problem. The PSP is a double-edged sword for most
developers when trying to determine whether or not to write
something from scratch or adapt someone else's code. It is my
learn-ed opinion that most developers overestimate the uniqueness
of their particular set of problems. It's natural that we emphasize
the differences and ignore the sameness.

But it has also been the genesis of a lot of really
technology-advancing projects. Developer becomes frustrated with
existing tool that won't work quite the way they want it to, so
they go and create their own version of it. I don't have enough
time to list all the successful projects that have come out of
this. My intention here is not to slam those who wish to scratch
the proverbial itch, but to try and focus attention on how to
determine when some subset of functionality in one application is
similar enough to another that you can extract it and simply build
in the differences by reacting to a sane number of parameters
passed in. My personal feeling is that unless you are introducing a
major paradigm shift for a particular technology, you are better
off building on what others have already done. Let me provide an
example.

The [Lithium](http://lithify.me) project is an example of what I
would call introducing a paradigm shift for a particular
technology. It was one of the earliest proponents of making their
framework compatible with PHP 5.3 and newer. Why? So they could
take advantage of closures / anonymous functions / whatever you
wish to call them in order to apply some unique features to the
framework. This would allow for some neat stuff like filters (in my
opinion a very-underrated feature that I expect to see appearing in
the next generation of Zend Framework and Symfony) *and* result in
less code being written. At the same time, it is code that makes
sense: creating stuff that gets done at certain, well-defined
points in the request cycle. At least I *think* that's what it is
supposed to be doing.

Let's take a look at my example of the desire to share
authentication between multiple applications. If you have
applications using different frameworks, well, you are going to
have to do this from the bottom up and invent a service these apps
can talk to. Maybe a web service is the way to go: provide the
credentials and shoot back the response because your applications
live on different servers. Perhaps a better solution is to make it
authenticate at the code level, thereby only having a database call
instead of a web service call and the associated database call.
What is good is that you are ACTUALLY THINKING ABOUT HOW TO
ABSTRACT IT OUT. Personally, my plan would've been to create a
code-related solution provided via a component because the two
applications in question lived on the same server, but breaking the
database-backed information into it's own database to make it
easier to move somewhere else should the need arise.

Decisions like this require courage and resolve. No, it's not a
cliche. It's the truth. You will encounter resistance towards your
efforts to make sense of the spaghetti and allow you to move to an
architecture where your framework of choice becomes a very thin
layer on top of a bunch of reusable, tested components. Who doesn't
want to work with a code base like that?

My final Idea of March: embrace the power of component
architectures and do what you can to move your own applications
(and company or even framework project) towards it. The best sign
that you're there? A very lean core for your application with lots
of components being called in as you need them, not monolithic full
stack applications where everything you need and then some is
always being included.

I hope you've enjoyed my contribution to the Ideas Of March for
2011, and perhaps I will resurrect it in 2012.
