---
layout: post
title: "War-room Driven Deployment" 
author: Chris Hartjes
date: 2011-12-05
comments: true 
sharing: true 
---
For a long time I have been an advocate of the philosophy that organizations
as a whole, not just the engineering team (if there is such a thing where
you work) should be striving towards the goal of treating any deployment
of your code into production as a non-event. Sadly, there is much work to be
done from both ends of the spectrum.

When deployments do go wrong the reaction is fairly predictable. It's almost 
like the five stages of grief, sometimes known as the Kuebler-Ross model. 
You've probably heard about them: Denial, Anger, Bargaining, Depression, 
and Acceptance.

The common thing that happens during those two first stages is that people are 
chewed out for their role in the deployment failure, and in many cases the anger
is legitimate. If you haven't written code that spectacularly failed in a 
production environment I will happily call you a liar.

What also then happens is that the non-technical people push for what I call a
war-room environment for dealing with deployments. By this I mean that, for
lack of a better phrase, orders come down from on-high that whenever a 
production push is going to be done that everyone needs to stick around and be
there "just in case" something goes wrong.

At the news of the new directive, the engineering staff roll their eyes and
mumble to each other about how the other side "doesn't get it" and how "this
won't solve these problems".

Both sides are right, but only up to a point.

I'm sure that some of my readers are familiar with the concept of perception
vs. reality. When you apply this to deployment failures, the perception
becomes that the entire team responsible for building the application
is to blame and that by making sure that everyone should be there it fixes
the problem. In my opinion, the reality is that the failure occurred due to 
the actions of one or two individuals and making the whole team suffer is 
counterproductive. I feel this way especially when I am directly responsible
for what has happened.

Finding bugs in development are magnitudes cheaper to fix than production ones,
and you will feel less pressure to fix them than if they are discovered in
production. To paraphrase Darth Vader, you know in your heart that this true.
Therefore the engineering side of the equation really needs to push back hard
on the idea that ALL HANDS ON DECK WE ARE DEPLOYING is not just making the
problem worse before it can get better.

I've had my fair share of time with war-room driven deployment. I understand
why it is viewed as a solution to the problem of failed deployments. It seems
very logical. By having everyone there when it happens you are more likely
to be able to quickly solve any problems you find. However, I feel like it is
masking the true problem in that everything that you find yourself doing when
practicing war-room driven deployment can be done before you even get to that 
point.

It also becomes an issue of trust. Frequent failed deployments results in the
engineering side of things to be labeled as sloppy, uncaring, not understanding
the cost of lost opportunities. All of those things may or may not be clear, but
I think forcing everyone to stick around "just in case" makes the situation worse.

By using war-room driven deployment you are making all stakeholders nervous about
deployments. Everyone will be exhorted to think of everything that could go wrong
with the deployment and if something does go wrong, the stress level gets cranked
up to 11 and there is frantic activity to try and solve the problem.

It is often hard to explain to non-technical people that they should stay calm
and understand that the engineering team knows what went wrong and has a real-world
solution in mind to fix whatever problem happened to minimize the chances that
it happens again in the future. I don't have any easy answers on how to solve
that problem other than staying calm yourself and offering real-world, practical
solutions to the problems.

If you put all the effort into making production pushes a non-event, then you will
not need war-room driven deployment. All you need is one person to push a button
and then everyone can go home.
