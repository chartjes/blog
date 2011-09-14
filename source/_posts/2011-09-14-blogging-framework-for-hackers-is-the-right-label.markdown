---
layout: post
title: "'Blogging framework for hackers' is the right label"
author: Chris Hartjes
date: 2011-09-14
comments: true 
sharing: true 
---
I don't regret moving from a Wordpress-powered blog to one that is created using a static site generator. But I can definitely say that the journey
to a static site (initially [Jekyll](http://github.com/mojombo/jekyll) and now using [Octopress](http://octopress.org)) is not a path I would recommend
to anyone who is not comfortable debugging issues from the command line or unable to write conversion tools from scratch depending
on the situation.

While I do like how easy Octopress makes it to manage my blog I find the whole setup to be, like so many other tools and web applications I've come across, to be brittle. Too many moving parts. Too much reliance on things being perfect and if they're off by even the tiniest bit everything falls apart. I am by no means innocent of creating brittle applications but I try and go out of my way these days to create things that are as robust as possible in the constraints of the existing system.

For me it was [RVM](https://rvm.beginrescueend.com/), the "Ruby Version Manager". I like to call it "what [virtualenv](https://github.com/pypa/virtualenv) would look like if Ruby guys got their hands on it". On the surface it sounds awesome: it sets up an environment containing the Ruby binary you want and the Ruby gems you want, isolating this application from whatever the defaults were on the system. Just like virtualenv. Sounds incredibly useful. But when it breaks, it breaks and there is NO way to tell what the hell has happened.

Somehow through deleting the .rvmrc file (the RVM config file) I managed to break my install of Octopress. This happened at the same time I upgraded the Octopress components by pulling from the master. I had no fucking idea what had happened, all I knew was that it wouldn't generate any more blog posts for me and was reporting errors about going too many stack levels deep, mal-formed YAML, and Unicode errors. Funny how none of that seemed to have mattered to Octopress before I updated.

In the end, I had to completely remove the install and start it up again from scratch. This is not what I call a successful error-resolution process. In my mind I shouldn't have had to do this at all, but through the removal and re-addition of one file everything was completely messed up. One upside was that in the process of getting things back to "normal" I created two scripts that I hope can be of use to people who ran into the same problems I did.

I used the stock migration script for Jekyll for Wordpress users who had their posts in a database. The script reads all your posts in and then spits out new posts in the Markdown format that Jekyll expects. The new version of Octopress likes Ruby 1.9.2 which, as far as I can tell, is much less forgiving of mistakes in YAML and Unicode characters. I don't use Ruby so I am not as familiar with these issues. It sure sucked when I was searching for solutions to my problems.

So, I had 427 posts that had been converted and there was no way I was going to search through each one by hand to resolve the issues. So I needed two scripts: one to parse all the posts to check for invalid YAML and one to force re-encoding of the content of each post into UTF-8 (because that's how Jekyll and I roll). Being a polygot programming wannabe, the first script for YAML validation was in Python:

{% codeblock lang:python %}
#!/usr/bin/env python
import getopt
import os
import re
import sys
import yaml

from yaml import load, dump

try:
    from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
    from yaml import Loader, Dumper

class Usage(Exception):
    def __init__(self, msg):
        self.msg = msg

def main(argv=None):
    if argv is None:
        argv = sys.argv

    try:
        try:
            print "Checking markdown files in the current directory..."

            #root = "/Users/chartjes/Documents/atthekeyboard/source/_posts"
            for r,d,f in os.walk('.'):
                for file in f:
                    fp = open(file, 'r') 
                    contents = fp.read()
                    marker = "---"
                    a = contents.find(marker)
                    b = contents.find(marker, a + len(marker))
                    try:
                        yaml_to_parse = contents[a:b]
                        yaml.load(yaml_to_parse)
                    except:
                        print "%s is invalid YAML" % file
        except getopt.error.msg:
            raise Usage(msg)
    except Usage, err:
        print >>sys.stderr, err.msg
        return 2

if __name__ == "__main__":
    sys.exit(main())

{% endcodeblock %}

It took me a while to find some code to extract just the YAML from the posts, and I am not 100% happy with the result but it did the job and identified a handful of posts that made it through the migration and didn't properly wrap post titles with colons (which YAML thinks is bad) in quotes. With the bad YAML fixed I then had to fix any bad characters in the posts. For that I dragged out my copy of "Programming Ruby" (proudly proclaiming on the cover that it was a Second Edition covering Ruby 1.8) and stole some code from a conversion script someone wrote for Wordpress blogs if you dumped the contents as XML.

{% codeblock lang:ruby %}
#!/usr/bin/env ruby
require 'fileutils'

markdown_files = Dir["*.yml"]

markdown_files.each do |m|
    puts "Converting #{m}"
    f = File.new(m)
    post_contents = f.read
    content = post_contents.encode("UTF-8")
    new_file = File.new(m + "-new", "w+")
    new_file.write(content)
    FileUtils.mv(m + "-new", m)
end
{% endcodeblock %}

Like I said, I'm happy I switched but the brittleness of the whole setup is something I find annoying. I realize that Octopress probably started it's life as one person's set of tools they were using to manage a Jekyll blog. The process of turning that extraction into a general-purpose tool is a difficult one and I want to say thank you to [Brandon Mathis](https://github.com/imathis) for providing quick and useful information in the #octopress channel on Freenode while I tried to figure out how to fix the problems I was facing.

