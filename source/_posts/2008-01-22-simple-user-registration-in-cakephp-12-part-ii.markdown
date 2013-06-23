--- 
layout: post
title: Simple User Registration in CakePHP 1.2, Part II
date: 2008-01-22
author: Chris Hartjes
---
<p>I got a question in the comments about my previous post on simple user registration about how to do some of the necessary validation for registration in the model.  I thought I'd show some code I did to do exactly that.
</p>
<p>
The key to all this stuff is using a second form field for doing the validation.  Here's some sample code for you, based on the latest straight-from-svn version of Cake PHP 1.2 (r6402)
<br /><br />
{% codeblock lang:php %}
<?php

/**
 * Class used for user authentication on the league website
 *
 */

class User extends AppModel
{
    var $name = 'User';

    var $validate = array(
		'id' => array('rule' => 'blank',
                      'on' => 'create'),
		'username' => array('rule' => 'alphanumeric',
			                'required' => true,
                            'message' => 'Please enter a username'),
        'password' => array('rule' => array('confirmPassword', 'password'),
                            'message' => 'Passwords do not match'),
		'password_confirm' => array('rule' => 'alphanumeric',
                                    'required' => true)
	);

    function confirmPassword($data) {
        $valid = false;
        
        if ($data['password'] == Security::hash(Configure::read('Security.salt') . $this->data['User']['password_confirm'])) {
            $valid = true;
        } 
        
        return $valid;
    }

}
?>
{% endcodeblock %}
</p>
<p>
So, let's talk about what's in there.  
<ul>
<li>make sure that the username is alphanumeric and has been entered</li>
<li>make sure the password exists and run the custom validation function 'confirmPassword' on the data being posted in</li>
<li>make sure that our confirm password field exists and is alphanumeric</li>
</ul>
</p>
<p>
The only tricky thing when I made this was figuring out how to compare the two password fields, and where to get the proper hashing from.  Initially I thought that I could somehow import the Auth component in there but a quick chat with gwoo showed me how stupid that was when I could just duplicate how the component itself is hashing the password field.  That's what is going in with the use of Security::hash(...).
</p>
<p>
Hope that helps.
</p>
