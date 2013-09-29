---
layout: post
title: "Testing Listeners"
author: Chris Hartjes
date: 2013-09-27
comments: true
sharing: true
---
I had an idea to put together some kind of "PHP Testing Koans" site as a way
to help PHP developers get better at learning how to actually write tests. Most
developers who are introduced to testing get blocked at the point of actually
writing a test. This, in my opinion, has been part of my advocacy that I 
have been struggling to find a good way to teach to people.

So I started to brainstorm ways to make it happen. With some help from [Joel Clermont](https://twitter.com/jclermont)
I stumbled upon using test listeners for this.

To be completely fair, I first ran across test listeners when [Alvfaro Videla](https://twitter.com/old_sound)
showed me a blog post he had written on how to [write unit tests for RabbitMQ](http://videlalvaro.github.io/2013/04/using-rabbitmq-in-unit-tests.html).
It's a very imaginative use of them, so I wondered if I could bend those test
listeners to my will.

From a high-level view, test listeners in PHPUnit are bits of code designed
to be executed whenever a test suite or individual test is run. For the example
of dealing with RabbitMQ, this makes total sense.

Imagine how happy I was to find that I could use it to determine if a particular
test existed. So how did I do it?

{% codeblock lang:php %}
<?php

class Koan1Listener extends PHPUnit_Util_Printer implements PHPUnit_Framework_TestListener
{
    private $expected_tests = array();
    private $found_tests = array();

    public function __construct()
    {
        $this->expected_tests = array('testHelloWorld');
    }

    public function __destruct()
    {}

    public function startTestSuite(PHPUnit_Framework_TestSUite $suite)
    {
    }
    
    public function endTestSuite(PHPUnit_Framework_TestSuite $suite)
    {
        foreach ($this->expected_tests as $test) {
            if (!in_array($test, $this->found_tests)) {
                throw new Exception("Missing test {$test}");
            }
        }
    }

    public function addError(PHPUnit_Framework_Test $test, Exception $e, $time)
    {}

    public function addFailure(PHPUnit_Framework_Test $test, PHPUnit_Framework_AssertionFailedError $e, $time)
    {}

    public function addIncompleteTest(PHPUnit_Framework_Test $test, Exception $e, $time)
    {}

    public function addSkippedTest(PHPUnit_Framework_Test $test, Exception $e, $time)
    {}

    public function startTest(PHPUnit_Framework_Test $test)
    {
        $test_names = get_class_methods($test);

        foreach ($test_names as $test_name) {
            $this->found_tests[] = $test_name;
        }
    }

    public function endTest(PHPUnit_Framework_Test $test, $time)
    {}
}

{% endcodeblock %} 

When you create a listener, you are implementing all the required methods
for *PHPUnit_Framework_TestListener*. You can see that there are a lot of
them, but in this instance all we needed were *endTestSuite* and *startTest*.

The approach is simple: for each test class that gets executed, add the names
of all the methods to an internal list. When the entire test suite is finished,
we then check to see if the test names that we were expecting are in our
list of methods we found. I am sure there is a more efficient way to do it, 
so let me know in the comments of a different approach.

In the case of the example listener, I wanted to make sure that the person
doing the first exercise has a test called *testHelloWorld* written. As more
koans (or whatever you want to call them) get created, I can use test listeners
to make sure that all the tests, and data providers, and internal class methods
designed to improve code reuse are actually getting written.

Despite all my years of using these tools, I still find things that I didn't 
know about that can be (ab)used to accomplish certain goals.

I hope you find that something you thought you couldn't figure out becomes
possible using test listeners. 
