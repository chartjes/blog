---
layout: post
title: Brain Dump for June 2011
---
Wow, it's been almost a month since I blogged anything. So I was
inspired to ask my twitter peeps to suggest some topics:

PHP legend Derick Rethans suggested I talk about
[food](https://twitter.com/#!/derickr/statuses/86103879980302336),
specifically biscuits. Well, I must confess, that I do love a good
biscuit. Every time I visit the US I always check to see if the
restaurant I'm in serves biscuits and gravy. Mmm, mmm, good.
Biscuits and gravy is something you just don't see on most Canadian
menus.

But all joking aside, I wanted to share some thoughts that have
been rattling around in my brain this past month.

PHP is undergoing what I think could only be described as a
personality crisis. First we had
[a well-intentioned guy making a bunch of patches he did to PHP available](http://www.xarg.org/2011/06/php-hacking/).
The reaction to this was predictable: the internals team responses
ranged from meh to outright dismissal due to his outsider status.
Predictably, users of PHP liked a lot of what he proposed. It's no
secret to those who have followed PHP internals, even sporadically,
that there is some dysfunction there. It's understandable: it's an
open source project without a real
[BDFL](http://en.wikipedia.org/wiki/BDFL) and the goals and desires
of the internal PHP core team are very different from those, like
me, who just use the language and are not in a position to
contribute any meaningful changes at the implementation level.

Next we had the \#phpneeds meme that made the rounds on Twitter,
culminating in the boys at Orchestra.io putting together a page
[outlining some of those requests](http://phpneeds.orchestra.io/).
Again, much of what was being said there makes sense but the same
old friction came up: the people with the ideas they want to see
implemented are not in a position where they can implement them. My
C and C++ skills are non-existent (although I have hopes that Zed
Shaw's proposal to do "Learn C The Hard Way" sees the light of day)
so all I can do is complain about my inability to effect real
change to PHP.

I even made my own
[contribution to \#phpneeds](http://twitter.com/#!/chartjes/status/83945075394088960)
that I thought now correctly puts PHP in the proper light: it is a
server-side solution that needs to decide if it wants to be bold or
meek. Look, I am not going to hash out all the old arguments here,
but I think there are some important issues to discuss. The big one
that I think gets ignored is that the core of PHP needs to decide
if PHP is going to continue to try and stay at the front of the
pack when it comes to it's suitability as a modern solution, or end
up like (don't hate me for saying this) Perl. By this I mean that
it's still a really good language, but it's been pushed aside and
left to those who either have to support legacy applications or is
being used by people who are strong enough to ignore the catcalls
from everyone else. Perl can still get the job done, but it's no
longer a consideration for anyone starting a new project...unless
they have many, many years of Perl experience and don't give a shit
about how it "looks" to be using a particular tool.

I'm not immune to this sort of thing either: I wish to branch out
and build applications using other languages and tools, but PHP is
the thing I know the best. I worry about the future: can I build
what I call Web Pi sites (Web 3.14159, get it?) full of real-time
information and distributed across multiple machines (cloud or
otherwise) using PHP as the server-side solution? What changes have
to occur at the bottom of the stack to keep PHP as a viable choice
for building web apps? Can I figure out how all this shit works so
I can actually build something like this?!?

PHP gets the job done, of that there is no doubt. Sometimes I yearn
for elegance in the languages I use, but then I realize it makes me
sound a lot like a whiny douchebag who hasn't shipped anything but
is quick to criticize other people's choices. I criticize my
choices all the time, whenever I find myself fighting the
components used to build the applications I work on. A good author
once said "write what you know" and for me that continues to be
PHP. Perhaps it's time to focus less on the language and more on
the problem you're trying to solve. I've taken to heart the concept
that the language you use for your application is simply an
implementation detail, because you can build shitty apps in any
number of languages. Because at some point it may be another
language that is the one that I know. Things change fast (says the
man looking warily at the marshalling forces of Node.js) so be
ready to make a paradigm shift when the time is right.

Which brings us back via rambling path to PHP. I think PHP 5.3
actually represented a large improvement for PHP itself: it
encouraged people who build things around PHP to re-examine what
they were doing and make things better. Witness all the new 5.3+
frameworks being built. Rather than being annoyed by there being
100+ PHP framework like I have in the past, I should look at this
as evidence of progress. I might never use one of those new
frameworks, but it's evidence that those who guide the future of
the language are trying to make things better. It may not be
happening at a pace that people are happy with, but it is
happening.

Now where did I put my copy of "Creating Web Pi Architectures"...

