--- 
layout: post
title: Having Problems When Upgrading CakePHP?
---
<p>
People on the CakePHP mailing list often complain about not being able to get CakePHP configured properly, with CakePHP usually displaying all sorts of weird errors.  Telling people these errors is very helpful, because it shows us that the problem almost always is people not following the installation instructions as outlined in the manual.  Those instructions are there for a reason.  Anyway, I guess I'm one of the lucky ones who gets it to work properly almost every time, hell even working with non-standard web servers like nginx.  Anyway, the latest version of CakePHP 1.2.x.x as I write this has deprecated a lot of things in the configuration file...and people are simply ignoring the warning messages and complaining about why things don't work.
</p>
<p>
Since I desire to not be as harsh as I have been in the past, here is some advice that I posted to the mailing list that I thought I would share:
<blockquote>
Perhaps I'm just lucky and Murphy is smiling down on me from above,
but I am using the latest version of CakePHP via SVN *and* have my
cake directory outside of app and I have NO problems getting my stuff
to work.

I followed all the notices that Cake threw when I updated the Cake
core, changed the code that it mentioned and that was it.  Really.  In
fact, here's my config file for everyone to see:

http://bin.cakephp.org/view/1205137498

I continue to be baffled by the problems people seem to be
experiencing when my own configuration has been just fine.  I've found
three things that help

1) pay attention to the warning messages that CakePHP spits out as
they usually point at the problem

When I upgraded, I saw lots of warnings about deprecated functionality
and suggestions on how to get rid of those problems.  Those error
messages are there for a reason, ignore them at your own peril.  They
tell you EXACTLY what to do.

2) permissions for the tmp directory really do matter

Use the firehose permission level if you're on some sort of UNIXy
system:  chmod -R 777 $APP/tmp

3) make sure you do your dev work with the debug level to 1 and save
debug level 0 for your production apps.

That little tip will mean you will never have to mess around with
deleting and recreating your $APP/tmp directory.

I hope this helps those who seem to be struggling to get their CakePHP
configurations to work properly.  I did all the things above I
mentioned and continue to have smooth sailing whenever I upgrade from
SVN (which is usually every morning).
</blockquote>
</p>
