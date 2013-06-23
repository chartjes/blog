---
layout: post
title: Scope is not a mouthwash 
author: Chris Hartjes
date: 2011-11-25
comments: true 
sharing: true 
---
One of the worst-kept secrets now is that I have started working on a book
about some practical techniques for building testable applications. I'd
say I'm about half done, and the book will be ready for sale
when I give my talk at [CodeMash 2012](http://codemash.org) on the same topic.

Why do I care about all this stuff that causes friction for programmers?
Because there is so much I want to learn and fragile, untestable applications
get in the way of me becoming the programmer I want to be. Naturally I am also
working on an application that will serve as a companion to the book, a hand-crafted
web application that will embody the techniques I describe in the book. It is also
very humbling to "eat your own dogfood", meaning build you applications using
the practices you are espousing.

So, I set out to show people in my chapter of the book about decoupling objects
via the magic of dependency injection how to use this awesome thing known as a
dependency injection container. Although they are more suited for very large
complex applications like web application frameworks but I thought "I could
see someone like a younger version of me wanting to mess around with something
like this even though it might be totally inappropriate for the application.
Let's do it!"

For this I am using [Pimple](http://pimple.sensiolabs.org), an incredibly small
but effective dependency injection container. Easy to use, simple and effective
documentation, just what I was looking for. I also noticed that Pimple supported
the use of closures (or anonymous functions) as a way of storing a dependency.

Then things got stupid.

I altered the bootstrap file for my application (it's using the [no-framework framework approach](http://toys.lerdorf.com/archives/38-The-no-framework-PHP-MVC-framework.html)) and set up an instance of Pimple and wrote this cool-looking code that stores
a mapper for one of my models in it:

{% codeblock lang:php %}
$container = new \Pimple();
$container['db_connection'] = function ($c) {
    return new PDO(
        'pgsql:host=localhost;dbname=ibl_stats', 
        'login',
        'pass'
    );
};
$container['franchise_mapper'] = function ($c) {
    return new IBL\FranchiseMapper($c['db_connection']);
};
{% endcodeblock %}

What you don't see in this snippet is that before this happens, I am using a PSR-0
compliant autoloader. Go Google for it, it's hard to explain in a few short words
and I am also using namespaces to show people just how easy they are to use. I 
love autoloading. Spares me dealing with 'require\_once' and 'include\_once' and also worrying
about if I've required or included a file somewhere else.

I reload my test page and...what the hell? "Cannot find class IBL\FranchiseMapper"

That...that...that cannot be! It's RIGHT THERE! I have unit tests that run just fine
and the autoloader grabs it there too!

So I start asking for help on Twitter. "It must be Pimple causing the problem." Pimple's
creator [smacks me down](https://twitter.com/#!/fabpot/status/139706391777648640) and
I look at the code and say "of course it can't be Pimple. Keep looking!"

Next I figure there is something specific to closures that is causing the problem. I reach
out for more help, trying things willy-nilly to try and figure it out. I contemplate using
Xdebug to trace what is going on in the autoloader. Not very easy to debug autoloaders. 
Finally I see something (of course I cannot find the link now) that talks about closures
and scope. That is when I realize how fucking stupid I have been.

So, let's talk about scope for a second. Besides being the brand name for a mouthwash, scope
is a topic that some programmers get tripped up on. Despite my 14 years of PHP experience I often
feel like it is 1 year repeated 14 times. Scope deals with variables (and in this case namespaces)
and where they can be accessed from.

You have global scope, meaning that the variable/object/function can be accessed from anywhere.
Then you have the scope of something inside a standalone function. Unless (mind you, this is PHP
and I cannot speak for other languages) you mark it as global, it can only be accessed from 
inside that function. Now, you can declare a variable/object/whatever as being accessible inside
that object via the use of (for example) $this->foo but that variable, and you can also slap
public/protected/private to decide who can see it when you interact with that object.

To roll back to me, my problem was not one of variable scope. It was one of namespace scope. With
the introduction of namespaces to PHP you now have the concept of the "global namespace", which is
where all the existing PHP functions and objects live. If you want to be pedantic (and Wotan knows
I sometimes enjoy pedant status) you should be prefixing all your calls to things like 
mysql\_query() with a backslash. Try it out and see if I'm telling the truth.

So I'm scratching my head looking at this code. "What the hell, dude. I've got nothing to lose
by adding a backslash in front of IBL." Of course it worked. But why did it work? 

(Grumpy developer's note: I was asked on Twitter to expand a bit on the reasons behind why
things work this way. I am not a PHP internals guy so everything I say here is
just an educated guess)

With the introduction of namespaces, PHP has to operate under some assumptions. If
you are going to remain backwards-compatible with a lot of code and support namespaces
then you have to make some rules too. As far as I can tell, when PHP encounters an object
or function, it assumes that it is in the global namespace first. This is how you can do
things like $query = mysql\_query() and have it not complain. No prepended backslash, it
assumes it is in the global namespace.

Now, let's say I am trying to do this:

{% codeblock lang:php %}
$mapper = new IBL\FranchiseMapper($container['db\_connection']);
{% endcodeblock %}

There is no pre-pended backslash but there *is* a backslash after the IBL, therefore PHP can
assume that there are namespaces involved. Then (I think) it goes and looks to see if
there is currently an 'IBL' namespace that it has been asked to use. Because of the autoloader
it is aware of that namespace, so then it happily loads it. 

So why does it behave differently inside closures? I am not 100% sure, but if I had to
make an educated guess I would say that when trying to resolve namespaces inside
a closure, the interpretor doesn't assume that it is already inside the global namespace,
that it is in a namespace of it's own. Hence the need to explicitly declare that you
are starting with the global namespace (prepending the backslash) and then working
your way down.

If any PHP interals contributors read this blog post I would appreciate a follow-up 
comment to confirm and/or explain how this works.

So, it looks like closures are stricter and was reminding me, via that error message, 
that I need to be aware
of the current scope of the namespace (is that even the right way to put it?) 
and prepend that backslash so my autoloader (which is hooked into spl\_autoload\_register)
can, you know, find and create that object for me. So here's how it looks now

{% codeblock lang:php %}
$container = new \Pimple();
$container['db_connection'] = function ($c) {
    return new \PDO(
        'pgsql:host=localhost;dbname=ibl_stats', 
        'login',
        'pass' 
    );
};
$container['franchise_mapper'] = function ($c) {
    return new \IBL\FranchiseMapper($c['db_connection']);
};

$mapper = $container['franchise_mapper'];
{% endcodeblock %}

Yay! I can create a mapper via the dependency injection container.

I know that a lot of beginning to intermediate javascript programmers \*cough\*me\*cough\* have
to pay attention to variable/function/object scope issues as well. Also, don't be like me when
there are no tests for your code and start randomly changing things in hopes that it works.

It usually doesn't.

