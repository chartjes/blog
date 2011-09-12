--- 
layout: post
title: How Easy Are Web Services in CakePHP 1.2?  Really Easy!
date: 2007-03-13
author: Chris Hartjes
---
<p>In a <a href="http://www.littlehart.net/atthekeyboard/2006/11/29/using-cakephps-native-web-service-support/">previous post</a> I talked about how to use the built-in web services in <a href="http://www.cakephp.org">CakePHP</a> 1.1.x.x.  A very popular piece too according to my site statistics too.  Well, I've discovered that it's even easier in Cake 1.2.x.x.  I bugged Nate via IM for some tips on how to put it together, and it's really very simple.
</p>
<p>
The biggest change is that the old way of doing custom routing in web services is gone in favour of handling them via extensions.  In the past, you would go into app/config/core.php and enable the special web services routing.  I was trying to do a web service with the URL http://localhost/cake_dev/foo and have it spit out an XML response.  According to what I was told "...going forward the routes part / extensions on the end of the URL is the recommended way of doing it".  So, if I was doing this the standard way I would be calling http://localhost/cake_dev/foo/index.xml.  I just like the cleaner URL.  Now, if I was to do it the proper way, I would add in the following to my app/config/routes.php file:
{% codeblock lang:php %}
/**
 * Add in support for web services by enabling generating output based on extension
 */
Router::parseExtensions();
{% endcodeblock %}
</p>
<p>Now, go and create your controller that will handle spitting out some XML:
{% codeblock lang:php %}
/**
 * Test controller for built-in web services in Cake 1.2.x.x
 *
 * @author Chris Hartjes
 *
 */

class FooController extends AppController
{
    var $components = array('RequestHandler');
    var $uses = '';
    var $helpers = array('Text', 'Xml');
    
    function index()
    {
        $message = 'Testing';
        $this->set('message', $message);
        $this->RequestHandler->respondAs('xml');
        $this->viewPath .= '/xml';
        $this->layoutPath = 'xml';
    }
}
{% endcodeblock %}
So what am I doing here?  I make sure to use the RequestHandler component so it understands that I want to spit out some XML, and I made sure to include the Xml helper.  Next, I tell the request handler that I want the output to be XML instead of HTML by using respondAs('xml').  Finally, I do some more controller voodoo (Nate contributed this part) by setting $this->viewPath and $this->layoutPath so that I don't have to specify index.xml to get it to spit out results.  A call to http://localhost/cake_dev/foo will spit out an XML result based on my template, which I put into app/views/foo/xml/index.ctp:
{% codeblock lang:php %}
<foo>
    <bar>< ?php print $message; ?></bar>
</foo>
{% endcodeblock %}
That spits out the following XML document:
{% codeblock lang:xml %}
<?xml version="1.0" encoding="UTF-8" ?>
<foo>
    <bar>Testing</bar>
</foo>
{% endcodeblock %}
</p>
<p>I'm hoping to use this setup for some web services I have to write for work but my boss likes <a href="http://framework.zend.com">some other framework</a>, which isn't surprising since he used to work for them.  I will continue to fight for my right to eat Cake.  Besides, it's all part of my evil plan to get paid to contribute code to the CakePHP project.  I mean, if I need to create an interactive console to do testing then I can build it with Cake and give it back to the community while getting paid at the same time.  What could be better?
</p>
