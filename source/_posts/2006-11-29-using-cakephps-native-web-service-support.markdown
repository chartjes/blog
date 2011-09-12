--- 
layout: post
title: Using CakePHP's Native Web Service Support
author: Chris Hartjes
date: 2006-11-29
---
<p>
Recently there was a posting on the <a href="http://cakephp.org">CakePHP</a> mailing list from someone complaining that CakePHP's native web service support didn't work, mainly because he couldn't figure out how to get it to work.  So, I took up the challenge and sent out an email to the list showing that you can indeed use them.  Might I add that until I tried this, I had never built a web service with CakePHP before.  I found that by turning on the debug mode and actually following the instructions that were in the error messages (best undocumented feature of CakePHP if you ask me) I was able to build it.  Oh yeah, a big shout-out to Samuel DeVore for his near-simultaneous reply to the original message showing an ever simpler example than mine.  Which I promptly stole and used it in this example. :)
</p>
<p>
This example works with the latest stable version of CakePHP (1.1.10.3825) running on a Gentoo Linux box with PHP 5.1.2 and Apache 2.  It's my understanding that the native web service stuff was originally built for Cake 1.2 (not released yet) and back-ported to Cake 1.1.  Perhaps some key parts are missing, hence the need for some hackery mentioned below.
</p>
<p>
First, open up /app/config/core.php and turn on support for internal web services:
{% codeblock lang:php %}
/**
 *  The define below is used to turn cake built webservices
 *  on or off. Default setting is off.
 */
	define('WEBSERVICES', 'on');
{% endcodeblock %}
</p>
<p>
Now, you have to understand that CakePHP won't magically spit out your content as XML, or SOAP, or as REST or whatever.  The internal web services support provides built-in URLs for spitting out your content in whatever alternate format you want.  This concept will become clear as we continue on here.  Basically it lets you do the following:
<ul>
<li>mydomain/controller/action for regular content</li>
<li>mydomain/xml/controller/action to spit out your content formatted as XML</li>
</ul>
</p>
<p>Okay, so first thing I did was create a test controller:
{% codeblock lang:php %}
<?php

/**
 * Test controller for built-in web services
 *
 * @author Chris Hartjes
 *
 */
 
class TestController extends AppController
{
    var $name = 'Test';
    var $uses = "";
    var $components = array('xml');
    
    function index()
    {
        $message = "This is a test of built-in web services";
        $this->set('message', $message);
    }
}

?>
{% endcodeblock %}
Those of you who are observant about CakePHP will notice that I've dragged in a component to be used.  Currently, you need to create a component *and* a helper to make the web service stuff work.  This is hackish, and hopefully goes away.
</p>
<p>
You need to create an XML component and put it in /app/controllers/components/xml.php
{% codeblock lang:php %}
<?php

class XMLComponent extends Object
{
    // Blank for now as we're not doing anything weird
}

?>
{% endcodeblock %}
and then create an XML helper, placing that in /app/views/helpers/xml.php
{% codeblock lang:php %}
<?php

class XmlHelper extends Helper
{
    // blank for now
}

?>
{% endcodeblock %} 
</p>
<p>
Now we need to generate a bunch of thtml files to display our output.  Of course, we have to create the default view for our action in the controller.  Put this in /app/views/test/index.thtml
{% codeblock lang:php %}
Content generated via regular view<br />
< ?php echo $message ?>
{% endcodeblock %}
Next is the XML stuff.  There are two files we need to create.  One is /app/views/layouts/xml/default.thtml, which simply tells CakePHP to use whatever data is passed into it.
{% codeblock lang:php %}
< ?php echo $content_for_layout ?>
{% endcodeblock %}
and then we create /app/views/test/xml/index.thtml to spit out our data in XML
{% codeblock lang:php %}
< ?php e('<?xml version="1.0" encoding="utf-8" ?>' . "\n"); ?>
<foo>
<bar>< ?php echo $message ?></bar>
</foo>
{% endcodeblock %}
I believe the e(blah) function is a built-in helper for CakePHP.
</p>
<p>
So, now when we go to mydomain/test we get the following output generated:
{% codeblock lang:html %}
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>CakePHP Web Services Test</title>
<link rel="stylesheet" type="text/css" href="/css/cake.generic.css" /><meta http-equiv="Content-Type" content="text/html; charset=UTF-8" /></head>
<body>
	<div id="container">
		<div id="content">
			Content generated via regular view<br />
This is a test of built-in web services		</div>

		<div id="footer">
			&nbsp;
		</div>
	</div>
	</body>
</html>
{% endcodeblock %}
and when we go to mydomain/xml/test we get the following output generated
{% codeblock lang:xml %}
<?xml version="1.0" encoding="utf-8" ?>
<foo>
<bar>This is a test of built-in web services</bar>
</foo>
{% endcodeblock %}
</p>
<p>
Like I said before, a lot of hoops to jump through and hopefully those go away when CakePHP 1.2 comes out.
</p>
