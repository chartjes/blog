--- 
layout: post
title: Deploying Applications
---
Recently I have been told "Chris, you're a great developer but a terrible sysadmin."  Considering how often I muck-up the box that hosts my various web sites, there might be some truth to that.  So now I'm trying to be less of a sucky sysadmin and find solutions that both myself (and my poor friend Sean who cleans up my sysadmin messes).

When one of my employer's <a href="http://www.autoforums.com">new sites</a> was about to be launched one of the tasks I was given was to come up with an automated deployment system instead of the do-everything-by-hand system that we have in place now.  In-house, there was already a web-based tool that would export stuff from the CVS repository but anything else had to be done by hand.

Being a Rails fan, I had known about <a href="//manuals.rubyonrails.com/read/chapter/97"">Capistrano</a> (used to be called Switchtower but they ran into some copyright issues on that name) but was unsure how it would work with a non-Rails app.  I did manage to hack something together but wasn't entirely happy with it.  

In the end, the project had scaled down quite a bit (only one server instead of the three they had planned for) so the manual system is okay for now.  But I was still frustrated by not having an elegant, CLI solution to deploy the site.  I had toyed around with the idea of writing my own Capistrano clone for PHP (as source material for another I googled around some more today and found that Geoffrey Grosenbach (Rails guy and main force behind the Ruby on Rails podcast) <a href="//nubyonrails.com/articles/read/460"">had done the same thing, but only better</a>.

Looking at that blog posting makes me realize that it's possible to use Capistrano to distribute PHP apps.  Wish this had been around at my old gig...
