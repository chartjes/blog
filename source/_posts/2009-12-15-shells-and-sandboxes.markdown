--- 
layout: post
title: Shells and Sandboxes
---
<p>
Now that I have become a born-again tester, I've started looking at the testing I'm doing at work from more of a high-level point of view.  What are tools like <a href="http://www.simpletest.org/">SimpleTest</a> and <a href="http://www.phpunit.de/">PHPUnit</a> *really* doing?  They are providing a mechanism for the automating of running of tests.  Such tools also exist for frameworks like <a href="http://www.djangoproject.com">Django</a> and <a href="http://www.rubyonrails.org">Ruby on Rails</a>.  I cannot speak for Django, but the Rails community has made a very large commitment to testing tools and testing best practices.  But there is also another very powerful testing tool that Ruby and Python make available that PHP does not.
</p>
<p>
Both Ruby and Python offer a <a href="http://en.wikipedia.org/wiki/REPL">Read-eval-print loop</a> that can be run from the command line to allow people to do the opposite of what conventional testing tools do:  allow you to run interactive tests of your code.  I used the REPL available in Python (you know, just typing 'python' from my command line) to test out how to use various geocoding libraries for a side project.  My <a href="http://gilesbowkett.blogspot.com/">favourite Ruby programmer</a> (who is offering career consulting that I might find too enticing to pass up even at $100/month) uses <a href="http://en.wikipedia.org/wiki/Interactive_Ruby_Shell">irb</a> all the time to work on stuff.
</p>
<p>So in a way, a REPL is the anti-automated test.  I think that if there was a good REPL available for PHP, testing best-practices might take better hold.  Perhaps there is hope for a good PHP REPL in Alan Pinstein's <a href="http://github.com/apinstein/iphp">iphp</a> project.  I remember trying to continue work on the testing console I had created a number of years ago for CakePHP, and quickly realized that what I needed was a REPL.</p>
<p>
Since I did not have the desire to write my own limted PHP parser by messing around with <a href="http://www.php.net/eval">eval</a> (although, to be honest I did try playing with it and realized I did not know what the hell I was doing), the testing console was dead.  Besides, how many PHP devs really use PHP on the command line?  10%? 1%?  Hard to know, as the group I follow is a self-selecting one and I'm sure most of them have used PHP on the command line.  Hard to become an advanced PHP developer without trying to do stuff on the command line with it.
</p>
<p>
I was also pleased to find out (after a year of using it, no less) that <a href="http://exist-db.org/">eXist</a> had it's own REPL for XQuery - they call it the "sandbox".  It's awesome because I can take my "wrote this 6 months ago and can't remember if it still works" XQuery scripts and test them out.  Sort of like a command line client to your RDBMS.  It even tells me when I've got syntax or formatting errors in them BEFORE I try and execute them.  Talk about saving a developer time.
</p>
<p>
Do things like this exist for RDBMs like MySQL and Postgres?  Imagine an interactive client that is checking your syntax out <i>while you type it</i>.  If such a thing exists, please tell me!
</p>
<p>
Once again, I see I have started to diverge.  Back on track again.  
</p>
<p>
So, from a testing perspective it's easy to see how shells and sandboxes can become essential tools.  For example, all the good advice I have ever seen about unit testing clearly advocates a sandbox approach.  You create fixtures containing data.  You create mock objects to simulate functionality that might potentially be destructive.  You might even create a separate database for doing test operations on.  Clearly, the goal here is to create an environment that is the same as the one your code will eventually be running in, but separate from the "real" one.
</p>
<p>
A REPL, on the other hand, is a very powerful and very dangerous.  If you're not careful, you could very easily insert data into your current "working" environment instead of a "test" one.  As with so many other things, power comes with a price.  Sure, I can run some code to figure out how to use, say, <a href="http://www.sqlalchemy.org/">SQLAlchemy</a> but I better make sure that I am not writing data to my production database.  That would be silly.</p>
<p>
I'm guessing the main reason PHP does not have a easy-to-use REPL is because it grew up on the web first and the command line second.  Ruby and Python started on the command line first, and out to the web second.  It's really that simple I think.  Will PHP ever get a widely-accepted REPL?
</p>
