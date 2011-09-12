--- 
layout: post
title: Glue vs. Full Stack
---
<p>[Note: looks like the move to the new server will take some time as I configure things *just so* so blogging can continue]</p>
<p>
So I'm sitting around thinking about how I'm going to build out the new rallyhat.com, turning it into a "plan a baseball road trip site" and figuring out what tech to use.  To be honest, I've gotten kind of bored with Ruby on Rails for a few reasons.  One is that I understand the tech behind Rails, and don't agree with a lot of the magic methods that Ruby seems to be encouraging.  I like to sort of understand what's going on rather than being told "just do it this way".  I don't understand Ruby enough to wade into the source for Rails and figure things out.  Secondly is that I haven't touched any Rails code in months, so any momentum I had has leached out.</p>
<p>So, I like to learn new languages because, well, it makes me a better programmer.  I've spent my time this year learning my way around Javascript so I can get a firm grip on just how all this Ajax stuff is supposed to work.  Now I'm glancing over at Python and trying to decide if I want to invest in learning Python so I can try out Django, a web application framework that gets lots of nice things said about it.  Not as flavour-of-web-pi that Rails has become, but a solid, well-documented web application framework.</p>
<p>
So naturally I do some research and found an interesting post about <a href="http://jesusphreak.infogami.com/blog/vrp1">Python web development frameworks</a> that talks about Django vs. Pylons vs. Turbogears.  Very interesting reading and it convinced me that Django is the way I should go if I'm going to become a snake handler on this project.  But I followed some other links and got to a page (can't find it now of course but I remember it) where there was a discussion of glue vs. full stack frameworks.
</p>
<p>
A glue framework provides you with a bunch of components that you can use together, but don't necessarily have to.  Zend Framework is a PHP glue framework, as it comes with all these cool components that you can pick and choose depending on what you need done.  You're not forced to use them, and this appeals to certain programmers who have fallen in love with their own quirky set of libraries and methodologies.  This used to be me.  To shift this over to Python, since I know no Python at this point i would be pointless to go with a glue framework.
</p>
<p>
A full stack framework gives you everything you need to create your web app, and pretty much forces you to use it.  <a href="http://cakephp.org">CakePHP</a> is a full-stack framework.  It has a bunch of conventions, and you must follow them or die.  Okay, maybe you won't die but your application will never work properly if you don't understand the conventions.  Django is a full-stack framework.  So, given my knowledge level of Python I think that would be my safe choice.
</p>
<p>However, I have the Imp of the Perverse mumbling into my ear that I should just build the damn site, screw Python because we're tying to get something done here.  So I'm thinking that I need to put my money where my mouth is, and build in CakePHP.  After all, I have that cool interactive console to test stuff with.
</p>
<p>
So, give me some feedback:  which do you prefer when building an application? Full stack or glue?</p>
