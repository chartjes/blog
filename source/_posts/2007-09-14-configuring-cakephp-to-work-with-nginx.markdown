--- 
layout: post
title: Configuring CakePHP to Work With Nginx
---
<p>I use the incredibly small high-performance web server <a href="http://wiki.codemongers.com/Main">Nginx</a> to run this blog and some of my other projects.  Again, the ADD developer in me likes trying out new technology and nginx is a great fit for me so far.  I had to dig around a bit to find some rewrite rules that work for using WordPress (I'll share those if people are interested) but I got an email this morning from a fellow <a href="http://www.cakephp.org">CakePHP</a> user who couldn't find any configuration info on how to get it to work with Nginx.  Well, I did some fooling around and I'm confident this set of rules will work.  This assumes that you've gotten Nginx already up and running.
<pre>
# CakePHP rewrite rules
location / {
     index index.php;
     if (!-e $request_filename) {
          rewrite ^/(.+)$ /webroot/$1 last;
          break;
     }
}

location /webroot/ {
     index index.php;
     if (!-e $request_filename) {
          rewrite ^(.+)$ index.php?url=$1 last;
          break;
     }
}
</pre>
I am by no means an nginx expert, so if you have problems you are probably on your own.  I hope this helps out other people wanting to run CakePHP on nginx.
</p>
