--- 
layout: post
title: \"Lies I Told My Kids\" -- Python + Flask + GAE
---
<p>As many of my readers know, I've been slowly expanding my Python skills over the last 18 months or so.  First, I fooled around with Django on my laptop, really liking what I saw. Next, I started using it to write scripts for pre-calculating fantasy point totals at my <a href="http://xmlteam.com">old job</a>. Finally, I had been looking at Google App Engine and seeing what it would take to put a very simple Python site up there. I had a few options.
</p>
<p>
I could use the web application framework Google provided in Python called <a href="http://code.google.com/appengine/docs/python/gettingstarted/usingwebapp.html">webapp</a>, but I decided I wanted to learn a framework I could use outside of GAE as well. I really like Django but, until recently, there were a whole bunch of hoops you had to jump through in order to get it to play nicely with GAE. It's easier now, but I started this project a while ago and it's been bitrotting on my laptop. Also, I was frustrated with Django because the application I was trying to build with it just wasn't a good fit and <a href="https://mapalong.com/hello">someone beat me to it</a>. Not Django's fault, and I would gladly use it again to build something else.
</p>
<p>
Finally, I decided I wanted to use a very lightweight framework because I felt that my lack of Python expertise meant a lot of the magic going on in Django (like any awesome full-stack framework) was difficult for me to understand as a PHP guy who was trying not to write Python code like a PHP guy. So, after hashing things out via IM with my friend <a href="http://chiggsy.com/">Kevin</a> I chose <a href="http://flask.pocoo.org/">Flask</a>, which bills itself as a "microframework for Python based on Werkzeug, Jinja 2 and good intentions.".
</p>
<p>
I found Flask very easy to use, and the documentation helpful to a beginner like me. I could easily start to see where a more advanced developer could create things just the way he wanted. Once I found <a href="https://github.com/kamalgill/flask-appengine-template">an awesome template for running Flask on GAE</a> I was off and running.
</p>
<p>
The application itself was very straight-forward: collect user submissions about the little white lies parents tell their kids, and show them in a paginated fashion. The twists? I was going to store them in the GAE datastore (so I had to learn their API) and I also wanted to use <a href="https://github.com/defensio/defensio-python">Defensio</a> to pre-filter submissions and identify ones that might be spammers trying to get stuff in there. Pro-tip for you developers out there: if the library you want to use has tests, that is the first place you should go to see how to actually use the library.
</p>
<p>
So, in bits and pieces over a few months (basically whenever inspiration struck and there was nothing I wanted to watch on TV with the wife) I put the application together.  It's functioning the way I want it to (although I admit I didn't do a ton of testing of the pagination, so maybe I'll hack at that later) but needs some help on the UI side. Feel free to <a href="http://liesitoldmykids.appspot.com">check it out</a> and add your submission.
</p>
