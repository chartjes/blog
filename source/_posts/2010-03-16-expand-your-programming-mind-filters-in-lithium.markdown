--- 
layout: post
title: "Expand your programming mind:  filters in Lithium"
---
<p>Out of the ashes of a severe personality clash in an <a href="http://cakephp.org">open source PHP web application framework project</a> rose a new framework proclaiming that it <a href="http://rad-dev.org/lithium/wiki">simply sucks less than all the others</a>.  Lithium, otherwise known as li3, is the latest PHP application framework to come onto the scene.  I know what you're saying.  *Yawn*.
</p>
<p>
As far as I can tell, Lithium is trying it's hardest to be fast, lightweight, and use all the features that PHP 5.3 has to offer.  I am unable to use it at work for a variety of reasons (not stable, required PHP 5.3 only, <a href="http://twitter.com/nateabele">Nate</a> is always picking on me via IM) but I am more interested in the ideas that are coming out of it.
</p>
<p>
It is using all the newest hawtness in the PHP world:  namespaces, closures, Phar, late static binding.  I could go on, but probably most of these things mean nothing to you until you actually need them.  In the framework world, namespaces are a big deal, an essential tool to avoiding collisions with 3rd party code you might want to integrate into your project.  Closures are very familiar to those who've done work with Ruby or Javascript.  Phar allows for some unarchiving on the fly of code, even potentially distributing your application as an archive that can be run.  Late static binding is something I'm trying to comes to grips with, as I have either never come across a need for it or never realized that I did and have implemented a workaround for it not realizing there is a simpler solution.
</p>
<p>
None of these are what I want to talk about.  I want to talk about something that I feel is a very underrated part of Lithium, the ability to define filters.  This is a concept that you find in <a href="http://en.wikipedia.org/wiki/Aspect-oriented_programming">Aspect-oriented programming</a>, and one that I imagine most programmers have never considered.  Here's why I think it's a big deal.
</p>
<p>
Most frameworks are designed around an OOP paradigm.  Yes, some mix them together (I'm looking at *you* CodeIgniter), but by and large you get the job done by extending on a base model / controller / helper / whatever to create new functionality.  Sometimes this is not avoidable.  But what AOP says is that there is another way, a way that Lithium has adopted as well.
</p>
<p>
Hence the creation of "filters".  As far as I can tell (and I'm sure I will be jumped upon if I am wrong) the purpose of filters in Lithium is to allow you to add functionality without extending the class itself.  When I saw that I immediately understood why that is so awesome.
</p>
<p>
The idea of callbacks is also very similar:  if X happens, run code Y.  A staple of jQuery, Rails and probably other projects I have forgotten to mention.  The idea is still the same though.  In Garrett Woodworth's <a href="http://www.slideshare.net/gwoo/li3-ocphp">presentation about Lithium to the Orange County PHP Users Group</a> he goes  over some solid examples of filters including:
<ul>
<li>automatic use of the <a href="http://mirror.facebook.net/facebook/xhprof/doc.html">XHProf</a> for code profiling</li>
<li>automatic setting of parameters upon saving a pasted bit of code</li>
</ul>
</p>
<p>It's also been used to <a href="http://misja.posterous.com/playing-with-lithium">automatically change string record ID's into a MongoDB ID</a> and <a href="http://latestatic.com/integration-testing-or-how-i-learned-to-stop">graceful failing of an integration test suite when an error occurs</a>.
</p>
<p>
These filters remind me of behaviors in Rails (and in CakePHP as well) and makes me wonder if signals are the same thing in the Django world.  All in all, this looks to me to be a better way to extend functionality than actually overriding existing methods or hacking at something deep inside a class.  Figure out what functionality you want, figure out where it needs to be called, and add your filter.
</p>
