--- 
layout: post
title: Chris' Brain - May 2009 Edition
---
<h2>Book Update</h2>
<p>
For those not following along on Twitter, the first month of sales of my <a href="http://littlehart.net/book">CakePHP book</a> have been a success:  70 PDF's and 5 print-on-demand copies via <a href="http://www.lulu.com/content/paperback-book/refactoring-legacy-applications-using-cakephp/6626981">Lulu.com</a>.  A big thanks to everyone who has purchased a copy.  My next thought has been a book about doing Test Driven Development using CakePHP, but perhaps that is just wishcasting.
</p>
<h2>Deployment Thoughts</h2>
<p>
At work I've been tweaking the deployment process for an <a href="http://www.sportsdb.org/sd/sportscaster">open source project</a> that talks to our infrastructure and came upon an interesting problem.  Like many projects, we have some configuration files that would be different from environment to environment (i.e. different database access credentials, paths to archived files) so we've chosen to instead create sample versions of those configuration files and include them in the  application when you either download it (as external clients of ours do) or update from SVN (like we do).  
</p>
<p>
Since I like to use <a href="http://capify.org">Capistrano</a> to do deployment, I needed a way to make sure that the configuration files that are currently being used by the application get copied into the proper place.  Lucky for me, it was easy enough to add this in as a task in my Capfile:
{% codeblock lang:ruby %}
  # Do nothing (To restart apache, run 'cap deploy:apache:restart')
  task :restart do
  	run "cp /var/www/settings/sportscaster/gateway/php/config.php #{deploy_to}/current/gateway/php"
	run "cp /var/www/settings/sportscaster/gateway/php_ci/config/gateway.config.php #{deploy_to}/current/gateway/php_ci/config"
	run "cp /var/www/settings/sportscaster/engine/_application/config/database.php #{deploy_to}/current/engine/_application/config"
	run "cp /var/www/settings/sportscaster/engine/_application/config/config.php #{deploy_to}/current/engine/_application/config"
  end
{% endcodeblock %}
As you can see, I've placed the configuration files in their own directory (off the web root I know, might make more sense to put them some place else but they can live there for now) and then simply copy them in place once I've deployed the latest code.  I'd be interested in seeing how other people handle this issue.
</p>
<h2>Getting paid to do open source work</h2>
<p>
I feel like I'm very fortunate to have an employer who (mostly for business reasons) has decided to make some of their projects open source so that others can use it without cost.  Sure, some of it is niche software to be sure (a web service that only works with our pay-to-use infrastructure) but still, d00d, I'm getting paid to write open source code!  We also have another project in the works, helping <a href="http://www.phpffl.com">these guys</a> create a newer, more generic version of their fantasy league management application that has hooks to allow users to pull in data from our own web services.  Sure, it's helping to drive our business but isn't that the point?  I create something that helps my company make money, and in exchange I get to share it with everyone else.  Sounds like a pretty good deal to me.
</p>
