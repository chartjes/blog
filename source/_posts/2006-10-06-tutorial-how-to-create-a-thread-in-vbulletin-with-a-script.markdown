--- 
layout: post
title: "Tutorial: How to create a thread in vBulletin with a script"
author: Chris Hartjes
date: 2006-10-06
---
<p>
My day-job requires me to create code that will talk to <a href="http://www.vbulletin.com">vBulletin</a> web sites we run.  My latest task involves taking data that we get from <a href="http://www.pa-sportsticker.com/en/index.html">PA Sportsticker</a> and create posts in one of our forums.  Lucky for me, somebody smarter than me figured out how to do this.  It's very simple, and I've taken their work and modified it for our needs.
<br />
{% codeblock lang:php %}
<?php

/**
 * Script that posts info sent to it by the Sportsticker parser as a thread in a forum
 * Based on code found in http://www.vbulletin.org/forum/showthread.php?t=97283&page=2
 *
 * @author Chris Hartjes
 */

require './global.php';
require './includes/class_dm.php';
require './includes/class_dm_threadpost.php';
require './includes/functions_databuild.php';

$threaddm = new vB_DataManager_Thread_FirstPost($vbulletin, ERRTYPE_STANDARD);
$post_userid = 1; // Admin
$userid = 1;
$user_name = 'chartjes';
$allow_smilie = '1';
$visible = '1';

if (isset($_POST['forum_id'])) $forum_id = (int)$_POST['forum_id'];
if (isset($_POST['post_text'])) $post_text = (string)strip_tags($_POST['post_text']);
if (isset($_POST['title'])) $title = (string)strip_tags($_POST['title']);

$threaddm->do_set('forumid', $forum_id);
$threaddm->do_set('postuserid', $post_userid);
$threaddm->do_set('userid', $userid);
$threaddm->do_set('username', $user_name);
$threaddm->do_set('posttext', $post_text);
$threaddm->do_set('title', $title);
$threaddm->do_set('allowsmilie', $allow_smilie);
$threaddm->do_set('visible', $visible);
$threaddm->save();
build_forum_counters($forum_id);

?>
{% endcodeblock %}
</p>
<p>
I did see some talk abot how using that do_set method is not recommended as it bypasses the data manager object vBulletin uses.  I tried using that datamanager by actually looking at the code that does posts, but couldn't get it to work.  I suspect part of the problem is that the data manager assumes you are logged in, while you can post without being logged in with the method above.  At least it sure looks that way.  More testing is obviously required but I think I'm on the right track.
</p>
<p>
In a nutshell, the script that I wrote to parse the XML feed that Sportsticker provides will grab all the necessary info from the stream and then send that data to the above code via a POST request.  Nice and simple.  Hope this code sample helps.
</p>
