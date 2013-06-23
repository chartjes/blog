---
layout: post
title: "Not Really Rebels: My Øredev 2012 Experience" 
author: Chris Hartjes
date: 2012-11-17
comments: true 
sharing: true 
---
Many months ago I found out about [Øredev 2012](http://oredev.org) and submitted
a proposal to give my talk on building testable PHP applications. Much to my
surprise it was accepted and plans were hatched to fly me across the Atlantic
and give my talk.

The theme of this year's edition of the conference was "Viva La Rebellion". 
I'm guessing that they were hoping by accepting talks that seemed to fall out
of the mainstream they would inspire people to want to do things differently.

In that regard, I think they can declare it a success. The content was
widely varied, as you would expect from a conference featuring multiple
platforms and multiple programming languages. 

However, the sad reality is that, in my opinion, it's really only the speakers
who were there doing something revolutionary. I ended up spending quite a
bit of time hanging around with legendary Internet curmudgeon [Zed Shaw](https://twitter.com/zedshaw).
He was generous with his time and his comments, even after he found out that PHP was my bread-and-butter.

He gave a lightning talk where he explained his own experiences in rebelling
from inside a large monolithic organization, the US army, in order to prevent
himself from doing something he didn't want to do. He also brought up the 
point that so many people project an aura of rebellion through clothes, or
programming language of choice, but still start each day by sitting down
in front of a computer and essentially asking their boss "how can I make
you rich today, sir?"

From my own perspective, that's bang on. I joke all the time when on IRC that
all the perks that employers attempt to provide their employees are really
just things to distract you from the fact that you are a slave, a digital
sharecropper. I instead prefer to work from home as a way of making my 
chains fit a little less snug and to not have to hear the constant rattling.

I will also be truthful when I say that my current [employer](http://synacor.com)
treats me very well, allowing me some real freedom in terms of projects I get
to work on. A shitty job is one where you little to no say in what you get to
do. Been there, won't ever do that again.

So if you have the fire that is "in your belly", that yearning to do something
more with your time than just help someone else get rich, you speak at
conferences. Those are opportunities to teach people about things, to speak
to other like-minded people, to really take chances and find out whether you
really know what you are talking about. 

More importantly, it provides a way for you to gauge your own knowledge and
skills compared to those who are your peers in terms of willingness to share
knowledge. I was pleasantly surprised to find that when I went to talks
about technologies I don't use, I was understanding the concepts they were
talking about. 

I'm only a rebel in the sense that I am attempting to popularize an approach
to writing code that most PHP developers don't use, by using automated tests to 
drive the design of the code. The real rebels are people who challenge
pre-conceived notions within a community and then share what they've found.
Just because you use Rails doesn't make you a rebel. More like using PHP
makes you one these days.  

I did attend sessions about 2/3 of the time, the rest of the time spent
either working on my PHPUnit book or just relaxing in the super-awesome
speakers "cave" they set up for us. 

On Tuesday I only went to a morning workshop given by [Drew Neil](http://vimcasts.org)
about "Vim Mastery". I had ulterior motives to go: I had sponsored an episode
two years ago and I bought a copy of his book ["Practical Vim"](http://pragprog.com/book/dnvim/practical-vim).
After I got him to sign it I got 3 hours of good instruction on how to best
use Vim by learning how to do things more efficiently. Text objects and figuring
out repeatable sequences were the two big takeaways for me.

After that I hung out with a few of the other speakers and somehow a group of
us who were supposed to go out on a tour of Malmo missed the bus for the 
tour. Oh well.

Wednesday was the first day of the conference proper, with Monday and Tuesday
being just for half-day and day-long tutorials. The keynote speaker was
David Rowan, who is the editor for the UK edition of WIRED magazine. Lots
of talk about how technology is awesome and how the world has been changed
by software, and how software will be used to help solve some really tough
problems going forward.

All I could think of was the future is already kind of looking like [this](http://zenarchery.com/full-text-of-the-grim-meathook-future-thing/).

I skipped the first set of talks to work on putting the final touches on
my own presentation that was later in the day and then watched /dev/hell
guest [Justin Searls](http://twitter.com/searls) give a talk about the
value of mock objects in your tests. Justin is an awesome speaker, despite
his protests to the contrary and presented a very compelling set of strategies
for using mock objects in your tests.

My favourite part of the talk (besides the end, HAHAHAH just kidding) was
where he talked about mocking anti-patterns. Yes, there is such a thing as
using mocks incorrectly. You can check out the talk [here](http://oredev.org/2012/sessions/budgeting-reality-a-new-approach-to-mock-objects).

After lunch I sequestered myself again to make sure I was ready to give my
talk, and then popped up at 3:45pm to give my talk. Yes, it's true, there
were only 5 people in the room for my talk. PHP is not popular in Sweden
and I was also up against some good speakers, including the creator of
[Jenkins](http://jenkins-ci.org). These things happen, but my talk was
[recorded](http://vimeo.com/53065670) for anyone who was not there to see.

After my talk I stuck around to watch Konstantin Haase from [Travis-CI](http://travis-ci.org)
talk about what they do at Travis and provide a little bit of insight into the
challenges they face in running a Continuous-Integration-As-A-Service application.

Finally, at 6pm there was a closing keynote by Jim McCarthy, one of those guys
who kept popping up at key points in the history of software development and
he talked about his experiences leading the team that ended up building
Visual C++. 

He went on to talk about how he and his wife have devoted a number of years
now to studying how groups of developers work and on techinques that can be
applied to help them get more interesting work done. Not that he shared many
of them as that is how he makes his living.

Can't say that I agreed with his statement that the fact that
people in China were banned from seeing Facebook and Twitter was "no big deal".
I had expected to hear more stuff about "culture hacking", but maybe I just
had some preconceived ideas as to what that really meant. 

Then I had dinner and drinks with some of the other speakers, and went to
bed happy that I delivered what I thought was a good talk.

Thursday's opening keynote was by fellow Canadian [Reg Braithwaite](https://twitter.com/raganwald)
where he really talked about rebellious people, and the 4 most common roles
we find within any marketplace of ideas: Leader, Rival, Innovater, Everyone Else.
Fascinating analysis of how people's refusal to understand these four roles
leads to much unhappiness and even how entities move from one role to another.

Again, I highly recommend
[watching the video](http://oredev.org/2012/sessions/the-rebellion-imperative)

Next I went to Fred George's talk on Micro-service architectures, where
he talked about how he led a team that went to extremes while building a 
service-oriented architecture, by creating services so small (on the order
of 100 lines of code) that some of the concerns about unit testing and
versioning just went away due to size.

I have my own concerns about how to scale something like this, but it provides
a valuable lesson in really breaking down functionality of services into
the smallest pieces possible and then monitoring services to make sure they
are being used. Sort of like a survival-of-the-fittest contest for services,
giving developers the freedom to create multiple versions of services, running
them at the same time. Being so small, the cost of rewriting them, even using a 
new language, was minimal.

Next up was a talk on automated testing strategies for databases. It's rare that
I see a talk that really disappoints me. This was one. Nothing new, nothing
unconventional, nothing that a few people with more than a couple of years' experience
using databases could not have come up with. 

After lunch I watched a talk about the [Event Store](http://geteventstore.com) and 
felt weirded out by the talk. I wasn't quite sure what it was for, what problem
it was solving, and the whole talk felt like a very smooth and practiced sales
pitch for a commercial technology. Yes, they had some impressive stats in terms
of how it performed on the presenters laptop but I came out of that talk not
really understanding what it was for. I also was 99.999% certain that one part
of the demo was completely faked. The presenter entered some data into a 
form for an online chat application built with it, and what was displayed on
the screen did not match AT ALL what he had typed in. Very strange.

Next was a series of lightning talks. I sat in the set from Hampus Jakobsson
(talked about learing if you really loved something by doing it every day
for a month and then giving it up), Chris Hughes (talked about his experiences
with really doing things the way he wanted and not caring about the consequences)
and then Zed Shaw talked about why none of the attendees to the conference were
really rebels.

Finally, I watched [Steve Klabnik](https://twitter.com/steveklabnick) talk about
building Hypermedia API's. I think that anyone who is designing an API they
really expect people to use should [watch the talk](http://oredev.org/2012/sessions/designing-hypermedia-apis)
to get a feel for how tough a task it is to really build one.

The next talk was "Why Mud Rules" by Brian Footer. Brian talked about the
tendency of code to become a big ball of mud, and why that offends so many
developers. The money quote in his talk was "What do you call people who
ship big balls of mud? Millionaires." It's a reminder that shipping still
matters, even if the code is terrible in quality.

I had dinner with Felix Geisendörfer and Drew after this talk and spent more time hanging
out with Felix while he hacked on the code for controlling his drone.

On Friday, what could've been an interesting keynote by someone working
extremely hard to get fibre and high-bandwidth internet connections to homes
around Sweden was
wrecked and cut short by the MC, who wasted a lot of time on an audience
participation stunt. Also a diversion into Swedish rape laws was unwelcome.

After the keynote I watched Felix give a talk about
Node.js by demonstrating the library he had written for controlling his
AR drone quadcopter using Node.js. You have not really been to a conference
until you've watched someone fly a drone using cURL CLI commands that speak
to a web server RUNNING ON THE DRONE.

After that I sat in [Denise Jacobs'](https://twitter.com/denisejacobs) talk
about sparking creativity, and some techniques for getting yourself into
The Zone, The Flow, whatever you want to call that state where you can be
really productive. Lots of good reminders on removing distractions and
obstacles to being productive at work.

Following Denise's talk, I went to José Valim's talk about [Elixir](http://elixir-lang.org), which is
a Ruby/Python style language that sits on top of the Erlang VM. It looked
very interesting to me, definitely worth checking out for potential future
use in applications where concurrency become an issue. Plus you can drop down
into the weirdness that is Erlang when required.

After that I just kind of hung out with people in the speaker area, having some
great conversations with all sorts of people, until it was time for Hojun Song's
presentation about his project to send an open source satellite into orbit.
I have to admire his persistence, and how he's financing the project by
selling t-shirts! I was going to buy one, but he was not selling one in my
size...

Then the conference was over. One last dinner with the speakers I had met
and then I spent Saturday doing a day trip with Reg Braithwaite to Copenhagen
to meet with two [new](https://twitter.com/jippi) [friends](https://twitter.com/jose_zap)
who are PHP devs working in Copenhagen. Christian and Jose were awesome hosts
as they led us on a walking tour of the city. I also found out just how expensive
alcohol really is in Northern Europe. Two Irish coffees with double shots of
whiskey: CDN$40. Yikes.

All in all, I had an awesome time. 

Even though I was the only PHP talk at this conference, I realized that
I understood a lot more about programming than I realized. So much is 
transferable across languages and platforms. Go to conferences like this
to broaden your skill set, to check out how users of other languages
are solving problems, and you cannot stop from becoming a better programmer.

Øredev treated me very well, and I would consider going back again to speak
if my future plans allow me to fit it in.

Please, PLEASE check out the [recordings of the presentations](http://oredev.org/2012/videos) 
they have made available. Not every presentation is there yet, but they have
plans to make them all available under a Creative Commons license.
