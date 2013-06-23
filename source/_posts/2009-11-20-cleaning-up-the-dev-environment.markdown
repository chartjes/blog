--- 
layout: post
title: Cleaning Up The Dev Environment
---
<p>Once I got a production push out of the way at work, I set about recreating my PHP development environment.  Currently I was running PHP 5.3.0 with Apache2 and Postgresql 8.4, all installed via MacPorts.  Why the time for a change?  Two reasons.  The first one is my desire to constantly tinker and tweak my environment.  The second reason was to test out some things for future work projects.
</p>
<p>
Those who follow the blog know that I had successfully convinced The Powers That Be at work to use Zend Framework to build out future PHP projects.  I also decided that it would be good to examine if <a href='http://www.zend.com/en/products/server-ce/index'>Zend Server Community Issue</a> is a viable stack for us.  In order to make that decision, I needed to install it and check it out.</p>
<p>
Being the cutting-edge guy that I am, I installed the beta version that comes with PHP 5.3.  I remember that I was having problems getting ZSCE working on Snow Leopard, but those problems seem to have disappeared.  Flawless install, and with about 10 minutes of work tweaking Apache configuration files I had my new PHP stack back.
</p>
<p>
I have to admit that to a jaded "I am sick of personally compiling my stack" person that I am acting like these days, the control panel for Zend Server is nice.  Point and click to add whatever extensions I need.  No more recompiling!  Perfect.  After playing with this, next week I will be installing it on our dev server at work.  MySQL is totally busticated for some reason, so wiping things clean and starting over with the Zend-provided version will be a welcome thing.  It will allow me to actually test some things front-to-back on the dev server.  Apathy towards your program's environment is a killer, so this will help me tighten things up.
</p>
<p>
So, with that out of the way the next step was figuring out what to do about Postgres.  Luckily this part was *really* easy.  I did a pg_dump of the entire database server and went and installed the version of Postgresql for OS-X that <a href="http://www.enterprisedb.com/products/download.do">EnterpriseDB</a> has.  Again, a flawless install and I was up and running in no time.  Created my desired users, and imported my database.  Again, it took about 10 minutes.
</p>
<p>
Other than the required tweak to my php.ini to declare the timezone for the server (I got this humungous warning in CodeIgniter about it) it was smooth sailing.  So now I had Apache 2, PHP 5.3, MySQL and Postgresql, all detached from MacPorts.  Next step was to remove MacPorts itself and I was good to go.
</p>
<p>
MacPorts, it was fun, but I've learned to get by without you.
</p>
