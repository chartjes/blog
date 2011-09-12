--- 
layout: post
title: "CakePHP Application Deployment: RFC"
---
<p>A co-worker of mine always complains that people don't read the <a href="http://en.wikipedia.org/wiki/Request_for_Comments">RFC</a> that covers a topic related to making their own stuff work with our stuff.  He's old sk00l like that.  Although my co-worker is a tad out-of-touch with the realities of programming these days (as in the amount of people who actually read the RFC when they can simply use someone else's library / module / function / application is very small), I thought I would at least adhere to some semblance of standards and do a blog posting about my plans for making CakePHP application deployment easier.
</p>
<p>
While I really prefer to use <a href="http://capify.org">tools like this</a> for deployment, I understand that not everyone wants to mess with standalone programs and configuration files.  I've been asked before about Cake-specific deployment techniques, so I figure the easiest way is to see about adding a task to the Cake console.  Let's call this 'cake deploy'.
</p>
<p>
As I <a href="http://groups.google.com/group/cake-php/browse_thread/thread/ea4e5ec768c8d95a#">explained on the mailing list</a> I am looking for opinions on what sort of things should be part of the 'cake deploy' task.  Right now, my thoughts are as follows:
<ul>
<li><i>cake deploy config</i></li> - setup and edit configuration parameters.  Initially I thought of setting things like transport method (ssh, ftp), logins and passwords, remote location, source directory, and destination directory.  The configuration file would be stored locally in APP/config
<li><i>cake deploy</i> - seems pretty self-explanatory to me.</li>
</ul>
</p>
<p>
In the RFC thread on the CakePHP mailing list, someone mentioned they'd like to see rsync, but I'm trying to avoid having to external programs required to make the deployment work.  Or, at least, use as few as possible.  Anyhow, if you have any thoughts on this feel free to add them to the comments.
</p>
