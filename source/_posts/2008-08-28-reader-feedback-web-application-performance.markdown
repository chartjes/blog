--- 
layout: post
title: "Reader Feedback: Web Application Performance"
---
<p>
<img src="http://www.littlehart.net/images/web-app-development.png"/>
</p>
<p>
Welcome to the 4th and final day of reader feedback week here.  Today's topic is one that comes up over and over and over and over again:  web application performance.  In particular, I wanted to discuss web application performance and frameworks.
</p>
<p>After seeing a slide from a presentation at FrOSCON about CakePHP's performance in the incredibly-unrealistic-and-irrelevant "Hello World" competition against vanilla PHP and other PHP frameworks I came up with that very aggressive statement you see above.  That prompted a flurry of tweets by other people about their thoughts on that matter, and so on and so forth.  I believe my earlier statements were misunderstood, so I shall clarify them here.
</p>
<p>
I stand by the statement "frameworks are about increasing development speed, not application speed".  I've talked about frameworks plenty in the past, and they all promise you this:  if you build things according to their rules (and this is the really important thing to remember) then you will gain a significant increase in application development speed.  If you fight against those rules, why are you even bothering to use the framework?  The goal is to speed up development time by following a set of conventions on how the application is put together.
</p>
<p>
So, if you've had enough courage to build you application with your framework of choice, you should have a working application.  That doesn't mean it is as fast as it could be, but remember the mantra I shared earlier:  "make it work, then make it work better".  Where frameworks typically fall down is in the "make it work better" part of that statement.  <a href="http://www.travisswicegood.com/">Travis Swicegood</a> pointed out to me when it comes to frameworks "...actually, a really good one should have mechanics in place to do both" (referring to increased development speed and application speed).
</p>
<p>
So, if you have a framework that actually cares about application performance (perhaps unfairly some frameworks have decided that performance is sole responsibility of the developer, not the framework itself) then it should come with things to make your application a little more responses.  Things like built-in output caching, or features in their ORM/ADM that cache your schema, things like that.  But in the end, there is only so much you can to make a framework-built application run really fast.  Sometimes you can do it with just the additional features I mentioned above.  Sometimes you can't do it because the architecture you've chosen for your application won't let you.  And sometimes, you can't do anything about it because it's too hard to modify the framework itself.  These things happen.  Look at Twitter and all the contortions they have gone through trying to take what was initially a Rails application and push it's performance up to it's current level.
</p>
<p>
There are also lots of 3rd-party solutions to help you make your application perform better.  <a href="http://www.danga.com/memcached/">Memcached</a> for caching data (ask me some time about my Memached story at an old job). <a href="http://pecl.php.net/package/APC">Alternative PHP Cache</a> if you're running PHP.  <a href="http://www.squid-cache.org/">Squid</a>.  <a href="http://nginx.net/">nginx</a>.  <a href="http://mongrel.rubyforge.org/">Mongrel</a>.  Those are just the ones I can think of off the top of my head.  Some of them are even framework agnostic.</p>
<p>
Having a framework that lets you BUILD things fast and RUN things fast is the perfect situation, but not too common.  I used to get mad when I'd see people asking if <insert framework here> can scale, because I felt it revealed a certain level of ignorance in the person asking the question.  I've now come to the conclusion that what they are really asking is if </insert><insert framework here> can scale without them doing any extra work.  Usually, the answer to that question is FUCK NO (emphasis mine) because scaling is an issue that goes far beyond just a simple framework.
</insert></p>
<p>
See, not every framework is slow.  Some frameworks, due to their internal structure, are faster than others.  I'm okay with that now, not so okay in the past.  In a lot of cases, the bottlenecks in your application aren't code-related.  I've come to understand that too, especially in the new Javascript-driven world web applications have started to run in.  If you think Twitter is slow because they chose Rails, I think that you do not have a firm understanding of how Twitter actually works.  Or maybe you don't care because it's easy to make fun of Rails and Twitter.
</p>
<p>
Luckily, we have lots of free and easy-to-use tools at our disposal that let us look at our up-and-running web application (remember, Just Build It, Damnit!) and see how it's performing.  Things like <a href="http://www.joedog.org/JoeDog/Siege">Siege</a> and <a href="http://developer.yahoo.com/yslow/">YSlow</a> are just two tools that their use will give you huge insights into the actual performance of your web application.
</p><p>
You shouldn't be GUESSING how your application performs, you should KNOW what is going on.
</p>
