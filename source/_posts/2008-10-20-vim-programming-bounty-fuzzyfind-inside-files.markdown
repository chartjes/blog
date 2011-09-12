--- 
layout: post
title: "VIM Programming Bounty: FuzzyFind inside Files"
---
<p>(Note: I have updated this posting with some more info on what I am looking for)</p>
<p>
Since I make a little bit of money every month in advertising off this blog, I thought I'd put some of this money to good use.  I've been trying very hard to use <a href="http://www.vim.org">vim</a> as my editor for day-to-day use.  Previously, amidst lots of waffling, I had settled on TextMate for my day-to-day work.  Awesome editor, nice and lightweight and full of the cool features I needed.  There were two features that were stopping me from totally switching over.
</p>
<p>
First one was Cmd-T inside a project, which allows you to search through your project doing a fuzzy search for files that match your search string.  Awesome, awesome feature.  Cuts down on the browsing using the project drawer that I tended to do.  That particular hurdle has been fixed thanks to <a href="http://weblog.jamisbuck.org">Jamis Buck</a> (of Capistrano and 37 Signals) through his <a href="http://weblog.jamisbuck.org/2008/10/10/coming-home-to-vim">FuzzyFinderTextmate</a> plugin.  It's extends the <a href="http://www.vim.org/scripts/script.php?script_id=1984">fuzzyfinder.vim</a> plugin with a little bit of Ruby.  Does the trick, but you have to do a little jiggering to get it to recognize new files. An argument for another day I guess.
</p>
<p>
The second one is the also-awesome 'Find In Project' feature in Textmate, which searches through all your files looking for matches for the string (or regex if you're up to it) inside those files, then providing you with a list of files that you can open.  I'm wanting functionality similar to how the fuzzyfindertextmate plugin referenced above works, but for searching inside files.
</p>
<p>I am aware of how :vimgrep and :grep work (thanks to those who pointed it out), but I do not like how the quickfix window works, as I want a dropdown list of the files that contain what was found so I can open them.  Again, very similar as to how the FuzzyFinderTextmate plugin works.
</p>
<p>
So, I am offering $100 of my own ill-gotten advertising revenue (payable via PayPal) to the person who comes up with the solution I like the best that actually works.  If you don't want the money, I can donate it to the charity of your choice as long as they will take PayPal as well.
</p>
 <p>
I know *someone* out there can figure this out.  I'll give you until American Thanksgiving to come up with a solution.  Please post your suggestions in the comments, but please realize that all comments are moderated and off-topic ones will definitely be sent to /dev/null
</p>
