--- 
layout: post
title: Fun with API's -- FRAPI and django-tastypie
---
<p>Throughout my career as a programmer I've had moments that I call "why the hell didn't I see that earlier" moments when it comes to embracing new technologies and techniques.  The first such moment was when I discovered frameworks.  I mean, how many times did I write PHP apps with page and/or front controllers.  And all that mixing of business logic and display logic.  It was madness!
</p>
<p>
The next such time was when my friend Kevin convinced me to throw away my GUI shackles and learn to use the <a href="http://www.vim.org">One True Editor</a>.  Given how often the advanced features of the never-ending parade of IDE's I used were not being used, vim turned out to be exactly the tool I needed.
</p>
<p>
Well folks, I've had another one of these moments.  What is it?  Repeat after me:  THOU SHALL BUILD YOUR APPLICATION AS AN API FIRST, AND FRONT END SECOND.  I've been toying with this idea for a while, but a recent side project and these <a href="http://phpadvent.org/2010/first-class-apis-by-helgi-%C3%9Eormar-%C3%9Eorbj%C3%B6rnsson">three</a> <a href="http://phpadvent.org/2010/the-thing-with-the-two-heads-by-ed-finkler">awesome</a> <a href="http://phpadvent.org/2010/building-mobile-apps-with-php-by-jonathan-stark">articles</a> finally convinced me that my instincts were right, and that the extra work involved with API-first development (wow, maybe I've coined a new term) pays off in our new world of multiple devices wanting to slurp up online content.</p>
<p>
So, here are two tools that I think my readers should know about.  For those working with PHP, I cannot recommend enough the use of <a href="http://getfrapi.com">FRAPI</a> if you have a legacy application that you need to provide an API for.  Now, I will admit that the installation procedure is not for the faint-of-heart (you have to install packages via PEAR, PECL, and perhaps even adding packages for your operating system) but once you have it installed, you now have a tool to allow you to quickly create an API.  
</p>
<p>
In a nutshell, FRAPI is a framework for creating a REST API.  Using the admin panel, you define the URL's you want for your API and it generates some code for you.  Then you edit the generated code to provide the actual output from your API, and reaction based on your GET/POST/PUT/DELETE request.   From when I downloaded it, it took me about 30 minutes to get FRAPI installed and create my first API call, including a customized output template.
</p>
<p>The documentation via the wiki isn't that great, but it gives you everything you really need to get started.  Kudos to the boys at <a href="http://twitter.com/echolibre">echolibre</a> for creating a super-useful tool.</p>
<p>
Now, if you're using Django there is an awesome add-on called <a href="https://github.com/toastdriven/django-tastypie">django-tastypie</a> that allows you to quickly create a REST API for your Django models.  Again, from the time I downloaded it, it took me about 30 minutes to create an API for one of my models.  Now, I can create the front-end for the project either in Django or take the leap of faith and create it using Javascript and have it call the API.
</p>
<p>The documentation for django-tastypie is good, and <a href="http://joshbohde.com/2010/11/25/backbonejs-and-django/">this article on JS on the front, scripting language on the back</a> shows you a practical use for it.
</p>
<p>
So don't be afraid to build your application from the API out, now that there are plenty of tools to allow for easy integration with your application.
</p>
