---
layout: post
title: Two-Headed Application Authentication in CakePHP 1.2
date: 2007-07-28
author: Chris Hartjes
---
<p>I've been working on an internal application for use at <a href="http://www.cakedevelopment.com">CDC</a> that required me to have what I call "two-headed" authentication.  By this I mean that there were two types of users in the system and while they could access some of the same controllers they could not always access the same actions.  I know what you're saying:  why not have them both use the same model instead of making my life difficult?  A few reasons, one of which was that one type of user was using their email address as the login while the other had a more traditional login name.</p>
<p>
After struggling my way through the Auth component (the API changed while I was starting to use it), and understanding the actual flow that the Auth component uses, I nailed down how to do it.  Using good CDC practices (as in "do it our way you stupid Kanuckistanian!") I started off with putting my Auth stuff into the before filter:
{% codeblock lang:php %}
function beforeFilter() {
        parent::beforeFilter();
               
        $this->Auth->loginAction = 'plugin/users/login';
        $this->Auth->loginRedirect = 'plugin/users/index';
        $this->Auth->fields = array('username' => 'username', 'password' => 'psword');
        
        $this->set('current', $this->action);
        
        if($this->Auth->isAuthorized()) {
        	
        	$role = $this->Auth->user('role');
        	
        	if($role) {
		        if ($role == 'admin' && strpost($this->action, CAKE_ADMIN) !== false) {
		            $this->Auth->allow($this->action);
		        }        
		        if ($role == 'admin') {
		            $this->set('adminNavigation', $this->adminNavigation);
		        }
		        
	            $this->set('userNavigation', $this->userNavigation);
        	} else {
        		$this->set('clientNavigation', $this->clientNavigation);	
        	}
        	
        	$this->set('userRole', $role);
        }
 }
{% endcodeblock %}
</p>
<p>
Now, I had an action in a controller where a "client" can view everything but a "user" could only view a specific action.  On top of that any "user" who also had an "admin" role could view any action in that controller.  In that particular controller I had to put in this code:
{% codeblock lang:php %}
function beforeFilter() {
        parent::beforeFilter();
        $this->Auth->userModel = 'Client';
        $this->Auth->loginAction = 'plugin/clients/login';
        $this->Auth->fields = array('username' => 'email', 'password' => 'psword');
        $this->Auth->authorize = 'controller';        
}
{% endcodeblock %}
In the latest version of the Auth component (from the bleeding edge of Cake 1.2.x.x) you can tell it to use an action in your controller for authorization.  This is if you're lazy like me and don't want to use the Acl (which has a number of steps you need to go through just to get it up and running) or want something very simple.  So, in the above beforeFilter() we override the parent beforeFilter() settings and tell Auth that we want to use our Client model as the source for verifying login credentials.
</p>
<p>
Now, I mentioned before that I had one action in the controller that could be viewed by the User and one action only.  So, I added in the isAuthorized() method to my controller that I told Auth to look for:
{% codeblock lang:php %}
    function isAuthorized() {
        if ($this->Auth->user('role')) {
            if (strpos($this->action, CAKE_ADMIN) !== false && $this->Auth->user('role') == 'admin') {
                return true;
            }
            
            if ($this->action == 'view') {
                return true;
            }
            
            return false;
        }
        
        return true;
    }
{% endcodeblock %}
I think the code is pretty self-explanatory.
</p>
<p>
Working with the Auth component taught me a lesson about frameworks in general: when you take the time to actually dig into the source code of a framework you will realize just how much work goes into some of the more "magic" functions.  I mean, you tell CakePHP that you want to use the Auth component, set a few parameters and *BAM* it takes care of directing people to your login page and validating login names and passwords (even automatically encrypting passwords upon account creation!) against your specified model.  Why wouldn't you want to use something like that?</p>
