--- 
layout: post
title: What's In Chris' Brain - Blog Experiment Version
---
<p>
I had a few drinks last night with my fellow <a href="http://www.hutchic.com">Milton-area PHP developer</a> and we got to talking about a lot of different topics.  I will summarize a few of them here:
</p>
<p>
<h3><em>Concurrency is still drawing significant interest from me</em></h3>
</p><p>I recommended my friend check out Tim Bray's <a href="http://www.tbray.org/ongoing/When/200x/2009/09/27/Concur-dot-next">Concur.next</a> series (yes, I know I'm whipping this topic like a dead hors).  We discussed how when you've done so much work in the stateless environment of the web, made slightly more state-full by hacks like sessions and Ajax, how hard it is to wrap your mind around the idea of concurrency and event-driven models of programming.  Much like Mr. Bray I believe that somewhere out there is what will become the popular toolkit for creating concurrent programs, both on the server and on web sites.</p>
<h3><em>What about data stores when coupled with concurrent code</em></h3>
<p>Say I were to create a stripped-down version of the XML-feed reading program that we sell at work.  Say I write it in, oh, Twisted Python and then have the documents it grabbed get tossed into the XML data store I'm using at work.  I imagine that I would grab my list of files to retrieve and then spin off a thread/agent/worker/whatever to grab each one, do the necessary processing and then insert that document into the database.</p>
<p>
So, I guess it comes down to the ability of the datastore itself to handle concurrent requests?  I mean, if I was talking to a RDBMS like MySQL or Postgresql, can I count on them to handle concurrent inserts or updates?  That is a question worth doing some research about.
</p>
<h3><em>There is an opportunity to become a domain expert in the NoSQL field</em></h3>
<p>
If you were a freelancer who wants to live on the cutting edge, I would seriously invest time in learning one of <a href="http://couchdb.apache.org/">CouchDB</a> / <a href="http://incubator.apache.org/cassandra/">Cassandra</a> / <a href="http://www.mongodb.org/display/DOCS/Home">MongoDB</a> and figure out scenarios where these can be used.  Next step?  Profit!!
</p>
