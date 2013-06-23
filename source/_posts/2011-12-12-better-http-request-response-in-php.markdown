---
layout: post
title: "Better HTTP Request/Response in PHP" 
author: Chris Hartjes
date: 2011-12-12
comments: true 
sharing: true 
---
I just started up a podcast called [Developer Hell](http://devhell.info) with
my fellow piss-and-moan-driven-development practitioner [Ed Finkler](http://funkatron.com)
. It basically consists of Ed and I sitting down and just having an open and
unedited discussion about whatever programming-related topic we feel like
rambling on and on about. Our first episode covered the always-riveting
topic of ["What We Hate About PHP"](http://devhell.info/post/2011-12-10/what-we-hate-about-php/).

Now even though it is just us complaining about stuff in PHP that we don't
like, regardless of the true merits of our complaints, it sparked a discussion
on Twitter about just what should be done to make handling PUT and DELETE
requests better in PHP.

$\_POST and $\_GET are workhorses of the PHP world, used in any application
that accepts web requests from somewhere. Sometimes accessing them is wrapped
inside objects or filtered out using the filter() extension of even [Inspekt](https://github.com/funkatron/inspekt)
but I think this illustrates the problem.

[Laura Thompson](http://twitter.com/lxt) made the suggestion that PHP should
look to port the concept of the Request object that Python uses over to PHP.
As a cryptopythonista I think that is an excellent idea. [Elizabeth Smith](http://twitter.com./auroraeosrose)
did ask for some constructive ideas on solving this problem. While my C skills
are non-existent, I thought I'd delve a bit into more higher-level thoughts
about this.

I think the fact that we have $\_POST and $\_GET lulls some of us into the
false sense that we should have $\_PUT and $\_DELETE objects, since that
would map to the commonly-desired set of HTTP verbs that REST likes to use.
But what should be inside those things, or should we be moving towards a more
Pythonesque solution where a Request object, as part of core or via a only-really-for-the-brave-
PECL extension?

What I'm really after is for an easy way to detect that a PUT or DELETE
request has been made. Existing solutions for these are not pretty and (
in my opinion) non-intuitive. With my thoughts that PHP is quickly turning
into a tool used for web service API end points that don't require insane
levels of concurrency, the idea that there is no native support for figuring
out if you're been given a PUT or DELETE request is disheartening.

The [PECL HTTP extension](http://www.php.net/http) is a step in the correct
direction, but it too has some rough edges and would require a lot of
polishing before it could be moved into the core where it really belongs.

Again, what I'm looking for is an easy way for PHP to be able to know what
type of request it is dealing with so I can make my PHP applications more
aware of what it being asked of them. It seems that pretty much every
framework implements their own Request/Response objects, so that should be an
indication that this kind of code abstraction is a desired core PHP feature.

Share your thoughts with me in the comments.
