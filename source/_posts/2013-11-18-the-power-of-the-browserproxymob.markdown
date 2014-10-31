---
layout: post
title: "The Power of the BrowserProxyMob"
author: Chris Hartjes
date: 2013-11-18
comments: true
sharing: true
---
At [work](http://synacor.com) I have been involved with an effort to put some
automated front-end testing in place. The combination of [Behat](http://behat.org),
[Mink](http://mink.behat.org) running tests using [PhantomJS](http://phantomjs.org)
is a good one for this. Open source, easy to configure, handles JavaScript-heavy
pages reasonably well.

There was just one wrinkle in our plans: our use of local host files.

Somewhere back in the mists of time it was decided that in order to properly
test our web applications without pummelling our production assets (like
image farms, content servers, API end points) that a "hostfile generator"
would be created and is accessible on every machine in our development VM
network.

You hit <hostname>/hosts and it spits out a file that you can use on your
laptop to alias production assets / resources / whatever to things on your
development server. I use a program on my MacBook called [Gas Mask](http://www.clockwise.ee/gasmask/)
that lets me quicky switch between host files when testing out sites on
various development boxes. I am sure a similar tool exists for Windows and
Linux users.

So, initially the only way to make Behat play nicely with the host files was
to manually over-write the /etc/hosts file on the development server with
the host-specific one the generator gives us. That way all the host aliases
in place.

This is fine and all, but I am pretty sure our sysadmins would never allow
the user that runs our continuous integration jobs have the proper permissions
to  overwrite the host files. If a test run were to crash and generate fatal
errors, we would end up with a machine with a bad host file in place.

So clearly what was needed was a proxy. After doing a little bit of digging
around I found a solution: [BrowserMobProxy](http://bmp.lightbody.net/). While
it bills itself as a tool for helping web developers "watch and manipulate
network traffic from their AJAX applications" it also has a feature that
is of great interest to our problem: it supports the ability to create aliases
to hosts...oddly enough just like we do with our host files at work.

So, BrowserMobProxy is great in that you can send requests to REST-style but
I didn't want to mess around with manual calls, so I was happy to find that
my friend [Adam Goucher](http://element34.ca) had written a PHP library for
interacting with it. I forked his code, cleaned it up a little and it's
now available via [Packagist](https://packagist.org/packages/chartjes/php-browsermob-proxy)
and ready to install via [Composer](http://getcomposer.org).

So, let's get started with what I did.

Here's my composer.json file for the project

{% codeblock lang:json %}
{
    "require": {
        "behat/behat": "2.4.*@stable",
        "behat/mink": "1.4@stable",
        "behat/mink-extension": "*",
        "behat/mink-goutte-driver": "*",
        "behat/mink-selenium2-driver": "*",
        "chartjes/php-browsermob-proxy" "dev-master",
        "sauce/connect": ">=3.0",
        "sauce/sasuage": ">=0.5",
    },
    "config": {
        "bin-dir": "bin/"
    }
}
{% endcodeblock %}

We are experimenting with using [SauceLabs](http://sauce.io) for testing our
sites on mobile devices (in case you were wondering).

With that stuff installed, I next downloaded a copy of BrowserMobProxy (herafter referred to as BMP) and
copied the CLI runner and JAR files into the 'bin' directory. Next, I installed
PhantomJS in /usr/local/bin on my server.

Next, we setup our Behat configuration file to point to PhantomJS when doing
our tests using Selenium2's web driver capabilities:

{% codeblock lang:yaml %}
phantomjs:
    context:
        class: "FeatureContext"
    extensions:
        Behat\MinkExtension\Extension:
            default_session: selenium2
            javascript_session: 'selenium2'
            base_url: http://synacor.com
            selenium2:
                wd_host: http://127.0.0.1:4444/wd/hub
{% endcodeblock %}

Now, we get to the tricky part.

BMP requires you to connect to it first to get it to start a
proxy connection running on a *different* port than the one the main service
runs on. In my Behat test runner script I use the PHP BMP library to create
a connection, and it assigns it to the first available port in a range you
can specify at run time.

Because I can count on this value to be the same all the time, I then start
up an instance of PhantomJS telling it to run in "accept requests like I am
WebDriver compatible" proxy all requests through BMP

{% codeblock %}
/usr/local/bin/phantomjs --webdriver=4444 --proxy=http://localhost:9091
{% endcodeblock %}


In my Behat context class I add in a step that reads in the host file via
our host file generator and assigns the host aliases to BMP so that when
Behat uses PhantomJS to load web pages, it will use the host aliases set
within BMP.

I know that it's pretty convoluted, but I know with 100% certainty that it
works.

If you spot anything here that doesn't make sense, let me know and I will
update the post.
