---
layout: post
title: "How Not To Suck At PHP" 
author: Chris Hartjes
date: 2012-02-03
comments: true 
sharing: true 
---

Since I hadn't blogged for a bit I thought I would ask my Twitter peeps what
they might want to hear my rant about. One of the more interesting suggestions
I got was from [Travis Northcutt](https://twitter.com/tnorthcutt) who said
the following:

> "Got it. I have no formal CS background, but I'm trying to learn enough
> to build (something). I know enough PHP to kind of, sort of get by
> but am trying to solidify my foundation. So if I'm being selfish, write
> a post to someone in my position who wants to not suck at building stuff."

This is actually a great question. Although the self-centered answer is
to start off by buying my [book](http://grumpy-testing.com), that isn't
really the question that is being asked.

I thought about this question for a while and have some thoughts on what it
really means to know how to not suck at building things using PHP. In my
never even remotely humble opinion I think the key is to understand what
PHP is really good at.

I have spoken at length about my opinion that PHP won the web war because
it was so tightly coupled with HTML and very early on had support to run
with Apache via mod\_php. However the world has changed, and the web war
itself has changed. I think I can say with a smirk that the web war is now
an asymmetrical one, where the expectations of behaviour by users is totally
different.

But PHP is still in a really good position because of its true nature:
PHP is glue. It's glue that binds things together in 
a way to quickly produce HTML output. There is a reason the LAMP stack (with
PHP as the "P") was so successful: if you had to get data out of a database
and onto an HTML page there was no easier way.

One of the trends that I see in PHP is that the frameworks that sit on top
of PHP are starting to ask for influence over the development and direction
of PHP itself. I have mixed feelings about this. On the one hand, it is
good that people push for newer features in their chosen programming 
language. I think the PHP core is not necessarily against these suggestions
but they move at different pace than the framework people. But my other 
concern is that we don't end up with a framework driving the language.

When you think of Ruby, unless you are in denial or a really old Ruby hacker,
you think of Rails. Without Rails Ruby does not get the push that it did
and continues to get. It's a good language but it would've languished in 
obscurity if not for DHH.

So what does this have to do with not sucking at building stuff in PHP? I 
think it's important to understand that you can build cool stuff without
relying on a framework. Heresy, I know. But if you keep thinking of PHP
as glue it totally makes sense. How many applications are REALLY just PHP?
They are *really* web server + data source + Javascript + CSS + HTML. Think 
about that for a minute. PHP is the glue that binds all that together.

The danger for people like Travis who are starting out with PHP is that they
will get caught up with a mindset that a framework is the solution to their
problems. It is *one* solution to the problem of building a web application,
but failing to understand how to write PHP that behaves like glue will lead
to a lot of problems later. Because when the time comes for you to do something
that the framework did not anticipate you will be fucked. And you will be 
incorrect when you blame the framework.

So my advice to Travis is that he should worry about learning to use PHP like
glue and correctly identify the problems he is trying to solve NOW instead of
worrying about the problems he might have to solve later. There will be time to
fix your problems. Some of those will be solved by using tools that are not
written in PHP, but PHP can still glue them together. NoSQL data sources.
Distributed workers. Queuing systems. Real-time document searching capabilities.
These are all things that are NOT written in PHP but it is extremely likely
that someone has written a library in PHP that can talk to them.

Hope that helps you Travis!
