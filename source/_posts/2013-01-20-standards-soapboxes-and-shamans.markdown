---
layout: post
title: "Standards, soapboxes, and shamans"
author: Chris Hartjes
date: 2013-01-20
comments: true
sharing: true
---
To paraphrase Batman:

> "Programmers are a cowardly, superstitious lot"

Programmers often look to external sources for validation of
all sorts of things they do. Did they choose the right
language? Are they writing good code? Will they be
accepted by their peers.

Of course, there are those who are leaders within a 
community. Those who manage to do great things
but with an idiosyncratic way of doing things.
Let's call these people shamans. In many ways
programming is a mystical thing: you conjure
up solutions to problems using tools that
often require strange incantations.

For those who pay attention to the workings of the PHP community
you might have heard about the "PHP Standards Recommendations"
that have been coming out of the [PHP Framwork Interop Group](http://www.php-fig.org/).

It's first contribution was [PSR-0](https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-0.md), which covers recommended standards for
autoloading of PHP code (no more remembering to require/include files
any more to load your class files), then followed by [PSR-1](https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-1-basic-coding-standard.md) (which covers basic coding standards) and [PSR-2](https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-2-coding-style-guide.md) which is about a coding style guideline.

More recently this group has been working on a standard for logging 
interfaces called [PSR-3](https://github.com/php-fig/fig-standards/blob/master/accepted/PSR-3-logger-interface.md). 

I spoke about this on Twitter, and I will repeat it here: 
I think PHP programmers should get behind PSR-0 and efforts like
PSR-3. I feel that PSR-1 and PSR-2 are solutions looking for
a problem and seem, to me anyway, to me out of place with
the solutions offered by PSR-0 and PSR-3.

Standards that are enforced by the community have a power
that people really don't understand. The classic example of
this are the [Python Enhancement Proposals](http://www.python.org/dev/peps/).
They cover a incredible range of ideas and concepts that a Python
developer needs to worry about.

PEP-8, which covers coding standards, is probably the one most
casual Python programmers are familiar with. The whole community followed
it, which might have been easier due to Python's use of significant
whitespace. But more importantly, it was championed by
Python's Benevolent Dictator For Life, Guido van Rossum.
He was able to use his soapbox as the guiding force behind it.

PSR-1 and PSR-2 are generating a lot of, well, pissing and moaning 
from people. I get it: I often grind my teeth when looking at
code written in a style that deviates quite a bit from my
normal coding style and practices.

However, it's far more important to be able to understand
what the code is doing. PSR-0, in my opinion, serves to standardize
application layout for the purpose of making it easier to
load classes you need in your code. PSR-3 (and similar interface
standard recommendations) serves to allow you to integrate
3rd party code with yours a lot quicker.

Standards, soapboxes and shamans are an integral part of
any programming community that wants to move forward and keep
producing better and better tools and applications. Any programming
language community that does not work as hard as possible to
make it easier to integrate other's libraries of code together
is asking for irrelevancy.
