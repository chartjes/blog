--- 
layout: post
title: Blog Maintenance
---
I always like to try new things, so I'm forever destroying my applications trying new things and updating.  Luckily I am smarter with this blog and Serendipity makes it dead simple to upgrade.  Mad props to them.

Over at my <a href="//www.littlehart.net/attheballpark"">other blog</a> I've decided to move it from being served up by the Apache2 + FastCGI combo that is pretty common for <a href="http://www.rubyonrails">Rails</a> applications to being served up by <a href="http://www.lighttpd.net">LightTPD</a>, which is a very lightweight webserver that handles FastCGI much better than Apache2 does.

I mean, Apache2 is great webserver for general purpose stuff, but most of it's features are overkill for my powered-by-Rails blog.  So, I dug around on the Rails wiki and got some great documentation.  Here's what you do:

1) make sure that you install mod_proxy for Apache 2
2) create a rule in your httpd.conf file that tells it to pass all requests for your blog to a webserver running on a different port (in this case it's lighttpd)
3) configure lighttpd to run your Rails blog, with much better control over how many FastCGI processes are running at any one time
4) test the snot out of it
5) cry when things don't work and you don't know why
6) triumph your success on your own blog when you get it to work

The truth is that lighttpd + FastCGI will consume less resources than the Apache2 + FastCGI combination.  The server that hosts both these blogs is getting a good workout these days, so the more memory available for things like JBoss, the better.
