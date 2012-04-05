---
layout: post
title: "Metatesting: Testing Constructors" 
author: Chris Hartjes
date: 2012-04-05
comments: true 
sharing: true 
---
If you have a PHP application that makes heavy use of objects (which is probably
95% of you reading this) then you will have objects with constructor methods
in them. It is also very likely that there is some stuff going on in those
constructors. So how do you test things like this?

Here is the constructor method that we are trying to test:

{% codeblock lang:php %}
<?php

class Alpha
{
    protected $_foo;
    protected $_bar;
    protected $_baz;

    public function __construct()
    {
        $container = Grumpy_Container::getInstance();
        $alphaConfig = $container->alphaConfig();
        $this->_foo = $alphaConfig->foo;
        $this->_bar = $alphaConfig->bar;
        $this->_baz = $alphaConfig->baz;
    }

    // the rest of our class is here
}
{% endcodeblock %}

In this example, Grumpy\_Container is an object that is available via
autoloading and it is used as a dependency injection container (DIC).

Okay, so how do we test that the constructor is doing what it is supposed to?
We would want to verify that those protected class attributes have been set
to values we are expecting.

In order to do that we will also need to override the values in our DIC so 
when we run the test we have values in there we are expecting.

{% codeblock lang:php %}
<?php

public testConstructorAssignsExpectedAttributeValues()
{
    $container = Grumpy_Container::getInstance();
    
    // Create our mock configuration object
    $alphaConfig = new stdClass();
    $alphaConfig->foo = 'testfoo';
    $alphaConfig->bar = 'testbar';
    $alphaConfig->baz = 'testbaz';

    // Place this back in the container to override what we have
    $container->alphaConfig = function() use ($alphaConfig) {
        return $alphaConfig;
    };

    // Create our mock object
    $alphaTest = $this->getMockBuilder('Alpha')
        ->disableOriginalConstructor()
        ->getMock();

    // Manually run the constructor
    $alphaTest->__construct();

    // Check for values we expect
    $this->assertAttributeEquals(
        $alphaConfig->foo,
        '_foo',
        $alphaTest,
        'Should set expected foo config value'
    );
 
    $this->assertAttributeEquals(
        $alphaConfig->bar,
        '_bar',
        $alphaTest,
        'Should set expected foo config value'
    );

    $this->assertAttributeEquals(
        $alphaConfig->baz,
        '_baz',
        $alphaTest,
        'Should set expected bar config value'
    );

}

{% endcodeblock lang:php %}

The magic method here is assertAttributeEquals(). It lets you check the value
inside any protected or private class attributes, which is absolutely a 
requirement in this example. It is probably better to have some other
publicly-available methods that can return us the protected (or in some
cases private because you don't want anyone to manipulate them) attributes.

Hope this helps you understand some ways to test your constructors.
 

 
