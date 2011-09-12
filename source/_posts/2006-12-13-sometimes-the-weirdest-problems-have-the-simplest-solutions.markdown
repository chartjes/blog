--- 
layout: post
title: Sometimes The Weirdest Problems Have The Simplest Solutions
---
<p>
A bug had been driving me CRAZY at work for a long time.  No matter what I changed in the code, the bug would still rear it's ugly head.  It would work PERFECTLY in development, but when you push the code to production it would generate the same bug.  I spent tons of time trying to figure out the difference between the data that the code would see in production (XML stream) and the data samples I had gotten from our partner for that piece of code.
</p>
<p>
Finally, I decided maybe it was time to take a different approach.  I put in some code that would notify me if an XML document that I had generated couldn't be read in by a simplexml_load_file statement.  Sure enough, that was the problem.  Permissions issues.
</p>
<p>
Ugh.  Don't I feel like a total moron.  Later tonight when the next set of results makes their way down the XML stream I will see if my latest discovery is actually the proper fix.
</p>
