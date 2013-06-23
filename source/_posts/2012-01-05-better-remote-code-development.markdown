---
layout: post
title: "Better Remote Code Development" 
author: Chris Hartjes
date: 2012-01-05
comments: true 
sharing: true 
---
I am struggling to find a better way to handle a new paradigm in development.
At [Moontoast](http://moontoast.com) all our servers are up on EC2, which
includes the two dev servers (one for each project) that I use every day.

I've been playing around with [Sublime Text](http://www.sublimetext.com)  (because of the awesome vim bindings)
and was thinking about why do I always have to be logged into the remote
server to do my work. Normally I connect using SSH, then attach to my [tmux](http://tmux.sourceforge.net)
session and then fire up vim.

This is okay but it lacks a certain elegance in it's approach. As a result
I end up using things like [Dropbox](http://dropbox.com) to synchronize my
.vimrc file so I get a consistent experience across environments. That's ok
for now, although I'm having some weirdness due to vim 7.2 vs. vim 7.3 issues
in one of those environments.

I also need to be able to use git to commit changes, create and merge branches, etc.
I need to be connected to the server to make that happen. But that is starting
to feel like a limitation to me. 

What I'm chafing against is having to deal with multiple environments all the time
to get my work done. I want to use ONE editor, tweaked out exactly the way I want
to edit code in multiple locations. I want to use ONE tool for handling git work
in multiple locations.

Any thoughts on how to achieve what I want? There are occasions when I do need to
connect to a server (say to tail a log while testing a Gearman job) but damnit
it's the second decade of the 21st century. This should be a SOLVABLE problem.

So for now I'm trying out SublimeText2 as my main editor and started using Transmit
(sorry Expandrive but I am finding Transmit to be a lot more responsive) so the
missing piece if for me to be able to commit code changes on a remote server
WITHOUT being logged into that remote server.

In a perfect world I am using virtual machines for my dev work, but I haven't convinced
our awesome sysadmin to put in the time necessary to make it happen for me.

Let me know potential solutions for my desired setup.
