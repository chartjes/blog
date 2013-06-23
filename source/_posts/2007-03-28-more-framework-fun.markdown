--- 
layout: post
title: More Framework Fun
---
<p>Sometimes you make a blog post that generates a lot of feedback.  In this case, Nate from CakePHP had a vigorous conversation with me via IM about my blog posting <a href="http://www.littlehart.net/atthekeyboard/2007/03/23/in-spring-time-a-not-so-young-php-programmers-mind-turns-to-frameworks/">about frameworks</a>.  In a nutshell, Nate took issue with my comment that CakePHP isn't quite there yet because you can't use components from it outside the framework itself.</p>
<p>
Nate does have a point here.  Zend Framework is perhaps being *overly* ambitious by not only providing an MVC component, but you can use parts of it outside that MVC component as long as you place the Zend Framework itself in your path.  So is Zend Framework truly a framework?  Yes, as long as you understand that a web application framework means more than just a MVC-based framework.
</p>
<p>
At this point, CakePHP is an MVC-based framework only.  That is changing (remember my interactive console project?), but Nate's argument was that perhaps Zend Framework is unfocused and should be concentrating on the MVC part of the web application problem.  Not to mention the fact that it still doesn't have an Active Record implementation for database access.  This particular thing baffles me, but what can you do?  Zend_Db_ActiveRecord (or whatever you could call it) wasn't a priority among the core developers for Zend Framework.  I still can't believe that I have to write SQL by hand with Zend Framework, when I have all those magic methods available to me in CakePHP.
</p>
<p>
Which brings me around to another point.  A disproportionately large number of successful open-source projects are the creation of one, very talented, egomaniacal developer.  David Heinemeier Hansson is a great developer (and has a big ego from what I've seen, heard and read about him) and still is one of the main driving forces behind Ruby on Rails.  Without him being there at the beginning, deciding on the core features and rejecting anything he didn't like, who knows how Rails would've ended up?  One of the toughest things to do is to say "no" to someone when they ask you for something.  Not many people can do it.  It's an especially important skill to have as a developer, because adding in features when they don't really add anything of value is the kiss of death for an application</p>
<p>
So, as a result of this sort of "cult of personality" that surrounds open source projects (or any popular project) you get people initially choosing projects based on the recommendations of others, not on the merits of the project itself.  Why pick Zend Framework?  It's rich in libraries, backed by a large well-known company in the industry, and has many talented contributors (including yours truly).  But *why* use it for your particular project?  Biggest flaw right now as I can see it is (beating a dead horse here today) lack of an ORM database wrapper.  Again, CakePHP has one so it can't be *that* hard to implement such a thing.  I know that <a href="http://pixelated-dreams.com/">Davey Shafik</a> has created such a beast for Zend Framework...but it's nowhere to be seen in ZF 0.91 beta and likely ZF 1.0.  C'mon, cut Davey a break and ram it in there.
</p>
<p>
So, at this point, CakePHP is probably better suited for building an MVC application, despite the lack of libraries that Zend Framework provides that CakePHP does not.  On the other hand, a decent programmer should be able to quickly implement such things themselves, right?  So, for MVC-based apps that I need to build in a hurry I'm going to pick CakePHP.
</p>
<p>There, Nate.  You happy now?</p>
