---
layout: post
title: "So you want to write tests" 
author: Chris Hartjes
date: 2012-12-17
comments: true 
sharing: true 
---
I often get asked for some advice on how to get started with writing tests
for your PHP code. It's a fair question, since I am presenting myself as an
expert-ninja-rockstar-sensei-opinionated-egomaniac on the topic.
I often struggle with coming up with an answer that can fit into the 140
characters available via Twitter, but clearly this is not a good strategy.

As an early Christmas 2012 present to all my loyal followers, who put up with
my never-ending stream of nonsense and provide a slowly-increasing portion
of my income, here are my thoughts on how to get started with testing your
PHP code.

## Learn how to recognize untestable code
The worst feeling in a programmer's world has to be sitting in front of a
piece of code that you didn't write yourself but is critical to the success
of your business. You will be told that it's of the utmost importance
that you GOD SAKES DON'T BREAK ANYTHING OR ELSE WE ARE DOOMED. 

While I don't get the same kinds of warnings from my employers, I am familiar
with that feeling of trying to figure out not only what the code in front
of you is supposed to do, but what the developer who came along before you was
even THINKING ABOUT in that code.

When it comes to testing code, there are two principles that you have to 
strive to aim for:

* find a way to pass dependencies into your code
* find a way to break down your code into the smallest modules possible

By following this two simple-but-extremely-difficult-to-do ideas, you will
end up with code where writing tests becomes so easy you will be doing it
without a second thought.

No more static method calls. Get rid of those private and protected methods.
Stop creating new objects inside a method. Think about passing data around
instead of objects. Work hard to make sure your methods have little-to-no
[side effects](http://en.wikipedia.org/wiki/Side_effect_(computer_science)).
Decouple your data source from the code that manipulates results from it. More
importantly, understand why all these things are barriers to having an easily-testable
code base.

In short: do all the kind of hard work and drudgery that many managers tell
you is a waste of time and will not return any value to your employer. I say
screw those guys and instead feel awesome about working on building light, nimble systems full
of tests that let you go home from work on time. 

## Keep learning the language
Tests are just code. Keep learning how to write better PHP code. Understand why
so much of what is on [PHP Sadness](http://phpsadness.com) is actually trying 
to help us get better. Understand why the array in PHP is awesome. Learn
the [iterator drinking game](http://www.meetup.com/dallasphp/events/59505212/).

In short, the more you know about the language the more likely you are to learn
how to solve problems using core functionality instead of constantly implementing
solutions in code you wrote yourself. 

## Chain units of code together for greatness
I've talked about in other places
about my thoughts on the UNIX philosophy. For the impatient, it is about creating
small, single-purpose units of code and then chaining them together to 
accomplish awesome things.

If you're ever searched online for ways to do things from the command line
in various flavours of Linux distributions, you will understand what I mean.
"Take sed and cat and awk and grep and pipe it through cut and then to sort 
and you will get exactly what you want." 

That sort of stuff is awesome, and fits in rather nicely with the concept of
writing small modules of easily-testable code.

## Start asking "how am I going to test this?"
This is the first question I ask when I am presented with a problem that I need
to solve using code. From that one extremely important question all the best
practices that are associated with building highly-testable code emerge from.

If it is not obvious how you are going to be able to create automated tests
for a particular set of functionality, it probably means you haven't thought
hard enough about the problem you are trying to solve.

I'm not saying every problem has a testable solution. But any problem where
you have expected results based on known input is a scenario that you can
test for. Database queries. 3rd party API's. Request routing. Fizz Buzz.
These are all things that we can test, by making sure to follow some of
those key ideas I advocated above.

Test-centric development is about using tools as a way to create API's and
interfaces that are simple, easily testable, and easy to modify going 
forward. 

Adding new features becomes a potentially-simple process consisting of:

* design new feature
* write tests for these new features
* write code until the tests pass
* go home on time
 
## Stop people from pushing code without proof it's fixed
Sure, you don't have any tests RIGHT NOW. But I'm sure you've got bugs to fix
in your code. Write tests to verify that the bug exists. I'm sure you'll find
your code isn't as modular or testable as you thought it was. 

Once you've reproduced the bug, then write some code until the bug GOES AWAY.
Then push your updated code into production. Rinse and repeat until you have
a very highly-targeted test suite and a bunch of highly-targeted fixes for
known mistakes in the application. That is what I call real-world testing.

So make sure that nothing that fixes something goes up into production, no
matter how desperate the circumstances, without proof that this fix actually
is a fix instead of a wild guess. 

## Stop people from doing things manually
It's the 2nd year of the 2nd decade of the 21st century. The internet is
full of instructions on how to automate just about anything. Spend an afternoon
studying that instead of dreaming about an advertising-driven disruptive
startup. 

[Chef](http://www.opscode.com/). [Puppet](http://puppetlabs.com). Shell scripts. [Jenkins](http://jenkins-ci.org). [Travis](http://travis-ci.org). Virtualized servers. Learn these things. Use them. You
will thank me. Maybe enough to send me money via PayPal. Automate everything
that you keep finding yourself doing manually, and then figure out if there
are ways to not even do those things. You might be surprised.

## Stop using tools without test suites 
I treat any PHP tool that does not have its own test suite as a black box
that cannot be trusted. Tests show that the developer cares about the quality
of the work they do, and also provides real examples on how to do things.

Black boxes are not things you should be relying on when the going gets tough.
Treat any code that you cannot easily test as being suspicious and likely
broken. I feel the same way about code *I* have written, so imagine what
I must think of other people's stuff.

## Always wonder if you're doing it right
Integration tests are a scam. Unit tests don't fix bugs. Simple enough code
doesn't require tests. Pair programming is a cargo-cult practice. PHP sucks.
Mobile applications are the future. Documentation comes after the work is
done. Nobody likes a developer who asks too many questions. You work in the
real world where results matter. Exit statuses are better than throwing
exceptions. Asynchronous calls always result in callback hell. 

Not everything in the above paragraph is true. The only way to find out is
to get out there and figure out if it is true or not for yourself. 

Keep on testing. I'm here to help. Merry Christmas everyone. 

