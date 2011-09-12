--- 
layout: post
title: WordPress 2.1 and Mint
date: 2007-01-30
author: Chris Hartjes
---
<p>I recently decided to ditch using Google Analytics for my stats tracking and installed <a href="http://www.haveamint.com">Mint</a> as my website stats tracking module.  I'm really liking it, and it's easily worth the $30 you have to pay for it.  C'mon, don't be cheap and steal everything, okay?</p>
<p>
Mint has a really cool plugin architecture that they call <a href="http://haveamint.com/peppermill/">Pepper</a>, and you can grab all sorts of cool addons.  I saw one called <a href="http://haveamint.com/peppermill/pepper/11/bird_feeder/">Bird Feeder Pepper</a>, which can track what's going on with your various feeds.  Now, the installation is fairly easy but there was a weird bug that was appearing, where a check to see if you are running a licensed copy of Mint kept getting triggered when I tried to access my feeds via a feed alias.  The solution?  An ugly hack, if you ask me.  To implement Bird Feeder Pepper and use the seeds (track individual items in your feed), there's a snippet of PHP code you have to insert in the various PHP files WordPress uses: wp-rss.php, wp-rss2.php, wp-atom.php and wp-rdf.php.  Place this snippet AFTER the line in the PHP file that executes a 'header' command and BEFORE the code that outputs the beginnings of the XML.  Here's an example:
{% codeblock lang:php %}
header('Content-type: text/xml; charset=' . get_option('blog_charset'), true);
$more = 1;

// BEGIN CODE TO IMPLEMENT BIRD FEEDER PEPPER SEEDS
global $Mint;
define('BIRDFEED', 'Articles (RSS)');
include($_SERVER['DOCUMENT_ROOT'].'/feeder/index.php');
// END CODE TO IMPLEMENT BIRD FEEDER PEPPER SEEDS
?>
<?php echo '<?xml version="1.0" encoding="'.get_option('blog_charset').'"?'.'>'; ?>
{% endcodeblock %}
</p>
<p>
Hope that helps anyone else who was struggling to get Bird Feeder Pepper working with WordPress 2.1.</p>
