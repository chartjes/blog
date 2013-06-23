---
layout: post
title: "Test All The Things?" 
author: Chris Hartjes
date: 2012-05-16
comments: true 
sharing: true 
---
I was asked on Twitter today for my thoughts on the topic of whether or not
there are things you should NOT test. Of course, I think that you should
[test all the things](http://www.littlehart.net/test-all-the-things.jpg)
but let's be honest in what we're trying to do.

Let's start out with the premise that every single bit of code in your
application. By this I mean we have 100% code coverage for your application.
This is difficult but achievable with lots of tests and proper use of
mock objects.

Even with 100% code coverage, it still might not be enough. So much 
depends on your actual test cases. Have you anticipated edge cases that
could cause your code grief? This is the one area of web applications that
I think leads to the greatest amount of problems: determining edge cases
when your code accepts user-generated content. So even if 100% code coverage
can't save you from every problem, what is a good compromise?

If you obsessively run PHPUnit code coverage reports like I do, you will be familiar
with the [CRAP index](http://www.artima.com/weblogs/viewpost.jsp?thread=210575) values
for your code. Go read the article about it. I'll wait.

I think that if you want to do effective testing, you can probably limit
your code coverage efforts to class methods or functions that have a CRAP index
of 5 of more. It's a low enough value that you will end up testing a very large
amount of your application's code base and will be testing non-trivial code.

You don't really need to test pass-through methods or functions (functions that are one-liners
that return the response from another methods or functions) or getter / setter
functions (if you're into that sort of thing). Chances are they will get
coverage in tests that call those methods.

In essence, don't waste a lot of time writing tests that test the trivial
or totally expected. You will have a much greater impact on your application
by writing tests for the complicated parts of your application.

Finally, I encourage you to pursue another very impactful testing practice:
whenever a bug is reported in your application, write a test to verify 
the bug. Then fix your application until the bug goes away. By doing things
that way, you end up with a collection of tests that reflect the various
ways that the users of your application actually, you know, use your
application.

Good code coverage results in a feeling that only weird edge cases are going
to bring your application crashing down. That frees you up to keep on
building out the application instead of worrying if a minor change is going
to wreak everything. 

So the ultimate goal is TEST ALL THE THINGS THAT MATTER. Aim for that, and
the rest will all fall into place.
