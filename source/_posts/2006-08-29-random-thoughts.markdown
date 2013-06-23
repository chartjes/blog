--- 
layout: post
title: Random Thoughts
---
<p>No real focus to this post today, just 2 things to talk about.</p>
<p>
First, I got an email from the fine folx at <a href="http://framework.zend.com">the Zend Framework team</a> informing me that the proposal <a href="http://derekmartin.ca">Derek</a> and I had done to add a component to the core of the framework to handle talking to <a href="http://last.fm">Last.FM's</a> web services has been moved out of the proposal stage and into the incubator, which is amazing news.  This means that once Derek and I finish all the unit tests we can move the component to the core of the framework.  We've done all the hard work, and just have to make sure nothing is broken thanks to our unit tests.
</p>
<p>Secondly, I was listening to the <a href="http://podcast.phparch.com">Pro-PHP podcast</a> and they mentioned briefly a talk about 6 things that Theo S. didn't like about PHP.  One of the more interesting ones was the idea that the PHP has the worst build system out there.  So that got me to thinking.
</p>
<p>
I've always wondered why some elements were build as part of the core of the language and why some were extensions.  From a build perspective, might it not be easier to make EVERYTHING an extension beyond just some core functionality.  That way you would install the base of PHP and then all the extensions you wanted to customize your install.
</p>
<p>
Sean Coates had commented that at some point, the whole build process for PHP was going  to have to be carefully examined.  Maybe it would be a good idea to think about a system similar to the one I've talked about.  Trim the core PHP install down to a bare minimum (no DB, no XML, etc) and then make all that stuff installable as extensions.  Not that I have any idea on how to make that happen, but it's an interesting idea for the core PHP team.</p>
