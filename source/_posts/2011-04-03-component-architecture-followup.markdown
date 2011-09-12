---
layout: post
title: Component Architecture -- Follow-up
---
After posting my thoughts on
[component architectures](http://www.littlehart.net/atthekeyboard/2011/03/31/component-architecture)
I asked Stu Herbert to provide me with any comments he had on this
particular topic, having been the original inspiration. He was kind
enough to do so and I have extracted some of his thoughts and
weaved them into this post along with some other thoughts I've
had.

First of all, I did a
[facepalm](http://en.wikipedia.org/wiki/Facepalm) when I realized
there were things I wanted to talk about in the original post that
I had missed. In his presentation at PHP UK Conference Stu pointed
out that PHP has not made the commitment to reusable components
like the other major scripting languages used currently for web
development, Ruby and Python. Ruby has it's excellent
[Ruby gems](http://en.wikipedia.org/wiki/Ruby_gems) system to allow
the installation and distribution of components written in Ruby.
Python has two solutions that I am aware of in
[EasyInstall](http://en.wikipedia.org/wiki/EasyInstall) and the
[Python Package Index](http://en.wikipedia.org/wiki/Python_Package_Index).
They both serve the same purpose: allowing the installation and
distribution of 3rd party components. In PHP
[PEAR](http://pear.php.net/) is the system we should all be using
for doing this. The reasons why are interesting, and I'd like to
share my thoughts before we see what Stu had to say.

It seems to me that the difference between PEAR and the solutions
offered in Ruby and Python can be thrown into one of two piles:
cultural and technical. On the cultural side, both Python and Ruby
have encouraged developers to use these 3rd party systems as the
primary means of distributing code. I think if you look at the
popular components available in something like Rails, I think you
would be hard-pressed to find one that did not exist as a gem. My
early experiments with Rails back in 2004 made me think that the
gem system was the perfect way to handle it. Sure, you can end up
in dependency hell trying to figure out what gems go with what
other gems, but I do not think there is ever an easy solution to
that problem.

When you look at the technical issues, this is where I think PEAR
breaks down. As far as I can tell, to make your component available
to install with PEAR you have to create your own PEAR channel.
What? Really?!? Am I the only one who thinks that this is an
unnecessary limitation? When I added
[Djaml](https://github.com/chartjes/djaml) to PyPi, all I had to do
was create two metadata files in a specific format and then push it
up to PyPi using tools that are provided by the same CLI utility
you install other packages with. Bingo presto, my package was now
available to anyone who wanted to use it. I didn't have to set up
my own channel. To me, this the main reason why PEAR is not the
dominant installation tool that it should be.

In a perfect world I would like to see all the major PHP frameworks
make themselves available via PEAR as their main method of
distribution. Wishful thinking, I know.

Okay, so now time for us to hear from Stu:

> Your question "how do you decide what stuff can be extracted out
> and built into a component?" merits more than just an email ... I'm
> sure this is a conference talk / tutorial day topic in its own
> right :) Would you say that most developers could recognise a
> component if they saw one? \* Clearly-defined purpose \*
> Clearly-defined API \* Clearly-defined data structures \*
> Separation of concerns \* Reusable \* Re-installable on multiple
> computers \* Replaceable / substitutable
> 
> But seeing one when designing (or refactoring!) software is
> something fewer PHP developers have had the opportunity to
> practice?

Stu is, of course, absolutely right. It is impossible to extract
code into a reusable component if you don't even know how to
identify it. Like many, MANY skills in programming, the ability to
refactor and extract code is a skill that needs to be cultivated
and learned. I myself have run into this many times during a coding
session while refactoring. Does this sound familiar?

-   implement some functionality
-   get a request to add something
-   realize that the new request is similar to something you've
    already done

The trick is realizing that the next step in this chain is not
"cut-and-paste the previous functionality because we supposedly
have no time". The next step is to extract that functionality into
something that can be re-used. Usually this in the context of the
application itself (ie extracting that code into a helper method if
you're using a framework) but it is worth thinking about how to
make that a component that can exist OUTSIDE of the application
itself.

More from Stu:

> I think you hit the nail on the head towards the end of your
> article, when you started talking about services. A component could
> be defined as being: \* a self-contained set of code \* that
> provides a reusable service \* to a larger body of code \* by being
> aggregated into that code
> 
> This differentiates it from a service-oriented architecture in one
> crucial detail: a component runs as part of your app - same address
> space, same process ID - whereas a service runs outside your app,
> and is contacted either locally via IPC or remotely via
> networking.
> 
> But none of that helps the first-time component writer, I fear!
> This is big-picture stuff, or perhaps better described as 20/20
> hindsight stuff - things that developers can only see after they've
> learned how to do it :) What they need is their first step to
> making a component - an additive process that builds on that first
> step until components are as natural a strategy as factories, DI,
> and the like. This is very similar to how one teaches martial arts,
> where we start from the floor (how a fighter stands, how they step)
> and work upwards.

Stu goes on to share some super sekret info with me surrounding his
plans in this area and I look forward to seeing them come to
fruition. Thanks Stu!

