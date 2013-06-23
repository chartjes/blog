--- 
layout: post
title: More XML-DB Fun!
---
<p>
We had a nice corporate retreat last week, an opportunity for all the members of <a href="http://www.xmlteam.com">XMLTeam</a> to get together (and in some cases meet face-to-face for the first time) and discuss what's going on and figure out priorities over the next 12 months.  If you're expecting some company secrets here, you'll be disappointed. :)</p>
<p>
One of the things that got bandied around was whether or not we would continue using <a href="http://exist.sourceforge.net/">eXist</a> to store the XML documents that the application is using or go with a <a href="http://xtoss.org">database-driven solution</a>.  So, my partner on this project was tasked with figuring out how to update existing elements and attributes in this documents using eXist only.</p>
<p>
How can I put this?  Oh, I know:  traversing through large complicated XML documents to find one element that you need to update when the location could be in multiple places sucks!  Part of the reason for this may be my lack of XPath foo within PHP itself.  Besides, if eXist can handle this for us then why shouldn't we leverage this?  I liken it to being able to do an UPDATE statement in a database.  I don't do a SELECT where I grab the whole data set, then drill down through the data looking for one specific row.  You do an update with the proper key.  So, Paul (that's the co-worker) got to work figuring out for me while I refactored code to be ready for it.  He got one script working (yay!) so I hacked away and got a very simple one to work today.  Here it is (with some info changed to protect the status of the project:
[code]
xquery version "1.0";
declare namespace sportsml="http://iptc.org/std/SportsML/2006-10-18/";
declare namespace xts="http://www.xmlteam.com";
declare namespace request="http://exist-db.org/xquery/request";
declare namespace xmldb="http://exist-db.org/xquery/xmldb";
declare namespace util="http://exist-db.org/xquery/util";

declare variable $league := request:get-parameter("league", "");
declare variable $league-name := request:get-parameter("league-name", "");
declare variable $team-key := request:get-parameter("team-key", "");
declare variable $colors := request:get-parameter("colors", "");
declare variable $location := request:get-parameter("location", "");
declare variable $name := request:get-parameter("name", "");
declare variable $nickname := request:get-parameter("nickname", "");
declare variable $abbreviation := request:get-parameter("abbreviation", "");

declare variable $league-doc := concat('/db/', $league, '/dynamic-resource-file/', $league, '.xml');

<dummy>
{
if (doc($league-doc)/sports-content/statistic/group//team-metadata/@team-key=$team-key) then

for $team-metadata in doc($league-doc)/sports-content/statistic/group//team-metadata[@team-key=$team-key]
return
update replace $team-metadata with
<team -metadata>
{attribute team-key {$team-key}}
{attribute colors {$colors}}
<name>
{attribute first {$location}}
{attribute full {$name}}
{attribute nickname {$nickname}}
{attribute abbreviation {$abbreviation}}
</name>
<affiliation>
{attribute membership-type {"league"}}
{attribute membership-key {$league}}
{attribute membership-name {$league-name}}
</affiliation>
</team>

else

return
} 
</dummy>
[/code]</p>
<p>
So, this sits in eXist, which is running on top of <a href="tomcat.apache.org">Tomcat</a> and I send the data in by POST-ing to the script.  I was all set to start using cURL for this task but a quick search on the net found <a href="http://netevil.org/blog/2006/nov/http-post-from-php-without-curl">this blog posting by Wez Furlong</a> showing how to use streams to do what most people automatically associate with having to use cURL for.  I liked it so much I went and refactored some other code that was using cURL to use that stuff instead.  It's always nice to find out that something you've been doing can still be done, but with fewer lines of code and *still* be elegant.
</p>
<p>
I'm off to look closer at streams in PHP 5 and see what other hidden treats are there...
</p>
