---
layout: post
title: Testing Web Services in Zend Framework 1.x
---
Typing that title made me feel weird, but the truth is that we are
getting close enough to ZF2 (at least in Release Candidate form) to
be released, so for posterity's sake I will start differentiating
between 1.x and 2. Makes me feel better at either rate.

Before I continue, I want to thank Giorgio Sironi for his very
helpful blog post about
[clever mock objects](http://giorgiosironi.blogspot.com/2010/03/clever-mock-objects-with-phpunit.html)
that showed me the technical details on solving my particular
problem, along with [@elazar](http://twitter.com/elazar) and
[@onyxraven](http://twitter.com/onyxraven) for their suggestions.

I needed to test a remote web service for an application at work.
Right away I knew I wanted to use
[Test Doubles](http://www.phpunit.de/manual/3.5/en/test-doubles.html)
to do it. I wanted to create a mock object to represent the web
service I needed to speak too, and create some data fixtures
containing known responses to queries so that I could test the code
without speaking to the web service itself. A key feature of a unit
test is that it should (unless not avoidable) never connect to a
web service or a database. Those sort of things are probably better
suited as either components tests or acceptance tests. I'm no
testing expert, but that is an approach that seems to resonate with
me.

The problem I ran into was that one of the web service calls would
react differently depending on what parameter is was passed into.
Reading the existing PHPUnit documentation did not provide me with
enough hints on how to solve this particular problem, so while I
dug around duckduckgoing for a solution I asked Twitter for help.
One blog post and 3 tweets later, I had the underpinnings for my
test. Check it out [here](http://gist.github.com/952286)

A walk-through is probably required in order to explain what I did.

First, we create a mock object using the Mock Builder interface and
map it to the web service object we wanted to use. Then, I loaded
in the fixture data I wanted to use, and also populated two arrays
that are a critical part of determining which response to return
based on the parameter passed in. Finally, I create an expectation
object for the 'get' method I am trying to test, telling it that I
am stubbing out 3 request-and-response pairings. Then I pass the
excpectation object and the two arrays containing acceptable
parameters and responses into a different method so that it figures
out how to handle my request for that method. It took me a while to
get this model working in my head to the point where I could
explain it.

To make things even easier to test, I created a Client object that
accepts an instance of the web service as a parameter, thereby
using Dependency Injection / Inversion of Control to make it
possible to actually test this thing. Doing it this way, the Client
really has no idea that it is in fact talking to a mock web service
instead of a real one. All it does know is that it is getting back
JSON responses from this "web service", and the code takes care of
the rest.
