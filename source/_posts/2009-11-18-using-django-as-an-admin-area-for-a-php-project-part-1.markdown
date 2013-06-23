--- 
layout: post
title: Using Django As An Admin Area for a PHP Project, Part 1
---
<p>My <a href="http://www.sportso.com">work project</a> needed an admin area for doing things like changing the key for a league, or changing the email address for someone's account.  You know, typical admin stuff.  In the past I had been *gasp* editing SQL by hand via <a href="http://www.pgadmin.org/">pgAdmin</a> (and my favourite trick of creating an SSH tunnel to the server the database is on).  Well, I'd had enough of that.  I also wanted to set things up so when my boss wanted changes done, I could tell him "go do it yourself using this neato-keen admin interface I whipped together".
</p>
<p>
So I got to work creating a <a href="http://www.djangoproject.com">Django</a> project, installed the <a href="http://docs.djangoproject.com/en/dev/ref/contrib/admin/">django-admin</a> application and got to work.
</p>
<p>
Have I mentioned how I *love* code generation these days?  Can I get "hell yeah!" from the lazy programmers out there?  Django comes with this awesome tool that you access via manage.py called <a href="http://docs.djangoproject.com/en/dev/ref/django-admin/#inspectdb">inspectdb</a>.  What it does is introspect the database you configured for your Django application and generates the output for your models.py file.  However, keep in mind the following:
<ul>
<li>You *will* have to fiddle with the order your classes that represent the models appear in the generated code</li>
<li>You *will* have to go in and alter any field definitions where inspectdb was not able to determine the proper field type and instead guessed.</li>
</ul>
</p>
<p>
So, after firing off inspectdb, I then issued a 'python manage.py syncdb' to create all the tables needed for django-admin, created a user for the admin site...and then it got hairy.
</p>
<p>
The documentation for customizing django-admin is good.  And I was able to create just about everything I wanted by actually, you know, READING the documentation.  But I found a problem that I was not able to solve.  I even <a href="http://stackoverflow.com/questions/1758805/problems-with-updating-records-in-django-admin">asked my favourite consultants for help</a> but I could not get it to work the way I *wanted* it to work.  When I told my buddy via IM that it would be easier to whip up this admin in PHP than slog through learning how to do it the Django way, he was not impressed.  He stopped short of saying "you're dead to me now", but I got that vibe.
</p>
<p>
Here's the problem.  I have these two models:<br />
{% codeblock lang:python %}
class Permissions(models.Model):
    league_key = models.CharField(max_length=15) 
    commissioner_id = models.ForeignKey(Accounts, db_column='commissioner_id',
                                        to_field='id')
    status = models.IntegerField()
    key = models.CharField(max_length=50)
    publisher_key = models.CharField(max_length=25)
    publisher_display_name = models.CharField(max_length=50)
    base_league = models.IntegerField()
    share = models.IntegerField()
    default_fixture_key = models.CharField(max_length=50, blank=True)
    
    def __unicode__(self):
        return self.publisher_key + ' / ' + self.league_key
    
    class Meta:
        db_table = u'permissions'
        verbose_name = 'Permissions'
        verbose_name_plural = 'Permissions'

class PermissionsAdmin(admin.ModelAdmin):
    list_display = ('league_key', 'publisher_key', 'commissioner_id', 'status',
                    'share', 'default_fixture_key')
    list_display_links = ('league_key',)
    exclude = ('base_league',)
{% endcodeblock %}
</p>
<p>
Now, if you look at the definition in there for the base_league field, you will notice that I gave up and called it an IntegerField.  But in reality, it is pointing to another record in the same Permissions table.  We have a concept in Sportso of a "shared league model" where you can base a league on another league and import all sorts of properties and data from it.  I was hoping that I could do something like this:
{% codeblock lang:python %}
base_league = models.ForeignKey('self', db_column='base_league', to_field='id')
{% endcodeblock %}
</p>
<p>
Whenever I did that, I would actually crash Python on my MacBook.  Not a good sign.  If I tried swapping them, I would get an error complaining about violating permissions_pkey, which is the Postgres sequence that was created for the auto-incremented ID for the table.  I did manage to take a look at the SQL it was trying to execute, and it keeps trying to update the 'id' field (which is the primary key) instead of the 'base_league" field.  So I gave up and will continue building out the other parts of the admin.  I just wish I could figure out WHY this self-referencing foreign key setup was not working.
</p>
<p>
If you know what's going on here, let me know via the comments.
</p>
