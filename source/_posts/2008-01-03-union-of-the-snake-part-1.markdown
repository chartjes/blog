--- 
layout: post
title: Union Of The Snake, Part 1
date: 2008-01-03
author: Chris Hartjes
---
<p>
C'mon ,you know that <a href="http://en.wikipedia.org/wiki/Duran_duran">Duran Duran</a> kicks ass!  I was trying to think of a catchy title for a series of posts as I wind my way through the building of my first <a href="http://www.python.org/">Python</a> app, using the <a href="http://djangoproject.com">Django</a> framework.  If you've used any other framework, you should be able to follow along with these posts as the concepts are all pretty much the same.
</p>
<p>
First off, I have great hopes that the <a href="http://tempdocs.cakephp.org">current CakePHP 1.2 manual</a> can morph into a resource as great as <a href="http://www.djangobook.com">The Django Book</a>, which looks to me to be the essential resource for anyone wishing to start off with Django.  Everything I'm doing at this stage in the project builds on what I've covered so far.</p>
<p>
Anyway, I've chose to build out Rallyhat, my sporting road planning site.  Much like when I build a <a href="http://www.cakephp.org">CakePHP</a> app, I start out with the models.  Django has a pretty good <a href="http://en.wikipedia.org/wiki/Object-relational_mapping">ORM</a> component, as compared to the associated data mapping model that CakePHP uses.  Now, to paraphrase from the Django book:  "introspection is hard", so in order to give the Model ORM some help you define the fields you will be using in your models.  Here are the definitions I'm using:
{% codeblock lang:python %}
from django.db import models

class Sport(models.Model) :
	name = models.CharField(max_length=30)
		
	def __str__(self):
		return self.name


class Team(models.Model):
	name = models.CharField(max_length=30)
	sport = models.ForeignKey(Sport)
	city = models.CharField(max_length=30)
	state_province = models.CharField(max_length=30)
	country = models.CharField(max_length=30)

	def __str__(self):
		return self.name
				
				
class Game(models.Model):
	home_team = models.ForeignKey(Team, related_name='home_team')
	away_team = models.ForeignKey(Team, related_name='away_team')
	start_date = models.DateTimeField()
	sport = models.ForeignKey(Sport)
	
	
	def __str__(self):
		return '%s vs. $s' (self.away_team, self.home_team)

{% endcodeblock %}
</p>
<p>
As you can see, I'm able to define all my fields I'm going to use with generic data types, and can even define the associations between the tables.  So, why do we do all this? Well, Django comes with some great CLI tools for helping you build stuff.  In fact, I dare say that you cannot build a Django application *without* using these tools.  Once you've defined the models you want to use, you validate the models using 'python manage.py validate', and it reports any problems it found.
</p>
<p>
While I was building this out, it told me that it couldn't determine the foreign keys I wanted, so I quickly figured out I had to put Sport first in the definition list, then Team, so that Game would know what to reference for the foreign keys.  It also told me that I had to set a 'related_name' attribute for my foreign keys in Game since I was reference the same model twice for a foreign key.  Very similar to how you can alias an association in Cake.
</p>
<p>
Okay, once that's done I can then get it to generate the actual SQL needed to create those models using 'python manage.py sqlall rh' (with 'rh' being what I'm calling the application within Django).  In this case I'm using a Postgres backend, so it generated SQL specifically for Postgres.
[sql]
BEGIN;
CREATE TABLE "rh_game" (
    "id" serial NOT NULL PRIMARY KEY,
    "home_team_id" integer NOT NULL,
    "away_team_id" integer NOT NULL,
    "start_date" timestamp with time zone NOT NULL,
    "sport_id" integer NOT NULL
)
;
CREATE TABLE "rh_sport" (
    "id" serial NOT NULL PRIMARY KEY,
    "name" varchar(30) NOT NULL
)
;
ALTER TABLE "rh_game" ADD CONSTRAINT sport_id_refs_id_66e4cc9c FOREIGN KEY ("sport_id") REFERENCES "rh_sport" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE TABLE "rh_team" (
    "id" serial NOT NULL PRIMARY KEY,
    "name" varchar(30) NOT NULL,
    "sport_id" integer NOT NULL REFERENCES "rh_sport" ("id") DEFERRABLE INITIALLY DEFERRED,
    "city" varchar(30) NOT NULL,
    "state_province" varchar(30) NOT NULL,
    "country" varchar(30) NOT NULL
)
;
ALTER TABLE "rh_game" ADD CONSTRAINT home_team_id_refs_id_20e54e34 FOREIGN KEY ("home_team_id") REFERENCES "rh_team" ("id") DEFERRABLE INITIALLY DEFERRED;
ALTER TABLE "rh_game" ADD CONSTRAINT away_team_id_refs_id_20e54e34 FOREIGN KEY ("away_team_id") REFERENCES "rh_team" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "rh_game_home_team_id" ON "rh_game" ("home_team_id");
CREATE INDEX "rh_game_away_team_id" ON "rh_game" ("away_team_id");
CREATE INDEX "rh_game_sport_id" ON "rh_game" ("sport_id");
CREATE INDEX "rh_team_sport_id" ON "rh_team" ("sport_id");
COMMIT;
[/sql]
</p>
<p>
Man, it creates the indexes too!  Okay, now that I'm happy with that all I have to is 'python manage.py syncdb' and it goes and actually creates the tables (and indexes) for me.  I took a look at the 'schema' task that exists for the Cake console (try 'cake schema' if you have already configured the console for use and poke around) and it will do similar things for you.  Nicely done, gwoo!
<pre>
(chartjes@jackjack ~/Sites/rallyhat)
>python manage.py syncdb
Creating table rh_game
Creating table rh_sport
Creating table rh_team
Installing index for rh.Game model
Installing index for rh.Team model
(chartjes@jackjack ~/Sites/rallyhat)
>
</pre>
</p>
<p>
Bingo, presto!  We have our tables created for us!
</p>
<p>
I hope you've enjoyed this little glimpse into Django (and how it relates to CakePHP, in an obtuse way I guess).  Next time we invoke the spirit of Duran Duran, I'll be showing how I built a search form to find all games for a particular team, showing how Django's MTV (Model-Template-View) system works.
</p>
