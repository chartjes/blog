--- 
layout: post
title: Rallyhat lives!
---
<p>
Some of my long-time readers have seen me mention a long-festering (I believe that is the correct term at this point) project that I dubbed <a href="http://www.rallyhat.com">Rallyhat</a>.  It first started out as a "figure out when some baseball teams are in town and buy tickets" and then morphed into "a tool for helping people plan road trips by tagging destinations with information".
</p>
<p>
What it really became was a tool for me to learn how to write a solid web-app using Python and Django.  I'm happy to say I finally have a version that I feel comfortable sharing with the rest of you.  So feel free to check it out.  Pound on it, try and break it and I will also read your feedback and comments.  I'm sure you can figure out my email address...
</p>
<p>
Also, I've found it has been easy to pick up not only Python and Django itself.  I'm ready to tackle some other applications using Django, and I have one just in mind.  
</p>
<p>
Yes, I am aware at how spartan it looks right now.  I'm more focussed on functionality than how it looks right now.  I've already gotten some interesting ideas on expanding the app to include adding in images to go with locations, so we'll see how that goes.
</p>
<p>
For those who are curious, I built it using the following:
<ul>
<li>Python 2.6</li>
<li>Django 1.2 beta 1</li>
<li><a href="http://couchdb.apache.org/">CouchDB</a> to store the trip plans</li>
<li><a href="http://code.google.com/p/couchdb-python/">couchdb-python</a></li>
<li><a href="http://code.google.com/p/geopy/">GeoPy</a></li>
<li><a href="http://bitbucket.org/ubernostrum/django-registration/">django-registration</a></li>
<li>Google Maps services</li>
<li><a href="http://github.com/robhudson/django-debug-toolbar">Django Debug Toolbar</a></li>
<li>deployed using Nginx + <a href="http://github.com/benoitc/gunicorn">Gunicorn</a>, configured with the help of <a href="http://twitter.com/ericlo">Eric Florenzano's</a> awesome Django Advent article about <a href="http://djangoadvent.com/1.2/deploying-django-site-using-fastcgi/">deploying Django using FastCGI</a> because it mentioned how you could use Gunicorn</li>
</ul>
</p>
