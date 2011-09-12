--- 
layout: post
title: "People Who Make Me Feel Stupid: Antirez"
---
<p>This is the second of a five-part series where I highlight some developers who are doing work or espousing practices that make me feel stupid and realize where I need to push my skills towards.  Today's source of inspiration:  the man know by many online as <a href="http://antirez.com/">Antirez</a>, Italian software developer Salvatore Sanfilippo.</p>
<p>Antirez is the driving force behind <a href="http://code.google.com/p/redis/">Redis</a>, which is described as "an advanced key-value store" where it holds your dataset in memory at all times but writes them out to disk in a couple of different ways depending on your choices (either from time-to-time or all the time to an append log, depending on what level of consistency you need from the data).
</p>
<p>When I first started watching the whole <a href="http://en.wikipedia.org/wiki/NoSQL">NoSQL</a> movement, I remember seeing Redis in there as an option there.  However, I didn't know much about Redis until I noticed that my friend <a href="http://twitter.com/jperras">Joel Perras</a> was following this guy with an awesome mop of hair in his Twitter avatar and a cool nickname.  When I also saw he was the creator of Redis I knew this was a guy I had to follow and see what he was up to.
</p>
<p>
I won't go into the whole rationale behind the NoSQL movement, but what makes me feel stupid is not just the *way* Antirez has chose to implement his key-value storage solution, but the man himself.  He is one really smart dude.
</p>
<p>
First of all, he might be the most prolific hacker I've seen out there who actually lets people know what he's been up to.  His Twitter stream is full of comments about stuff he's been working on in Redis, some of which I understand and some of which goes right over my head (especially the <a href="http://antirez.com/post/redis-virtual-memory-story.html">stuff about the Virtual Memory work he's done with Redis</a> just shows me what I missed by not taking computer science courses.  Too busy teaching myself the new and shiny I guess.
</p>
<p>
Second, he spits out this volume of information in English.  Which is NOT his first language.  I couldn't imagine translating technical terms into my second fairly proficient language (which is German, and I understand it spoken way better than I speak it, read it or write it).  I have a hard enough time understanding technical terms written in English, never mind translating them in my head from another language.
</p>
<p>
So back to Redis now.  So not only is it a high-performance key-value store, using memory (the fastest storage medium) to store your data, but it also suited for use in a master-slave replication setup (claiming very fast replication speeds, and given the torturous bench marks I have seen Antirez talk about on twitter and his blog, I believe him) but can also do something that a lot of post-relational data stores (perhaps that's a better name than NoSQL) can't do:  unions (am I correct in assuming that is the equivalent of JOINS from the SQL world?), set intersections, comparisons between sets, and even generating sorted results.  I could see using Redis as the data store for the web front end of the corporate fantasy draft application at work.  I'm using a lot of key-value pairs in it, so a hybrid approach would probably work the best if I were to try it.
</p>
<p>
I mean, when you read that Virtual Memory post how can you *not* feel stupid for failing to see why Redis needs such a thing:  if you are storing everything in memory (remember, disk is the new tape) then you need your use of that memory to be as advantageous as possible and not rely on the operating system to do it for you.  For Redis, you want to keep as much memory available for your data so Antirez felt that he needed to find a way to free up the memory being used by the least-frequently accessed data.  A hard problem to solve for sure, but reading about what he did is just so inspiring.  As a bonus, you also learn some computer science skills along the way.  I felt the same way when I listened to a lecture about building virtual machines for Ruby:  awed and wondering if they teach that sort of stuff in computer science courses.
</p>
<p>While Redis might not be a solution I ever use at work (I am trying to keep our stack from adding too many new components just because I feel like playing with them) it's worth the lost hours reading Antirez' blog to understand all that goes on behind the scenes to make a cool piece of technology usable outside some very narrow scenarios.
</p>
<p>So, in the end, why did Antirez make me feel stupid?  <b>It was because he made me realize that you could take a simple idea (the key-value store) and add all sorts of very desirable features onto it without compromising it's main goal</b>.
</p>
