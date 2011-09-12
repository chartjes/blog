--- 
layout: post
title: Rallyhat.com -- moving forward
---
<p>
I've gotten some work done on Rallyhat lately, mostly on the train ride home but some stuff in the evenings when I need an internet connection for looking up some sites and testing.  Here's what I've gotten working:
<ul>
<li>User signup (complete with email and activation code)</li>
<li>User authentication</li>
</ul>
<br />
The next thing I'm working on is the Hunt stuff.  I've got to write some code to create hunts, allow people to join up with a hunt and stuff like that.  As part of that I will also have to do work on the image upload and storage part of the site, which has me worried due to potential bandwidth issues, but I might use Amazon's awesome SSS for that and see what the bills are like.  Along the way, I'm writing unit tests to go with my code because when my current host upgrades to Rails 1.2 I want to be able to do the same at my end, and a simple "rake test" command will run all my tests and point out anything that will be broken and needs to be fixed.  I suggest that interested parties go to <a href="http://weblog.rubyonrails.org">the Rails blog</a> to see the latest news about Rails 1.2
</p>
