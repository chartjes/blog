--- 
layout: post
title: Git Mah Code From Th' Repository, Ma!
---
<p>
In my quest to try and learn new things (more like trying to avoid being bored with stuff I'm doing) I decided to take a look at another version control system I had heard about called <a href="http://git.or.cz/">Git</a>.  According to it's <a href="http://en.wikipedia.org/wiki/Git_(software)">entry over at Wikipedia</a> it is "..a <a href="http://betterexplained.com/articles/intro-to-distributed-version-control-illustrated/">distributed revision control</a> / software configuration management project created by Linus Torvalds."  Yes, the same Linus Torvalds who created Linux.  When I first heard about Git I thought to myself "why should I care that Subversion supposedly sucks and that distributed version control is awesome?".  So I decided to dig a little further.
</p>
<p>
I found <a href="http://video.google.com/videoplay?docid=-2199332044603874737">this video of Linus talking about Git at Google</a> and while I did laugh at Linus' professed hatred for all things CVS (and it's hip descendant SVN) I did grow to understand git.  Basically, he created the version control system *he* wanted to use for the Linux kernel after his experiences with <a href="http://www.bitkeeper.com/">BitKeeper</a> led him to stop using it, but there was no way he could go back to the old patches-and-tarballs way they used to maintain the Linux kernel.  Just too many people using it now I guess.  So, he hit on the idea of using a bunch of existing tools, hacking them together with some glue of his own and creating a distributed version control system that he could use on a daily basis.</p>
<p>
Linus had a problem with CVS/SVN because of a few things as far as I can tell:  branching and merging was terrible (I agree that branching and merging is not the easiest thing to do in SVN if you get to any level of complexity) and he disagreed with the 'you need access in order to commit things' model that CVS/SVN promotes.  As someone who has commit-level access to the CakePHP repository, I can understand why that bothers some people:  once you can commit stuff you can wreak a lot of havoc with bad commits.
</p>
<p>
My understanding of a distributed version control system is that anyone can grab a copy of the repository and start playing with it locally, making their own commits.  Once they are happy, you can then push those changes up the chain to where yo u originally got them from and then continue merrily on your way.  The people who are working off of the source of your ORIGINAL checkout can then choose to pull your changes into their working copy whenever they are ready, and so on, and so forth.  I hope I'm not oversimplifying things here, and Linus does a really good job of explaining this in the talk.
</p>
<p>
The main advantage seems to be that it's greatly increased the speed at which merges and commits can happen.  Also, because you have a copy of the entire repository at your fingertips you don't need to be connected to the net in order to commit stuff:  the commits happen locally and don't go anywhere until you execute a git-push, which sends those changes back to the original source of your checkout.  Randall Schwartz, who gave a <a href="http://video.google.com/videoplay?docid=-3999952944619245780">follow-up talk about git</a> talked about how nice it was that he could do stuff on his laptop on the plane, committing and reverting changes locally.
</p>
<p>
So, I installed git both on my laptop and my VPS that hosts this blog and decided to try it out.  After fumbling around in the documentation for a while I figured out how to (a) create the repository, (b) how to get a copy of the repository, (c) how to commit and revert things and (d) how to push those changes back to the main repository.  Really, not that much different from how I use SVN these days...except I think it's neat how I can do local commits and know that if someone else was working on the project, they could mess around locally committing things and not run the risk of accidentally blowing something away.  Maybe I need to get another developer involved in the projects I'm trying out with git to see how this stuff will work.
</p>
<p>
So, right now I've got <a href="http://www.ibl.org">the IBL web site</a> and Rallyhat using git.  No complaints, and I really do see how fast the commits and updates (in this case git-commit and git-pull on the servers where the projects are in production) are compared to SVN.  Of course, I've automated deployment of these projects using Capistrano. :)
</p>
<p>
Now, don't take my word for it but I really think that distributed version control systems are a great idea that is starting to gain traction.  The Linux kernel uses it, and I believe the KDE project is using it as well.  I suggest you do what I did before I decide to actually use it:  watch the two videos I mentioned above, do some research into how distributed version control systems should work and then actually try it out.  You might be surprised.
</p>
