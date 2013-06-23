--- 
layout: post
title: "Reader Feedback: Working with XML In PHP"
---
<p>
Welcome to the 3rd installment of me answering reader feedback questions.  Today we deal with a topic that I deal with every day at my <a href="http://www.xmlteam.com">day job</a> -- working with XML in PHP.</p>
<p>
First of all, I do all this in PHP 5.  SimpleXML makes it so easy to manipulate XML.  For my main work project, I've written a PHP application front end that talks to <a href="http://exist.sourceforge.net">eXist</a>, an open source XML database.  Since we deal with XML all day long it was decided that we needed to <a href="http://en.wikipedia.org/wiki/Eat_one's_own_dog_food">eat our own dog food</a> and go with an XML database to store the information that the <a href="http://sportso.com">application</a> generates.  So a lot of my code does some of the following things:
<ul>
<li>Do a call to a xQuery script running on the database that returns info that I'm looking for, usually both comma and pipe-separated data</li>
<li>Load a specific document into a SimpleXML object and pull out some specific info</li>
<li>Load a specific document into a SimpleXML object and then use it's XPath functions to pull some information out.</li>
</ul>
</p>
<p>
Those 3 techniques seem to work well for me when dealing with XML data in PHP.  If I had to go back and redo some of the earlier code, I'd probably change things a little differently in how I'm using eXist to simulate how some of our other products work:
<ol>
<li>Use eXist to give me a list of documents that contain the info I am looking for</li>
<li>Load those documents into SimpleXML</li>
<li>Use Xpath to grab the data I needed</li>
</ol>
But in the interest of Getting Things Done, what I've done works pretty good and the code is really not horrible.</p>
