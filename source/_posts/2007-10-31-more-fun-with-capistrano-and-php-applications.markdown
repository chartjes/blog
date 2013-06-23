--- 
layout: post
title: More Fun With Capistrano and PHP Applications
author: Chris Hartjes
date: 2007-10-31
---
<p>
So, I need to deploy changes to a work-related project from my laptop to a dev server.  I was told that one of our other developers had a solution using shell scripts, but I couldn't figure out a problem with it and didn't want to hack away at his scripts in case I broke something he was depending on.  So, I figured it was time to go back to Capistrano and simply hack my deploy script I had used <a href="http://www.littlehart.net/atthekeyboard/2007/09/21/deploying-cakephp-applications-using-capistrano/">for another deployment</a> to fit this circumstance.</p>
<p>
So, off I went hacking away at it and testing it.  Then I discovered something:  I need to be able to send a password for both running some commands on the remote server and for checking some stuff out of a <a href="http://en.wikipedia.org/wiki/Subversion_%28software%29">SVN</a> repository.  So, I did some googling and here's what I came up with:<br />
{% codeblock lang:ruby %}
task :deploy do
     run "sudo cp -r #{deploy_to} #{deploy_to}-old" do |ch, stream, out|
          ch.send_data "#{sudo_password}\n" if out =~ /Password:/
     end

     run "sudo svn --quiet --force #{checkout} #{repository} #{deploy_to} do |ch, stream, out|
          ch.send_data "#{svn_password}\n" if out =~ /.xmlteam.com's password:/
     end
end

task :rollback do
     run "sudo mv -r #{deploy_to}-old #{deploy_to}" do |ch, stream, out|
          ch.send_data "#{sudo_password}\n" if out =~ /Password:/
     end
end
{% endcodeblock %}
</p>
<p>
All those #{...} values are simply variables I defined in the recipe file.  You don't actually expect me to tell you what my passwords are for access to various machines, do you? :)  I remember how difficult this stuff was to do in previous versions of Capistrano, requiring all sorts of hacks to make it deploy non-Rails applications but they removed that dependency with Capistrano 2.0, thus making it possible to use Capistrano with ANY project, not just a Rails one.  Although you can use a lot of built-in magic if you use Capistrano to deploy a Rails project.</p>
<p>Now that I know how easy it is to pass data to the remote server, I can actually envision some fairly complicated deployment scripts.  Hope this helps out other people who've come here and read my other post about using Capistrano to deploy their CakePHP projects.</p>
