--- 
layout: post
title: Communication Tools for Teams
---
<p>Being one of the lucky few who telecommutes full time.  You can drag my cold, lifeless body into an offirce, thanks very much.  So, the big issue that you face when telecommuting is how to talk to all your fellow co-workers.  Where I work, we use our own IRC server to not only talk to each other (we're spread across three time zones) but as front-line support for our customers as well.  This actually works out quite well, so I've been thinking about what other tools are helpful for this.</p>
<p>
In terms of just talking amongst yourselves, it seems that <a href="http://www.campfirenow.com">Campfire</a> has a lot to offer.  In fact, I would consider using it at work if we weren't running our own IRC server.  Via <a href="http://gilesbowkett.blogspot.com/">Giles Bowkett</a> I found out about <a href="http://propaneapp.com/">Propane</a>, a desktop client for connecting to Campfire.  Really cool stuff, and it makes me wonder what other options are out there.
</p>
<p>
An oft-neglected category of communication tools is messages about what has been worked on by the developers.  Me, I can't stand having someone coming around all the time asking me when I've finished what I'm working on.  As a result I decided to be proactive and configured post-commit hooks for our company SVN repositories.  So now any of us who do coding work commits something, we all get a nice email about it.  Since I've done that, we've been a lot more proactive about testing things because, well, you can no longer hide when you've made a change. ;)
</p>
<p>
As for bug and ticket tracking, well, we've got a homebrewed system (created before I got there) that I don't really like.  However, it is not going away so if I want to make any changes I will have to make them myself.  First thing I was thinking about was adding something to the post-commit hooks that will add a comment to the thread for particular ticket indicating you checked in some code that dealt with the ticket.  A common feature in things like trac I'm sure, but one I'd like to see in our own system.
</p>
<p>
Let me know in the comments what type of tools you use at your company.
</p>
