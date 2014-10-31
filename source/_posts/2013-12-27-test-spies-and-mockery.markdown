---
layout: post
title: "Test Spies and Mockery"
author: Chris Hartjes
date: 2013-12-27
comments: true
sharing: true
---
While recording some screencasts I was struggling to figure out how to
get PHPUnit's built-in object mocking tools to allow me to create what is
known as a "test spy". I talk about them briefly in my [PHPUnit Cookbook](http://grumpy-phpunit.com)
but I think that what I wanted to do in this instance was beyond what PHPUnit
could give me.

I had some code-under-test that had a conditional statement inside a foreach()
loop (aggravating my desire to use [object calisthenics](http://www.slideshare.net/rdohms/bettercode-phpbenelux212alternate))
and I wanted to make sure that both branches of the conditional statement got
executed.

I first tried something like this:

{% codeblock lang:php %}
    // $db is our mocked database object based off stdClass for testing
    $db->expects($this->once())
        ->method('query')
        ->with($update, ['id' => 1]);
    $db->expects($this->once())
        ->method('query')
        ->with($delete, ['id' => 5]);
{% endcodeblock %}

I was using [Aura.Sql](http://auraphp.com/manuals/v1/en/sql/) and it's Update
and Delete objects. I wanted to be sure that I was using both objects.

I also tried using _$this->at(0)_ and _$this->at(1)_ as well, I got errors
ranging from "method query was not mocked" to problems complaining about
expected values not showing up at the expected sequence.

I knew there had to be a better way, but I really wanted just to use PHPUnit's
built-in mocking. I couldn't figure it out. So instead I turned to a mocking
library that I knew supported test spies: [Mockery](https://github.com/padraic/mockery).

The code reads a lot smoother:

{% codeblock lang:php %}
    // m is an alias to \Mockery
    $db = m::mock('stdClass');
    $db->shouldReceive('query')->with($update, ['id' => 1])->once();
    $db->shouldReceive('query')->with($delete, ['id' => 5])->once();
{% endcodeblock %}

The first thing that jumps out at me is that the Mockery version looks cleaner.
Well, really, it's only one less chained call. But looks do count for something.

More importantly, my test worked the first time with no weird error messaging
about unexpected behaviour.

So the next time you are writing a unit test and need to create spies on
methods of a mocked object, I cannot recommend enough that you take a look
at Mockery.
