--- 
layout: post
title: Thoughts About My Upcoming Talk
---
As you can see from the graphic in the upper-right-hand corner of my blog, the php|works conference isn't that far off.  I've been working on the outline for my talk "What Can PHP Learn From Rails?" and have settled upon the basics for it.

But it begs a bigger question:  is it possible to take what is really great about Rails (and by definition that means some great features of Ruby) and make it work in PHP?  When going to my friend <a href="http://derekmartin.ca">Derek's</a> goodbye party (he's switching jobs to work for a company next door to his old one) I was talking to my old co-workers about my talk.  And they raised a good question: what are PHP's strengths.

I opened my mouth to say something and then closed it.  Maybe it was the beer that made me pause.  I'll be honest:  I really like Ruby and there are some really neat things being done.

The biggest problem with being able to duplicate a lot of what Rails is doing is, well, PHP isn't Ruby.  Ruby's method of treating everything like an object is something that PHP just can't do.  ActiveRecord in Ruby works so well because Ruby can examine it's own properties (I believe that is called reflection), and ActiveRecord takes full advantage of that.  One of the thrusts of my talk is that developers who are creating tools for other developers to use (I'm not talking about creating applications) have to use the strengths of PHP instead of railing (heh) against PHP's perceived limitations.

I've probably posted things like this before, but ActiveRecord is able to do things like this:

{% codeblock lang:ruby %}
person = new FamilyMember
data = person.find_by_last_name_and_sex('Hartjes', 'female')
{% endcodeblock %}

Without me doing *anything*, ActiveRecord knows to translate this into "SELECT * FROM familymembers WHERE last_name = 'Hartjes' AND sex = 'female'

Can you do that in PHP? I do know that <a href=http://www.cakephp.org>CakePHP</a> (which has been getting lots of favourable reviews) has their own ActiveRecord implementation.  Can it do the above?  Not quite yet.  It does handle something like this: (taken from the CakePHP website):

{% codeblock lang: php %}
$this->Post->findByTitle('My First Blog Post');
$this->Author->findByLastName('Rogers');
$this->Property->findAllByState('AZ');
$this->Specimen->findAllByKingdom('Animalia');
{% endcodeblock %}

I can see how this behaviour would be easier to implement in PHP 5, and I will have to take a look at CakePHP to see how they do it in PHP 4.  With a little bit of effort I'm sure you can add multiple terms to a PHP ActiveRecord implementation to mimic how ActiveRecord works in Ruby.

We, as PHP developers, should hesitate to take good ideas from other programming languages and see if there is a way to make an implementation that is just as easy to use as the original.  Object Relational Mapping works not just with ActiveRecord in Ruby, but with other items in Ruby as well.  I saw a slide show of David Heinemeier Hansson's presentation he gave at a Ruby conference in Japan.  He showed an item called ActiveResource that acts just like ActiveRecord but will work on all sorts of things.

Where are the people who are creating things like that in PHP 5?  Maybe people are doing that work, but they aren't as eager to share that info with the rest of the world as DHH (and the rest of the Rails crowd in general).  Maybe this is what happens when the core group of people working on a language gets to the point where one person can't drive the language my the sheer will of their ego.  This isn't a bad thing, by any means.  It shows that PHP has gotten a huge level of acceptance and that there are now many people capable of contributing to it.

Anyway, I should save some of this for my presentation instead of sharing it on the blog. :)
