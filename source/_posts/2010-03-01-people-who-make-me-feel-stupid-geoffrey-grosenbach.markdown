--- 
layout: post
title: "People Who Make Me Feel Stupid: Geoffrey Grosenbach"
---
<p>For this upcoming week I am going to be doing 5 blog posts about developers who have been doing work that makes me feel stupid as a developer.  The main reason for this is a week spent on introspection as to not only how I am building applications for my employer but also how I build things on the side.  To be blunt, I'm not happy.  This is not to say that the work isn't interesting (building out corporate fantasy sports draft web front-ends and also plans for our next-gen fantasy gaming platform) but rather that my method of choosing what pieces I glue together have been missing the mark.
</p>
<p>Some of this is due to my desire to always push myself to learn new things, so sometimes the joy of discovery tramples the ability to get things done as quickly as I would like.  So I've been looking around at how other people have been solving problems in an attempt to discover blind spots I've developed.  The first person I found that made me say out loud "boy, does this guy make me feel stupid" during this process is <a href="http://geoffreygrosenbach.com/">Geoffrey Grosenbach.</a>
</p>
<p>
About 5 years ago I was looking to get into the Ruby on Rails world.  I had bought the <a href="http://pragprog.com/titles/ruby/programming-ruby">Pick Axe Book</a> and the 1st edition of <a href="http://pragprog.com/titles/rails1/agile-web-development-with-rails-1st-edition">the Rails book</a>.  Through my online digging I discovered the <a href="http://podcast.rubyonrails.org/">Ruby on Rails podcast</a>, run at the time by the previously-mentioned Geoffrey Grosenbach.  It was all cool and interesting, and he seemed to have a knack for asking the right kind of questions.  Either that or he was really good at the editing. ;)
</p>
<p>
Alas, things didn't work out.  I built a Rails site, but it had some problems due to my n00bishness with the framework and the language.  Let's just say I wasn't using Ruby best practices.  The final nail in the coffin for my Ruby aspirations was when I turned down a Rails gig to instead take a telecommuting PHP gig (life choices dictated that one) and I drifted off into other things.  But I kept an eye on what Geoffrey was doing anyway and was happy to see him find success with Peepcode along the way.
</p>
<p>
Then I came across an awesome blog post from him where he talked about <a href="http://blog.peepcode.com/tutorials/2010/about-this-blog">how he builds the Peepcode Blog</a>.  I read it and was totally blown away, and totally humbled by the simplicity of what he has done.  Rather than simply do some link bait and show you everything he used, you can go and look at it
</p>
<p>
He explained that his goal was to produce an "art blog" for Peepcode, where every blog post would have it's own unique look to it.  In order to do this, he had to think about what goes into building something like this:
<ul>
<li>A CSS grid layout system, because it's really too hard to always come up with your own unique layouts.  A grid makes it easier to make interesting content I think.</li>
<li>A very simple application framework for spitting out static images and HTML. (This was the lightbulb-went-on thing for me, as a blog that does not have comments can be totally static)</li>
<li>A modified version of an existing lightweight blogging engine to fit his needs.</li>
<li>Storing blog content in flatfiles on the system.  Again, without dynamic content why bother with the overhead of storing posts in a database (says the guy using WordPress, one of the favourite targets of criticism by PHP developers who like their code clean and modular)</li>
<li>The use of a markup language to reduce the actual HTML he had to write</li>
<li>The use of a CSS framework to again reduce the need to write actual CSS</li>
<li>A sprinkling of Javascript to add unique features to each page</li>
</ul>
</p>
<p>I've read that blog post at least a dozen times now, and still marvel at how frickin' obvious it was to do things the way he did.  It's also obvious that he put a lot of thought into what he needed and the best way to couple things together to make it happen.</p>
<p>
Compare his methods to my current set of decisions as to the various tools to build a web front end for a corporate draft
<ul>
<li>A glue framework with lots of components that can be legitimately accused of starting to become bloated</li>
<li>Use of an ORM to spare me from writing SQL to pull in dynamic sports data</li>
<li>Table-driven HTML layouts from the previous generation of the application</li>
</ul>
When you start to factor in the time to actually learn not only the framework itself (and also heavily relying on a particular module of it to give me the MVC features I wanted) but the ORM itself, I wonder if it was the right decision.
</p>
<p>
Because if I were to break it down in a similar fashion to how the Peepcode blog was built, I'd say I need the following
<ul>
<li>lightweight scripting language front-end (in this case PHP because that's what all our other client-facing applications use)</li>
<li>a component to handle dynamic routing of requests, although I could really use web server rewrite rules instead of making the front-end code figure it out.  My mod_rewrite skills have gotten a little better in the last year or so.</li>
<li>An RDBMs because the source data is in a database already, and so few NoSQL solutions allow you to do the kind of grouping and aggregate math functions I need to do that MySQL can handle for me.</li>
<li>An authentication component.  I've written enough of these to know it's easier to use someone else's that just works</li>
<li>An access control component.  I've written enough of these to know it's easier to use someone else's that just works too.</li>
<li>Grid-based CSS framework for layouts so we can use as few tables as possible.</li>
<li>An easy-to-use Javascript library to take care of everything else that I cannot do in the scripting language or via CSS.</li>
</ul>
</p>
<p>
Man, I'm starting to think that <a href="http://toys.lerdorf.com/archives/38-The-no-framework-PHP-MVC-framework.html">Rasmus was right</a> with apologies to my friend <a href="http://twitter.com/chiggsy">Kevin Beckford</a>.  Kevin is of the opinion that main reason to use a framework to build something is because unless you will be the only one ever to write and maintain that application, the rules and structure that a framework gives are essential to help your fellow coders stay on track.  It's like having a common language that you both speak, and easy access to a dictionary (the documentation for that framework).
</p>
<p>
In my case, I am using PHP + Zend_Framework + Zend_Application + Zend_Auth + Zend_Acl + Doctrine + MySQL (plus Python on the server to do some data munging)  to build this thing out.  Luckily, no Javascript needed at this point.  So what could I strip out to build it the way I put it above?  We could end up with PHP + Apache rewrite rules + Zend_Auth + Zend_Acl + MySQL + Python, with Blueprint CSS thrown in to help me with the layouts.  Not a *whole* lot of difference from before.
</p>
<p>
But of course, I was able to quickly build out admin functionality for the front end due to the ability to map out relationships between tables and having Doctrine pull in all that data and return it to me in a ready-to-go package for easy display.  Also, to be realistic, we are too far into the project to rip all that stuff out and quickly refactor it.  I mean, how do I justify stripping out Doctrine and writing all the "query, process and stick into variables" code now?  It's a delicate dance, and it's obvious those decisions need to be made before you start, not when you're experiencing some mild <a href="http://en.wikipedia.org/wiki/Buyer%27s_remorse">Buyer's Remorse</a>.
</p>
<p>So, in the end, why did Geoffrey Grosenbach make me feel stupid?  <b>It was because he made me realized that I have a tendency to what to overengineer things a bit, wrapping them in framework solutions when perhaps the more direct route is to couple existing modules together to have a more flexible solution</b>.
</p>
<p>
But I have at least considered that the tools I was using were going to make it easier to build out the behind-the-scenes stuff.  Sure, I could write all the SQL code myself (I've finally understood the power of joins), but once I've learned how Doctrine does things it becomes super simple to build on the existing work.  
</p>
<p>
Look at the Peepcode blog setup shows that he was using a bunch of tools already in widespread use in the Ruby and Rails communities.  There are not many equivalences for that stuff in the PHP world (HAML and SASS only have incomplete implementations for use with PHP as far as I can tell) but the approach he used is the one to really think about.  I mean, what would this blog look like if I decided to go the minimalist route, but with tools that I am more comfortable with?  Could I do it with <a href="http://werkzeug.pocoo.org/">Werkzeug</a> + a simple blog engine + <a href="http://en.wikipedia.org/wiki/Textile_(markup_language)">Textile</a> + <a href="http://www.blueprintcss.org/">Blueprint CSS</a> + jQuery?  I have no spare time as it is, what would this type of project do to me?
</p>
