--- 
layout: post
title: Handling Multiple Environments In Your PHP Application
author: Chris Hartjes
date: 2008-11-28
---
<p>In anticipation of my <a href="http://conf.phpquebec.com/en/session#deployment_is_not_a_4_letter_word">talk at PHP Quebec 2009</a> I've been going over my slides and thinking about what I'm going to update for it.  One little nugget I'd thought I'd share is one way of handling having multiple environments your code must run in.
</p>
<p>
For a work application, I have *three* environments that the code must run in:  'dev' (which is my laptop), 'staging' (which is where I look for the infamous "bug does not exist in production" type of errors), and 'production'.  For all these environments, there are different web services that they need to speak to so I tried to think of an easy way to handle this.  I have a configuration file that is used, so it seemed to me that this would be a logical place to do the *check* for what environment we are in.  But *how* to define where we are?  That turned out to be easy.
</p>
<p>
If you are using Apache, you have the ability to define server variables that can be read in using $_SERVER.  I'm sure you can do the same thing with other web servers, but this example is Apache-specific.  So, I figured the best way to handle this problem was to define a server variable and have a unique value for each environment.  Then, I added in code that checks the contents of that server variable and reacted accordingly.  Here's an example:
</p>
<p>
{% codeblock lang:php %}
<?php
// In Apache, add SetEnv APP_ENV "<unique environment value>" somewhere in your http.conf file
// e.g. SetEnv APP_ENV 'dev'

switch ($_SERVER['APP_ENV']) {
    case 'dev':
        $config['webservice'] = 'http://admin@localhost:8008';
        $config['putfeed'] = 'http://dev.domain.com:8080/put/sml';
        break;
    case 'production':
        $config['webservice'] = 'http://admin|password@ws.domain.com:8080';
        $config['putfeed'] = 'http://in.domain.com/put/sml';
        break;
}
?>
{% endcodeblock %}
</p>
<p>(NOTE:  <a href="http://snook.ca/jonathan/">Jonathan Snook</a> asked me to add an example on how to configure SetEnv)</p>
<p>
Then, in your Apache httpd.conf file you add the SetEnv directive.  Here's a snippet of how I did it for a work project:
{% codeblock %}
<virtualhost *:80> 
     ServerName local.sportso.com 
     DocumentRoot /Users/chartjes/Sites/sportso.com 
     SetEnv SPORTSO_ENV "dev" 
  
     <directory /Users/chartjes/Sites/sportso.com> 
         Options Indexes FollowSymLinks MultiViews 
         AllowOverride None 
         Order allow,deny 
         Allow from all 
          
         RewriteEngine on 
         RewriteCond %{QUERY_STRING} ^last-accessed=(.*)$ 
         RewriteRule ^(.*)$ $1/last-accessed/%1? 
         RewriteRule ^$ /index.php [L] 
         RewriteRule ^/$ /index.php [L] 
         RewriteCond $1 !^(index\.php|images|styles|js|robots\.txt) 
         RewriteRule ^(.*)$ /index.php/$1 [L] 
     </directory> 
      
     LogLevel warn 
     ErrorLog /opt/local/apache2/logs/sportso.com-error.log 
     CustomLog /opt/local/apache2/logs/sportso.com-access.log combined 
</virtualhost> 
{% endcodeblock %}
</p><p>
Hope that helps out any other developers struggling to think of an elegant way to determine what environment you are in.  As opposed to the lazy method of checking a production version of the config file into your version control system and then simply not checking back in the hacked-up dev version of it. ;)
</p>
