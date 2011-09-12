--- 
layout: post
title: Application authentication
---
<p>On the CakePHP mailing list I see frequent questions about various ACL and authorization plugins that are available for cake.  I've never used anything beyond simple authentication and access control and always felt that ACL schemes were either too hard to implement or too restrictive.  Honestly, do you really need to have one person who can see 5 reports and another see 6?  I never saw the point of that, but perhaps one day I will run into a scenario where that is needed.
</p>
<p>Rallyhat needed some authentication.  Being a Rails app, there were tons of options.  Basically, they revolve around the same principle:  there is a feature called a before_filter that runs before you execute any action in a controller.  Lucky for my fellow CakePHP users, there is a similar feature in CakePHP.  So, you create a function that you call via the before_filter (beforeFilter in CakePHP) that verifies that the person has permission to access the current controller.  Yep, it's really that simple.
</p>
<p>
Of course, there are many varied ways to do the whole login / assign roles to users, too many to list here.  Don't expect any code here either, as I haven't written any.  Like any lazy programmer, I steal from the best. ;)  For Rallyhat I'm using Rick Olson's awesome <a href="http://technoweenie.stikipad.com/plugins/show/Acts+as+Authenticated">acts_as_authenticated</a> plugin.  Man, it is PERFECT for what I need.  You install the plugin, head over to the stikipad where the documentation is and it gives you just about everything you need.  Signup, login, activation codes, email confirmation, "forgot my password" stuff.  I can't imagine how much time this has saved me.  Oh yeah, on top of it it comes with tests to make sure everything is working.  Make a change, run 'rake test' and fix any errors that pop up.  Rallyhat will require a full commitment to writing tests, so I'm glad to get into the habit of it.
</p>
<p>
So, if you want some simple authentication then if you're using CakePHP, fool around with using a beforeFilter to do things like look for a cookie or look in the session for a variable that says you are logged in.  Authentication doesn't have to be complicated, it just has to work.
</p>
