---
layout: post
title: "Data providers and arrays"
author: Chris Hartjes
date: 2013-10-26
comments: true
sharing: true
---
I was asked a question on Twitter by [Tex Morgan](https://twitter.com/tex_morgan) 
about a problem he was having with [PHPUnit data providers](http://phpunit.de/manual/current/en/writing-tests-for-phpunit.html#writing-tests-for-phpunit.data-providers). He was trying to pass in some data and kept wondering
why PHPUnit was serializing the data instead of doing what he was expecting.

{% codeblock lang:php %}
public function preLoaderArrayDataProvider()
{
    return array("one" =>
        array(
            'http://yahoo.com',
            'http://google.com',
            'http://facebook.com',
            'http://twitter.com'
        ), "two" =>
        array(
            "http://jquery.com",
            "http://jqueryui.com"
        )
    );
}

/** testSetArray
 * @dataProvider   preLoaderArrayDataProvider
 */
public function testSetArray($array)
{
    $this->expected = true;
    $this->actual = $this->object->setArray($array);
    $this->assertEquals($this->expected, $this->actual);
}
{% endcodeblock %} 

I see what Mr. Morgan was trying to do, and more importantly why it wasn't
working. The problem he was running into has to deal with how PHPUnit expects
data to be sent by the data providers.

The method under test is expecting one parameter that consists of an array.
Data providers are supposed to return an array of arrays, where each element
of the inner array maps to a parameter the method under test is expecting.

So what went wrong? The data provider is passing in 5 strings as a parameter.
Here's the results:

{% codeblock %}
PHPUnit 3.7.28 by Sebastian Bergmann.

FF

Time: 28 ms, Memory: 2.50Mb

There were 2 failures:

1) TexTest::testSetArray with data set "one" ('http://yahoo.com', 'http://google.com', 'http://facebook.com', 'http://twitter.com')
Failed asserting that false matches expected true.

/Users/chartjes/src/php-test-bootcamp-practice/tests/TexTest.php:29

2) TexTest::testSetArray with data set "two" ('http://jquery.com', 'http://jqueryui.com')
Failed asserting that false matches expected true.

/Users/chartjes/src/php-test-bootcamp-practice/tests/TexTest.php:29

FAILURES!
Tests: 2, Assertions: 2, Failures: 2.
{% endcodeblock %}

The fix is easy. The method under tests is expecting one parameter that is an
array, so let's give it one.

{% codeblock lang:php %}
public function preLoaderArrayDataProvider()
{
    return array("one" =>
        array(
            array(
                'http://yahoo.com',
                'http://google.com',
                'http://facebook.com',
                'http://twitter.com'
            )
        ), "two" =>
        array(
            array(
                "http://jquery.com",
                "http://jqueryui.com"
            )
        )
    );
}
{% endcodeblock %} 

The result?

{% codeblock %}
PHPUnit 3.7.28 by Sebastian Bergmann.

..

Time: 17 ms, Memory: 2.25Mb

OK (2 tests, 2 assertions)
{% endcodeblock %}

Problem solved. Hope this helps you give a better understanding of how
PHPUnit data providers work. 

