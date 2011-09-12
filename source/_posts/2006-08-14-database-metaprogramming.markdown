--- 
layout: post
title: Database Metaprogramming
---
<p>
In the absence of anything really pressing to talk about, I thought I'd share two tidbits I found via my feed reader.
</p>
<p>
J. Scott Johnson had a great post at his blog about <a href="http://fuzzyblog.com/archives/2006/08/12/sql_calc_found_rows-and-faster-count-alternatives/">SQL_CALC_FOUND_ROWS and Faster Count(*) Alternatives</a>.  If you've ever had to write some code that loops through a database searching for counts that match specific where clauses, then go and read this posting.  It just makes so much sense and I had always suspected there was a better way to do the old "query once to get the data you want and then query again to get the count that matches that data" trick.  I must get my SQL skills boosted up one of these days.
</p>
<p>The second posting is from Josh Susser where he talks about <a href=http://blog.hasmanythrough.com/articles/2006/08/13/how-dynamic-finders-work>how ActiveRecord's dynamic finders work</a>.  For those not wiling to go through the archives, ActiveRecord is an Object Relational Mapping wrapper for database connections that makes using databases in your Rails code insanely easy.  <a href="http://www.cakephp.org>CakePHP</a> has it's own ORM stuff and I've been thinking about trying to find a way to expand the findByFoo to be able to handle findByFooAndBar, which it currently does not support.
</p>
<p>I know this is a posting for hardcore programmer geeks, but even if you're mildly interested I suggest you check both those posts out.</p>
