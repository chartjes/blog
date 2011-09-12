--- 
layout: post
title: It's Not Just Birds That Migrate
---
One of the cooler features of <a href="http://www.rubyonrails.com">Ruby on Rails</a> is it's support for a concept that they call database migrations.  In a nutshell you can create Ruby code that will generate tables and insert data into them.  Why is this a good idea?  It's also database agnostic, so it doesn't matter what database server you're running:  your database changes just work.

For the <a href="http://www.ibl.org">baseball league web site</a> I'm running <a href="http://www.typosphere.org">Typo</a>, which I've hacked and extended for the things that I need that aren't part of the weblog engine.  It also supports migrations.  Whenever I create a new model (a representation of a table in a database that I need to work with) it also created a migration file.  Which is cool, but not totally necessary for the league site as it's not being deployed in multiple places.

Now, I'm also running the trunk version of Typo, meaning I updated it directly from the <a href="http://subversion.tigris.org">Subversion</a> repository it's hosted in.  When I did an upgrade of the site on Friday afternoon, it also grabbed some migrations as well.  Except those migrations conflicted with ones I had already created when I created all sorts of model code.  The result:  a crashing web site.

Arrrgh!  I panicked for a minute.  Then I hit Google trying to find a solution.  After about half-an-hour of looking I finally found a solution.  Turns out there is a table in the Rails structure that keeps track of what migration you're currently up to (schema_info for those who want to look into it).  I updated that to point to the migration BEFORE I accidentally started adding in my own.

Okay, so I executed a 'rake migrate' command...and still nothing.  Site still complaining that it couldn't find a table...that the migration is supposed to create.  More panicking.  Another deep breath and more searching on Google.  I finally found an example of how to manually run a migration script.  I did that for the first migration and then everything else went okay.  Phew

I think so many sites would just crash and die if it wasn't for Google.  I guess it's a vicious circle:  solutions to problems available in Google lead to more and more sites making it through tricky points which leads to more people looking for solutions.

So everything is just fine now.  The latest addition to the site is a stats module.  There appear to be some problems in the stats themselves (one series entered twice from the looks of it, which isn't supposed to be possible) but I'll get that sorted out.
