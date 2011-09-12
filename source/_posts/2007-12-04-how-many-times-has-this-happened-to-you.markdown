--- 
layout: post
title: How Many Times Has This Happened To You?
---
<p>
I had recently upgraded to a new laptop (white MacBook) and had just gotten stuff setup up the way I liked.  So I continued doing development work for my latest work-related project and it was time to push the changes up to the staging server.  Oh wait, I hadn't installed Capistrano yet.  So I installed that and found, oooh, we moved up to version 2.1.  Cool!  Progress is good.</p>
<p>
So I go to deploy and WTF!?!??! It won't work!??!  No error messages except to say the remote command failed.  I dig around on google.  The amount of documentation available for Capistrano 2.0 (or 2.1 for that matter) makes CakePHP's slowly-growing documentation look like Wikipedia.  God damn it, why would you release something that breaks so many things and then don't tell people WHY it won't work.  Maybe I'm doing something wrong, but I'll be damned if I can figure out what it is.
</p>
<p>
So, on to the backup plan.  <a href="http://phing.info/trac/">Phing</a>, despite it's use of XML which I am not huge fan of in terms of it's use as a configuration file, but at least it's PHP and there is lots of documentation on how to use it.  Now, where did I put <a href="http://domain51.com">Travis Swicegood's</a> e-mail address...
</p> 
