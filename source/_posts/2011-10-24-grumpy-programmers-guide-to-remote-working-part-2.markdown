---
layout: post
title: "The Grumpy Programmer's Guide To Remote Working, Part 2"
author: Chris Hartjes
date: 2011-10-24
comments: true 
sharing: true 
---
As mentioned in the previous post about remote working, you do have to work a lot harder when you're not in the same office as your co-workers in order to simply get things done. If you took my advice you've got yourself a sweet setup at home, with a comfy chair and a nice desk. But that is only the first battle in the on-going war that is successful telecommuting. In this post I want to talk about some tools that I use that I feel help me Get Shit Done when working from home.

First, since you don't have the instant feedback loop of a fellow cubicle dweller or even office-sharing partner, you need tools that can act as a second set of eyes for you before you open what is often an expensive communication channel to your co-workers. Not expensive in terms of money (unless you have to call people long distance and don't either use VOIP at home or Skype) but expensive in terms of time. Making that initial "communication handshake" is expensive in time and commitment.

So for me, the first set of eyes I use are [Firebug](http://getfirebug.com/) or Chrome's web developer tools, depending on which browser I'm using. Those let me peek at the HTML being generated and debug any Ajax calls your application is making. It used to be my primary tool until [my boss](http://twitter.com/ramsey) asked me why I wasn't using [Charles](http://www.charlesproxy.com/), an awesome debugging proxy application for OS-X, Windows and Linux.

Charles acts like what it says: it's a web debugging proxy. It sits between your browser and your next work connection, monitoring and showing you what connections you are making. Why is this awesome you might ask? I can record an entire series of clicks on a web page and play them back later for testing purposes.
I like Charles for a few reasons. This is helpful because one of our main applications at Moontoast is a flash-based store and Charles will show me the request that the flash SWF is making *and* I can see the response that is coming back. I am not a flash developer, but I do need to make sure that code I write that is supposed to talk back to the SWF (via AMF) is returning correct values. I like to record Ajax calls and repeat them over and over until I am happy with the response coming back. Please, please, PLEASE check out Charles. It is worth every penny.

So now that I have someone else helping me debug my Ajax and AMF calls, what other tools do I find useful. Well, if you don't have your editor already tricked out to reduce the amount of work you have to do *outside* of your editor to get things done then I advise you to actually learn your editor inside and out. As a vim user I spend a lot of time evaluating plugins that can help me out. I use [Syntastic](https://github.com/scrooloose/syntastic) to run my code through a [code linter](http://en.wikipedia.org/wiki/Lint_programming_tool) every time I save it. I use [Fugitive](https://github.com/tpope/vim-fugitive) to work on my Git commits and merges. All in all, it's important that you be as productive as possible using the tool you write your code with day in and day out.

Of course, it goes without saying that you should be probably be writing your own tests for your code that you can automate. Don't worry, this is not going to turn into another sales job for automated testing. PHPUnit, PHPSpec, Selenium, please use something that acts as an automated tester for you. I mean, it seems to work for me so maybe it can work for you.

So that's really it in terms of tools that I have found that I used more and more as I telecommuted more and more. My criteria for evaluating any tools is this: is it easy to use, can it automate something I don't want to do manually, and does it easily integrate into my existing workflow. Firebug and Charles fit that criteria. Plugins for my editor fit that criteria. CLI test runners fit that criteria.

In other words, any tool that can make you more productive in an office setting is even more important when working remotely with a team. Anything that you can do to reduce the testing and integration step benefits you and your team, and helps to convince management that their decision to allow you to continue to work remotely is a good one.

I'm interested in hearing other people's experiences telecommuting and tools that they have found to be helpful. Comment in this post, send me some email (chartjes AT this domain) or hit me up on Twitter.
