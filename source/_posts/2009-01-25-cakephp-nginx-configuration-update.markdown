--- 
layout: post
title: CakePHP + Nginx Configuration Update
---
<p>In a previous post I had talked about how to configure CakePHP to work with <a href="http://nginx.net/">Nginx</a>, a lightweight, high-performance HTTP server.  I'm in the process of creating the website for my upcoming book *and* had recently switched back from using Apache to using Nginx again, so I thought it might be time to roll up my sleeves and figure out how to make it work in a subdirectory.  After much gnashing of teeth and pissing and moaning, I figured it out.
</p>
<p>
In this example, let's assume that we are going to be running our application out of /foo, and that we already have PHP applications running with Nginx already.  There are plenty of examples out there that you can google for.  So, what took me forever to do was to figure out how to properly make the second part of the rewrite rule.
</p>
<pre>
# configure Cake app to run in a sub-directory
# Cake install is not in root, but elsewhere and configured
# in APP/webroot/index.php
location /foo/ {
    index index.php;

    if (!-e $request_filename) {
        rewrite ^/foo/(.+)$ /foo/webroot/$1 last;
        break;
    }
}

location /foo/webroot/ {
    index index.php;

    if (!-e $request_filename) {
        rewrite ^/foo/webroot/(.+)$ /foo/webroot/index.php?url=$1 last;
        break;
    }
}
</pre>
<p>
As stated before, I am not an Nginx expert so I will simply tell you what I *think* this configuration is doing.  First, it looks at any request that comes into /foo and if it can't find it right away, it then rewrites the request to go over to /foo/webroot.  Then, any requests that come in for /foo/webroot, it checks to see if it can serve the file directly, like if it was in the css or js directories.  If it can't, it then strips out everything *after* /foo/webroot in the request and passes it over to APP/webroot/index.php.</p>
<p>It was that second part that gave me the toughest time.  Once it finally dawned on me that I needed to remove '/foo/webroot' from the request, everything worked perfectly.
</p>
<p>
If there are any Nginx experts who can tweak this to work better, let me know.
</p>
