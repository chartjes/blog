---
layout: post
title: "PHPSpec and the new wave of testing" 
author: Chris Hartjes
date: 2012-10-18
comments: true 
sharing: true 
---
I promised [@everzet](https://twitter.com/everzet) almost two weeks ago that
I would take a look at his latest project, [phpspec](http://www.phpspec.net),
and let him know what I think.

I think that we are witnessing the first wave of new testing tools in the PHP
community that allow developers to wrap their applications in automated tests.

I am familiar with the BDD-style that is being promoted in PHPSpec, through
my work with [Behat](http://behat.org) to create automated user acceptance
tests. I think if you want a tl;dr version of PHPSpec I would tell you
"write hybrid unit/integration tests using plain language".

The concept that is being promoted is "SpecBDD". It means "writing tests
to a specification and then writing code until that specification is met."
Not a lot different than writing tests using tools like PHPUnit. 

Your still going to have to write code that you can test if you want to
use phpspec. That means you still need to know about dependency injection
and other characteristics of testable code. Sorry, no magic testing pixie
dust here.

I was also surprised to see the use of mock objects, which are being 
called "Prophet Objects", but that means that you can really write specs
that test for things in isolation.

Mock objects are, in my opinion, the conceptual stumbling block that
developers need to get over in order to really, deeply understand how
to write effective tests. I am happy to see phpspec promote this idea
and provide a fairly simple API to do it.

The process is the same as it would be if you were using PHPUnit: write
the test / spec, and write the damn code until everything passes. Again,
no magic testing pixie dust.

(By the way, if someone makes me a "magic testing pixie" t-shirt, men's size
XXL or larger, I will purchase it YESTERDAY).

Keep on cranking out the tools, make them useful for people OTHER than testing
zealots to use them, and you have yourself an unstoppable wave of automated
testing.



