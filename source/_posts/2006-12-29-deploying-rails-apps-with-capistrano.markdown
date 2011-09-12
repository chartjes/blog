--- 
layout: post
title: Deploying Rails Apps With Capistrano
---
<p>After much digging around on the net, I finally got rallyhat under version control AND using <a href="http://manuals.rubyonrails.com/read/book/17">Capistrano</a>.  For the uninitiated, Capistrano is a tool for deploying your application.  It's command-line driven, has hooks in it for version control (I keep my code in a <a href="http://subversion.tigris.org">Subversion repository</a>, and has all sorts of cool little features to it.
</p>
<p>
I found a great <a href="http://blog.digitalduckies.net/articles/2006/10/31/howto-capistrano-deployment-on-media-temples-grid-server/">tutorial on using Capistrano on media temple</a> and then found another link that showed <a href="http://jonathan.tron.name/articles/2006/07/15/capistrano-password-prompt-tips">some tips</a> for dealing with password prompts and such.
</p>
<p>
So now when I do my development work on my laptop, when I'm happy with the code I can push it up onto the live site with a series of commands.  It even allows me to roll stuff back if I have to.  I wish there was a tool this great written in PHP, but luckily you can use it with PHP or any other web-based scripting language.  All Capistrano cares about is that your code is located in the right place.  One of these days I'll put together the deployment script for pushing a PHP app as proof of concept.
</p>
