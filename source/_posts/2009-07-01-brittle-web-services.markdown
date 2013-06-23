--- 
layout: post
title: Brittle Web Services
---
<p>Happy Canada Day to all my Canadian friends and readers!</p>
<p>
For a project at work I've been working a lot with web services, creating a new one and tweaking an existing one.  That work got me to thinking that not only can you have brittle code, but you can have brittle web services as well.  Things like:
<ul>
<li>Dependencies on 3rd-party tools that might force you to send parameters in a certain order (I'm looking at *you*, XSLT tools)</li>
<li>Non-intuitive parameters</li>
<li>Misleading error responses</li>
<li>Poor permission schemes that allow you to access data you shouldn't</li>
</ul>
I could go on and on, but a lot of the things that make web services "brittle" are the same things that make regular code "brittle" as well.  C'mon people, it's not so hard!
</p>
<p>
I've worked very hard to adhere to a set of standards when building these web services:
<ul>
<li>All services must be authenticated against using login and password</li>
<li>You pass in a parameter indicating how you want the response back (in this case XML, HTML made pretty using XSLT, or JSON</li>
<li>Standardized the parameters being passed in across all internal web services</li>
<li>Cache everything you can using read-through caching strategies.  I would've loved to use write-through caching but it's just not possible at this time.</li>
</ul>
</p>
<p>The main reason for all this pedantry is for maintenance reasons.  When (not if) I go back to work on it, I want to know that I will not have to remember any weird exceptions made in the code in the pursuit of Getting Things Done, Damnit.  When you're the only developer working on it, it's easy to fall into the trap of the quick fix or the non-intuitive block of code.  
</p>
<p>
Share your tips for building solid web services with me in the comments.
</p>
