--- 
layout: post
title: The Scary Future World I Will Program In
---
<p>
A lot of the reading I have done on the Internet in the last few years has led me to the following conclusions about the future world I will be programming in:
<ul>
<li>It will require manipulating exponentially more data than now</li>
<li>It will require you to understand both parallel processing and concurrency (although to this simple programmer's brain they appear to be the same thing</li>
<li>A stateless model of the web looks more and more like something that works against human nature</li>
</ul>
</p>
<p>
I have become fascinated with languages that talk about dealing with concurrency:  <a href="http://ftp.sunet.se/pub/lang/erlang/index.html">Erlang</a>, Python using <a href="http://twistedmatrix.com">Twisted</a>, <a href="http://clojure.org">Clojure</a>, and the newest kid on the block <a href="http://golang.org/">Google Go</a>.  I have no idea why these interest me so much.  But I find them all fascinating, and I wonder how anything we do at work on the XML-feed-parsing side could benefit from concurrency (and that gets me into the topic of whether or not concurrency matters if you have to write data to a relational database and dealing with locks etc, god I sound like a programming nerd!).
</p>
<p>
Rich Hickey, the creator of Clojure, gave this <a href="http://www.infoq.com/presentations/Are-We-There-Yet-Rich-Hickey">awesome talk</a> about current programming language paradigms and how well suited they are to the highly statefull, concurrent future that I feel we will be facing when building online applications.  Go and watch it and you will find that you knew oh so very little about programming language concepts.
</p>
<p>
So not only are we dealing with concurrency, we also need to deal with state.  PHP is stateless.  "Share-nothing" was a revelation for it's time, and allowed you to build web applications that could horizontally scale quite well.  But then we started requiring state.  So we use things like sessions, and cookies:  tricks that allow us to let data persist between requests.  You could almost throw databases into that category.
</p>
<p>
Perhaps this is ignorant rambling.  All these things make it harder and harder for a statefull environment like the web to act like it is actually retaining values between requests.  Maybe something like <a href="http://en.wikipedia.org/wiki/Seaside_(software)">Seaside</a> is a model to look at it:  it preserves state across requests using continuations, which is a programming concept that you just don't learn when you teach yourself PHP.
</p>
<p>
You could argue that we are on the verge of a major shift in programming language methodologies.  The challenge of programatically handling concurrency and state in a way that programming trolls like me can understand is a huge one.  Tim Bray has been covering this on his blog via his "so fascinating it makes me understands how stupid I really am" <a href="http://www.tbray.org/ongoing/When/200x/2009/09/27/Concur-dot-next">Concur.next</a> series.
</p>
<p>
Will we ever have a statefull, concurrent language for building web apps.  I'm sure we will.  I just don't think it's been written yet.
</p>
