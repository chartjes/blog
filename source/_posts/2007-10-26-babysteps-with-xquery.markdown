--- 
layout: post
title: Babysteps with xQuery
---
<p>I know what you're thinking:  "Chris, aren't you supposed to be talking about CakePHP, or PHP, or your ever-changing working conditions?!?".  Alas, enough about my storied working career.  Working <a href="http://www.xmlteam.com">here</a> now means that I'm going to become Mr. "I know how to manipulate XML" in a hurry.  Lucky for me, I can use PHP 5 and have access to SimpleXML to make fooling around with raw XML (is that actually a term?) so much easier.  I remember working with <a href="http://www.sportsticker.com">PA Sportsticker</a> XML feeds and having to write code to parse stuff out in PHP 4.  Compare that to using SimpleXML in PHP 5.  Go ahead, I'll wait while you go and look it up.</p>
<p>
So, for a project I'm working on (no names until it goes beta) I'm having to write and retrieve information from an XML document repository system (<a href='http://www.caucho.com/resin-3.1/'>Resin</a>  + <a href='http://exist.sourceforge.net/'>eXist</a>).  Now, I'm not too bad with database stuff but this system doesn't use SQL.  It uses something called <a href="http://www.w3.org/TR/xquery/">XQuery</a> to retrieve information.  I can pull back XML snippets, whole XML documents, or just extract data from it.  On the storing side, you can simply insert whole XML documents into it and then eXist takes care of indexing etc so you can look for information inside those documents.</p>
<p>
Lucky for me, my company has a subscription to O'Reilly's <a href="http://safari.oreilly.com">Safari</a> system so I grabbed 'XQuery Kick Start' and started reading up on how xQuery works and how I can cheat and only learn what I needed to do for this first task. So, what I had to do was this:
<blockquote>
Give me all games that belong to this league
</blockquote>
So, I had the key for the league, and every document that was a game has the key for the league as an attribute.  Now, if I was doing SQL you'd have something like:
<code>
SELECT * FROM games WHERE league_id = $leagueKey
</code>
and then you iterate through the results like normal.  Let me tell you, xQuery is VERY different.  <a href="http://bin.cakephp.org/saved/24839" target="new">Here's what it looked like</a>.  My apologies for the link to the saved paste but it was looking terrible in preview. :)
</p>
<p>Wow, not too intuitive at first glance, is it.  Anyway, here's what the output looked like:
<code>
2007-10-25 01:00:00AM|Monrovia Madness|Monrovia Madness,
2007-10-26 04:00:00AM|Monrovia Madness|Monrovia Madness,
</code>
Note the extra ',' at the end.  I'll have to figure out how to stop it from doing that so I don't have to do any code workarounds based on the output.  Sorry for the ultra-boring and non-informative test data, but you gotta start somewhere.  Now, the syntax does actually make a little bit of sense to me now that I've had the chance to muddle through from where I started.  I'll keep you posted as I get into some more-than-basic uses of xQuery.
</p>
