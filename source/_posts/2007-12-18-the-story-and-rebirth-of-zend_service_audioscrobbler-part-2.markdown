--- 
layout: post
title: The Story and Rebirth of Zend_Service_Audioscrobbler, Part 2
author: Chris Hartjes
---
<p>
So, dear readers, I received some nice emails and comments from those you have used Zend_Service_Audioscrobbler, along with having a nice email conversation with Wil Sinclair from Zend (who is involved with Zend Framework).  Wil told me that backwards compatibility for the 1.5 version is important so I can't just rip everything up like I want to.  Well, I could but it probably wouldn't be accepted.  I'd have to write some letter to convince the Elder Gods Of Zend Framework of why I needed to break backwards compatibility.  In Wil's words: "?I find it embarrassing and want to destroy the evidence? will not be considered a good enough reason. ".
</p>
<p>
I had a good chuckle at that, but Wil did offer up a very good suggestion on how to go about the refactor that I hadn't thought of:  use a _call() method in the class to intercept all the old calls and translate them into new calls.  I would also get it to trigger a warning that the old method would be deprecated in a future release as a way to get people to upgrade to the newer ones.  Once I have some code, I will show it.  Thanks Wil!
</p>
