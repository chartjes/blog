--- 
layout: post
title: Converting Legacy Apps to CakePHP, Part 2
---
<p>
<i>(Note: after being schooled by Nate Abele via IM about the various ways you can deal with schemas without built-in relationships, I have altered the post)</i>
</p>
<p>
Now you've decided to convert your legacy app over to CakePHP, you will run into the first serious obstacle:  your database schema. If your schema does not already account for relationships between multiple tables you are in for a lot of extra work.  If the tables already have foreign keys pointing to other tables, you're in pretty good shape.
</p>
<p>
If you're still looking at not having foreign keys in the existing schema, all is not lost.  You can set the foreignKey property in a model association to false and then create a custom query that pulls in the joined records, which I imagine is useful if you need to use multiple foreign keys or something.  So despite my previously hard line stance on this, you *can* deal with tables that don't have bulit-in foreign keys.  It's just extra work. 
</p>
<p>
Without a database schema that contains relationships, you will not be able to use CakePHP's awesome associated data mapping abilities that are offered as part of the model.  Basically, given a set of conditions and knowing the relationships between the tables it will generate fairly well-tuned SQL queries and then return the results to you as nested arrays.  Is this perfect ORM?  No, but it's very easy to pass these result sets to your views for iterating over.
</p>
<p>
In my case, this was going to be the easiest part: the schema already contained relationships between the tables so I was able to use the Cake console and in under an hour I had used 'cake bake' to create all my models.  I did go back after the fact and tweak some of the relationships because they weren't *perfect* matches with the Cake conventions, but that was the exception rather than the rule.  Had there been no relationships between the tables, or extreme denormalizing of the data, I am unsure what I would've done.
</p>
<p>
On the topic of working with denormalized data, I'll late Nate speak for himself here:
<blockquote>
"Again, you can get this to work fine, it just takes a bit of extra effort.  It's nice when you can move this effort down to the database (i.e. cascading foreign key updates) but if not, you just have to write a little extra callback code."
</blockquote>
</p>
<p>
What Nate is referring to here is that you will have to some work in your models to create functions as "callbacks" that are executed when performing updates or saves.  For example, a site I worked on had broken out user profile information into 4 different tables depending on what type of search you were doing.  In this case, I'd be writing a callback function that would go and update all the other search tables whenever I updated the master record.  That's the "cascading foreign key updates" thing Nate is referring to.
</p>
<p>
Now that I had my models, it was time to start thinking about how to switch over old queries.  In order to understand how to turn old SQL queries into results you get from Cake, I think you have to understand the following things (all of this applies to Cake PHP 1.2):
<ul>
<li>Understanding how relationships (i.e. hasMany, hasAndBelongsToMany) work in CakePHP.</li>
<li>How to use the <a href="http://book.cakephp.org/view/474/Containable">Containable behavior</a> so you limit what comes back in the result set</li>
<li>Pretty solid SQL skills so you can decipher legacy code that might be using JOINS and subselects</li>
</ul>
</p>
<p>
I think that if you are really good at those three things, you will be able to quickly determine how to turn that legacy SQL code into the proper parameters that need to be passed to your models to get back the results you need.
</p>
<p>
So now armed with the tools needed to convert those old queries over, I was onto the next and probably most difficult part of this particular project:  converting the old page controllers that used a token-replacement system for the templates over to Cake controllers and views.
</p>
