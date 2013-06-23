--- 
layout: post
title: Why Code Generation Just Works, Damnit!
---
<p>In a previous post <a href="http://www.littlehart.net/atthekeyboard/2007/06/22/whats-in-chris-brain-june-2007-edition/">where I rambled on about what I was thinking about</a> I briefly talked about bake, the wonderful tool that comes with <a href="http://cakephp.org">CakePHP</a>.  In the comments for that post I was asked by 'keymaster' to expand a bit on why bake is such a powerful tool.  In a nutshell: it creates a skeleton for EVERYTHING that you will need.</p>
<p>
At <a href="http://www.cakedevelopment.com">Cake Development Corporation</a> it's our secret weapon that allows us to build out a site faster than our competition.  With bake I can build the following:
<ul>
<li>If I've already created my database tables following CakePHP conventions, I can create models, along with all their associations (the belongsTo, hasMany, etc</li>
<li>Create controllers, and even create not only the common <a href="http://en.wikipedia.org/wiki/Create%2C_read%2C_update_and_delete">CRUD</a> actions but create the admin-related actions as well</li>
<li>Create views for the CRUD actions AND the admin-related ones too</li>
</ul>
</p>
<p>That's 99% of the work taken care of for me!  Why *wouldn't* you want to use a tool like that?  Part of the reason people have been slow to come around to using it is because, well, there is no graphical interface for it.  It's all command line, and for those developers who work on Windows, using the command-line is often a daunting task.  It's not their fault, really.  Windows is a graphical environment after all.  For OS-X types like me, I just pop open a terminal and start baking.  I highly suggest people go and watch gwoo's <a href="http://cakephp.org/screencasts">screencasts</a> about setting up the CakePHP console for both *NIX environments (including OS-X) and Windows.  By installing the console, you can access bake by simply typing 'cake bake' in the root directory of your app.</p>
<p>
Recent additions to bake like the ability to specify your own templates for views means that you can roll out a slightly-customized version of a site even faster.  There are enhancement requests in the CakePHP development queue to extend the abilities of bake to create components, helpers and plugins.  A great tool just keeps on getting better!  Now that I use bake as part of my regular work habits, I ask myself "how the hell did I ever create anything without it before?"
</p>
