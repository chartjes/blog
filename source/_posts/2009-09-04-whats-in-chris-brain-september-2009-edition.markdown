--- 
layout: post
title: What's In Chris' Brain - September 2009 Edition
---
<p>I've been feeling a little blogged-out lately, as work is ramping up on a project with some critical milestones to be met, and the stress of getting my basement lair all renovated for occupation after Labour Day.  But the mind never stops working.  Here's two big things that have been occupying my thoughts:
</p><p>
<h3>The arrival of PHP 5.3 and it's impact on frameworks</h3>
</p><p>
When I upgraded my MacBook to Snow Leopard I noticed that it comes with PHP 5.3 as part of the standard install.  After I got finished fixing my <a href="http://www.macports.org">MacPorts</a> install that I somehow butchered while following two different sets of instructions (way to go Chris), I was not at all surprised to find out that the <a href="http://codeigniter.com">framework I shall not say out loud</a> did not like running with PHP 5.3.  Tons of deprecation warnings abounded, and I had lost my enthusiasm for figuring out how to make them go away.  If anyone cares to tell me, feel free to add it to the comments as I would prefer to run 5.3 on my laptop.</p>
<p>
As far as I can tell, <a href="http://framework.zend.com">Zend Framework</a> is the only framework that is claiming <a href="http://www.zend.com/en/company/news/Press/zend-framework-features-php-readiness-and-new-professional-components">that it will run just fine in PHP 5.3.</a>.  Although I cut my teeth so-to-speak with <a href="http://www.cakephp.org">another framework</a> that has been good to me (hey, <a href="http://www.littlehart.net/book">buy my book to see why</a>, I cannot but remain impressed that a production-ready framework is ready to go with PHP 5.3.
</p>
<h3>Finally figuring out Design Patterns and how they relate to refactoring</h3>
<p>
In <a href="http://www.codersatwork.com">Coders At Work</a> Brandon Eich talks about how Peter Norvig once said (I'm paraphrasing here) "a design pattern shows a flaw in your programming language".  As I'm expanding functionality for <a href="http://www.sportso.com">a project at work</a>, I am starting to wonder if it's maybe time I really looked at them closely.  I see myself doing certain things in my code and wondering if there is an easier way to do them.  You know, the same sort of if-the-else comparisons, having to do the same thing but slightly differently inside a method.  Some of these are <a href="http://en.wikipedia.org/wiki/Code_smell">code smells</a>, but I am wondering about what's the best way to approach refactoring them.
</p>
<p>
Of course, you always have to consider the environment in which your code lives.  Since I'm using a framework, there are rules I have to follow.  Most of the time, these rules are okay.  Other times I find myself fighting against them a tiny bit, which shows that maybe I need to go and buy the <a href="http://www.amazon.com/Refactoring-Improving-Design-Existing-Code/dp/0201485672/ref=sr_1_1?ie=UTF8&s=books&qid=1252100204&sr=8-1">seminal classic on refactoring</a> and read it.  Maybe one of my generous readers would send me a copy?
</p>
