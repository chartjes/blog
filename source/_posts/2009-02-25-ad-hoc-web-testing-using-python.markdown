--- 
layout: post
title: Ad-hoc Web Testing using Python
---
<p>
"But Chris, I thought you were a PHP guy?"  Yes, in my day-to-day work I use a lot of PHP.  However, I am branching out as required by my desire to learn new things.  One of those new things is <a href="http://www.python.org">Python</a>, both on the web and the server side.  I thought I would share with you a tool I whipped together to do some testing of webservices at work built using <a href="http://www.sportsdb.org/sd/sportscaster">an application front-end that we have released under the GPL</a>.  Of course, you need to be using our non-free sports data feed fetching software, but that's not the point.
</p>
<p>
So, as of March 1 we are turning off an old server that uses an older, Perl-using-CGI web service and redirecting those customers using it to one built using PHP (Code Igniter specifically.  Again, this decision was made before I started at that job.)  As the lead engineer on the project (okay, the only one) I had to make sure that all the old queries would work on the new server.  When my boss told me to "manually check them" I scoffed and said "manual checking is for suckers, I'm going to write a script to do it.".
</p>
<p>
The methodology is as follows:
<ol>
<li>Make sure that calls to the old web service return properly formed XML *or* HTML with a certain string  in it when we are doing XSLT transforms</li>
<li>Do the same thing with the new web service</li>
<li>Tell me when something isn't right</li>
</ol>
</p>
<p>
I could do more work in this script, to do things like look for certain tags in the XML document to be populated but we can skip that for now.  The new web service has been tested quite well and we are getting back results as expected via some other tests I've written using PHPUnit.</p>
<p>
With help from <a href="http://diveintopython.org/">Dive Into Python</a> and some judicious searching on Google, I came up with this script.  As far as I can tell, the only outside dependency was me using <a href="http://www.crummy.com/software/BeautifulSoup/">Beautiful Soup</a> to read in the HTML output.  Maybe I could've used Beautiful Soup for both the XML and HTML, but this still works just fine.
</p>
{% codeblock lang:python %}
#!/usr/bin/python 

import urllib2
from xml.dom import minidom
import fileinput
from BeautifulSoup import BeautifulSoup

host = 'http://w04.foo.com';
host2 = 'http://w05.foo.com';
users = ["foo", "bar", "baz", "alpha", "omega"] 
passwords = ['xxxxx', 'xxxxxx', 'xxxxxx', 'xxxxx', "xxxxx"]
key = 0

for username in users:
    print "Doing check for " + username
    password = passwords[key]
    password_mgr = urllib2.HTTPPasswordMgrWithDefaultRealm()
    password_mgr.add_password(None, host, username, password)
    handler = urllib2.HTTPBasicAuthHandler(password_mgr)
    opener = urllib2.build_opener(handler)
    urllib2.install_opener(opener)
    password_mgr.add_password(None, host2, username, password)
    handler = urllib2.HTTPBasicAuthHandler(password_mgr)
    opener2 = urllib2.build_opener(handler)
    urllib2.install_opener(opener2)

    for line in fileinput.input(username + "_url.txt"):
        try:
            data = urllib2.urlopen(line)
            
            try:
                xmldoc1 = minidom.parse(data)
            except:
                html = urllib2.urlopen(line).read()
                soup = BeautifulSoup(html)

                if not soup.find(text="XML Team Solutions"):
                    print "Bad XML+HTML:" + line
        
        except:
            print "Could not load " + line

    key = key + 1
{% endcodeblock %}

<p>
URL's that I wished to test were stored in text files that this script then read in.  Using a little grep + awk magic I was able to extract URL's from our web server access log in order to test.  I'd appreciate any tips from Pythonistas out there on how to make this code conform more to the "Python way" if there is such a thing.
</p>
