--- 
layout: post
title: The Rise of the App Cloud
---
<p>
These are heady times for any web developer.  Two of the biggest companies on the web are now offering access to what I call their "app cloud" so you can run your web app in a hugely scalable environment.  Amazon was first out of the gate with their great combo of <a href="http://www.amazon.com/gp/browse.html?node=16427261">S3</a>, <a href="http://www.amazon.com/gp/browse.html?node=201590011">EC2</a> and <a href="http://www.amazon.com/gp/browse.html?node=342335011">SimpleDB</a>.  Of course, you didn't expect Google to stand idly by and they have delivered as well with <a href="http://code.google.com/appengine/">Google App Engine</a>.  So, what do they have in common?
</p>
<p>
You're limited in what you are allowed to do.  It's really that simple, because in order for you to gain the advantage of being able to have scalability out of the box you are going to have to follow a bunch of rules.  Sandboxes are good, but the problem occurs when you fight against the sandbox rather than embrace it's constraints.  Sort of the same thing I see on the CakePHP mailing list where people are determined to do what they want, and who gives a flying fuck what the conventions are.  But in this case, you cannot avoid it.
</p>
<p>
Having looked into the idea of running an app using Amazon's EC2 + SimpleDB structure for Rallyhat, it looks like it's pretty simple to get up and running with those tools.  I know I'm grossly simplifying the process, but you create your app, create an image, upload it into the cloud and away you go!  With Google App Engine, all you can do is create Django-based apps...but they've severely limited what you can do as they require you to use a GAE-specific wrapper to talk to things.  That means a lot of the cool Python libraries that are out there WILL NOT BE ABLE TO HELP YOU.  Maybe that's just for now, but that's a pretty serious limitation.
</p>
<p>
Secondly, both SimpleDB and BigTable have the same limitation in that you cannot do joins, so that means you have zero hope in hell of using any sort of ORM wrapper on your data.  It's all about the denormalized data.  Go look it up if you don't believe me.  Now, this can be a problem if you have a very complex database structure that requires a lot relationships between your tables...like most of the apps that use modern web application frameworks.  Maybe my thoughts on using a very simple REST-based framework in PHP isn't such a crazy one for this.
</p>
<p>
Rallyhat is using relationships between tables because that makes it easier for me.  Games belong to Teams, Locations belong to Games, Teams belong to Sports.  Also, I've been using CakePHP long enough that all my apps are designed around the idea of data having relationships.  If I had to denormalize that data by putting it all in one big table essentially, I lose the use of ORM / data mapping.  Django lets me do the same sort of relationships as Cake, so why the hell wouldn't I use it?  It's about speed of development, after all.  Quicker to a usable state is really the key here, as you're bound to spend all sorts of time in maintenance-and-bug-fix mode no matter what.
</p>
<p>
So this leads me to what I consider an inevitable conclusion:  using an app cloud is only for certain types of applications.  What a huge leap in logic, no?  All sarcasm aside, this is the same sort of logic that dictates that most web application frameworks are only good for certain types of sites.  Once you step up to a certain level of complexity, you have two choices:  work really, really hard to simplify things as possible OR understand that you are in the land of Custom Solutions and hope that you are smart enough to come up with one that works.  What's that old adage:  simple systems can display complex behaviour?  Now that there is a solution for certain types of scalability issues, the trick is to figure out how to build an app to leverage that.
</p>
<p>
The biggest problem I see with putting your app up in the cloud is the issue of data sharing.  Scalability usually requires as little sharing between parts of your application as possible.  If you have a central data store, that will forever be your application choke point.  Whether it's clustering or sharding, it is a non-trivial task to build scalable data stores.  I haven't looked at SimpleDB and BigTable enough to form an opinion on whether or not these are viable contenders for this type of solution.  Hopefully it is.
</p>
<p>
It's ironic to me that while we have a definite rise in the use of frameworks for web application programming, some of the most powerful tools available to build web applications that can handle the complexity of scaling well require you to throw all that stuff away and get back to really simple things.  Perhaps this is a good thing, as all these magic methods in frameworks give the developer simplicity, but you become dependent on those magic methods.
</p>
<p>
Heady days indeed.  Time to look at whether or not Rallyhat could run in those environments...just because I want to see if it's possible.  Learning Python is one thing.  Learning Python + Django + SimpleDB, or Google App Engine (if I could ever get an invitation) is another.  Seems to me I could whip something together in PHP that could run on EC2 with SimpleDB, but is that really much of a challenge?
</p>

<
