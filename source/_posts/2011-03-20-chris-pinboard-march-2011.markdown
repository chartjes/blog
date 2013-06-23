---
layout: post
title: Chris' Pinboard -- March 2011 Edition
---
I haven't done a "what's in Chris' brain" posting for a while, so I
thought as part of the Ideas of March it was as good a time as any
to resurrect it.

I had been a Delicious user and had not used it much except as a
dump for links I intended to read later. I often didn't come back
but it was nice to have those links around for those times when the
coding part of my brain wasn't working and I needed to some more
research into topics I had flagged for further study. Then the
infamous leaked graphic that showed that Yahoo was planning on
[sunsetting](http://en.wikipedia.org/wiki/Application_sunsetting)
Delicious started making the rounds. It got me to thinking about
the dangers of relying on a free service for long-term archiving of
information. Delicious could just go POOF one day, taking all the
stuff I found interesting with it. I decided to move my links to
[Pinboard](http://pinboard.in/u:grumpycanuck) and have introduced
time to go over the links I store once a week into my workflow. I
even read up a but on their architecture and found their
development philosophy refreshing.

They are using PHP on the front, Perl in the back, with MySQL and
S3 as data stores. As they put it, very vanilla. No framework being
used, and I'm starting to see that perhaps my framework "obsession"
is having a drawback other than me having a mind full of how to do
things in 10 different ways. Anyway, feel free to browse through my
bookmarks: no secrets in there and I'd be glad to discuss anything
you come across. I wanted to go over a few things I recently
"pinned" to my brain.

[Beyond Frameworks](http://vimeo.com/21145583) is a presentation
that Stuart Herbert gave at the
[PHP UK Conference](http://phpconference.co.uk/) this year. He
talks about the challenges of trying to prevent the frameworks you
build your applications with from swallowing everything up around
them. When is the last time you actually upgraded an application
written in one version of a framework to work with a newer version?
Personally, I always like to keep upgrading the framework for my
applications to the latest stable versions and dealing with errors
by making sure I have decent test coverage. Others are not so lucky
to have the kind of control that I am allowed to exert over the
code base. Heck, I don't know how much of a task it would be to
update a Zend Framework application I'm using right now at
Moontoast. Maybe I should go and look.

Anyway, I want to take a deeper look at the architecture he
proposes: keep the framework-specific stuff to a bare minimum and
write as many standalone components that can then be shared by
other applications in your company. His use of PEAR as the method
of organization and installation is just genius: why reinvent the
wheel. I watched the presentation once while distracted by other
things, I will take a run through it again. Jason Gilmore is the
publisher of my CakePHP book, co-founder of the awesome
[CodeMash](http://codemash.org) conference and a pretty prolific
author. He recent blogged about the
[tools he used to write his latest book](http://www.wjgilmore.com/blog/entry/why_i_published_easy_php_websites_with_the_zend_framework_using_docboo).
I have a supersekret project I am working on and are using a lot of
these same tools at Jason's suggestions. Writing a book was a very
interesting project, and I agree that you should not be fighting
with the tools you are using. Jason's tool chain has allowed him
flexibility in the formats he can release his book in. As someone
who just bought a Kindle, I can appreciate how important it is to
have ebook options.

Interested in know what some of the PHP 5.3+ frameworks are shaping
up to look like? Check out
[Symfony2](http://www.slideshare.net/hhamon/symfony2-introduction-7237021),
[Alloy HMVC](http://www.slideshare.net/vlucas/alloy-hmvc-php-framework)
and what I consider to be the "first to the post" PHP 5.3+
framework [Lithium](http://lithify.me/). I'm not sure what
framework I would pick if I was starting a PHP project from
scratch, but I do know that I would be avoiding using some of the
previous full-stack options available to me. Especially if I want
to move into a layered architecture as proposed by Mr. Herbert.

My sister got me an [Arduino](http://arduino.cc) starter kit for
Christmas (still haven't actually received it due to scheduling
conflicts as she lives 250 miles away) and I can't wait to hack
around with it. It uses it's own little language called
[Wiring](http://wiring.org.co/) but I found some info on how to use
Python to [control Arduino devices](http://www.pyaler.org/).

Finally, I've been working on a new version of the web site for the
[simulation baseball league](http://www.ibl.org) I've been a part
of for 14 seasons and counting and I've been
[building it](https://github.com/chartjes/ibl) using Django and a
few other things. I'm also using this project to get myself more
familiar with
[BDD](http://en.wikipedia.org/wiki/Behavior_driven_development) and
are using an awesome tool called [Lettuce](http://lettuce.it) to
write my tests. I have a sneaking suspicion that since I could do
some Facebook integration testing using Cucumber (I linked to it in
a previous post) I might be able to use Lettuce along with some
Facebook libraries in Python to do that too. We'll see, but Lettuce
has proven to be easy to get up-and-running with.

So, my third Idea of March: share the things you've been
bookmarking and tagging for later use. You never know what other
people will find useful from them.
