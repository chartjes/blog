---
layout: post
title: "You need tests...just not yet" 
author: Chris Hartjes
date: 2013-01-07
comments: true 
sharing: true 
---
Every once in a while I come across a blog post or a presentation that helps
me figure out something that has been bothering but I was having problems
articulating. Lately I've been struggling to come up with strategies to help
developers figure out when they should REALLY be writing tests for their code.

If you believe in the power of TDD, then the answer is "you write tests from
the beginning of the project and forever after." I am a believer that TDD can
be a very powerful design tool for building things at the unit / module / component
level.

Then some people asked me my thoughts on the comments by the creator of the
Rails project about the usefulness of dependency injection. As happens when
I am feeling frustrated, I started firing out the tweets on my feelings on
testing and the lonely Crusade that I am on.

Then I saw a talk by Dan North called ["Decisions, Decisions"](http://www.infoq.com/presentations/Decisions-Decisions) at the recommendation of [Ian Barber](https://twitter.com/ianbarber) that made me realize that someone else has articulated my feelings on
when you should be doing testing. Slides for the presentation can be found
[here](http://qconlondon.com/dl/qcon-london-2012/slides/DanNorth_DecisionsDecisions.pdf).

You should watch the whole presentation. So many decisions about programming
are made without understanding, REALLY understanding the trade-offs involved
when making one decision vs. another. 

Let's look at TDD vs. Test whenever. The trade-off being made here is not
about quality of code or guarding against regressions. It's about opportunity cost.
This had occurred to me but I had dismissed it as being "anti-testing".

But I think I was wrong, and here's why.

In that awesome presentation he talks about "patterns" he observed on the team
he was working with at the time. He was amazed at how much work this team was
getting done, so he spent time analyzing what they were doing and trying to
turn some of their activities into patterns of behaviour. Repeatable processes
are good, right?

The one that he saw being related to writing was a pattern he called "Spike
and Stabilize." Basically, you write code without any tests until it becomes
a solid part of your application's architecture. Once this code has proven
it's usefulness, you start writing comprehensive tests in order to verify
that it is in fact doing the job and doesn't break going forward.

This is so obvious to me now. Clearly, you are leaving yourself open to the
potential of writing not just application code but testing code that gets
tossed away if the idea you are implementing is unable to prove it's value.

Opportunity cost is huge and often dismissed by developers too. If you have
some prototype code, or even functionality with a half-life measured
in 3-month-increments, what else could be worked on while tests for this
code are being written? 

Could this hybrid approach be an easier sell to skeptical managers or
other stakeholders? That's hard to say. The "too busy to write tests"
camp still has many members, and is still seems that it takes catastrophic
failures before many people join the Testing Crusade.

To be perfectly clear: I find great value in prototyping code and then
committing to tests once the prototype is ready to move to a more stable
environment.

I try and do prototyping before I commit to writing code, because I often
feel that way. My prototypes are usually command-line scripts that try
and accomplish the task I've been assigned. That way, it's easier to
actually write some tests once I know what I'm doing and guard against
regressions later. 

The key to all this is being able to identify at what stage in this particular
pattern your code is at. Is it still a spike, meaning you are working out
implementation details and trying to figure out if it will even have the
desired result? Or is it stable, providing solid value to the application 
as a whole and ready to be wrapped in tests to protect against regressions?

Next time you are thinking about "I need some tests for this", consider the
Spike and Stabilize pattern. The answer might be "you need tests...but not yet."
