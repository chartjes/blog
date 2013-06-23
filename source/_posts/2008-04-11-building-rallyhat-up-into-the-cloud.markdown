--- 
layout: post
title: "Building Rallyhat: Up into the cloud"
---
<p>It pays to have friends who have connections.  After reading my blog posting about <a href="http://www.littlehart.net/atthekeyboard/2008/04/09/the-rise-of-the-app-cloud/">the rise of the app cloud</a> I got an IM from <a href="http://marcgrabanski.com/index.php">Marc Grabanski</a> asking me if I wanted an invite to get in on <a href="http://code.google.com/appengine/">Google App Engine</a>.  Needless to say, I said yes.</p>
<p>
So I have an account up there now, but nothing to show you guys yet.  The tutorials they have are actually quite clear and make sense.  What makes it even more ironic is that all you can use is Python (which I'm learning) and runs Django 0.96 standards (although you can use dev versions if you like). Is that fate trying to give me a hint or something?
</p>
<p>
Anyway, it looks like it will be trivial for me to redo my database structure so that it fits in nicely with BigTable.  I need to massage the data in the new format and then find a tool that lets me upload that up into BigTable itself.  My data is simple enough so the fact that I can't do joins won't really matter.  All my data can be per row in a database anyway, the relational stuff just makes it easier to write code.  Or at least I've found that when doing stuff with Cake.
</p>
<p>
As far as Rallyhat Extreme Alpha goes, I've got it working in that you can do the following:
<ul>
<li>pick your teams and date range</li>
<li>see the list of games and pick which ones you want to go to</li>
<li>plot the stadiums on a map so you can see distances</li>
</ul>
<br />
The UI isn't pretty so I have lots of work on making that easier to use.  But I am excited.  Once I figure out how to create driving-distance stuff dynamically it will be even cooler.
</p>
<p>
I have to say that I have noticed that the Python "way" is quite different from the PHP "way".  Maybe it's more accurate to say the Django "way" is different from the PHP "way".  Django has deliberately limited what you can do in their templates out-of-the-box.  Yes, you can write custom code for stuff in templates by extending it yourself (the documentation is actually quite clear on how to build them) but out-of-the-box you can only do so much.  Frustrating when you come from the PHP world where you are able to put PHP code in your templates to accomplish certain tasks.  You can't just dump any old Python code in there, as I have found.  Much of what I'm trying to accomplish simply needs to be done in a different place, as a lot of the form-processing magic in both CakePHP and PHP itself has hidden that from me.
</p>
