--- 
layout: post
title: CakePHP and the iPhone
---
<p>I lost my cellphone last night, which sucks because the phone I want isn't going to be available until July 11th.  I'll get a loaner phone until then, but it is exciting times to be a web developer.  Why?  Because the introduction of the iPhone there is a renewed interest in web sites that cope well with mobile browsing.  I'm working on an app that is perfect for mobile browsing, but that is still down the road.</p>
<p>
Anyhow, I saw a post the other day showing how to create an <a href="http://www.symfony-project.org/blog/2008/06/09/how-to-create-an-optimized-version-of-your-website-for-the-iphone-in-symfony-1-1">iPhone-optimized version of your Symfony app</a>.  Yawn.  Cake <a href="http://bakery.cakephp.org/articles/view/building-an-iphone-app-in-a-day">had that a year ago.</a>.  No code provided *but* the article does tell you exactly how he did it.
</p>
<p>
But that's really the key here.  You don't need to do anything special to make a web-based app in CakePHP that will work nicely on your iPhone.  Contrast that to all the stuff I see in that article that you need to do.  Off the top of my head, it seems to me the best way to do it is:
<ul>
<li>create CSS and layouts for regular and iPhone versions of your application</li>
<li>do a check in your beforeFilter() method where you check the User-Agent</li>
<li>pass that info to your actions, and render whichever layout+CSS you need</li>
</ul>
</p><p>Compare the Symfony article to the CakePHP article plus my notes, and let me know what you think.</p>
