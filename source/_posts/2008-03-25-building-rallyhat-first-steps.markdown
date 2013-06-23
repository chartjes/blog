--- 
layout: post
title: "Building Rallyhat: First Steps"
---
<p>This will be the first in a series of posts chronicling my building out of Rallyhat, a site that people will use to plan sporting road trips, baseball first.  In this first installment I wanted talk a bit about the first steps I too to actually get this thing rolling.</p>
<p>
Now, I could easily build this site in CakePHP, so that's not really much of a challenge.  I already have <a href="http://www.ibl.org">one site that runs Cake</a> to keep me on top of things there, and future work-related projects are going to be CakePHP for me as well.  So, something else then?  I already did the Rails thing, and tore that down to build the CakePHP one.  I thought about using <a href="http://merbivore.com/">Merb</a>, and I'm going to attend a talk at <a href="http://openwebvancouver.ca">Open Web Vancouver</a> about Merb so I get a better idea about what it could do for me.  So that left just <a href="http://www.djangoproject.com">one choice</a>.
</p>
<p>
C'mon, you're not really surprised are you?
</p>
<p>
One of the things I really liked about Django is the admin app that you get for free.  I've already been using it to full some of my support tables for the application, but I wanted to talk about a neat little thing you can do here.  In Django, you define the names of the fields in your model in order for the ORM magic to work.  Here's a little sample:<br />
{% codeblock lang:python %}
from django.db import models

class Sport(models.Model):
	name = models.CharField(max_length=30)
	
	class Admin:
		pass

{% endcodeblock %}
</p><p>
The Admin stuff is so that those models show up properly in the admin part of the application.  So, just like in CakePHP where you can use $this->Model->find('list') to get an array for use in your dropdowns for forms.  Django, does this a little differently.
</p>
<p>
Being totally object oriented, if you drop into the Python interpreter and ask it to return a model to you, you'll get something like this, taken from the Django tutorials:
{% codeblock lang:python %}
(chartjes@jackjack ~/Sites/rallyhat)
>python manage.py shell
Python 2.5.1 (r251:54863, Jan 17 2008, 19:35:17) 
[GCC 4.0.1 (Apple Inc. build 5465)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from rallyhat.www.models import Sport
>>> Sport.objects.all()
[<sport : Sport object>]
>>> 
{% endcodeblock %}
<p>
WTF?  What good is "Sport: Sport object" to us?  I want something more descriptive.  How about the name of the sport?  That's easy.  We can modify the Sport model and tell it that when we return the object, return the "name" field instead.
</p>
{% codeblock lang:python %}
class Sport(models.Model):
	name = models.CharField(max_length=30)
	
	class Admin:
		pass
	
	def __unicode__(self):
		return self.name
{% endcodeblock %}
</sport></p>
<p>
So, when I drop into the shell, I get the following:
{% codeblock lang:python %}
(chartjes@jackjack ~/Sites/rallyhat)
>python manage.py shell
Python 2.5.1 (r251:54863, Jan 17 2008, 19:35:17) 
[GCC 4.0.1 (Apple Inc. build 5465)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
(InteractiveConsole)
>>> from rallyhat.www.models import Sport
>>> Sport.objects.all()
[<sport : MLB>]
>>> 
{% endcodeblock %}
</sport></p>
<p>
Same result, different way to get to it.  		
</p>
