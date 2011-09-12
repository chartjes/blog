--- 
layout: post
title: Zend_Service_Audioscrobbler
---
<a target="_blank" href="http://derekmartin.ca">Derek</a> and I got our submisison in today for a component for the <a target="_blank" href="http://framework.zend.com">Zend Framework</a> called (oddly enough) Zend_Service_Audioscrobbler.? As the name states, it's intended to allow people to access Audioscrobbler's REST service.

For those who don't know, Last.fm is powered by Audioscrobbler's stuff and the Zend Framework handles REST sevices very easily.? It's in the new proposals section right now.? We're keeping our finger's crossed that it gets accepted.

At work I'm working on a prototype for a new stats tracking system.? I want to use the Zend Framework for it...but there is no built-in authorization component.? I know, I know, I should roll my own...but do I really want to?

I have two choices:? figure out a way to do simple .htaccess based auth so I can continue to use the Zend Framework (it uses .htaccess already to handle rewrites) or forget about Zend Framework and go with <a target="_blank" href="http://www.cakephp.org">CakePHP</a> instead.? CakePHP is a really good Rails clone...but given I have to write a talk with code examples in PHP I think it's wise I stick with Zend Framework unless I can't make it work.
