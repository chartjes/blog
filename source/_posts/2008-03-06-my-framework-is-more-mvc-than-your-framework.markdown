--- 
layout: post
title: "My framework is more MVC than *your* framework!"
---
<p>
I like to check out the <a href="http://reddit.com/r/programming">programming section on Reddit</a> on a regular basis because it usually contains some interesting links.  Yesterday I came across a link that discussed the fallout surround a presentation at phplondon08 where <a href="http://pookey.co.uk/blog/index.php?url=archives/43-phplondon08-the-crazy-guy-mail.html">panelists on a discussion of frameworks got heckled</a> but some guy claiming to be an expert on what a real MVC framework is.</p>
<blockquote>
All major Rails clone PHP frameworks that exist on the market today are a complete and utter failure. All of them call themselves MVC frameworks and none of them implement actual MVC. In fact, some of the worst ones merely resemble MVC, and have no right whatsoever to be called frameworks. Whatever benefits of sexy ORMs and flexible build systems and scaffolding and other secondary tools these frameworks have are nullified by the fact that using them results in architectural chaos which is no better than your usual spaghetti code. This is because the people who wrote Rails didn't bother to understand MVC, and the PHP amateurs who were excited about the idea of getting done more in less time blindly tried to clone Rails into PHP and in so doing not only replicated the stupidity of Rails into PHP but also multiplied it by their own incompetence and PHP's shortcomings as a language and a platform.
</blockquote>
<p>
No, tell us how you really feel about it.
</p>
<p>
Anyhow, this guy apparently works for the <a href="http://agavi.org">Agavi</a> project, a (wait for it) MVC framework written in PHP as an "evangelist".  Well, he certainly talks like you would expect an evangelist too.
</p>
<p>
The comments for that post are really interesting too, as people take their usual swipes at PHP, and CakePHP, and the Symfony guys come out in droves to talk up Symfony, and on and on it goes.  Sadly, this is not a unique occurance on the web.
</p>
<p>
So, back to the topic of the post.  Is this guy right?  Is *nobody* except Agavi doing it right on the PHP side of things?  I took a peek at their documentation.  Lots of statements about what a framework should and shouldn't do.  
</p><p>
<em>(Author's note 03/10/08: removed code example as, well, it's not really relevant to the discussion, other than making me giggle about mixing business logic with presentation logic)</em>
</p><p>
Digging through the documentation some more, it's quite dry.  Short and sweet, not a lot of tips on building an Agavi app from scratch.  Again, to be fair, that might not be the point of the documentation.  But it's approach is very, *very* different from the "Rails way" that CakePHP has been following.  Before you flame, there is nothing wrong with the "Rails way" because, if nothing else, it has forced developers to crank their skills up a notch and actually *think* about what they are building.
</p>
<p>
I knew one of the original developers of <a href="http://www.mojavi.org">Mojavi</a> (of which Agavi is a fork) and he was a really smart guy (Hi Shawn!). My early forays into framework use was with Mojavi, when trying to convince a previous employer that we needed to rewrite this monster PHP application with Mojavi so we could get things like a private branding version of the site done a lot easier.
</p>
<p>When I compare this to Cake, they are as different as night and day.  Agavi (and Mojavi) are heavily configuration-oriented (XML *everywhere* for config files), while Cake uses conventions to try and speed things up.  But the real truth is this:  they are both trying to separate your business logic and your presentation logic to make things easier for the poor saps who have to build these applications.
</p>
<p>
Our lovely heckler has missed the forest for the trees, as far as I'm concerned.  It's like complaining that you can't call it a forest because the trees aren't growing straight up and down, but tend to branch out in different directions.  They're still trees, right?
</p>
<p>Frameworks are designed to try and help you to get things done faster *and* to organize your code in a much more consistent manner.  Cake uses the <a href="http://en.wikipedia.org/wiki/Model-view-controller">Model-view-controller design pattern</a>, and I think that the quote below makes it clear that Cake is doing it the right way:
<blockquote>
Model-view-controller (MVC) is an architectural pattern, which at the same time is also a Multitier architecture, used in software engineering. In complex computer applications that present a large amount of data to the user, a developer often wishes to separate data (model) and user interface (view) concerns, so that changes to the user interface will not affect data handling, and that the data can be reorganized without changing the user interface. The model-view-controller solves this problem by decoupling data access and business logic from data presentation and user interaction, by introducing an intermediate component: the controller.
</blockquote>
If you are trying to tell me that CakePHP does not follow that practice, then I am calling you a fucking idiot who is more interested in pedantic minutiae than understanding that there is more than one way to implement MVC.
</p>
