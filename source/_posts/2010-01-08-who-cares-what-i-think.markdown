--- 
layout: post
title: Who Cares What I Think?
---
<p>So we're at a natural point for reflection.  It's the start of a new year *and* the start of a new decade.  Despite my wife rolling her eyes talking about this, it is an incredibly exciting time to be involved in web development.  Internet time is like dog time, in my opinion: one year online is seven years in the real world.  Of course, this is a gross oversimplification.  But I think it's accurate nonetheless.
</p>
<p>
So as we start 2010, and you're a web developer, what is out there for you to play with?  Let's see...
<ul>
<li>Mature web application frameworks for the Big 3 open source scripting languages (PHP, Python and Ruby) that can help you, when used properly, rapidly build applications, if you are willing to spend the time understanding the limitations of frameworks.  You might hate frameworks, but you certainly cannot ignore them.  Yes, you could consider WordPress itself to be a framework</li>
<li>Multiple languages that will run on the JVM that can be used for web development, if you are willing to spend the time understanding the JVM and how to get these things talking to Java as well.  Ignore the Java haters, I think this is a good trend.</li>
<li>Multiple actually-usuable-outside-of-small-projects alternatives to RDBMs, if you are willing to spend the time to figure out when you should use them.  The trend is towards having ridiculous amounts of data, and it appears that in the open source world the RDBMs is not up to the task.  Think <a href="http://incubator.apache.org/cassandra/">Cassandra</a>, <a href="http://code.google.com/p/redis/">Redis</a> and <a href="http://hadoop.apache.org/">Hadoop</a> along with <a href="http://hadoop.apache.org/pig/">Pig</a>.</li>
<li>multiple mature Javascript libraries that make creating all that awesome Ajax goodness easy, if you are willing to spend the time to pick one with the features you like</li>
<li>multiple mature (or soon-to-be mature) functional programming languages that can be used to build web applications, if you are willing to spend the time to learn functional programming.  I mean, really, how can you not look at <a href="http://clojure.org/">Clojure</a> and <a href="http://ftp.sunet.se/pub/lang/erlang/index.html">Erlang</a> and not be impressed?</li>
</ul></p>
<p>
But again, who cares what I think?  If you do care, then you are at the same place as me:  paralysis by analyses.  What framework should I pick?  Do I go document database or key-value store?  If I don't want to learn Java, can I do some stuff with <a href="http://www.scala-lang.org/">Scala</a> or see if <a href="http://www.jython.org/">Jython</a> is up to the task?  Can <a href="http://www.jquery.org">jQuery</a> do long-polling / comet stuff?  Is functional programming too weird for a web monkey like me to figure out?
</p>
<p>
Crap, that's a lot of stuff to worry about, isn't it?  Is it any wonder I get stressed out trying to figure out how to build stuff at work?  Or what stuff to dabble with in my spare time?  We are suffering from an embarrassment of riches, which is being hidden by the constant religious wars that developers seem to get embroiled in.  If it's not "my language is better than your language", it's "my editor is better than your editor".  "My programming paradigm is better than your programming paradigm."  "If you did interesting work, you'd get accepted to speak at conferences more".  (Sorry, that was me arguing with myself).
</p>
<p>
If anything, I have found that my focus is starting to change.  I've started realizing that what is really happening is that despite there being ridiculous amounts of choices of tools to solve problems, it has become EASIER to solve these problems.  In my planning for a work project I stumbled across the now-infamous <a href="http://toys.lerdorf.com/archives/38-The-no-framework-PHP-MVC-framework.html">Rasmus Lerdorf "The no-framework PHP MVC framework" blog post</a>.  While Rasmus is a programming god, he is also a very smart guy.  He understands that programming is about solving problems, and he (at least to me) seems to not have the ego that says you must build up your own complicated solutions to problems.
</p>
<p>
This has gotten me to consider how I had been approaching problems.  Too often, I have been approaching them from the code out to the display.  Worrying about the technology, instead of how people will use it.  Rasmus proposes an easy problem - a sample Ajax app that uses exactly 4 things: a scripting language, a Javascript library, a data storage source, and a data exchange format.  In his specific example he used (in order) PHP 5, Yahoo YUI,  sqlite and JSON.  You could've done this with Python, JQuery, MySQL and XML.  Or Ruby, Dojo, CouchDB, and JSON.  My point is that we often find ourselves caught up in what we are USING to build something rather than solving the problem.
</p>
<p>I have really dislike the idea of New Year's resolutions, because they are almost always broken.  But in this case, I think a few are warranted:  this year I resolve to do a better job of figuring out the problem I need to solve first and worry about the technology needed second.  Sometimes my desire to feed the part of me that wants the new and shiny takes control and creates a potentially bad solution.  Sure, it would be awesome to get paid to learn a new programming language and a new web application framework to go with it, but if it gets in the way of solving the problem, well, you've suddenly become the problem instead of the solution.  Sounds so cliched, doesn't it?
</p>
<p>
So, in the spirit of that, let's look at 3 problems I need to solve in the next little while that I perhaps can also use to feed the Imp of the New and Shiny:
<ul>
<li>Analysis of some MySQL slow-query logs are needed at work.  First solution was to play with a tools specifically for analyzing the slow query log.  They provided summaries that were simply not useful to me. Perhaps Pig + Hadoop will give me the high-level solution to collect the information we seek.</li>
<li>I have a very simple idea for collecting absurd stories you've told to your kids.  My first instinct was to create the project using a web application framework.  Upon reflection, perhaps the combination of WordPress and then a custom-written story submission and approval system is the better approach.</li>
<li>Plans are being made to create the next platform our company will use for online fantasy games.  Since we cover multiple sports, I have no desire to create a separate version of the platform for every sport.  Instead, inspired by the realization that Rails is nothing more than a DSL (or Domain Specific Language) on top of Ruby, I have started work on a very simple DSL for defining scoring rules.  Wouldn't it be awesome for the games admin to be able to select a stat category for a sport (say, rushing yards in football) and then use "(1 point each 10) + (5 at 100 total)" as the scoring rule?  Parsers are actually pretty easy as long as your DSL is consistent.</li>
</ul>
</p>
<p>
I hope I've made sense here, as I'm trying to show how I wish to change my approach to solving programming problems.  There is no doubt that I will pick up the new and shiny as I find a way to solve these problems.  Some might be written in PHP.  Some will be written in Python.  Some will be written in ScoreRule (to pull a name for my sports DSL out of my ass).  But the real winner is the people who will use these things.  Shhh, don't tell anyone:  I'm thinking about the end user for once instead of the programmer.
</p>
