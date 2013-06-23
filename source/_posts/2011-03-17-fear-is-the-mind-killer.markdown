---
layout: post
title: Fear is the mind-killer
---
Dune is probably my favourite science-fiction novel of all time.
It's in a cool settings, with some really well-designed characters,
and is a sprawling epic in the way that sprawling epics should be.
In that book, the main character Paul Atreides learns the ways of
the mysterious Bene Gesserit through his mother. One of the things
he learns is called the *litany against fear*, something they say
to themselves whenever they are in danger:

> *I must not fear.* Fear is the mind-killer. Fear is the
> little-death that brings total obliteration. I will face my fear. I
> will permit it to pass over me and through me. And when it has gone
> past I will turn the inner eye to see its path. Where the fear has
> gone there will be nothing. Only I will remain.

Living on the bleeding edge of technology means you spend a lot of
time trying to convince the people around you that this awesome bit
of technology that you've noticed is worth investigating. I
remember being mocked and dismissed over my thoughts on
[memcached](http://www.memcached.org/) in 2003. And being mocked
and dismissed on my thoughts on how valuable writing automated
tests could be for an out-of-control code base in 2004. It's now
2011 and both of those things are considered integral parts of best
practices for web applications.

Some of the problems I faced were due to an abrasive personality
very early in my programming career (although some would argue that
not much has changed) that resulted in ideas being rejected because
of who the messenger is. Let's be honest, we've all done that:
dismissed information because of who was delivering it. I've gotten
used to facing the uphill battle to get my particular set of
programming practices accepted but it is a battle I'm winning.

But there is often another reaction to new technologies. That
reaction is fear. Fear of working with a set of technologies they
are not comfortable with. Fear of automated systems deploying code
that might not be adequately tested. Fear of putting effort into
things that provide very little benefit in the short-term but lots
of benefits in the long-term. Fear is the mind-killer, the little
voice in your head telling you that you are not good enough, that
your ideas are crap, that you have no idea what you're talking
about.

Seth Godin talks about how when a technology has been labeled dead
that
[the real cool stuff can happen](http://sethgodin.typepad.com/seths_blog/2011/03/bring-me-stuff-thats-dead-please.html)
with it. PHP has been labeled dead by the "drive-by technorati"
that Mr. Godin talks about, despite the fact that it still
well-positioned as a tool to be used when building web
applications. At the same time, I can feel that tickle of fear in
my brain. "Don't get left behind" is whispers to me. "Drop PHP for
Technology X" it pleads to me. When the voice gets too loud, I
start reciting the litany against fear. There is still lots of
innovation to be done within PHP itself. Each successive release of
PHP is getting faster and (quite correctly) implementing features
that have made other scripting languages interesting. Exhibit A?
[Anonymous functions](http://ca.php.net/manual/en/functions.anonymous.php),
allowing for some very interesting code to be written. It's an
integral part of the newest [breed](http://lithify.me/)
[of](https://github.com/symfony/symfony)
[frameworks](https://github.com/zendframework/zf2).

Don't let fear dictate the technologies you use. Today, I am most
comfortable building web applications using PHP with some
Javascript thrown in to improve the user experience. Tomorrow, it
will be a different story. Not literally tomorrow. You know what I
mean. I've been adding Python,
[Django](https://github.com/chartjes/ibl),
[Flask, and Google App Engine](https://github.com/chartjes/liesitoldmykids)
to the skill set. To be blunt, being a mono-ecosystem (ie PHP only)
specialist is a very risky for someone with the "Jack of all
trades" career path such as mine. Far better to be
[standing on the shoulders of giants](http://en.wikipedia.org/wiki/Standing_on_the_shoulders_of_giants)
than to just stay only where you are comfortable.

I guess the point I'm trying to get across is that you can use the
*litany against fear* as a tool to motivate to truly analyze your
reactions to situations. For example, I'm having a very hard time
figuring out how to get Zend Framework + PHPUnit to adequately test
the ability of an application at work to use Facebook Connect. I
just can't get it to do things with a regular request, for a bunch
of reasons I'm unable to understand. I can't peer inside the
request to the extent I would like. I foresee having to drop down a
level in the application and admit that I cannot test the request
itself, but the code that is executed after control is returned to
the application.

Fear would say "give up because it's too hard to properly test
things". The reality is that while I cannot test the *output* of
the request, I can certainly test what is supposed to be going on
behind the scenes. Tests like that are just as valuable as being
able to capture the response from a request and verify that
elements exist in the DOM as expected. Perhaps one day there will
be better tools in PHP to accomplish this task. I know it can be
done
[using other tools](http://opensoul.org/blog/archives/2009/03/05/testing-facebook-with-cucumber/)
and I'll be honest here: it makes me bark out a few choice words
about the state of PHP testing tools.

So, here's my second Idea of March: Fear is the mind-killer for
your skill-set.
