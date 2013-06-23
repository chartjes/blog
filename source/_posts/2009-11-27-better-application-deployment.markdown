--- 
layout: post
title: Better Application Deployment
---
<p>I've been working on the <a href="http://www.sportsdb.org/sd/sportscaster">open source web service</a> that we make available to our clients, trying to get some caching into the application to improve performance.  It got me to thinking:  what would be the best way to get our clients to install this application.
</p>
<p>
By best way, I do not mean easiest way.  The easiest way is to say "here's the tarball, extract it and install it in place".  That's currently the method we use for distribution.  I must admit that I have been negligent in updating recent builds on the site.  The real solution here is to create an automated build system that I can use to package up newer versions of the code and put them up on the web site.
</p>
<p>
Others have suggested that I should examine the use of Pear as a way to distribute this PHP application.  That's fine, but the next time they update it would overwrite any changes they made to things like display templates.  So I guess the current method is the best...
</p>
