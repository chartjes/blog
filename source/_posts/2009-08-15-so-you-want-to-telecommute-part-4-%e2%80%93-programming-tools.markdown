--- 
layout: post
title: "So You Want To Telecommute? Part 4 -- Programming Tools"
---
<p>(This is the 4th part in series about my experiences as a telecommuting developer.  For more info, check out <a href="http://www.littlehart.net/atthekeyboard/2009/08/08/so-you-want-to-telecommute-part-3-collaboration/">part 3, </a><a href="http://www.littlehart.net/atthekeyboard/2009/08/01/so-you-want-to-telecommute-part-2-accountability/">part 2</a>, and <a href="http://www.littlehart.net/atthekeyboard/2009/07/29/so-you-want-to-telecommute-part-1-building-trust/">part 1</a>)</p>
<p>
If you really want to set of a flame war on the internet, start talking about what you use as (a) your programming language and (b) what editor / IDE you use.  Thankfully, this posting is not about either one of those things.  After all, who can argue with using <a href="http://www.vim.org>the One True Editor</a>.  Here, I want to share my thoughts on the type of tools you are likely to need as a telecommuting developer.
</p>
<p>
So now that you've gotten the trust of your employer, and you have tools in place to provide accountability, and have a system in place to collaborate with your fellow employees (hah, tied those all together nicely!) we now have to talk about what you are going to use to get the job done.  
</p>
<p>
Chances are that if you are telecommuting, you are working for a small company.  Which also means that it is very likely that you will doing a lot more than just writing your code and handing it off to someone else for deployment into production.  When you also take into account that response times for your fellow telecommuters is likely slower than if you were in the same office, you almost needs to put into place practices that are defensive in nature.
</p>
<p>
The importance of a reliable set of development tools is something I've touched upon both in previous posts on this blog and in talks I've given.   This toolset becomes even more important when you're responsible for getting your code into a state where you can deploy it with confidence.  There is a reason that the amount of information available about unit testing, continuous deployment, and tools for automating other parts of the development process has exploded lately:  they are all things that can help you get error-free code deployed faster.
</p>
<p>
Many do not believe in the Cult of Unit Testing, and that's okay.  There are lots of other testing that can be done.  Even something as simple as testing things out in a browser can become a critical part of your programming toolkit.  I'm sure it comes as no shock to people how many bugs slip through the development process and into production that could've been detected with a simple check of the application via a web browser.  We are all guilty of this kind of thing.  These days thanks to things like <a href="http://seleniumhq.org/">Selenium</a> and <a href="http://www.getwindmill.com/">Windmill</a> it is easier than ever to create scripted web browser sessions for testing purposed.  
</p>
<p>
Sure, it will take time to learn to use these tools but it's hard to argue that it is anything other than (a) laziness or (b) fear of the unknown in the form of other languages or environments that stops people from implementing tools that will give you such a huge return on the investment made into setting them up.  I have been guilty of this in the past too, so I'm familiar with the anxiety that accompanies the attempt to automate parts of your testing.
</p>
<p>
So with some sort of testing in place, the next step is to get into place automated deployment tools.  Readers of my blog know my fondness for <a href="http://www.capify.org/index.php/Capistrano">Capistrano</a>, and it's use has become an integral part of my toolkit.  Why?   It allows me to do automated *repeatable* deployments to both my staging and production environments.  I work very hard to eliminate the idea that "we need to do things differently in production", because you can pretty much guarantee that you will end up with bugs that only exist in production and are difficult, if not impossible, to duplicate in your development environment.
</p>
<p>
I am not aware of any tools like Capistrano that exist for those who use Windows as their production stack.  If you know of some, let me know in the comments.  For my friends who use PHP and cannot use Ruby, I highly recommend investigating the use of <a href="http://phing.info/trac/">Phing</a> as a substitute.  I've also been playing around with <a href="http://www.nongnu.org/fab/">Fabric</a> as an alternative to Capistrano.  Much as with testing, there is no shortage of tools available to you.  Heck, even something as simple as shell scripts that check out your code from version control and copy it into a desired location are a step up from manual deployment of code.  Sure, it's easy to do 'svn update' in a directory, but that will only be easy until you have to start doing things like database changes at the same time.
</p>
<p>
I guess what I'm really trying to say is that you should be using tools that make deploying error-free code into production *easier*, because chances are you will be the one doing the deployment.  Where I work, each developer is responsible for deploying their own code so it was in my best interest to create something that was "fire and forget" when it came to pushing up changes.  Need to copy new scripts in place for pulling data from our XML db?  No problem.  Need to update the schema for the database?  No problem, got it totally covered.
</p>
<p>
A lot of these issues are something I've covered <a href="http://www.littlehart.net/atthekeyboard/2008/04/17/deployment-is-not-a-4-letter-word-the-screencast/">before</a>.  Instead I will focus on a final thought on tools -- they need to be as easy to use as possible.
</p>
<p>
When you telecommute, one of the biggest problems is response time.  Since you're not in the same office (or even same city) as your co-workers, when something goes wrong it is likely that you will have to be the one that fixes it without help from others.  Building a tool kit like the one I've suggested will go a long way towards helping you when things go wrong.  Which they will.  By automating as much of this as possible, it becomes quite simple to fix any problems.
</p>
<p>
If you have to fight against your tools, then I think you're doing it all wrong.  Surround yourself with tools that you are comfortable using, and understand just how essential they really are.  When I think of how I used to program when I started 12 years ago, I have no idea how I got anything substantial done.  With my tool set in place, I'm ready to tackle just about anything I need to do at work.  My ability to customize the tools I use means I can do my job from anywhere I can get a reliable internet connection.  And that is really the key to successful telecommuting:  getting things done so they won't ever ask you to come into the office again.
</p>
<p>
Thanks so much for reading this series on telecommuting.  If you have any questions about anything I've discussed here, feel free to add them to the comments.
</p>
