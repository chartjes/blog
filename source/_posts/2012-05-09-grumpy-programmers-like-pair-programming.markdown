---
layout: post
title: "Grumpy Programmers Like Pair Programming" 
author: Chris Hartjes
date: 2012-05-09
comments: true 
sharing: true 
---
Some of you might have a vision of me, the self-described and oft-labeled
Grumpy Programmer as the type who prefers to work in solitude. Uninterrupted,
I crank out code while in The Zone.
 
I prefer working in collaborative environments where the entire team gets to
work on the entire application. None of this siloing bullshit that I see happen
time and time again. "Borat is the only guy who understand our reporting system.
We can't possibly let anyone else work on it!" That sort of nonsense doesn't
belong on any team and also speaks of ridonkulous communication problems.

At [Kaplan Professional](http://www.kaplanprofessional.com) they've chosen to
use [pair programming](http://en.wikipedia.org/wiki/Pair_programming) as a normal,
everyday development practice. Our team consists of 3 developers in the main
offices in La Crosse, 7 remote workers spread across 3 time zones, 2 QA staff, 
one testing engineer, and our development manager. Pair programming has worked
out awesomely and I want to try and explain why.

One of the biggest hurdles facing a team with in-house and remote workers is
communication issues. Your classic pair programming setup is two developers
sitting together at the same desk, one typing while the other helps out with
suggestions on how to write the tests we're going to need and how to hand-crafted
our artisanal code. Sadly we still have people writing the tests AFTER they've
written the code, but grumpiness is not eliminated in one day.

At Kaplan we use the dynamic duo of [Join.me](http://join.me) and [TeamSpeak](http://www.teamspeak.com/)
for pair programming. Whomever is driving will start a join.me session, share the
link with their partner and away they go. There is much coding and playful banter
as Shit Gets Done. I cannot put it any other way.

Your partner keeps you honest and focussed on the task you're trying to solve. For
example, when I was coding a feature I was not 100% familiar with I was able to 
get my pair to do research on other parts of the code base while I was creating
the skeletons for some tests. Many times my pair would suggest "don't you think we
could make that bit of code better by...", and more often than not we'd have a good
discussion about writing easy-to-understand-yet-efficient code or discuss how what
we are doing is out of character with the rest of the code. [Object calisthenics](http://www.slideshare.net/rdohms/bettercode-phpbenelux212alternate)
is a favourite topic of mine and has led some of my other fellow developers to rethink
how they have been building things.

See, people have this idea that pair programming means that one guy codes while the
other sullenly watches or surfs the internet instead. Or it means two developers
fucking around instead of working. I cannot speak for other developers, but I don't
put up with that shit while paired. I am expecting my pair to devote as much attention
to the task at hand as I am, and I return the favour by being attentive and helpful
towards my pair when I am not driving the session.

Because developers are taking turns solving problems and implementing solutions,
the amount of tribal knowledge (knowledge about the application itself locked up 
in people's brains instead of shared and/or documented) decreases and everyone's
understanding of the system goes up. This transfer of knowledge can only really
happen as one developer shows another just what the hell is going on inside this
application. There is no better way I can think of to do this than while paired.

Pair programming also has the added good side effect of allowing team members to
get to know each other. It's only the most anti-social of co-workers who won't end
up discussing things outside of work while pair programming. I don't see any reason
to work with robots who only care about how many story points we are cranking out
every sprint. We are people first and coders second. Don't forget that.

Finally, pair programming results in more than one person understanding how a 
particular problem was solved and how the solution was implemented. At Kaplan
we always have a sprint demo day at the end where we demonstrate the various
features that were implemented during the sprint. With everyone having used
pair programming, it's much easier for the group as a whole to decide who will
demonstrate what. No need for one developer to hog all the glory!

This also ends up being a great way for those who already understand the
application to teach new hires how things work. Kaplan Professional had 
expanded its team quite rapidly when I started and I think that without pairing we would
still be struggling to meet our sprint commitments. Nothing prompts rage-quitting
more than a situation where it is incredibly difficult for new hires to make
positive contributions to the team within a few days of starting.

I understand that not every organization is ready to make a commitment to use
pair programming. Just like not every organization is ready to make a commitment
to writing tests as part of their normal flow. But don't harbour any misconceptions
about what pair programming *really* is: two developers working together towards
solving problems, alternating who is mashing keys on a keyboard. Both developers
*are* working, they are just working *together*.

The goal is to solve problems within a unit of time that you have committed to. 
Kaplan Professional is no different in that it expects you to honour your commitments.
Pair programming has been a way for problems to get solved faster than if 
individual programmers had been trying to solve them. Communication is up, non-working
features are done, and the amount of work actually getting done has increased
noticeably in the two months since I started working in pairs.

I cannot recommend enough giving pair programming an honest try in your work
environment. You might be surprised to find out that you are Getting More Shit Done
than you realize.
