---
layout: post
title: "Thoughts on testing APIs" 
author: Chris Hartjes
date: 2012-02-22
comments: true 
sharing: true 
---

I have been asked a few times on Twitter for some advice on how to use
testing tools in order to test APIs. It just so happens that I am writing a
bunch of tests for an API at work so perhaps this is a very timely blog post.
Rather than show you exactly what I did (I'm using [Behat](http://behat.org))
I wanted to discuss some common strategies I use when contemplating testing
APIs. 

When you are testing an API you main concern is your ability to reproduce
the results of a specific API call. If your API is such that repeating a
call several times will give you different results, you do have some 
challenges on your hands.

Testing that an API just works is what I would call a functional test. At
the highest level you are saying "will this call actually work". Since you
will be actually making API calls in your tests they can take quite some
time to run depending on how many you have. Long-running tests are the
type of tests that really should be forming the last line of defense just
before you're about to go into production.

Why? Functional tests have a lot of moving parts: HTTP calls, request and
response parsing, and likely communications with some sort of data store.
Not exactly the types of things that lead you to having a test suite that
can run in 10 seconds or less.

In my opinion the only way to have really effective functional tests is
by making sure that the API endpoints you are testing are using a known 
data source, one that will not be altered by your tests. That
way it will be easy to verify that a particular call had the expected
response. Remember, at the most basic level testing is about repeatedly
verifying that your code is returning an expected result.

If you are testing someone else's API, I hope there is a test mode or a 
sandbox that you can use. A lot of APIs are rate-limited or only allow a
limited number of requests a day (I'm looking at you, Google Analytics). 
The last thing you want is for your application to longer be able to access an
API because you went nuts testing things. Remember, the goal of functional 
tests in this scenario are to make sure that the API is returning results
that you expect, nothing more.

Integration tests of APIs are a bit of a tricky thing to do in an effective
way. Sometimes 3rd party APIs change. Sometimes you are also lucky enough
to be told ahead of time that it's happening. If your application relies
heavily on 3rd party APIs then your integration tests are a key line of
defense. While tests like these shouldn't be run as much as the unit
tests for the API, they should be run before a production push. Nobody
likes their application to be broken because of an unannounced change to
an API.

Finally, we have tests designed to make sure that your application is 
correctly handling the results of API calls. To make these sorts of tests work, 
you will end up either creating mock
objects of the code that will do the calls or data fixtures representing 
results of API calls. It is also for this reason I always recommend wrapping
the calls to an API in code, just so you can mock them for testing purposes.
Sure, it might be easier to cheat and do file\_get\_contents() on a URL but
that approach is pretty difficult to test. 

Remember, these tests should not even be calling out to an API in order to
work. Mocks and data fixtures are supposed to provide that data. All you
are doing is testing the code that needs results from the API. Again, if
you have been building your application with testability in mind your
suite of unit tests should be blazing fast.

In the end, it doesn't really matter what tools you are using to test either
your own APIs or ones that your application depends on. Be clear in your
mind about what it is you are actually trying to accomplish and don't get
create tests that provide very little value to your application.


