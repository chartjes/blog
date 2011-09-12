--- 
layout: post
title: A Hopefully Useful Tutorial For Using CakePHP's Auth Component
date: 2007-09-11
author: Chris Hartjes
---
<p>One of the parts of CakePHP that caused me the most grief while trying to learn the finer details of the framework was the <a href="http://api.cakephp.org/1.2/class_auth_component.html">Auth component</a>.  The problem at the time was that there was scant information available on how to actually use and configure it.  Luckily, I was able to get some insider information via gwoo and Nate from the CakePHP core team.  Plus there was stuff floating around on different web sites.  So, here I will attempt to collect some of that information and show you some basic-to-intermediate info on how to use the component.  Note, this code is for 1.2.x.x, and the API for the Auth component had not been declared 100% stable at the time of this post.  In other words, don't blame me if this doesn't work 6 months from now. :)</p>
<p>
So, in order to use this component, you have to add it to the list of components your controller is using.  I tend to put this info in app_controller.php since I usually need Auth to work for all my controllers.
{% codeblock lang:php %}
var $components = array('Auth');
{% endcodeblock %}
So, now that we want to use it we suddenly have a huge variety of options that can and need to be set.  For this example I use code from an existing project, with some info changed to protect the innocent.  You set the various Auth options by putting code in your beforeFilter() method for your controller that will be using Auth.
{% codeblock lang:php %}
$this->Auth->fields = array('username' => 'email', 'password' => 'pasword');
{% endcodeblock %}
By default, Auth expects you to have a model called User that has a 'username' and 'password' field in it.  You can override what fields contain the username and password information though.
{% codeblock lang:php %}
$this->Auth->loginAction = array('controller' => 'users', 'action' => 'login');
{% endcodeblock %}
You need to tell Auth what controller / action pair it needs to use to present the login form.
{% codeblock lang:php %}
$this->Auth->loginRedirect = array('controller' => 'users', 'action' => 'index');
{% endcodeblock %}
Tell the Auth component where the user should be redirected after a successful authentication...
{% codeblock lang:php %}
$this->Auth->logoutRedirect = '/';
{% endcodeblock %}
... and where they should go when you logout.
{% codeblock lang:php %}
$this->Auth->loginError = 'Invalid e-mail / password combination.  Please try again';
{% endcodeblock %}
You can specify what error message you want displayed if authentication fails.
{% codeblock lang:php %}
$this->Auth->autoRedirect = false;
{% endcodeblock %}
Sometimes you don't want to send an authenticated user to the location specified in $this->Auth->loginRedirect because you need to do some work based on the user being authenticated.  I've used this in this bit of code that checks to see if we have a cookie that has user credentials in it for logging in.
{% codeblock lang:php %}
	function login() {
		if ($this->Auth->user()) {
			if (!empty($this->data)) {
				if (empty($this->data['User']['remember_me'])) {
					$this->Cookie->del('User');
				}
				else {
					$cookie = array();
					$cookie['email'] = $this->data['User']['email'];
					$cookie['token'] = $this->data['User']['pasword'];
					$this->Cookie->write('User', $cookie, true, '+2 weeks');
				}

				unset($this->data['User']['remember_me']);
			}

			$this->redirect($this->Auth->redirect());
		}
	}

$this->Auth->authorize = 'controller';
{% endcodeblock %}
This is a newer addition to Auth, where you can specify some additional information about where Auth can look for more information.  Normally, Auth will expect you to have already setup stuff using Cake's own ACL stuff.  I didn't need anything as complicated as that, so I was happy to see I could bypass it.  When you set $this->Auth->authorize to 'controller', you're telling the Auth component to look for an action called 'isAuthorized' for more information on whether the user is authorized or not.  Here's a sample one:
{% codeblock lang:php %}
    function isAuthorized() {
        if (isset($this->params[Configure::read('Routing.admin')])) {
            if ($this->Auth->user('admin') == 0) {
                return false;
            }
        }
        
        return true;
   }
{% endcodeblock %}
I assume that example is self-explanatory.  Now, if you set $this->Auth->authorize to 'model' then you can create a special method in your User model that can do similar things.  Thanks to AcidMax for <a href="http://www.ogrn.com/andy/2007/07/10/auth-changes-in-cakephp-12-and-how-to-use-basic-auth/">this post</a> that shows you what to do if you use 'model' for $this->Auth->authorize.  There is also a 'crud' option for $this->Auth->authorize, but I have not used it myself. You can use $this->Auth->mapActions to then tell auth what actions map to the various CRUD actions:
{% codeblock lang:php %}
$this->Auth->mapActions(array('read'=> array('display')));
{% endcodeblock %}
Like I said, I haven't fooled around with it.  Once I do, I'll update this blog post to expand on it some more.
{% codeblock lang:php %}
$this->Auth->allow('add', 'view');
{% endcodeblock %}
You need to tell Auth what actions in your controller can be accessed without needing to be authorized.  What trips most beginners up is that 'login' and 'logout' are already actions that Auth expects to not needing to be authorized.  If you put 'login' and 'logout' in there, Auth starts acting very weirdly and totally bypassing authorization.  So, don't do that. :)
</p>
<p>
Now, there are also some other features that are useful to those using Auth:
{% codeblock lang:php %}
	function logout() {
		$this->Session->setFlash("You've successfully logged out.");
		$this->redirect($this->Auth->logout());
	}

{% endcodeblock %}
$this->Auth->logout will return the URL to whatever location you told Auth you wanted people to be sent to upon them being logged out.
{% codeblock lang:php %}
$userId = $this->Auth->user('id');
{% endcodeblock %}
You can retrieve info from the User model if you've been successfully authorized.  Whatever fields are in your User model can be retrieved.  Wouldn't it be nice to do stuff like this:
{% codeblock lang:php %}
if ($this->Auth->user('admin') == true) {
     $this->Session->setFlash('You are an admin');
}
{% endcodeblock %}
</p>
<p>
Phew.  That's a lot of stuff to try and keep in your head when building apps using Auth.  But there's still more.  The Auth component will automatically hash whatever value you place in the 'password' field in your form.  It will do this both upon login *and* if you are creating a record in your user model, so you need to make sure that your field in your table that stores the password is large enough that it will accept the hashed password.  If you need to do something with that password before you store it, call the field something other than what you've told Auth your password field is, then you can get the value needed to store it by using $this->Auth->password('passwordtostorehere').</p>
<p>
Anyhow, I'm sure I've missed some other more esoteric stuff, but I hope I've done a good job of showing just how easy the Auth component really is to use...once you understand how it actually works. :)</p>
