--- 
layout: post
title: Converting Legacy Apps to CakePHP, Part 1
---
<p>In order to make some extra money, I do side projects from time to time.  In my rapidly dwidling spare time I have been working on a project to convert an existing site for a legal services company over to PHP.  I'm *this* close to being done, so I thought I'd share what I went through to get to where I am right now.</p>
<p>
The existing code is typical of what I call the pre-framework era.  It had grown organically, much like many applications do.  When I initially did the code review (contact me if you're interested in having me do a code review of your application) I noticed lots of stuff that needed fixing.  No escaping of database input or filter of output.  Plaintext passwords in the database.  Total mixing of business logic with presentation logic.  To make things a little more difficult, SOME of the application was done properly in terms of separating business logic from presentation logic through a system of HTML templates that would have parts of it filled in via token replacement.  Not great, but not the end of the world.
</p>
<p>
I could also tell that multiple people had worked on it.  How?  Inconsistency in coding standards.  That and the comments strewn throughout it indicating who had done what.  Did I also mention that no version control was used on the project at all, so lots of copies of files like user_search.php.old, user_search.php.old.2.  You get the idea.  The best news of all was that the application DID work and met the objectives of the business.  Never lose sight of that when contemplating a legacy rewrite.
</p>
<p>
So after giving the code review I was asked to do the rewrite.  The client realized that they had some serious maintenance issues on their hands and were in the process of creating a new look-and-feel for the site.  Being the framework guy that I am, I indicated that porting the code over to a framework would be the best way to reduce maintenance issues going forward.  Why?  More and more developers are starting to work with frameworks, and gaining the discipline that comes from using the Model-View-Controller design pattern.  Also it would be a lot easier to start creating new templates for the site since only the presentation will be changing, not the data itself.
</p>
<p>
After considering using this project as a learning tool for Django, I settled on CakePHP.  Time was sort of important here and I thought that a paying job was not one where I should be fooling around learning Django.  Plus I had no confidence that the host they were using would be able to accomodate my desire for a Python + Django + mod_wsgi setup. 
</p>
<p>
In part two I will talk about the first thing I did once I started:  tackle the database structure.
</p>
