--- 
layout: post
title: Deploying CakePHP Applications Using Capistrano
---
<p>There was a question on the <a href="http://groups.google.com/group/cake-php/">CakePHP mailing list</a> where somebody was asking about deploying CakePHP apps using <a href="http://www.capify.org/">Capistrano</a>.  What is Capistrano?  From the web site:
<blockquote>
Simply put, Capistrano is a tool for automating tasks on one or more remote servers. It executes commands in parallel on all targeted machines, and provides a mechanism for rolling back changes across multiple machines. It is ideal for anyone doing any kind of system administration, either professionally or incidentally.
</blockquote>
Sounds like exactly the type of thing a lazy programmer like myself needs.
</p>
<p>
In a nutshell, here's what you do:  you create a file that contains instructions on what tasks you need to run on your remote server, then you get Capistrano to load the file and execute the tasks you've defined.  In the past, Capistrano was pretty tightly integrated with Rails, but with version 2.0 I found I didn't need to have a Rails app installed *anywhere*, which is good news for anyone wishing to use this amazing tool with other web applications.
</p>
First thing I did was go and <a href="http://www.capify.org/install">install Capistrano</a>.  Relatively easy, but I had to install the Ruby gems system on my MacBook, something that was easy to do.  Once I had that installed, I then grabbed a <a href="http://simplisticcomplexity.com/assets/2006/9/21/deploy.rb">sample deploy.rb file</a>, and hacked away at it until I got  something very basic that would work for my situation (with names changed to protect the innocent):
<pre>
set :application, "yourapp"
set :repository, "svn://location.ofrepo.com"
role :web, "server.domain.com:
set :deploy_to, "/cakeapp/:
set :checkout, "export"

desc "This will deploy the app"
task :deploy do
     run "svn --quiet --force #{checkout} #{repository} #{deploy_to}"
end
</pre>
That sure looks simple, doesn't it?

In the spirit of convention over configuration, Capistrano has a few defaults.  It assumes you're using SSH to connect to the remote server.  It also assumes that you are using Subversion as your version control system.  "But you're accessing svn directly!" I can hear you saying.  Yes, but that's because I'm lazy and wanted to get the thing working as soon as possible.
<p>
I then saved the file in the config/ directory of my Cake app.  Why?  Seemed like a good place to put it.  Then, when I'm ready to deploy the changes I've made, here's what happens.  I tend to place my cake root outside of the web root so that I can have multiple Cake apps running off the same library.  ~/src/www.ibl.org is the app/ directory if you look at it that way.
<pre>
cupcake:~/src/www.ibl.org chartjes$ cap -f config/deploy.rb deploy
  * executing `deploy'
  * executing "svn --quiet --force export svn://server.littlehart.net/www.ibl.org/trunk /home/wwwroot/www.ibl.org/public/app/"
    servers: ["phantasm.ibl.org"]
Password: 
    [phantasm.ibl.org] executing command
    command finished
cupcake:~/src/www.ibl.org chartjes$ 
</pre>
That's it!  Now, when I finish my local development and check my changes into my repository I can deploy them to production via the command line.  For more advanced deployment schemes I suggest you checkout <a href="http://www.capify.org/">the main Capistrano site</a> and as always, Google is your friend.
</p>
