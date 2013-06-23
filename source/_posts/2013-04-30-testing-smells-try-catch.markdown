---
layout: post
title: "Testing Smells - try/catch"
author: Chris Hartjes
date: 2013-04-30
comments: true
sharing: true
---
As part of a project to migrate the PHP code at [work](http://synacor.com)
from PHP 5.2 to PHP 5.4, I'm using our extensive test suite to look for instances
where something that changed between the versions of PHP that we are using
has caused some unexpected behaviour.

In one of our code bases, I found some tests that are exhibiting a test smell
through their use of a try / catch block in the test itself.

Here's a totally-contrived example:

{% codeblock lang:php %}
    <?php
    public function testThatExceptionIsThrown()
    {
        // Use a helper to give us a ready-to-go parser
        $parseHelper = $this->getHelper('parseHelper');

        /**
         * If we pass a string as the first parameter to parseGrumpyRambling
         * instead of an array, we should get an exception generated because
         * we are using a type hint
         */
        try {
            $weirdCanadianWords = '';
            $phrase = "No doot aboot it, we're gonna win at hockey!";
            $parsedText = $parseHelper->parseGrumpyRambling(
                $weirdCanadianWords,
                $phrase
            );
            $this->fail();
        } catch (Exception $e) {
            $this->assertContains(
                'must be of the type array, string given',
                $e->getMessage()
            );
        }
    }
{% endcodeblock %}

Okay, so why does this test offend me so much?

First, I am of the opinion that writing a test to check to make sure you are
enforcing type hinting for your class method parameters is probably not a
good use of your time. I mean, what potential problem are you catching?

Consider the following:

* you likely have access to info about what type of value each parameter
is expected to be
* you are probably much better off filtering for parameter type before you
even call that method

I can say with confidence that a test like this is returning very little
value for the effort.

Second, putting any logic inside your unit tests is a great way to end
up with unexpected results. Need an "if" statement? Write two tests
for that condition. Need a switch / case? Again, one test per case is a
much better way to logically divide things up.

The worst thing about using try / catch is that *PHPUnit gives you two built-in
methods to not ever have to use it*. I've had people say to me "but Chris,
if you use try / catch you get much better control over determining where
in the process to test that the exception was thrown." I don't buy it, and
I will try and explain why.

If you are using docblocks on your tests (which you should) it is super easy
to indicate what exception you are expecting to be thrown.

{% codeblock lang:php %}
    <?php
    /**
     * @expectedException Exception
     * @expectedExceptionMessage must be of the type array 
     */
    public function testThatExceptionIsThrown()
    {
        // Use a helper to give us a ready-to-go parser
        $parseHelper = $this->getHelper('parseHelper');

        /**
         * If we pass a string as the first parameter to parseGrumpyRambling
         * instead of an array, we should get an exception generated because
         * we are using a type hint
         */
        $weirdCanadianWords = '';
        $phrase = "No doot aboot it, we're gonna win at hockey!";
        $parsedText = $parseHelper->parseGrumpyRambling(
            $weirdCanadianWords,
            $phrase
        );
    }
{% endcodeblock %}

Now we have a much cleaner-looking test with no conditional logic inside it.

You can also choose to use a built in PHPUnit method to set what exception
you are expecting.

{% codeblock lang:php %}
    <?php
    public function testThatExceptionIsThrown()
    {
        $this->setExpectedException(
            'Exception',
            'must be of the type array'
        );

        // Use a helper to give us a ready-to-go parser
        $parseHelper = $this->getHelper('parseHelper');

        /**
         * If we pass a string as the first parameter to parseGrumpyRambling
         * instead of an array, we should get an exception generated because
         * we are using a type hint
         */
        $weirdCanadianWords = '';
        $phrase = "No doot aboot it, we're gonna win at hockey!";
        $parsedText = $parseHelper->parseGrumpyRambling(
            $weirdCanadianWords,
            $phrase
        );
    }
{% endcodeblock %}

Again, a much cleaner-looking test with no conditional logic in sight.

On Twitter Brian Fenton shared a [blog post](http://www.brianfenton.us/2011/09/bad-practice-setting-expected.html)
he wrote back in 2011 that disagrees with me. In it he very briefly talks about
why you should use try / catch in your tests, but I feel like he is contradicting
himself when he talks about why.

Basically, Brian is concerned about how @expectedException and _setExpectedException()_
can be triggered by other errors in your tests (including other exceptions
being unexpectedly triggered. He feels that by using try / catch you have
much better control over when and where you wish to trigger an exception.

To quote Brain's post:

> "The basic idea here is that the most specific test is best, because
> you have the least likelihood of a false negative or a test error slipping
> through the cracks."

If you are making sure that every test is the most specific test that you
can write, then you NEVER have to worry about whether or not some other
code under test is throwing an exception or other error that is messing up
the current test.

Using try-catch because you want to not miss errors that might occur before
you deliberately throw an exception is a sign that you are doing too much
in that test.

A test failure is a test failure, no matter what caused it. The harder you
work to make sure that a test is actually testing the most specific thing
possible, the less likely you have to worry about the things that Brian
feels require him to use try / catch.

This is the same reason I don't like seeing tests like this:

* do Task A 
* do an assertion on the results of Task A
* do Task B 
* do an assertion on the results of Task B

Those are really two separate tests, so split them up. In fact, you could 
write two tests that look like this:

* do Task A
* do an assertion on results of Task A

* do Task A
* do Task B
* do an assertion on the results of Task B

That second test doesn't need to re-assert that Task A did it's job because
Task A was already covered in the previous test.

Test smells, testing anti-patterns, whatever you want to call them, do exist
and many programmers are often unaware of the consequences of those decisions
are.

Keep your tests small, keep them very specific, and don't use conditional
logic in your tests. I have yet to see a specific example where the use
of conditional logic did anything except reduce the amount of lines of
code a grumpy developer didn't want to type.
