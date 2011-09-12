--- 
layout: post
title: Bad programming practices, example 1
---
As shocking as it seems, I sometimes don't follow smart programming practices. <img src="//www.littlehart.net/atthekeyboard/templates/default/img/emoticons/smile.png"" alt="-)"" />  As a good example, I was refactoring the code that I use to keep track of results from the <a href="http://www.ibl.org">simulation baseball league</a> I am the commissioner of.  It's a PHP 4 app.

Specifically, I was changing database access to use the <a href="http://www.martinfowler.com/eaaCatalog/activeRecord.html">Active Reord</a> pattern.  Everything was going just fine until I did the update method.  I forgot to specify the id of the record I was updating.  Instead I overrote EVERY SINGLE ENTRY in the table.  Of production data.

<strong>sigh</strong>

We have backups, but it will be some work to get back what I need back.

So the lesson?  Backup the database before you do anything like I did OR have a development database you can use.  One of the things I like about <a href="http://www.rubyonrails.com">Ruby On Rails</a> is that they build that capability right into it.  You have a database config file that you tell where to find the development databases, production databases and test databases.
