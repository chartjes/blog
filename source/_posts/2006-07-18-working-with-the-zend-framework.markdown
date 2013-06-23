--- 
layout: post
title: Working With The Zend Framework
---
I am delivering an "alpha" version of a project for work, a centralized stats reporting system for the various (I believe we are almost up to 40 of them now) forum sites my employer owns.

Having built a few sites with Rails, I found it very easy to build something using the Model-View-Controller pattern.  Although the framework isn't at a 1.0 stable release, the components I am using are stable enough for production use.  There is a component that is in the "incubator" (which is considered unstable and under development) that I would like to use as a helper for the views (it generates URL's based on the controller and action) but I'm trying to avoid the realy unstable code.

When I do the database stuff, that is when I really miss Rail's ActiveRecord database implementation.  The funny thing is that I stumbled across a posting on the <a href=http://phplens.com/phpeverywhere>PHP Everywhere blog</a> (a great web site by a PHP developer who knows what he's doing) where he talked about how he quickly hacked together an ActiveRecord implementation for ADODb (his own DB abstraction layer) based on an early Zend_Db_Model component.  That component isn't in the current code base, which is very weird.

I'm wondering if we'll see that any time soon?  Maybe I'll switch to using ADODb version for the stats reporting system when I get to phase 3 of the project (which is adding pretty graphs to the reports).
