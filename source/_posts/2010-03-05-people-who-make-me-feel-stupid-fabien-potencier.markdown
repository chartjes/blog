--- 
layout: post
title: "People Who Make Me Feel Stupid: Fabien Potencier"
---
<p><i>This is the final in a series of blog posts about programmers who make me feel stupid due to the amazing work they've done and their ability to explain it.  Check out my thoughts on <a href="http://www.littlehart.net/atthekeyboard/2010/03/01/people-who-make-me-feel-stupid-geoffrey-grosenbach/">Geoffrey Grosenbach</a>, <a href="http://www.littlehart.net/atthekeyboard/2010/03/02/people-who-make-me-feel-stupid-antirez/">Antirez</a>, <a href="http://www.littlehart.net/atthekeyboard/2010/03/03/people-who-make-me-feel-stupid-rich-hickey/">Rich Hickey</a> and <a href="http://www.littlehart.net/atthekeyboard/2010/03/04/people-who-make-me-feel-stupid-ezra-zygmuntowicz/">Ezra Zygmuntowicz.</a></i></p>
<p>I am, for lack of a better phrase, a framework whore.  I use frameworks to build all my web applications.  Why?  Because I prefer to stand on the shoulder of giants rather than constantly reinvent things.  But in many ways, my addiction to frameworks is counter-productive because I find myself constantly wanting to use a new one.  So I end up churning instead of pushing forwards.   I've been learning Zend Framework, and I'm struggling.  Too many ways to do things, too much documentation that provides me with a tease of what it is I'm trying to do but not the full solution.  Then I have to ask people for help and feel stupid for not being the Rock Star Developer(tm) with all the answers.  
</p>
<p>
So, even though I use Zend Framework now (unless I change my mind, get pissed off and go with the <a href="http://toys.lerdorf.com/archives/38-The-no-framework-PHP-MVC-framework.html">no-framework framework</a>) I do watch other frameworks.  While I might not agree with some features of <a href="http://www.symfony-project.org/">Symfony</a>, I am astounded at what <a href="http://fabien.potencier.org/">Fabien Potencier</a> continues to produce.
</p>
<p>
Creating a framework is an achievement in itself.  Creating a framework in a language as your first real PHP project, like Fabien did, is nothing short of amazing.  Symfony is a full-stack framework, the kind of comfy and warm blanket I like to use when building an application on a short timeline.  Like many other full-stack frameworks, they also wrote stuff that other people had already written.  It's a common thing, everyone goes through the "not invented here" phase.  Sometimes, that's the only way you learn how to do something.
</p>
<p>
But as Symfony glides smoothly along towards a 2.0 release, imagine the shock of people when they see Fabien talk about how he is going to use parts of Zend Framework in the 2.0 core and dump existing components like their own unit-testing framework in favour of PHPUnit.
</p>
<p>
In the blog post about <a href="http://www.symfony-project.org/blog/2010/03/04/symfony-2-0-and-the-php-ecosystem">decisions about Symfony 2</a>, he mentions the logic surrounding what appears to be a new public philosophy from Symfony: "Use what's out there; realise it sucks; write your own; wait until others suck less; dump your own; use other."
</p>
<p>
This is a very refreshing stance for the guiding power of a popular web application framework to take.  It reminds me of when Rails and Merb decided to quit fighting and instead become the same project in Rails 3.  The hater in me thinks that it's because Merb was becoming what Rails wanted to be, so kudos to the effort to rework Rails to make it better.  After all, that's the goal -- to produce better, faster software.
</p>
<p>
So why does Fabien make me feel stupid:  <b>His constant willingness to do the right thing for his project, even if it means tossing away stuff that spent a long time working on.</b>  Again, just like all the others I've talked about here, he does an amazing job of explaining what he did in a way that makes it obvious.  His thoughts on <a href="http://fabien.potencier.org/article/11/what-is-dependency-injection">dependency injection</a> helped me to understand why it's important to consider it when building your applications.  I've written code that uses it and code that does not.  I found it easier to refactor code when I used dependency injection, but that just might be me.
</p>
<p>
Thanks for following this series this week.  I hoped I've exposed you to some people you might not have heard of or known about their work.
</p>
