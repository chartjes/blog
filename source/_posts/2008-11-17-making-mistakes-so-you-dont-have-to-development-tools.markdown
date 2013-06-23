--- 
layout: post
title: "Making Mistakes So You Don't Have To:  Development Tools"
---
<p>I've been thinking about topics for conference talk submissions a lot lately (I have a serious case of conference envy the last little while), which usually gets my dev juices going and trying to make a better dev environment for myself.  I've started using a few newer techniques so forgive me if some of these seem old to you, dear reader.
</p>
<p>
<h3>MySQL over an SSH tunnel</h3>
</p><p>
I certainly can't be the only person who has to do development (or refactoring) work involving databases that have GB of data in them.  It's not even remotely practical to copy it over to my laptop, and taking a snapshot is pretty much impossible given the relationships between the tables.  It would be 3 times the work to create a tool to give me a snapshot that includes all the proper related records.  How do people handle that anyway?</p>
<p>
So I discovered via <a href="http://lazyweb.ca">my favourite pair-program-via-IM partner</a> the technique of tunnelling to MySQL over SSH.  It couldn't be easier:
<pre>
ssh -fNg -L3310:127.0.0.1:3306 user@server.domain.ext
mysql -h127.0.0.1 -P 3310 -u user -p database
</pre>
<br />
You can use whatever port you want at your end, but the key here is telling SSH that you want to map port 3306 on the remote server to a specific port at your own end.  
</p>
<p>
The only downside I've seen is that when I was pounding on a remote server with a very involved query that the remote server started writing MySQL tmp files to disk.  Files so large that they started to trigger our <a href="http://www.nagios.org/">Nagios</a> monitoring process that look at free drive space.  Maybe I shouldn't do that on a production server.  Heh.
</p>
<h3>Use an editor that supports remote debugging in PHP</h3>
<p>
I took a Twitter poll and asked how many people actually use debugging tools like <a href="http://xdebug.org">xDebug</a> and was surprised by how many don't.  I have used them off an on (more on these days) and now that I'm using <a href="http://www.vim.org">vim</a> I have also started <a href="http://2bits.com/articles/using-vim-and-xdebug-dbgp-for-debugging-drupal-or-any-php-application.html">debugging stuff inside of vim</a>.  Is there *nothing* you cannot bend and twist vim to do for you?
</p>
<p>
This just further reinforces my recommendation that whatever editor you do decide to use every day, learn it inside and out.  Right now I'm trying to break myself of the habit of using the arrow keys to move around in vim, instead relying on the hjkl home row keys to do so.  Debuggers are so common in other languages (Ruby and Python have an awesome interactive console to act as a debugger for you) there is no reason except for, I dunno, laziness and an unwillingness to learn how to add an extension to your PHP install, to not at least try using xdebug.
</p>
<h3>Don't procrastinate, read the documentation</h3>
<p>
A side project I've been working on has some of the tightest production-level PHP code I've ever written in it.  Why?  Because I took the time to dig into the documentation of the newer features in Cake to see how they apply to the work I'm doing.  Containable behavior that is now part of the core.  Johnathan Snook's <a href="http://snook.ca/archives/cakephp/multiple_validatable_behavior/">Multiple Validation behavior</a>.  Fat models and skinny controllers.  Reusable elements in your pages.  Pestering Nate and Garrett via IM to confirm my suspicions on how to tackle certain problems "the Cake way".  It's amazing what happens when you stop to think about all the techniques you've learned and then figure out the best way to weld them all together to solve a problem.
</p>
<p>
Again, I've said this before and will continue to say it:  making the effort to fully understand the tools you are using (that includes editor AND programming environment) can only make you better.
</p>
<h3>If the documentation is bad, don't even bother using it</h3>
<p>My IM pair-programming partner once said to me "Chris, if the documentation is shit then don't even think about using it."  Lately I've seen the wisdom in that.  If the documentation is lacking, just forget about using that tool.  Of course, if you *do* have the skills to dive right into it and figure out what's going on then this technique probably doesn't apply to you.
</p>
<h3>Learn your version control system, or else have it decide your fate for you.</h3>
<p>
There is incredibly well-written documentation for what I call the Big Three (CVS, SVN and Git) open source version control systems.  For the love of Wotan, go and learn the one you are using beyond how to commit a change.  And if you AREN'T using a version control system (no, renaming files to index.php.old.frank is NOT version control) then you should stop calling yourself a programmer.  Seriously.</p>
<h3>Peer code reviews are good, not bad</h3>
<p>
Even if it consists of taking 15 minutes to talk with your boss who wrote stuff and says "but I'm not really a programmer" so he understands the changes (for the better that you are making, it pays off huge in the end.  Especially when you know they will be going back in to tweak things as they play with the code you wrote.
</p><p>
That's all I can think of for the moment.  What programming techniques or tools have you come across that have made your work go faster or help you produce better code?  Let me know in the comments.</p>

