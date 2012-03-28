---
layout: post
title: "Metatesting: Understanding Mock Objects" 
author: Chris Hartjes
date: 2012-03-27
comments: true 
sharing: true 
---
One of the things that I have learned to quickly appreciate about working at
[Kaplan Professional](http://kaplanprofessional.com) is the very large suite
of unit and integration tests. I believe there are 2000+ tests, and although
there has been a dip in code coverage, it is still impressive to see coverage
levels for most things in the 65%+ range. We'll get it back up to where it
belongs in no time.

With such an extensive array of tests, I have received an education in what
it really means to write unit tests for live, production-ready code that really
takes unit testing seriously. I think that the biggest problem that most
developers face when getting into Test Driven Development is not understanding
of how to efficiently use mock objects.

If you are really writing your unit tests the way you should, each test is
focusing on testing one bit of functionality in isolation, which means that
you will be heavily relying on mock objects to make things work. I've come
up with an example scenario that I hope goes a long way to explaining how
to effectively use mock objects.

In these examples I am using PHPUnit's [built-in support](http://www.phpunit.de/manual/3.0/en/mock-objects.html)
for mock objects. At Kaplan our testing engineer told me that he likes to use
[Mockery](https://github.com/padraic/mockery) but there were problems getting
it to play nicely with the dependency injection container that is in use (it's
a customized version of [Pimple](http://pimple.sensiolabs.org). Can't argue
with that. Not until I experiment with Pimple myself to see if it gains us
anything instead of using what comes with PHPUnit.

So here is our scenario: we have a class called Alpha, that contains a method
called munge(). We wish to test that method in a unit tests. So what does
this class look like?

{% codeblock lang:php %}
<?php

class Alpha
{
    // Omit code showing constructor...

    public function munge(Foo $foo, Bar $bar)
    {
        $fooDetails = $foo->getDetails();
        $fooId = $foo->getId();

        $barStartDate = $bar->getStartDate();
        $barEndDate = $bar->getEndDate();

        $source = "{$fooId}|{$fooDetails}|{$barStartDate}|{$barEndDate}";
        
        return md5('rocksalt' . $source);
    }
}
{% endcodeblock %}

My grumpy tester's eye looks at that and immediately says "we will need to 
mock those Foo and Bar objects to make this test work." First we need to look
at the Foo object

{% codeblock lang:php %}
<?php
class Foo 
{
    // Omit code showing how we construct a Foo object

    public function getId()
    {
        return $this->_id;
    }

    public function getDetails()
    {
        $tree = $this->_tree;
        $branch = $this->_branch;

        return $tree . '->' . $branch;
    }
}
{% endcodeblock %}

So it looks like this class represents 1 "Foo" object in the system. I omitted
the constructor as it's not really important to the lesson I'm trying to teach
here. Let's assume we have a way to generate a Foo object via some sort of
mapper. 

Our Alpha->munge() method expects to be passed in a Foo object and to retrieve
info via getDetails() and getId() calls. Let's start our test and mock that up.

{% codeblock lang:php %} 
<?php
class Test extends PHPUnit_Framework_TestCase
{

    public function testAlphaMunge()
    {
        $mockFoo = $this->getMockBuilder('Foo')
            ->setMethods(array('getDetails', 'getId'))
            ->disableOriginalConstructor()
            ->getMock();
        $mockFoo->expects($this->once())
            ->method('getDetails')
            ->will($this->returnValue('1->2');
        $mockFoo->expects($this->once())
            ->method('getId')
            ->will($this->returnValue('1');

        // More test fun to come
    }
}
{% endcodeblock %}

When you build a mock for use in your test, you generally have to do two things:

* create a mock of the object itself
* tell it what to do when specific methods are called

What I've done here is pretty standard EXCEPT for the use of that disanleOriginalConstructor()
method. Why is it used? Well, sometimes when you are creating a mock of an object
it will often have a constructor that accepts parameters. I'm not testing to see
if we can create the object, I merely am trying to simulate some of the methods
of that object.

Once I've created the mock of the object, I then tell this mock object what
to do when I make certain method calls. Clearly I've just pulled some 
arbitrary values out of my ass for this example, but usually you can figure
out what some reasonable return values are supposed to be by, you know, actually
looking at the code you are mocking.

So what does our Bar object look like?

{% codeblock lang:php %}
<?php
class Bar
{
    // Same drill, no need to show constructor details
    
    public function getStartDate()
    {
        return $this->_startDate;
    }

    public function getEndDate()
    {
        return $this->_endDate;
    }
}
{% endcodeblock %}

Time to add a mock Bar to our test

{% codeblock lang:php %}
<?php
class Test extends PHPUnit_Framework_TestCase
{
    public function testAlphaMunge()
    {
        $mockFoo = $this->getMockBuilder('Foo')
            ->setMethods(array('getDetails', 'getId'))
            ->disableOriginalConstructor()
            ->getMock();
        $mockFoo->expects($this->once())
            ->method('getDetails')
            ->will($this->returnValue('1->2');
        $mockFoo->expects($this->once())
            ->method('getId')
            ->will($this->returnValue('1');

        $mockBar = $this->getMockBuilder('Bar')
            ->setMethods(array('getStartDate', 'getEndDate'))
            ->disableOriginalConstructor()
            ->getMock();
        $mockBar->expects($this->once())
            ->method('getStartDate')
            ->will($this->returnValue('2012-03-27');
        $mockBar->expects($this->once())
            ->method('getEndDate')
            ->will($this->returnValue('2012-04-09');

        // More test fun to come
    }
}
{% endcodeblock %}  

A quick note about $this->once(): when you mock the objects you can tell it
how often you expect that method to be called. This is usefull if you need
to make sure you ONLY call something once or if it needs to behave differently
the second time you call. In a lot of cases you can probably be lazy and
just use $this->any() but I tend to stick with $this->once() unless I know
otherwise.

So now we have our two objects mocked. Now we can go back to our test and
add in the creation of our Alpha class, inject the two mocks into the 
method we are testing, and check for expected results.

{% codeblock lang:php %}
<?php
class Test extends PHPUnit_Framework_TestCase
{
    public function testAlphaMunge()
    {
        $mockFoo = $this->getMockBuilder('Foo')
            ->setMethods(array('getDetails', 'getId'))
            ->disableOriginalConstructor()
            ->getMock();
        $mockFoo->expects($this->once())
            ->method('getDetails')
            ->will($this->returnValue('1->2');
        $mockFoo->expects($this->once())
            ->method('getId')
            ->will($this->returnValue('1');

        $mockBar = $this->getMockBuilder('Bar')
            ->setMethods(array('getStartDate', 'getEndDate'))
            ->disableOriginalConstructor()
            ->getMock();
        $mockBar->expects($this->once())
            ->method('getStartDate')
            ->will($this->returnValue('2012-03-27');
        $mockBar->expects($this->once())
            ->method('getEndDate')
            ->will($this->returnValue('2012-04-09');

        $testAlpha = new Alpha();
        $expectedMunge = '57fc444798b313a9a4839ddb36d319e1';
        $munge = $testAlpha->getMunge($mockFoo, $mockBar);

        $this->assertEquals(
            $expectedMunge,
            $munge,
            'Munge value should match expected'
        );
    }
}
{% endcodeblock %} 

And there you have it! A test for a specific method that uses mocks to properly
isolate functionality that is required for the test to work.

I hope this blog post makes things a lot clearer when it comes to understanding
the role of mocks when creating unit tests.
