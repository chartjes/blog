--- 
layout: post
title: What Happens When A Good Idea Doesn't Actually Work?
---
<p>Being a programmer with Attention Deficit Disorder when it comes to new ideas.  I'm always interested in new ideas, technologies and programming languages.  So, since I had been doing some work with web services I found the RADAR idea very interesting.  I even posted some code snippets and thoughts about it.  Then I went and tried to actually implement it.  Not so good.
</p>
<p>
The pages worked fine in Firefox, but IE was complaining all over the place about it.  Bad XSLT and other weird errors.  Since I had to get the thing fixed in short order, I followed my "just build it, damnit" mantra and ripped out all my code that called the REST service and did it without the web service.  Am I disappointed?  Hell yes.  I was *convinced* this was a good idea.  But perhaps the truth of the matter was that I was trying to solve a problem that did not exist, with the lofty goal of "make your application the API" that I've seen espoused in many places.
</p>
<p>
So what went wrong?  I still have no clue.  All I can do is go back to what I did and try it again.  On the surface it should've worked properly.  The problem with what I was doing was that with it spitting back information via XML, debugging things when they've gone wrong is hard.  Or maybe it's hard *for me* because I haven't spent much time doing something like this.</p>
<p>
That's really the downside to playing with new technologies:  if you're not 100% sure how to debug it when it goes wrong, you could end up doing more harm than good.  I think REST is still a really good method by which to "make the site your API".  I can now spend some time looking at it and seeing if I can't figure out just where I went wrong.</p>
