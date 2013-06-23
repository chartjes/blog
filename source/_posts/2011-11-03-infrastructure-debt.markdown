---
layout: post
title: Infrastructure Debt
author: Chris Hartjes
date: 2011-11-03
comments: true 
sharing: true 
---
You might have come across the term "technical debt", used to describe the small
mistakes that are made in your code base as the application grows and requirements
change. You end up with a big tangled mess if you are not very careful about
how you make those changes. If you've ever worked on an application where you
were afraid to make changes for fear of breaking something, then you have
run into technical debt.

It's very easy to build up technical debt: you put a quick hack in because you
feel like you are under pressure to get a task accomplished. It takes courage
to push back and say "no, damnit, I need time to fix this particular problem
correctly!". I understand, and it's okay. We can hug it out if it will make
you feel better. 

Technical debt can be dealt with via ruthless refactoring and wrapping your
application in tests that poke and prod at the edge cases that your application
deals with. But there is another type of debt you end up dealing with. One that is
even more difficult to deal with and change. I call it infrastructure debt.

Infrastructure debt is debt that you build up because you have not been paying
attention to the process of creating the environments your application will exist
in and have not been paying attention to the process of how your code gets from
development into production. In my opinion, infrastructure debt is much more 
difficult to "pay off" than technical debt. Why? It is often very difficult
for people to understand that it even exists.

Before I go any further, if you are not using a version control system to keep
track of changes to your code, then please stop reading and go and install one.
Having versions of your files with extensions like .1 and .old is the worst
kind of infrastructure debt that you could possibly have. It's the 2nd decade
of the 21st century. Version control is an almost 40-years-old, well-understood concept.
Nothing I suggest will work if you insist on acting like version control
is of no use to you. Passing around diff patches is not version control, my
friends. It's denial. Don't tell me just because people used to do it in
the past that it's okay now given all the available options. People used to
think that the earth was flat once too.

Let's start with an easy infrastructure debt to pay off: inconsistency in development environments. These
days it is pretty easy for someone to create a development environment for their
language of choice along with associated components like databases. The problem?
That it's pretty easy for someone to create the development environment of their
choice.

You end up with your developers all having environments that are slightly different
due to choice of source for packages or preferences on versions of components. I have
PHP 5.3.8 via a custom Homebrew recipe while one of my co-workers has the stock
version of PHP that comes with OS-X Snow Leopard. He has a version of MySQL that is
two versions ahead of mine. See how easy it is to get out of sync?

You have two options. The first one is the draconian one, where you force everyone
to use the same operating system and the same tools to minimize the chances of 
conflicts between development environments. Given how that leads to developer
unhappiness, I prefer a more sane approach: use tools like [VMWare](http://www.vmware.com) or [VirtualBox](http://www.virtualbox.org) to
let your developers do their work on identical virtual machines while giving
them the freedom to use the development and debugging tools of their own choosing.

Also, by using a virtual machine you can encourage developers to push the envelope
and test destructive things like library upgrades or database changes. Messed it up?
Just fire up a new virtual machine and try again. When you combine it with good
version control practices you should be able to recover from your mistakes even
faster.

Just make sure to take the time to create virtual machines that are as close to
an exact match as your production systems as you can. Honestly, the only difference
between your development environment and your production environment should be the data
your application is manipulating. It's not really that hard to even create
a cluster of virtual machines on your own computer to simulate an architecture
that has application servers, a database server and a memcached server.

It also helps you to get new developers up to speed quickly. "Oh, working on 
Project Alpha? I'll email you the link on the wiki where you can download
the virtual machine for that project." 

Check out [Vagrant](http://vagrantup.com) for a great option for developers
wishing to do their work in a virtual machine.

So, having injected some structure into your development environment there is
really one last frontier where infrastructure debt builds up like the
credit card bills of a shopaholic: deployment processes.

I really think there is one rule: if you cannot do your deployments with one
command then you are DOING IT WRONG. If you can type the commands you are 
doing into a shell then you can script them so you don't have to type
them in again. If you can script deployment, then you can automate
deployment. If you can automate deployment then you now have a consistent
and repeatable process that will behave the same way every single time
you deploy.

At [Moontoast](http://www.moontoast.com) we have automated deployment in place.
When we merge code into our staging and production branches, a version control
hook triggers our deployment tool. It checks out our code into it's proper
location on the production server. It runs database migrations that need
to be done. It starts and restarts various services that are used by the
application. In short, it does everything that I see far too many of my
colleagues doing manually. Stop that. Clean up your infrastructure debt
by making the process of deploying your code a non-event. 

If you want to automate your deployment process, examine tools like 
[Capistrano](https://github.com/capistrano/capistrano/wiki) or [Phing](http://www.phing.info/trac/)
or you could even use a tool like [Jenkins](http://jenkins-ci.org) and use
it's concept of Builds to automate the process of taking your latest code
changes into production.

Note that I said the PROCESS, because technical debt might mean that your
application is fragile enough (doesn't have enough tests and/or test coverage)
that the changes you made might cause it to behave improperly or even crash
the system altogether. Not a good feeling, so by investing the time into
automating your deployment process you can eliminate at least one headache.

I think the main point I am trying to get across with respect to infrastructure
debt is that you really need to examine your processes beyond just coding. 
If you find yourself constantly fighting the "works on my computer" battle, 
you likely have serious infrastructure debt. If you find yourself constantly
referring to a checklist whenever you do a deployment, you likely have serious
infrastructure debt.

Whenever I bring this topic up, I hear many of the same excuses that I hear
when I advocate a commitment to writing tests and automating the execution
of those tests. What is it that people have against this sort of thing?

I have found that people terribly underestimate the amount of manual work they
do to accomplish a task. For many, it is a fear of losing control that leads
them to conclude that automated deployment cannot be trusted, or that 
developers shouldn't have the freedom to pick the tools that they use to 
build their applications. 

Technical debt is real, make no mistake. But so is infrastructure debt. Just like
the cost of finding bugs in production is more than finding them in development,
the cost of fixing infrastructure debt gets more and more expensive. Just think
of the large number of problems solved by eliminating inconsistencies between
development environments. Add to that the ability to eliminate user error
during manual deployments of your application. Why would you not want to have 
this? 

The decision to start paying down your infrastructure debt is not an easy one,
because it will often require many changes to be made by many people. Most
programmers are creatures of habit and dislike change, even when it is 
obviously better. Don't be scared of change, be scared of the debt growing
in your code base and in your infrastructure. It won't go away and
there is no government bailout on the way to fix it.

As always, I welcome your thoughts via email, Twitter and comments on this blog. 
What sort of infrastructure problems have you come across and how did you fix them? 

 
