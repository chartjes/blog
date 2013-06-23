--- 
layout: post
title: Simple User Registration in CakePHP 1.2
date: 2008-01-08
author: Chris Hartjes
---
<p>In the comments for my seemingly-popular post about using <a href="http://www.cakephp.org">CakePHP's</a> Auth component (available in CakePHP 1.2), people have been having some questions about how the password is hashed and questions about a user registration system.  Of course, the snarky response is "go and read the source for Security::Hash() and create some of your own code", but it is easier to just give people some code so they stop asking.
</p>
<p>
I'm in the process of building out an admin area for my <a href="http://www.ibl.org">simulation baseball league</a> web site, and I created a registration system.  Here's a condensed version of it.
</p>
<p>First, I have my User model
<br />
{% codeblock lang:php %}
<?php
class User extends AppModel {

	var $name = 'User';
	var $useTable = 'users';
}
{% endcodeblock %}
</p>
</p><p>
Next, I created my controller for my users and the registration action for it
{% codeblock lang:php %}
class UsersController extends AppController {
	var $name = 'Users';
	var $helpers = array('Html', 'Form');
	var $components = array('Auth');
	
	function beforeFilter() {
		$this->Auth->allow('register');
	}
		
	function register() {
		if (!empty($this->data)) {
			if ($this->data['User']['password'] == $this->Auth->password($this->data['User']['password_confirm'])) {
				$this->User->create();
				$this->User->save($this->data);
				$this->redirect(array('action' => 'index'));
			}
		}
	}
}
{% endcodeblock %}
</p>
<p>
So, let's dissect this controller:
<ul>
<li>We're using the Auth component, set via "var $components = array('Auth')"
</li><li>We tell Auth to not ask for authentication when doing the 'register' action</li>
<li>When we detect data coming into the 'register' action (usually via a POST), then check to see if the hashed password that Auth has created from the 'password' field in our form matches the hashed value of the 'confirm password' field from our form</li>
<li>If all that is okay, we create and save our new user record</li>
</ul>
Yes, it really is that easy.
</p>
<p>
The form for this is very simple as well
<br />
{% codeblock lang:php %}
<?php
echo $form->create('User', array('action' => 'register'));
echo $form->input('username');
echo $form->input('password');
echo $form->input('password_confirm', array('type' => 'password'));
echo $form->submit();
echo $form->end();
?>
{% endcodeblock %}</p>
<p>
Throw all that stuff together and you now have a very simple user registration system.
</p>
