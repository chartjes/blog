---
layout: post
title: "Why I Began Testing" 
author: Chris Hartjes
date: 2012-05-14
comments: true 
sharing: true 
---
In the run-up to [php|tek 2012](http://tek.phparch.com) next week I wanted to
do a blog entry every day this week. Since I am supremely lazy I made sure to
ask my followers on Twitter what they would like me to blog about. There were
some interesting suggestions but I will start out with one that I think
explains a lot about me.

I've spent quite a bit of time in the last few years helping to spread the word
that having automated test suites and testable applications is a good thing.
I know it's not easy and I've had conversations with many other developers who
still think that writing tests is a waste of time, not appropriate for their
unique situation, and so on and so forth.

If I were to make some sweeping generalizations about those people who feel
that test-driven development is a waste of time, I would call them supremely
overconfident in their own abilities in the face of plenty of evidence that
suggests otherwise. Many developers that I respect immensely still seem to
think that Getting Shit Done Does Not Include Writing Tests. 

I will return to that topic later.

I don't remember when it was that I exactly discovered [SimpleTest](http://simpletest.org) while
working at an online dating site. I do remember it was in 2003. If I had to make an educated guess it was
because I had gotten tired of testing everything through a browser. Loading
the same pages OVER AND OVER AND OVER again, hoping I had covered all the
scenarios for the incredibly crummy code I was writing (this was quite early
in my programming career) in my manual testing. Only to find that I had 
missed something and it was causing problems on the live site.

Once I discovered unit testing, it was like a bit was flipped in my brain.
I immediately understood the benefits of a test suite that we could run from
the browser AND provide proof that all was good. No more manual testing unless 
absolutely necessary!

It took some time and some lobbying but not too long before I left, the
application architect they had hired decided that we needed to write a bunch
of tests using SimpleTest as part of progressing towards a refactoring and
rewrite of the application itself, since it really was the type of spaghetti
PHP application the language is derided for encouraging.

I don't know what happened to all those tests after I left. I would keep
running into people who I worked with there and new hires and would sometimes
ask what was going on. Never did ask about tests though, as I assumed that
they were either still there but not being used, or ripped out under the
guise of Getting Shit Done Does Not Include Writing Tests.

So why am I still in the minority that values testing? I think it's because
many people blind themselves to the reality of how much work they are really
getting done. Writing tests as part of the development process, in my opinion,
simply moves the debugging of your application from after you've written the
code to while you are still writing it.

Look, it still takes the same amount of time to write code + debug whether you
use TDD or GSDDNIWT. Be honest with yourself. Every time you are up until the
early hours of the morning trying to fix a problem is an opportunity to be
really honest with yourself and say "how can I avoid this?" instead of saying
"oh well, this is how it really is." I believe that having tests will reduce
the amount of time you spend trying to understand why things are not working 
the way that you expect them to.

If anything, the rise of startup worship makes the job of people like me
even tougher. Minimum Viable Product goes hand-in-hand with GSDDNIWT. I cringe
when people forward me conversations with their bosses and co-workers that
seem to imply that only inexperienced developers really need tests. "Rockstars
have the codebase memorized and can intuitively make changes that won't break
anything." Really?

I can only speak for myself, but testing is my way of not having to remember
the entire code base. It lets me examine discrete modules of code and see
clear examples of how they work and how they are supposed to interact with
other modules. When it's crunch time and something absolutely needs to work,
my memory is the last thing I want to be relying on to tell me where to look
for the problem.

I could write a very long ranty blog post about testing but I will save my
energy for those ready to be converted instead of those who have decided to
rely on their immense programming skills and eidetic memory about their
application. Lesser mortals like me will knit themselves a comfy blanket
using tests and simplified application models and hopefully be sound asleep
while my rockstar compatriots are up at 2am debugging their application 
after a painful production launch.

