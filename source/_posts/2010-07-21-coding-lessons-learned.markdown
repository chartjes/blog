--- 
layout: post
title: Coding Lessons Learned
---
<p>In discussions with my friend <a href="http://chiggsy.com">Kevin</a>, I have come to realize that we have arrived at the same conclusions about the use of <a href="http://en.wikipedia.org/wiki/Web_application_framework">web application frameworks</a>.  Much of these conclusions have driven from 12+ years in building applications using them, with various rates of success.  Suffice it to say, only the most l33t programmers out there are using their own frameworks, be it a custom one or contributing to the creation of an open-sourced framework.  Everyone else is like me:  a user of frameworks, and extremely rare contributor back to those frameworks.
</p>
<p>Since Kevin and I are travelling together through the world of <a href="http://python.org">snake handling</a>, we have been looking at the available options for building web applications in that environment.  Our conclusions have been surprising to ourselves, but I think they can be very instructive to others.   These two lessons are applicable to other programming languages as well, so feel free to substitute your favourite language where applicable.
</p>
<h3>Lesson 1: Full-stack gets you in the door, lightweight lets you find your niche</h3>
<p>
If you want to learn Python for the web, the first place you go is <a href="http://djangoproject.com">Django</a>.  It is a full-stack solution for building things in Python.  Awesome documentation, and with some help from Python's online documentation, you can build an app in a reasonable time frame without knowing a ton of Python.  Awesome tutorials and code samples FTW!  I have built a Django app and briefly made it public.  It was, like so many other things, a piece of crap missing functionality so I am trying to rectify that in my ever-dwindling spare time.   I did not find any serious obstacles to building this app, except for figuring out how to do some dynamic form-field-generating code.  It took me a while to find the right info (amazing how having the correct keywords in your search helps) but I did.
</p>
<p>
As an old warrior of frameworks (10 and counting across 3 languages) I found that because I already understood the concepts behind MVC (or MVT in the case of Django) I could concentrate on learning Python first, and then the unique features of the framework after that.
</p>
<p>
In many ways, my early experiments with Rails (back in 2004-2005) helped me understand frameworks a lot better.  All frameworks have their own magic methods for doing things, with Rails making heavy use of Ruby's ability to create Domain Specific Languages to make Rails the incredibly useful framework that it is today.  But eventually, your skill with the language and the framework gets to the point where you see the limitations of the conventions and magic methods the framework uses.
</p>
<p>Now that I've gotten my hooks into building stuff with Django, I now recognize the same seductive promises that I found in things like CakePHP:  the full-stack takes you away from actually figuring out how to code things, and instead you find yourself just using all the built-in methods.  Don't get me wrong, the built-in stuff for Django is awesome.  But if I want to push my skills forward so I can say "I can build stuff for the web using Python" instead of "I can build stuff for the web using Django" I need to use other tools.  What if I want to run my stuff on Google App Engine?  Sure, there are these hacks available for Django that make it "usable" on GAE, but that's not what I want.  And what about the use of WSGI instead of relying on mod_python?  Forgive me if this stuff comes across as technobabble.  It was technobabble to me at one time too.
</p>
<p>
So now the next step is (after finishing the current Django app) is to build an application using a much more <a href="http://flask.pocoo.org/">lightweight framework</a>.  Why?  Because it's time to actually learn how to do something instead of relying on magic methods.  Because once I learn to write code to duplicate those magic methods, I'll be able to use Django *and* Flask.  And that, my friends, is how you make yourself useful.  That and the ability to run the app both as a standalone WSGI app or on Google App Engine seems like a bonus to me.
</p>
<p>
So now that you've gone from full-stack to lightweight, it's time to look at the next lesson...
</p>
<h3>Lesson 2: Don't use anything made by One Guy</h3>
<p>
This will undoubtably be a touchy subject for some.  Let me try and explain it.
</p>
<p>
In the quest for the lightweight solution, I ran across <a href="http://web2py.com">web2py.</a>  Nice and lightweight, awesome documentation, but it's all driven by ONE GUY.  Experience has taught me that projects driven by ONE GUY end up looking like how the ONE GUY would do it.  Sometimes the ONE GUY is brilliant and it all works out.  That is rare, in my experience.   Open source projects are littered with the wreckage caused by egos and control freaks who were unwilling to accept outside help to solve problems.
</p>
<p>So look for projects where it appears there are solid contributors beyond ONE GUY.  web2py sure has an impressive list of people who contribute, but is Massimo the ONE GUY when it comes to actually making non-trivial code changes?  I sure hope not.
</p>
<h3>There will be no test afterwards</h3>
<p>
While I do not expect other people's experiences to be the same as mine, I'm pretty sure I am not the only person who has learned these lessons.  So the next time you are evaluating using a web application framework (in a new language or an existing one) think back on these lessons.
</p>
