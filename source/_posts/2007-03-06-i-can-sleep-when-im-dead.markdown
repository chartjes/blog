--- 
layout: post
title: "I can sleep when I'm dead!"
---
<p>That is a phrase I've used more than once with my wife as a way to explain why I'm staying up late screwing around on my computer.  But some side projects have been keeping me up past my normal bed time.</p>
<p>I'm racing to get my Last.fm / Audioscrobbler component for <a href="http://framework.zend.com">Zend Framework</a> all taken care of.  I've changed it to use <a href="http://framework.zend.com/manual/en/zend.http.html#zend.http.client">Zend_Http_Client</a> to talk to the web services, and found a neat trick where I can create a <a href="http://framework.zend.com/manual/en/zend.http.client.adapters.html#zend.http.client.adapter.test">test connection</a> for the client.  Why is this needed?  Well, I got told that I needed to create tests that didn't require an internet connection.  Kind of hard for a web service, so luckily Zend_Http_Client_Adapter_Test lets me create some tests that don't actually connect to the web service.</p>
<p>
I'm also fortunate enough now to have gained access to <a href="http://www.cakephp.org">CakePHP's</a> inner circle (i.e. access to the SVN repository) as to make my work on a series of CLI tools (like the interactive console) part of CakePHP itself.  I know it's very nerdy, but I'm excited to contribute to the project.  Having an interactive console for a framework is a huge advantage for quickly testing something.  There are lots of examples for the Ruby on Rails crowd for how to use the console for tryign things out.  Thanks to Nate and Larry for letting me join the club.
</p>
<p>
I'm a little behind on development work because I'm still waiting to get my new laptop from my new job, but once I get that I anticipate churning out a beta of the interactive console in short order.
</p>
