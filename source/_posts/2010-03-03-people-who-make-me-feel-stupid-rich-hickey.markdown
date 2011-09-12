--- 
layout: post
title: "People Who Make Me Feel Stupid: Rich Hickey"
---
<p><i>This is the third in a series of blog posts where I talk about people who's skills as programmers make me feel stupid.  Check out my thoughts on <a href="http://www.littlehart.net/atthekeyboard/2010/03/01/people-who-make-me-feel-stupid-geoffrey-grosenbach/">Geoffrey Grosenbach</a> and <a href="http://www.littlehart.net/atthekeyboard/2010/03/02/people-who-make-me-feel-stupid-antirez/">Antirez</a>.</i>
</p>
<p>
As a person who learned the hard way about how tough it is creating web applications that can handle state and concurrency  issues (if you've ever seen MySQL replication lag times as high as 30 *minutes* you can sympathize), the rise of languages designed from the ground up to support concurrency has caught my eye.  If you've heard of <a href="http://erlang.org">Erlang</a> or <a href="http://www.haskell.org/">Haskell</a> you are somewhat familiar with the topic.
</p>
<p>
Then one day I ran across <a href="http://clojure.org/">Clojure</a>, a language that is a dialect of Lisp but runs on the JVM.  My, my, what in interesting combination.  I've talked about Clojure before, but I have not talked about the amazing person behind it, <a href="http://en.wikipedia.org/wiki/Rich_Hickey">Rich Hickey</a>.
</p>
<p>
The idea of <a href="http://createyourproglang.com/">creating your own programming language</a> is one that I find extremely intimidating, not having a formal background in computer science.  I have a vague idea of how you would do it:  write parsers for your code and then compile them into byte code that can be run by something.  Very simplistic, I know.
</p>
<p>
So Rich Hickey is a one of these programming gurus who I am sure is a super-nice guy but I would be totally intimidated to have any sort of meaningful programming-related discussion with.  First of all, he's a Lisp hacker.  Some of my friends have described Lisp as "the cockroach of the programming world, which will be around long after the sun of other languages have dimmed" and I can't say that I disagree much with that statement.  For someone who learned to program by teaching himself PHP, Lisp's syntax takes a lot of getting used to.  
</p>
<p>But then I think the best trick was making Clojure run on the <a href="http://en.wikipedia.org/wiki/Jvm">JVM</a>.  Why do I think this is significant?  It means that if there is a feature or a library that doesn't exist in Clojure, you can always use a Java equivalent (if such a one exists).  In Tim Bray's "Concur Next" series he showed an example where he used a Java library in Clojure to help him speed things up.
</p>
<p>
So not only does he have a well-designed and well-thought-out programming language, he is also great at explaining programming concepts.  Go and watch this video on the topic of <a href="http://www.infoq.com/presentations/Are-We-There-Yet-Rich-Hickey">basic principles like state, identity, value, time, and many others</a> in order to understand how to build concurrent and parallel systems.  Fascinating talk, and I highly recommend seeking out other talks that he's done as well.
</p>
<p>
All this stuff is absolutely fascinating to me, because my entire programming career has been spent in the stateless environment of the web.  Oh sure, we can fake state and concurrency using sessions and cookies, but they are really just hacks.  Does a web application need to be stateful and/or concurrent?  The answer is, of course, it depends. ;)  Online games with multiple participants definitely need to worry about sharing state across multiple clients, and any web application that is taking large amounts of data and processing it (like munging it together based on aggregate conditions) could benefit from being able to crunch the data concurrently, with all jobs reporting stuff as they go.  Any task that would benefit from being broken down into smaller tasks that can be run at once is a candidate for concurrency.
</p>
<p>
So, why does Rich Hickey make me feel stupid?  <b>Not only is he also capable of explaining the hows and whys of a concurrent programming language, he is encouraging people to think ahead to the next generation of programming problems and potential solutions to those problems.</b>.  It's highly unlikely I will ever create a full-blown, general-purpose programming language.  But Rich Hickey's work has gotten me thinking about programming in event-driven environments, and wondering what tasks that my current applications perform could benefit from concurrency and parallelism.
</p>
