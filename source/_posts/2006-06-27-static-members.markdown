--- 
layout: post
title: Static Members
---
As I work on code using the Zend Framework for a project at work (a stats reporting system for all our forums) I noticed that a lot of static class methods are being used instead of calling them dynamically:

{% codeblock lang:php %}
<?php
$db = Zend_Db::factory('pdoMysql', $params);
Zend::register('db', $db);
$view = new Zend_View();
$view->setScriptPath('../app/views');
Zend::register('view', $view);
$controller = Zend_Controller_Front::getInstance();
?>
{% endcodeblock %}

So I said to myself "why are we using these static class calls instead of dynamically creating instances of these classes?".  Little did I know that I had stumbled upon another one of the Great Holy Wars of Programming:  static vs. dynamic.

Not only does this war cover static typing vs. dynamic typing for languages (PHP uses dynamic typing), but it also covers the use of static methods vs. instance methods.  50+ messages in the thread later and we're nowhere closer to solving the problem.  All I wanted to know was why we were doing it this way, and as a secondary goal to try understand when we need to do it dynamically (when the state of the object is important) and when to call an object method statically (when the state of the object that the method belongs too is not important).

My thanks to Ralph Shindler for pointing me at <a href="http://www.javaworld.com/javaworld/javaqa/2001-11/03-qa-1121-mrhappy.html">this little gem</a> that tries to explain the static method vs. instance method problem.  This is one area of OOP that I hadn't paid much attention to since I had heard "static bad, dynamic good" back in my very early OOP days.  Like everything else, there is a place for static methods and a place for instance methods.

One of the common reasons to NOT use static methods was that it can make unit testing difficult.  Of course, you could always wrap the call to the static method so that it comes off as an instance method in your code, but that is a topic that is left to more experienced OOP developers.

As an aside, I've pretty much settled on the outline for the talk I'm going to be giving at php|works.  Now I'm working on some code snippets involving the Zend Framework to illustrate just what the heck I'm talking about.
