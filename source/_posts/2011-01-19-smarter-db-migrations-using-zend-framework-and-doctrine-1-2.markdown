--- 
layout: post
title: Smarter DB Migrations Using Zend Framework and Doctrine 1.2
---
<p>This posting is a lesson on the value of actually looking at the source code of a third-party library when you are trying to figure something out...</p>
<p>
I'm using Doctrine 1.2 for a Zend Framework project (loving the power of DQL) and I'm also big on continuous integration...which relies on being able to automate things.  Consequently, I was using Doctrine's <a href="http://www.doctrine-project.org/projects/orm/1.2/docs/manual/migrations/en">migrations</a> system to handle making changes to the database.  But I was frustrated.  The solution I had was running <b>each and every migration each time</b> and causing a lot of noise in the form of warnings about changes that had already been applied.  Was it hurting anything?  Just my pride and sense of Having Done Things Right.</p>
<p>So, I started searching around for solutions.  There seemed to be something missing in everything I found, some sort of smug assumption that the system was smart enough to know which migrations had already been done so you could double check.  Totally frustrated I decided to look at the source code for Doctrine itself...
</p>
<p>
"Hrm, this method seems to allow you to write a value to a table in a database...what table is that...goddamn it Chris, you are such a dumb-ass for not seeing this earlier!"
</p>
I had noticed that there was a table in the database for this project called 'migration_version' but I kept ignoring it, thinking it was an artifact of an earlier attempt by me to implement roll-your-own migrations.  Little did I know that was the actual table I was supposed to use.  After some experimentation, I confirmed that I was indeed a dumb-ass and needed to start using this table properly.

<p>
Next step was then to create a new PHP script to handle the migrations.  Keeping in mind that I'm using Zend Framework, here's what it looks like:
{% codeblock lang:php %}
< ?php
define('APPLICATION_PATH', realpath(dirname(__FILE__) . '/application'));

if (!defined('APPLICATION_ENV')) {
    define('APPLICATION_ENV', (getenv('APPLICATION_ENV') ? getenv('APPLICATION_ENV') : 'testing'));
}

set_include_path(implode(PATH_SEPARATOR, array(
    realpath(APPLICATION_PATH . '/library'),
    get_include_path(),
)));
 
require_once 'Zend/Application.php';
 
$application = new Zend_Application(
    APPLICATION_ENV,
    APPLICATION_PATH . '/configs/application.ini'
);
 
$application->getBootstrap()->bootstrap('doctrine');

Zend_Loader_Autoloader::getInstance()->registerNamespace('Doctrine')->pushAutoloader(array('Doctrine', 'autoload'));  
$config = new Zend_Config_Ini(APPLICATION_PATH . '/configs/application.ini', APPLICATION_ENV);
$manager = Doctrine_Manager::getInstance();  

foreach ($config->doctrine->attr as $key => $val) {
    $manager->setAttribute(constant("Doctrine::$key"), $val);  
}  

$migration = new Doctrine_Migration(APPLICATION_PATH . '/migrations');
$latestVersion = $migration->getLatestVersion();
$currentVersion = $migration->getCurrentVersion();

if ($latestVersion > $currentVersion) {
    echo "Migrating from v{$currentVersion} to v{$latestVersion}\n";

    try {
        $nextVersion = $currentVersion + 1;
        $migration->migrate($nextVersion);
        $migration->setCurrentVersion($latestVersion);
    } catch (Exception $e) {
        echo 'Caught exception: ', $e->getMessage() . "\n";
    }
} else {
    echo "No migrations were performed\n";
}
{% endcodeblock %}
I will explain the logic a little bit here
</p>
<p>
First, we have to do a bunch of stuff to load in our Zend Framework application.  I'm using autoloading of modules so I never have to worry about including something so long as I've followed the proper naming conventions.  Next, I create an instance of the Doctrine_Migration object, then determine whether or not we need to actually perform a migration by comparing the value in the 'migration_version' table to what the latest migration class says.
</p>
<p>
See, Doctrine is smart enough to look at all the classes you've written to do migrations and figure out which one is the latest.  The easiest way to do this is prefix the name of the file with a number, or if you are dealing with multiple developers you could go with YYYYMMDDHHMM or even a timestamp (if you're feeling l33t) as the prefix.  Anything you can do to make sure that the order of migrations is the way you want is good.  I went with a 4-digit number as the prefix.  We're currently at migration 0016.  I figure that if we get to 9999 migrations then I've probably done something wrong. ;)
</p>
<p>
Armed with the info about the last migration and the current migration, it's simple to determine if we actually need to run the migrations or not.  Problem solved in an elegant way, and no more unnecessary noise in the output from my continuous integration builds.
</p>
