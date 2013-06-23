---
layout: post
title: "Yummy sauce on my Behat" 
author: Chris Hartjes
date: 2012-06-20
comments: true 
sharing: true 
---

At [work](http://www.kaplanproffessional.com) we have started creating a suite of
automated user acceptance tests, using [Behat](http://behat.org), [Mink](http://mink.behat.org)
using selenium [Zombie.js](http://zombie.labnotes.org/) and [Selenium](http://seleniumhq.org/)
as our browser drivers.

I will be honest: I have been less-than-happy with Zombie.js' performance. It has a feel
of being unfinished and newer versions of it don't work correctly with the Behat + Mink
combo. Given that we already had some [smoke tests](http://en.wikipedia.org/wiki/Smoke_testing)
that use Selenium, we decided to have some of our AUAT's use Zombie and some use Selenium.
After a while, I get tired of seeing a test run just fine using Selenium but fail using
Zombie.js.

I have been pushing us every-so-slightly towards using VM's for doing our development. Getting
Zombie.js installed and available for running Behat tests isn't a big problem, but given how
flaky it has been for me and the proven use of Selenium for our tests that require the use
of Javascript I wanted people to be able to use Selenium even though they are using a 
Linux VM.

Enter [Sauce Labs](http://saucelabs.com), a software-as-a-service product that allows you to 
use Selenium to run tests in browsers that are running on VM's in Sauce Lab's own infrastructure.
Basically, if you could use Selenium on your local machine you could do the same thing using
Sauce Labs. 

For us, we're interested in using their Even better is that you can make it work using Behat + Mink 
and the Selenium RC1 drivers. The [WebDriver](http://seleniumhq.org/docs/03_webdriver.html) stuff for 
Selenium 2 does not work with the Sauce Labs On Demand service. If I've understood correctly what
the lead developer being Behat [@everzet](https://twitter.com/everzet) said to me, Sauce Labs is
working on a Selenium 2 / Webdriver extension for use with Behat. I'm sure I'll be corrected if
I am wrong.

So what did we do in order to get our tests running on Sauce Labs? These instructions already
assume that you have installed Behat, Mink and any other support libraries and tools you need.
Check out [this blog post from Sauce Labs](http://sauceio.com/index.php/2012/01/adding-sauce-to-behat/)
for details on how to get that all sorted out.

## Step 1: Go create an account with Sauce Labs

I created the free one, contains plenty of testing minutes to allow you to play
with it. 

I'll wait here while you go and do that.

## Step 2: Go download [Sauce Connect](https://saucelabs.com/connect)

From their web site:

> Sauce Connect securely proxies browser traffic between Sauce Labs' 
> cloud-based VMs and your local servers. Connect uses ports 443 and 80 for 
> communication with Sauce's cloud. Most companies allow this without 
> special exceptions. 

As far as I can tell, Sauce Connect sets things up so that when you tell Behat + 
Mink to run some tests on a Selenium browser located at 'ondemand.saucelabs.com'
that Sauce Lab's infrastructure knows how to connect with the application you're
testing. This sort of architecture is incredibly important if you are having to test
things (like we do) only exist on a VPN and have no public-facing URLs.

Follow the directions on the web site on how to install it, run it, and
some tips for troubleshooting. Can't say I agree with their suggested method of monitoring
and making sure it stays up (c'mon people, just use [Supervisor](http://supervisord.org/))
but otherwise the instructions are easy to follow.

## Step 3: Modify your Behat configuration files to use Sauce Labs On Demand service

Of course, your behat config file looks different, but here's how ours looked
(scrubbed to remove any sensitive info)

{% codeblock lang:yml %}
default:
  paths:
    features:   %%BEHAT_CONFIG_PATH%%/features
    bootstrap:  %%BEHAT_CONFIG_PATH%%/features/bootstrap
  context:
    parameters:
      base_url: "https://cannot-tell-you.com"
      zombie:
          port: 9124
          host: localhost
          auto_server: true
          node_bin: 'node'
      selenium:
          host: ondemand.saucelabs.com
          port: 80
          browser: >
            {
                "username": "chartjes",
                "access-key": "like-i-would-tell-you-bro",
                "browser": "iexplore",
                "browser-version": "8.",
                "os": "Windows 2003",
                "name": "Kaplan Behat Selenium Testing"
            }
  formatter:
    parameters:
      verbose: true
      time: true
      decorated: true
      language: 'en'
      output_styles:
          comment: ['black', 'yellow', ['bold']]
{% endcodeblock %}

As far as I can tell, we can only run things under Windows 2003 but I do not
know if that is a limitation because of the free account I have. It sure would
suck to not be able to test things on Windows XP.

## Step 4: AUTOMATE ALL THE THINGS

Now we can run all your Behat tests that use Selenium on Sauce Labs infrastructure.
Why is that such a big deal? Because Sauce Labs very thoughtfully records videos
of all your tests, along with screenshots and nice, easy-to-read log of your
tests.

I cannot emphasize how useful having this information is. Why? Because it gives
you something to look at when things go wrong, as Behat itself will give you
some very terse info when tests fail. The [other test engineer](https://twitter.com/FreshWillisms) and
I let out a little squee when we saw all those things.

If you truly want to build a modern QA department, tools like Sauce Labs are
the standard to aim for. It's not enough to just run your automated tests using
Behat, you need to also be able to record things so you can go back and check
them out when things go wrong. 

I mean, really, it's more important to know why a test failed than to know that
everything passed. Passing tests are boring, failing tests are a call to action
to find out why it doesn't work.

Anyway, I hope this blog post helps you get your own Behat + Mink environment
configured to use Sauce Labs. 
