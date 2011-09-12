--- 
layout: post
title: Dynamic Models in CakePHP 1.2
---
<p>While working on a consulting gig where I'm using <a href="http://cakephp.org">CakePHP</a> to rewrite an existing site, I was fooling around with the latest version of Cake from SVN and discovered a nifty little feature.  Cake now has dynamic models.
</p>
<p>
I discovered this because my app was working, pulling data from the database but I hadn't baked any models at all.  After confirming with gwoo via IM that I was not going crazy, he told me what was going on.
</p>
<p>
By default now, Cake will automatically use the AppModel class and create a unique alias to a database table if it does not find the file.  This means that if you have a table that follows the Cake conventions, needs no validation, and has no associations to other tables, you <b>don't even have to create the model file any more</b>.  Woah, talk about a serious time saver in some cases.
</p>
<p>
However, keep in mind that this feature *also* means that if you misspell the name of your model file, this dynamic model feature will mean that your misspelled model file will NOT get loaded, and you might be scratching your head as to why your associations don't work and why validation is not going on. So pay close attention to the naming of your files to avoid confrontations with grumpy Canadian programmers on the mailing list.
</p>
