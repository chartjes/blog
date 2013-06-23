---
layout: post
title: "Baby Steps with Node.js" 
author: Chris Hartjes
date: 2012-02-13
comments: true 
sharing: true 
---

In a desire to stay relevant, I have been spending some time taking a look
at [Node.js](http://nodejs.org). Why? I believe it is always a good idea
to take a look at whatever the new hawtness is, if only to evaluate it's
suitability for use within your own applications. Sometimes it is also
a good idea to see if you can wrap your brain around it.

So I went and bought a good [bundle of ebooks about Node](http://leanbundle.com/b/node/)
and started going through the tutorial code. These two seemed like a good
place to start: an introductory tutorial and then another book that leaps
right into things with the aim of really giving you some hands-on work with
Node. 

The crowning glory of my early work is this bit of code from a tutorial that
emits events and then allows you to react to them:

{% codeblock lang:javascript %}
var EventEmitter = require('events').EventEmitter;
var util = require('util');

var Ticker = function(){};

util.inherits(Ticker, EventEmitter);

Ticker.prototype.tick = function() {
    self = this;
    interval = setInterval(function() {
        self.emit('tick');
    }, 1000);
};

var myTicker = new Ticker();

myTicker.on('tick', function() {
    console.log('TICK');
});

myTicker.tick();
{% endcodeblock %}

Now I realize that this code sample is something very trivial but I also
think it shows what someone who has mostly worked in languages without
callbacks is up against when they start using node.

As a PHP guy I am used to my code being executed pretty much in the order
that you read it when looking at the source code: from top to bottom, with
jumps out to other code as required but always returning to this flow.

Once you start getting into callbacks and other evented paradigms it becomes
a lot more difficult to intuitively figure out what's going on. Note that
I said "intuitively" because I'm sure that to anyone past the beginner
stage with Node would understand what is going on there.

There is a lot that looks familiar though. We have the importing of modules
via require statements. I also think this a good point to mention the
outstanding job that [npm](http://npmjs.org/) does in helping to manage
dependencies. I used to think that the [Ruby gems](http://rubygems.org) system
was one that should be aspired to. If you're going to ignore [CPAN](http://www.cpan.org/)
that is. 

Then I create what I can only describe as an empty object, and then we
say that our Ticket object is going to inherit whatever is in EventEmitter.
Okay, so far so good in terms of familiar territory.

Next we have the block of code that lets us create a tick method for our
overall Ticker object, and this is done with a callback. We have scoping
issues to deal with (hence the self = this line) and we are creating something
that will emit a 'tick' event once a second (1000ms). That looks a little
weird if you're not used to callbacks, and we even have an anonymous function
inside an anonymous function.

After that we then grab a Ticker object, tell it that every time there is a
'tick' event detected we want to log TICK to the console. Finally, we tell
it to run myTicker.tick() and then it goes on it's way emitting TICK once a second.

That's not such a mind bender once you break it down the way I did. But what about
this type of thing:

{% codeblock lang:javascript %}
var fs = require('fs');

fs.open('./a.txt', 'a', function(err, fd) {
    var writeBuffer = new Buffer('7');
    var bufferOffset = 0;
    var bufferLength = writeBuffer.length;
    var filePosition = 10;

    fs.write(fd, writeBuffer, bufferOffset, bufferLength, filePosition, function(err, written) {
        if (err) {
            throw err;
        }

        console.log('wrote ' + written + ' bytes');
    });
});
{% endcodeblock %}

We all know that it is easy to write spaghetti code in PHP because of the fact
that it grew up on the web: it was a templating language with C library 
wrappers. Very easy to just mash everything together. I see the same sort of
spaghetti possibilities there in Node, with the added bonus of callbacks
being mixed in there to make certain things difficult.

I understand what I did there: I am opening a file and then writing to it. The
way that I got to do it made me scratch my head. Writing to the file happens
as a callback that is executed as a result of opening up the file for
appending? Like I said before, that does not strike me as very intuitive
for programmers coming to Node with a little understanding of Javascript
and jQuery, which is probably most programmers' introduction to anonymous
functions.

But I do get it. You cannot get non-blocking IO without doing such gyrations
but I am concerned that sufficiently large Node applications will be, to put
it bluntly, a fucking nightmare to debug. Is this something that cannot be
moved away from if you choose to write programs using tools that suppoort
concurrency and/or evented concepts?

I'd love to hear what sort of best practices people are using in order to
tame the potential for Node applications degenerating into spaghetti hell.
