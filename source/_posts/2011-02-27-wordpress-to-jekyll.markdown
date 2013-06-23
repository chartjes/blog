---
layout: post
title: WordPress to Jekyll -- Adventures in Static Page Generation
---
*(I would like to apologize for blasting all my RSS readers with EVERY SINGLE POST on this blog when I set things up. The new template for the feed is different and I guess it forced changes on everyone. I didn't intend to do it that way, and I'm sorry for any problems it causes my readers)*

I've been using WordPress for a long time. It's served up 5+ years
of blog content with very few problems. But with each release of
WordPress, I find myself asking the question "is it worth dragging
all this extra functionality around with me?" I've come to the
conclusion that the answer is no.

Code generation is a programming technique that I think is both
unappreciated and under-utilized by programmers. Naturally, when I
started looking into turning my blog into static pages (I feel like
it's a really good fit for what I'm doing) I looked at solutions in
both Python and Ruby. In the end, I settled on
[Jekyll](https://github.com/mojombo/jekyll).

Then I headed to my
[favourite search engine](http://duckduckgo.com) and looked for
examples of how to convert a WordPress blog into a Jekyll blog. I
ended up finding this
[awesome blog post by Paul Stamatiou](http://paulstamatiou.com/how-to-wordpress-to-jekyll)
that provided me with pretty much all the information I needed. His
"here's all the things I wanted to do and how I achieved them"
worked out really well for me. I even used his
[own fork of Jekyll](https://github.com/stammy/jekyll) to build the
new version of this blog. If you follow his instructions and
advice, I don't think you can go wrong.

Not everything went 100% smoothly of course. I had to tweak things
because I was running my blog out of a subdirectory instead of out
of the root. That meant I had to pay attention to the value for
base\_url in the Jekyll configuration file, and I also had to be
careful of what I put in my Nginx configuration.

The big changes were to the WordPress migration tool that was
provided. I hacked it to automatically add a header to the post and
to also play with the
[YAML Front Matter](http://wiki.github.com/mojombo/jekyll/yaml-front-matter)
details inside each post. I had decided to use
[Disqus](http://disqus.com) for my comments and it took me a while
to figure out how to provide the proper reference values for the
Disqus javascript to find the comments since they had originally
been imported via a WordPress plugin.

I also had to deal with needing to change how syntax highlighting
worked. I had been using a plugin that supported
[GeSHi](http://qbnz.com/highlighter/) but Jekyll has support
out-of-the box for using [Pygments](http://pygments.org/), a
Python-based syntax highlighter. Armed with a little Perl one-liner
skills I quickly search-and-replaced all the old syntax
highlighting tags with the new pairs that I needed.

Now, my blog sits on my laptop and I edit the posts in Vim. When
I'm ready to check things out, I get jekyll to generate the blog
pages for me and I check them out using the local development
server. When I'm happy, I then fire up the deploy shell script that
I use (which runs jekuyll and then uses rsync to push the files up
to my blog) and BOOM I'm done.

I'll be keeping an eye out for any weirdness with the blog and I
hope to make some subtle changes going forward. Doing it as a
static site means I can experiment with the layout from
time-to-time like
[PeepCode has done](http://blog.peepcode.com/tutorials/2010/about-this-blog).
It's always good to learn new skills, and now I can add "static
page generation" to the toolkit.
