---
layout: post
title: "CodeMash 2012 Review" 
author: Chris Hartjes
date: 2012-01-16
comments: true 
sharing: true 
---
Last week I attended [CodeMash 2012](http://codemash.org) as a speaker and
gave my talk on [building testable PHP applications](http://www.slideshare.net/chartjes/building-testable-php-applications) (don't forget to buy the [book](http://grumpy-testing.com) that the talk inspired). Held in Sandusky, Ohio in the
cold of January it is an interesting conference. Unlike most conferences that
I attend, it is multi-disciplinary. There were talks on .NET, Java, Ruby, Python,
and two lonely talks about PHP. 

For me, this is somewhat uncomfortable. It is only natural that people who use
certain tools tend to flock together at a conference. I joked that where were
only 3.7 PHP developers (with someone stating that the 0.3 part is part of someone
that I cut off for not writing tests) but the fact was that unless you knew
members of multiple communities you were going to have to be content to feel
a little excluded.

Anyway, I did have a really good time hanging out with my friends and making
some new ones. It's a really good idea to talk to as many people as you can,
even they are not using the same tools you are using. You can gain some
perspective.

Let's go over the talks I attended and my thoughts on them.

# It's the Little Things (Brad Colbow)

[Brad](https://twitter.com/bradcolbow) is a freelance graphic designer from the Cleveland area. He also does
an online comic called [The Brads](http://bradcolbow.com/archive/) so, as expected,
his presentation was full of all sorts of awesome visuals. Also, I thought
that *I* talked fast, this guy made me look like one of the Ents from Lord of The
Rings.

The main take-away I got from his talk was that it never hurts to pay attention
to the little things. I realized that this holds true from both an UI/UX perspective
and in your code. A bunch of bad little things always turn out into one huge
bad thing.

His slides describing the blog posting he made about [how crazy it was to check out an audio book from his local library](http://bradcolbow.com/archive/view/the_brads_why_drm_doesnt_work/?p=205) were awesome.

# Vagrant: Virtualized Environments Made Simple (Matt Stine)

[Matt](https://twitter.com/mstine) took what he said was normally a 3 hour
tutorial and crammed it into a very informative 1 hour talk. It did help
that I had been considering the use of Vagrant anyway, but I got a better
picture of more practical uses of Vagrant. I did not know about [veewee](http://www.ducea.com/2011/08/15/building-vagrant-boxes-with-veewee/)
as a tool to help you create your own Vagrant boxes.

This is of interest because I had a hankering to play around with an [Arch Linux](http://www.archlinux.org/)
VM but found the existing base boxes out there, well, not working with the
version of Virtualbox I had installed. I think veewee will let me pursue
that further.

# Breaking the Sound Barrier with Node.js on Windows and Azure (Glenn Block)

While sitting in this talk I took a picture and tweeted about how it was time
to make myself "personally uncomfortable" by sitting in a talk involving a
technology that I don't use running on a platform I don't use. What I was hoping
to find out was some more basic information on Node.js and why it is such a 
big deal. 

To be perfectly honest, the more I see Node.js the more I start to understand
the allure of it. What really bothers me is that so many people are gambling
their applications on a tool that hasn't even reached 1.0 yet. I understand
the power of how Node.js gets things done. Evented + concurrency + JS is a platform that
has lots of appeal to people who maybe haven't done that sort of work before.
Not that I'm including myself in the group that "gets it" but at this point
in time I'm still on the "I will use Twisted/Tornado if I need to create event-driven,
high-concurrency web servers."

Maybe when Node.js gets to 1.0 I will think differently. 

Azure itself didn't really thrill me that much, but I do see the advantage of
that environment to people who have already made a large investment on the 
server side in Microsoft. What is really admirable is that they are making
some great contributions back to the open source community. The SDK for running
Node.js on Windows is open source, and I must give them credit for that.

# Code Kata and Analysis (Jim Weirich)

This was a talk that I went into expecting to be surrounding by Ruby hipsterism.
After all, this is the guy who created [Rake](http://rake.rubyforge.org/) and works
for a well-known [Ruby consultancy](http://edgecase.com/). Once I saw him I
knew I was in for a treat. Older guy. White hair. Unix-style beard. Runs emacs.

I was not disappointed.

A code kata is a programming exercise that serves a few purposes. You do it
in order to learn how to implement common algorithms in different languages
and learn how to solve the easy problems by habit, with the goal of then 
freeing up your mind to solve hard problems.

The code kata this time was to create an arabic number to Roman numerals
converter. The language of choice was Ruby (no big surprise there) and I
was even happier to see that it was a test-driven kata using [Rspec](http://rspec.info/).

This brings me around to a topic that makes me super uncomfortable. It seems 
to me that testing has become an integral part of the Ruby and Python ecosystems.
It does not appear to be common at all in the PHP and .NET communities. I care
about this sort of stuff so it does pain me to see such opposition in the form
of apathy and excuses amongst PHP programmers. I wish I could surround myself
with developers who feel like I do about the value of automated testing in
delivering solid applications. Maybe in the next life.

It was also good to see someone walk you through the whole TDD practice *and*
refactor stuff after getting a particular set of tests working. In the end
we had two great examples of code: an easy-to-understand converter and tests
that are easy to understand. 

# Dealing with Information Overload (Scott Hanselman)

One of the more dynamic speakers I saw, [Scott](https://twitter.com/shanselman) gave
a talk to a packed room on tips for dealing with information overload. From him
I learned some new techniques I'm going to be phasing in:

* No reading email until noon, and then "office hours" from a certain time onwards when
anyone can speak to you
* [Instapaper](http://www.instapaper.com/) is awesome because I can flag things to read later *and* get them
delivered to my Kindle on Friday afternoons for some after-dinner reading
* [If this, then that](http://www.ifttt.com/) is an extremely interesting tool
that can be used to trigger events that help you delegate things into the future
* The [Pomodoro Technique](http://www.pomodorotechnique.com/) is a very useful
tool to help with short-term focus. Cut out the distractions and concentrate
for 25 minutes. Even I think I can do that. 
* Keep your email responses very short (he reccomends [Five Sentences](http://five.sentenc.es/)) and
instead write a longer response to that issue and post it somewhere others can
find it, whether it is a company wiki or on your own blog. That way, next time
someone asks you that same question you can point them there 

Excellent talk full of lots of excellent ideas. I knew it was gonna be awesome
when he put [this video up](http://www.funnyordie.com/videos/e685c7e4ff/literal-video-total-eclipse-of-the-heart)
to entertain us before his talk. 

# A Few of My Favorite [Python] Things (Mike Pirnat)

[Mike](http://www.twitter.com/mpirnat) is a long-time Python programmer who
shared with us a "series of lightning talks crammed into one presentation".
While I have some basic Python knowledge I did see a bunch of really interesting
libraries and other tools that I did not know about. He covered so much, so fast
that I was glad he was going to post a link to the slides on his blog.

It also reminded me how, coming from the PHP world, languages like Ruby and Python
really are more terse. You might not think it matters (or even hate significant
whitespace) but for some people the elegance that can be found in Ruby and
Python code often makes it easier for others to understand what you are doing.
I know that I *feel* like I'm doing more with less when I write Python code.

Then I gave my [own talk](http://www.slideshare.net/chartjes/building-testable-php-applications).
I was disappointed that I actually ran out of time(!) for it. In the scheme of
things, 90 slides is about 20 too many for a talk on as dense a topic as unit
testing tools, strategies for writing code, and complementary tools to make the
whole thing easier.

I have identified abotu 20 slides that I think I could chop out and turn into
2 slides of the "and if you're interested in some tools that I think are
helpful" type.

I had a good time (including hanging out at the Kalahari's water park with my
kids) at CodeMash 2012 and hope to go back for CodeMash 2013.

# Why so little PHP?

I was asked about why I felt that there were so few talks about PHP and what
could be done to make it better. Well, when only 7 people even submit PHP
ideas I think there is a problem of visibility.

Given that this conference covers a wide variety of technologies I think it
is safe to say that there was quite a bit of overlap. 31 .NET talks? Really?
There is nothing wrong with .NET but do you *really* want to exclude an entire
sector of the web programming world at your conference?

Also, there is the issue of speaker reimbursement I know that the official
policy of CodeMash is "we cannot guarantee speaker reimbursement". That's cool
but that will also stop talented people who are not willing to travel from
where they are to the Cleveland airport and then hitch a ride to the Kalahari.
Maybe in the PHP world we have gotten spoiled by those who run conferences 
since they tend to cover a significant portion of the costs a speaker might
incur to get there.

There is no easy answer to how to get more PHP people to submit talks and to
attend the conference in general. It probably also doesn't help that the 
conference sold 1200 tickets in 20 minutes, making it that much harder to
get a ticket.

I'd love for more PHP folks to come to this conference and get their horizons
expanded with a glimpse at what other communities, just as full of energetic
people but with different focusses, are doing.


