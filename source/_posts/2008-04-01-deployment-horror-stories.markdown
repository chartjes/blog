--- 
layout: post
title: Deployment Horror Stories
---
<p>I was going to do a rant today in honour of April Fools' day, talking about how much it frustrates me to no end that people prefer complicated explanations for their bugs:
<blockquote>
Them: "I notice that module X is no longer working when I moved from BloatOS to TinyNX, and my framistat widget is now displaying stars instead of being in plain-text.  Why is the component doing that?"
Me: "Dude, that component doesn't just magically stop working because you're on TinyNX.  Are you using the same version of FooWorks in both environments?"
Them: "I think so."
Me: "Don't f*****g THINK so, MAKE SURE".
Them "But it was working just fine..."
Me:  "SILENCE!  I'll bet you the balance in my savings account that you are using the star framistat widget on TinyNX and the two code bases aren't the same"
Them: "Oh, will you look at that...somehow an older intermediate version of the code using the star widget was deployed on the TinyNX version"
Me: "You owe me lunch"
</blockquote>
People, people, people.  Weird problems almost ALWAYS have a simple solution.  But enough about how smart I think I am, back on topic.
</p>
<p>
I've started working on my presentation I'm giving in two weeks.  Oh, don't worry, I know what I'm going to say but I just need to create the slides that results from it.  Part of the presentation is pointing out some deployment horror stories and how they could've been avoided.  If you can swallow your pride and share some of those stories with me, I'd appreciate it.  I will start off with one of my own.
</p>
<p>
Back when I used to work for an adult dating website, we built a database abstraction class that passed all data modification statements to our master database server...via HTTP.  Yes, we wrote code that listened for a string to be sent to it and then executed the code on the server.  I don't have the time or the patience to explain how this decision was made, but there it was.  We were lead to believe that MySQL replication at the time (this is 5 years ago) was in 'milliseconds' so we thought we were okay dealing with the very large number of updates that would happen to the master, and then being replicated to the 7 to 8 application servers we had running at the time.
</p>
<p>
That was until we found out that replication is slow, and some machines were up to 30 minutes behind on processing the replication requests.  Holy shit.
</p>
<p>
The solution was to decide what requests could be done later, and creating a queuing system for processing those delayed requests.  Apparently this same system is in place today, despite the current software architect's desire for switching things to a clustering or sharding scenario for the data.  Since the site is so dependent on people signing up for paid accounts, nothing is allowed to be done that can disrupt the site when deploying changes.  Best of luck with that.
</p>

