--- 
layout: post
title: Don't Get Too Cute With Your Refactoring
---
<p>For those who follow me on Twitter, I'm pretty sure it was obvious I was having a very rough day today.  I'm in the process of making some pretty invasive changes to an application and work, and I approached it with much trepidation because of an extreme lack of tests.  I managed to get part one of these changes done, and refactored some stuff to get away from constantly passing parameters around like messages.  Instead I decided to place these values inside class variables.  Chortling to myself at how much better it was than passing the same values around all the time, I wrote some unit tests and all systems were green.  Awesome.</p>
<p>
Then I noticed the application itself didn't work properly now.  "How can this be, o seasoned veteran of 12+ years of web application experience?!?!" I can hear you saying.  Alas, forgive me for I have committed the sin of being too cute with my refactoring.
</p>
<p>
Well, actually, the problem is that I did not write enough tests to cover the code I was refactoring and simply <a href="http://en.wikipedia.org/wiki/Cowboy_coding">cowboy coded</a> my way through it today to get it to work.  Well, it's *sort* of working and there are many refactorings still to do.  But for sure I have to step back and examine my test coverage to make sure I am testing EVERYTHING I'm fixing.  The mistakes I made were SO obvious once I took the time to trace what I call the "call flow", which is tracking what gets executed and in what order.  If I had written tests for everything I encountered in this "call flow" I think I would've been a lot better off, instead of yelling obscenities targeted at myself while trying to figure it out.
</p>
<p>
Looking back at my choices in refactoring, well, I could've gone either way:  passing messages around in the form of parameters is a pretty safe way of doing things, but I'm determined to cut things down to the least amount of code possible while still achieving the desired results.  I'm not talking about non-intuitive code hacks, or using trinary expressions whenever possible.  If I'm using objects, I might as well use class variables to store values that need to persist throughout the request. 
</p>
<p>
So when I fire up <a href="http://www.vim.org">the one-true editor</a> tomorrow morning to keep going, I will say to myself out loud "don't get too cute with your refactoring, Chris.".  Oh yeah, and I'll make sure to write my tests as I go along.
</p>
