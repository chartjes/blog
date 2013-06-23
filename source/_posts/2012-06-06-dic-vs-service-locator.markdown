---
layout: post
title: "DIC vs. Service Locator" 
author: Chris Hartjes
date: 2012-06-06
comments: true 
sharing: true 
---
People often ask me what's the one thing they could do for their code base
RIGHT NOW that will make it easier to test. To me, the answer is simple:
make sure you are using [Dependency Injection](http://en.wikipedia.org/wiki/Dependency_injection)
(yes the link is long and has code samples in Java, but whatever). Without
the ability to "inject" your dependencies into your code (whether it is 
class methods or functions) you will have problems testing modules of
code in isolation from each other.

In my [book on buiding testable PHP apps](http://grumpy-testing.com) I touched upon Dependency Injection
and I also mention the concept of a [Dependency Injection Container](http://martinfowler.com/articles/injection.html)
(sometimes also called Inversion of Control Containers). On the surface it
sounds like a really useful tool: you put all your dependencies inside the
container and then inject those dependencies into your classes and functions.

The use of DIC's has become a common pattern in PHP frameworks, as it does
offer you an easier way to access those dependencies. But I encourage people
to be careful with how they choose to use these containers, because they can
add unanticipated dependencies to your application.

If you use dependency injection without the container, then you have code that
looks like this:

{% codeblock lang:php %}
<?php
namespace Grumpy;

class Foo
{
    protected $_bar;
    protected $_baz;

    public function __construct(\Grumpy\Bar $bar, \Grumpy\Baz $baz) {
        $this->_bar = $bar;
        $this->_baz = $baz;
    }
}

// In our test, using PHPUnit's built-in mock support
$mockBar = $this->getMock('\Grumpy\Bar');
$mockBaz = $this->getMock('\Grumpy\Baz');

$testFoo = new \Grumpy\Foo($mockBar, $mockBaz);

{% endcodeblock %}

Very straightforward to see the dependencies that we are trying to inject
into the class, and you can see exactly what dependencies you will have to
create mock objects for in your tests.

If you use a container as a container ONLY then your test setup changes 
a bit.

{% codeblock lang:php %}
<?php

/**
 * Code for Foo is the sanme but how we get the dependencies is different
 * because we are going to place them in the container first and then
 * explicitly inject them
 */
$container = Context::getDependendencyContainer();
$container['bar'] = $this->getMock('\Grumpy\Bar');
$container['baz'] = $this->getMock('\Grumpy\Baz');

$testFoo = new \Grumpy\Foo($container['bar'], $container['baz']);

{% endcodeblock %}

The purpose of the DIC is to have all your dependencies in one place
where they are easier to grab. It's a great concept, but it can easily
morph into a new dependency with one architectural change.

{% codeblock lang:php %}
<?php
namespace Grumpy;

class Foo
{
    protected $_bar;
    protected $_baz;

    public function __construct(\Grumpy\Container $container) {
        $this->_bar = $container['bar'];
        $this->_baz = $container['baz'];
    }
}

// In our test, using PHPUnit's built-in mock support
$mockBar = $this->getMock('\Grumpy\Bar');
$mockBaz = $this->getMock('\Grumpy\Baz');
$mockContainer = $this->getMock('\Grumpy\Container');
$mockContainer['bar'] = $mockBar;
$mockContainer['baz'] = $mockBaz;

$testFoo = new \Grumpy\Foo($mockContainer);

{% endcodeblock %}

So what is so potentially bad about this? Well, now you've introduced a
dependency into your code such that it relies on the dependency container
instead.

I've worked with code bases that make heavy use of containers to do more
things than just store dependencies to be injected into your code. If 
you've every used Zend\_Registry to store things that you then retrieve
later you will know what I am talking about. 

So what is really the difference between a service locator and a 
dependency injection container? I think the difference is in how you
use them. If you are using a container and manually injecting dependencies
into your code, then you are using what I guess you could call a 
"pure" dependency injection container. Once you start injecting
the container itself into your objects, it's no longer just a container.
It's a service locator since you will use it to retrieve all sorts of
things your application might need. 

I understand why people use the container that way. It's easy! It's
convenient. It's a pain in the ass to test, is what it is.

In the end, it's really an architectural choice that you need to make.
Personally, I prefer to combine the two: use the container to store
you dependencies but "manually" inject them into your classes and
functions. I prefer this technique because it makes it easier up front
to determine the dependencies the code you are testing are going
to need.

Remember kids, the
goal is to create code that is easily understood and easily testable, 
or else [this guy](http://twitpic.com/9p5o2x/full) might come looking
for you to "ask you some questions about your code".






