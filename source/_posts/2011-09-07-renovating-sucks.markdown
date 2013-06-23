---
layout: post
title: Renovating Sucks
date: 2011-09-07
---
My apologies for the big mess here. As some of you who follow me on twitter might
be away, I accidentally blew away all the source for this blog while trying to fix
a syntax highlighting problem with some older posts. I thought I had a back-up of
the source on my external drive but it turns out that I was not telling it to
back up my home directory, for whatever reason. How awkward. 

Luckily I sill had the dump of data from my old WordPress blog in a database so
since I was still going to use Jekyll, I used one of the provided converters and
got back to work. I was still missing 13 posts though. Those were fairly easy to
recover thanks to the awesomeness that is [Pandoc](https://github.com/jgm/pandoc). What is
Pandoc? It bills itself as a "universal file converter" and it does a pretty
good job. I used it to convert those old posts in HTML format into Markdown. Now that I had
all my posts (stretching back to October of 2005) it was time to renovate.

I'm not using just Jekyll. I decided to use [Octopress](http://octopress.org), which
is a suite of tools written in Ruby that sit on top of Jekyll. I edit my posts in Markdown 
as usual, and then it's "rake generate && rake deploy" to make new posts. Of course, it 
wasn't quite that simple but that is the basic version of it.

(Edit: I previously had said I was going to drop comments from the blog but because I kept the same URL structure, the Disqus plugin
for Octopress was able to easily find them. Another small victory for Octopress)

Finally I apologize to people who are reading my feed if I have just blasted them with 800+ posts
due to me setting the blog up again. 

Anyway, I'm back and expect the info to start flowing again.
