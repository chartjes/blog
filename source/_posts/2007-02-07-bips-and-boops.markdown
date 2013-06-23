--- 
layout: post
title: Bips and Boops
---
<p>This time next week I will be trying to flag down a taxi at the airport in Toronto, having come back from the <a href="http://vancouver.php.net">Vancouver PHP Conference 2007</a>.  I'm looking forward to giving my "What Can PHP Learn From Ruby on Rails" talk because I'll be doing a screencast of my talk.  However, I'm struggling with trying to decide what to do with it.
</p>
<p>
If I give it away, then the people who see me in person are getting ripped off.  If I charge for it, the question then becomes how much to charge?  $5?  $10.  One model I've been thinking of trying is that if 20 people by the screencast I will give it away for free after that point.  We shall see what ends up happening.
</p>
<p>
Over on the CakePHP mailing list, someone asked a question about how to build a model without accessing a database.  I pointed out that it can be done, and that there were examples.  Then, I got schooled by <a href="http://cake.insertdesignhere.com/">nate</a>...


<blockquote>I definitely wasn't agreeing with you, but I wasn't really making fun
of you either.  I'll give you a hint: there's a reason why we have a
base DataSource class, which is extended by DboSource, which talks to
the database on behalf of a model.  Felix's Google Analytics model is
actually a pretty poor example.  Not because Felix is a bad coder or
anything (quite the contrary), but because up till now, there are a
few things that people really haven't clearly understood (or perhaps,
there are a few things we haven't made clear for people).  Basically
what I'm trying to say is that you should never have to extend Model
in that way.  Models are designed to *model* data, not handle the
details of accessing it.</blockquote>
Ouch
</p>
<p>But Nate did have a good point.  I didn't fully understand how the Model was built up in CakePHP because, well, I never really had to before.  I think when I build my first CakePHP 1.2x site I'll dig into the internals a little more.
</p>
<p>
Now, I've noticed a few blog postings about <a href="http://dev.mysql.com/downloads/connector/php-mysqlnd/">mysqlnd</a>, a native MySQL driver for PHP 6 (for now) and beyond.  As an aside, I should try installing PHP 6 somewhere just to see how they are progressing.  Anyhow, back to mysqlnd.  Why is this significant? There are, in my mind, two things why you should know about it.
</p>
<p>Firstly, mysqlnd is designed to take advantage of PHP's own infrastructure.  I imagine this means that you can expect better performance from this library as opposed to the old libmysql or the newer libmysqli.  I understand it's aimed at PHP 6 for the time being, due to some of the work being done with Unicode in PHP 6.  There is talk of backporting it to PHP 5, or even PHP 4 (something to do with streams meaning you could backport) but it's aimed squarely at PHP 6 for now.</p>
<p>
The second big reason is that it will provide a library for PHP to talk to MySQL databases that has a license that is more compatible with PHP.  In fact, it will be released under the PHP license.  MySQL has an exception for allowing libmysql to be integrated with <a href="http://www.mysql.com/company/legal/licensing/foss-exception.html">FLOSS</a> projects, of which PHP is one.  Having a native driver that doesn't require an exception to use can only be a good thing.
</p>

