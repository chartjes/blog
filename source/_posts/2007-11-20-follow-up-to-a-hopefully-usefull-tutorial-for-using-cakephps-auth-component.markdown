--- 
layout: post
title: Follow-up to "A Hopefully Usefull Tutorial For Using CakePHP's Auth Component"
date: 2007-11-20
author: Chris Hartjes
---
<p>
There have been some mention in the comments for <a href="http://www.littlehart.net/atthekeyboard/2007/09/11/a-hopefully-useful-tutorial-for-using-cakephps-auth-component/">this post</a> for clarification on the 'remember me' cookie that is mentioned in the code.  I thought I'd elaborate a bit on how I used it for this example.</p>
<p>
As part of a project I was working on while at <a href="http://www.cakedevelopment.com">CDC</a> there was a requirement for there to be 'Remember Me' functionality for the authentication system.  I'm sure you've seen this elsewhere.  Implementing such a thing is actually very simple, but I should've clarified that 'remember me' functionality is NOT part of the Auth component.  
<ul>
<li>When they go to log in, check to see if there is a 'remember me' cookie present.</li>
<ii>If there is, read in the cookie (containing the user name and encrypted password.  Never EVER put plaintext passwords in a cookie!) and then compare those values to the database table (or whatever data source you are using) that you are authenticating against.  If they match, then set the user as being 'authorized' and they can proceed on their merry way.  Otherwise, delete the cookie (it may be a bad cookie) and send them to the login screen
<li>If there is no cookie, let the person log in as usual and if they are successfully authenticated then store that information  in your 'remember me' cookie before you let them proceed to whatever areas require authorization.</li>
</ii></ul>
</p><p>
Now, to drop into CakePHP for a minute the key thing that was left out of the previous blog posting is *how* you get the Auth system to accept the values in the cookie.  It took a quick IM conversation with <a href="http://rd11.com/">gwoo</a> to jog my memory.
{% codeblock lang:php %}
function beforeFilter() {
     /**
     * Code that does other Auth stuff goes before this...
     */

     /**
     * If you've checked the data against your auth model,
     * you have to put that info into $this->data so that the
     * Auth component can use it
     */
     $this->data['User']['username'] = $cookie['username'];
     $this->data['User']['password'] = $cookie['password'];
}
{% endcodeblock %}
The password stuff is critical here.  By default, the Auth component will take any password that you've entered via a form and then hash it using the default for Auth (this value is configurable, check the Auth section API to see how to do it).  So, make sure that the *encrypted* password value is being placed into $this->data, and consequently stored in your cookie.  In the example above 'User' is the model being authenticated against, so feel free to change it if you're using something else.  Keep in mind it's probably not a good idea to put a field called 'password' in your cookie, so feel free to change it to something less obvious or come up with another method of obscuring the true contents of the cookie.
</p>
<p>
Hope that clears up the 'remember me' cookie mystery for people.  Thanks again to gwoo for helping me rummage around in my brain for the details.
</p>
