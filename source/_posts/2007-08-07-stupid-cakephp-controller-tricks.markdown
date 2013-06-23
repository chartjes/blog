--- 
layout: post
title: Stupid CakePHP Controller Tricks
date: 2007-08-07
author: Chris Hartjes
---
<p>A big shout-out to my <a href="http://cake.insertdesignhere.com/">favourite typist</a> for showing me some of these gems, which I will gladly share with you</p>
<p>
So, one of the things that often happens in CakePHP is that you will have multiple values to send to your view, so you might have code that looks like this:
{% codeblock lang:php %}
$this->set('user', $this->User->read(null, $id));
$this->set('foo', $foo);
$this->set('bar', $bar);
$this->set('baz', $baz);
{% endcodeblock %}
Seems simple enough, yes?  Once when I showed code similar to this to the above-mentioned typist, he said "ew" and showed me two neat little tricks to make the code (a) more readable and (b) a little more efficient.  
</p>
<p>Solution one?  Use <a href="http://www.php.net/compact">compact()</a> to pass all the variables to your view.
{% codeblock lang:php %}
$user = $this->User->read(null, $id);
$this->set(compact('user', 'foo', 'bar', 'baz'));
{% endcodeblock %}
</p><p>
What does the compact() function do?  It takes the array you pass into it and looks for variables of the same name as the elements in that array.  It then spits out an array of key => value pairs.  So, one little trick with compact() means you only have to use one set statement.  This works because all those $this->set() statements simply add those values to an array.  But you already knew that, right?
</p>
<p>The second solution is similar to sing the "chmod 777 firehose" to solve UNIX-based permissions problems.
{% codeblock lang:php %}
$user = $this->User->read(null, $id);
$this->set(get_defined_vars());
{% endcodeblock %}
Now, while this looks neat it does come with one big caveat:  if you use <a href="http://www.php.net/get_defined_vars">get_defined_vars()</a> you will be passing a lot of stuff into your view that you might not want there.  In a way it's like using REGISTER_GLOBALS in your CakePHP.  Every variable you've defined in the controller (and some other ones that CakePHP has defined for you) in your current scope will be available in the view.
</p>
