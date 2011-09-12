--- 
layout: post
title: Database Shards and CakePHP
---
<p>As I've mentioned in this blog before, I spent 4 years working for an adult dating web site.  One of the biggest problems we ran into was a bottleneck involving database replication lag.  In a normal replication setup you have your application do writes to a master database and then those changes get replicated to the slaves.  That's okay...until you start dealing with huge amounts of updates.</p>
<p>
So, the quick solution was to make sure that we had fast enough hardware on the slaves to handle the huge volume of updates.  I remember partition lag in the order of 30 minutes on some of the machines (that's right, THIRTY MINUTES).  But the bigger problem came down to trying to find a way to minimize replication problems.  One of the things discussed (and I have no idea if it ever got implemented after I left) was partitioning the data into groups that made sense.  Some of the suggestions were to partition based on geographical location of the users, or simply do grouping based on the record ID.</p>
<p>
The other day I came across a great blog posting talking about <a href='http://highscalability.com/unorthodox-approach-database-design-coming-shard'>database shards</a> and instantly realized that they were talking about exactly what we were facing.  The goal is to spread the data around, denormalize things so that you have all your necessary data in one spot and to try and minimize replication issues.  So you'd be reading and writing to a shard depending on whatever criteria you are using.</p>
<p>Now, I know that you could put code into the beforeSave() method on a model to figure out what shard you would be writing to, but how to figure out what shard you would be *reading* from is something I am still mulling over.  Suggestions from #cakephp-dev (where I hang out during the work day) seem to point towards using a behavior (go to <a href="http://bakery.cakephp.org">the Bakery</a> and search for "behavior" to see lots of examples) to make this work.  I'll fool around with some code to see if I can come up with something that works.
</p>
