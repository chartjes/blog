--- 
layout: post
title: The Upcoming PHP Framework War
---
(Wow! Two posts in one day!)

There is a great blog posting by Jared White where he is talking about <a href="http://www.theideabasket.com/2006/05/17/winning-the-php-5-framework-wars/">Winning The PHP 5 Framework Wars</a>.  He brings up some very valid points (mainly that there will be no winner because adoption of PHP 5 has been so slow.  In some of the comments for that post (both on his blog and at php|architect magazine's linking to the article) comes the idea of why does there have to be a war and that there is plenty of room for everyone.  I used to think that way but have come to the conclusion that there can only be ONE dominant framework for a programming language.

In theory the idea of "there is plenty of room for everyone" sounds nice when it comes to frameworks.  The reality of the situation is that one dominant framework is needed to drive things forward.  The more frameworks there are, the more people are having to "reinvent the wheel" in order to make their stuff work.  More cycles wasted redoing work that other people (usually smarter than you, which is a good thing) have already done and made stable and made easy to use.

Look at Rails as an example.  Rails is not the only framework that works with Ruby but it is by far the dominant one.  That enables Ruby developers who want to do web work to stop worrying about nuts and bolts and instead start worrying about fine details.  I came to this realization when I started using Rails for some hobby projects.  I still do PHP at the day job and don't intend on stopping.  But there are just too damn many PHP web frameworks out there and it's impossible to pick one.  I'm betting that the Zend Framework becomes the Rails of PHP (meaning the dominant web framework for PHP 5) and the rest of us can get on with applying finishing touches instead of building from scratch.

The pragmatic approach to programming extolls the virtue of Don't Repeat Yourself and You Ain't Gonna Need It.  What does this have to do with frameworks?  Unless you have huge amounts of spare time I can't imagine why you need to create Yet Another Framework, unless you are trying to learn how to create one of these things.  I thought about it.  Then I realized how much I enjoy sleeping.  To me, creating your own framework smacks of both DRY and YAGNI.

Now, before you think I'm an arrogant person or just deluded, hear me out:  there is nothing wrong with taking something that someone else has created and changing it to suit your needs.  Let's be honest:  the number of projects that are <strong>so</strong> different and <strong>so</strong> unique that they require a totally written-from-scratch solution are really slim.  It's only developer arrogance (and often developer ignorance) that says you can't take something that someone else has done and make it work for you.

As far as I can tell there are three types of frameworks any web-based programming language needs:

1) One that a beginner can use to get a site up and running quickly.

This is Rails.  A programmer experienced in other languages can get a Rails site up and running pretty quickly.  The <a href="http://www.ibl.org">IBL website</a> took my about a month to do working in my spare time and building off an existing application, a blogging app called <a href="http://www.typosphere.org">Typo</a>.  There is nothing like this for PHP yet.  Yes, Cake and Trax (I think it's called Trax) are very close to this by copying Rails and I think that the Zend Framework is also aiming to be helpfull this way.

2) One that an intermediate programmer can use because they understand what the hell they are doing.

I would put the Zend Framework in there too, moreso than in the beginner camp.  ZF is for PHP developers who understand the concepts behind building a web application.  They know about MVC, they know how to build applications of moderate complexity.  A good framework of this type gets all the details out of your way so you can just build the damn thing.  You don't have to worry about database abstraction or templating or even program flow.  It gives you the structure you need.  Like little children, programmers need structure as well and a framework forces you to do things a certain way.  I know that Rasmus Lerdorf hates framworks, but most of us non-savant developers desperately need the structure that a framwork gives you in order to save ourselves from debugging and maintenance hell.

3) Custom solutions that require a great overall application architectural solution.

This is, of course, the place where frameworks fear to tread.  Ookles.  Wikipedia.  Hell, even the dating site I used to work on is in here.  When you get to a certain level of traffic on your site you can no longer use off-the-shelf solutions and you are forced to create completely custom solutions.  No web application scales up to huge levels without undergoing serious changes.  I listened to a great interview with the head of Ookles and everything he talked about is what I encountered while working on the dating site.  Makes me appreciate even more that the dating site worked as well as did during my time there.  Perhaps I'm just too critical.

So, if we stray back to the topic of the post I can try and wrap things up.  The upcoming framework war in PHP is also the battle to push PHP 5 to where it needs to be.  The structure that a framework provides will create a group of developers who all speak a common langauge and understand how to accomplish the same thing.  Yes, the rugged independants will scorn frameworks or even show us how to push them to their limits.  But pushing your skills to their limits is the best way I know of to get better.

Pay attention to the Zend Framework because it has the type of community around it that is determined to see good ideas pushed forward.  Already the calls for "when will it be production ready" are coming on the mailing list.  Me, I wouldn't use it for production stuff yet because there is much that will change.  For small side projects, I heartily endorse it's use if you're doing PHP stuff.
