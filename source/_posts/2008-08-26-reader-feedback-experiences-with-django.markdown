--- 
layout: post
title: "Reader Feedback: Experiences With Django"
---
<p>Welcome to Day 2 of my answering reader feedback questions here in the month of August.  I was asked to share my experiences with Django.  I will confess that I am a complete n00b when it comes to Python (wrote a few scripts for work-related stuff) and got an early alpha of my baseball road-trip planning site actually working using Django.  Sure, it was ugly and very rough around the edges but I got it to work.  But I will say this:  if I had the opportunity to start working with Python and Django every day (and for the same pay I'm getting now) I would take it in a heartbeat.  Seriously.
</p>
<p>
So why all the love for Django and Python?  As a guy who's used PHP for a very long time, I'm really blind to the syntax of it.  All the griping about needle vs. haystack and "PHP is ugly" is just wasted on me.  Just so much pissing and moaning by people who should know better and lack the courage to learn the language they way they should.  I heard it described by Evan from Identi.ca as being "the working man's language".  Nothing wrong with that, as PHP is great at Getting Things Done.  But Python...Python is vastly different from PHP.  It's about objects.  It's about consistency.  It's about the most amazing interactive interpreter I've seen since I was a kid fooling around on my VIC-20 typing in programs from Compute! magazine.  Bet you didn't think I'd been using computers for that long.  To shift into bragging mode, I first got paid for programming when I wrote a program for my mother's school (she's a teacher) to create the salary grid for the teachers.  I was 12. I think.
</p>
<p>
Also, there's a dirty little secret about using frameworks that nobody really tells you.  After a while, it makes you lazy.  You forget how to do certain things because, well, the framework does it for you.  The other day there was a tweet from someone asking about the best way to sanitize data before you put it into the database.  My first thought was "sheesh, that's built into the framework" and then I stopped myself and said "you are getting goddamn lazy!".  My response was "try using mysql_real_escape_string(...)" but was also told about using PDO's binding of parameters as another way to do it.  See, those things are all done by the framework meaning lazy old Chris doesn't have to remember how to do it.  Until the time he's confronted with non-framework code that he cannot simply rewrite as part of a framework.  *gulp*.  So, since Python and Django are so different from the other frameworks I've used it forces me to STOP being lazy and actually learn how not only Django itself works but how the insides of it work as well.  
</p>
<p>
Now, being an old hand at frameworks means using Django is not that big a stretch.  I spent a lot time googling around for the "Python (or Django) Way" to do things.  Except for a few concepts that are not familiar to a long time PHP guy (generators?) it wasn't that hard to get up and running with Django.  The documentation is awesome, and once you learn to stop writing PHP code in Python and instead embrace doing things the Python way, it becomes a lot easier.
</p>
<p>
In the end it's still datasource-backed models talking to some controller code and passing it onto some template.  I find the Django templates to be very limiting after my initial experiences and my "PHP is the template" background, and I think that as I get deeper into it I really have to find out how to do things the Django way.  What CakePHP calls Model-View-Controller, Django calls Model-View-Template, but it's really the same thing.
</p>
<p>
When I compare Ruby to Python, I don't get the feeling that I will have to resort to dynamic functions and closures to Get Things Done in Django like I see happening in Rails.  Besides, they seem to be two very different communities.  That's probably because the leaders of the Django community are so different in temperament and I don't see the same type of "Django rules, everything else sucks!" mind sets that I saw in the Rails community.  Maybe I'm just looking in the wrong places, but I feel more at ease in the Django community than the Rails community, albeit from the outer fringes of it.
</p>
<p>
So don't be lazy and complacent about the tools that you use.  Go and checkout Django and you might feel the same way about it as I do.
</p>
