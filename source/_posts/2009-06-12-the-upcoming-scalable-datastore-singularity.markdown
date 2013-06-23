--- 
layout: post
title: The Upcoming Scalable Datastore Singularity
---
<p>I talked about this briefly on Twitter but I am wondering if we are at the edge of an upcoming "singularity" for technologies dealing with really large data sets.  Things like <a href="http://couchdb.apache.org">CouchDB</a>, <a href="http://tokyocabinet.sourceforge.net/">Tokyo Cabinet</a>, <a href="http://incubator.apache.org/cassandra/">Cassandra</a> and some other non-RDBM's datastores that I'm sure I'm forgetting about are starting to filter down from the experimental level to the usable-by-developers-like-me level.  We all dream of working on a project that has to deal with highly scalable data sources, because that means the project has been an awesome success.</p>
<p>
I just wonder if use of these types of technology for a site that you have no idea whether or not it will be wildly successful is a case of premature optimization.  I mean, it's cool that I can use CouchDB for a little side project that is more an exercise in learning CouchDB and Python.  But could I use something like this at work?
</p>
<p>(Warning, this is where I start talking about some of the things I do at <a href="http://www.xmlteam.com">my day job</a>.) Our systems accepts tens of thousands of XML documents per day from different sources, and then a lot of them get translated from source XML into <a href="http://en.wikipedia.org/wiki/SportsML">SportsML</a>.  Now, granted, some of these things are updates of previous information, but we still have to process them.  One of our products queries our servers, pulls down the SportsML documents and then parses them to stick the results in a RDBMS.  Customers can then build their own products on top of this system, writing SQL to pull out the info they want.
</p>
<p>
But what if instead of parsing them, we drop them into a document datastore?  I've been using <a href="http://exist.sourceforge.net">eXist</a> for a work-related project and after some initial struggles (mostly learning to use <a href="http://www.w3.org/TR/xquery/">XQuery 1.0</a>) it's the perfect datastore for a project where you need to deal with XML.</p>
<p>
I work on a web service front-end for all these stats, which we both give to our customers (it's open-sourced under the GPL) to run themselves *and* use it internally (eating our own dog food!).  I've often wondered if we switched to using eXist as the back-end instead of a more traditional RDBMS, would our customers be able to handle it?  Finding a developer who knows SQL or a DBA who can tweak the queries is probably easier than finding someone who is familiar with XQuery / Xpath and eXist.</p>
<p>So while switching to something like eXist would make sense on a certain level (skips the intermediate step of parsing the XML, we have in-house knowledge of writing XQuery scripts to pull data out) it definitely does not make sense for us from a customer support perspective.  Definitely a research project for when the company makes enough money to hire some minions for me to boss around.
</p>
<p>
Maybe I'm wrong, but much like the <a href="http://en.wikipedia.org/wiki/Magic_8-Ball">Magic 8-ball</a> says: all signs point to yes.  Non-RDBMS datastores are getting right up into our faces, and it's only a matter of time before a high-profile project uses one of these and then everyone jumps on board.  Keep your eyes open and read up what you can about these things.  You never know when you might get the opportunity to use one in a serious way.
</p>
