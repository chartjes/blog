--- 
layout: post
title: Zend_Application and Zend_Acl
---
<p>One of the more frustrating things about using Zend Framework is that for pretty much any topic, there is always at least 2 ways to accomplish a particular task.   For a beginner with the framework, this is a humungous barrier to overcome.  When I try to implement something, my first question is no longer "how will I do this" but "where the hell should I put this code?".  In my case, the problem I was attempting to solve was "how do I implement ACL for one module in my application?".
</p>
<p>
I'm using:
<ol>
<li>Zend Framework 1.10.5</li>
<li>...and Zend_Application</li>
<li>...and building functionality out using modules</li>
</ol>
</p>
<p>
So off I go <a href="http://duckduckgo.com">duck hunting</a> and find lots of samples on how to do it.  Except none of them fit how my application is currently built.  Plugins?  Front controllers?  Placing code in preDispatch?  Yikes, this will take some time to sift through all the available info and come up with a solution custom-tailored to my application's structure.
</p>
<p>
I ended up using info from <a href="http://stackoverflow.com/questions/2046608/practical-zend-acl-zend-auth-implementation-and-best-practices">here</a> and <a href="http://devzone.zend.com/article/3510-Zend_Acl-and-MVC-Integration-Part-II-Advanced-Use">here</a> to form my solution.  The first step was to create a plugin to hold all the info about my ACL's and roles. 
{% codeblock lang:php %}

< ?php

class Xmlteam_Football_Acl extends Zend_Acl
{
    protected static $_instance;

    protected function __construct()
    {
        $this->addRole(new Zend_Acl_Role('guest'));
        $this->addRole(new Zend_Acl_Role('admin'));
        $this->addRole(new Zend_Acl_Role('normal', 'guest'));
        $this->addRole(new Zend_Acl_Role('photoadmin', 'guest'));
        $this->addRole(new Zend_Acl_Role('captain', 'normal'));

        $moduleResource = new Zend_Acl_Resource('football');
        $this->add($moduleResource)
            ->add(new Zend_Acl_Resource('football:help'), $moduleResource)
            ->add(new Zend_Acl_Resource('football:messages'), $moduleResource)
            ->add(new Zend_Acl_Resource('football:photos'), $moduleResource)
            ->add(new Zend_Acl_Resource('football:standings'), $moduleResource)
            ->add(new Zend_Acl_Resource('football:stats'), $moduleResource)
            ->add(new Zend_Acl_Resource('football:team'), $moduleResource)
            ->add(new Zend_Acl_Resource('football:transactions'), $moduleResource);

        $this->allow(null, 'football:help');
        $this->allow(null, 'football:messages');
        $this->allow(null, 'football:photos', 'view');
        $this->allow(array('admin', 'photoadmin'), 'football:photos', array('delete', 'manage')); 
        $this->allow(null, 'football:standings');
        $this->allow(null, 'football:stats');
        $this->allow(null, 'football:team');
        $this->allow(null, 'football:transactions', array('closed', 'league'));
        $this->allow('captain', 'football:transactions', 'request');
        $this->allow(array('captain', 'normal'), 'football:transactions', 'index');

        return $this;
    }

    public static function getInstance()
    {
        if (self::$_instance === null) {
            self::$_instance = new self();
        }

        return self::$_instance;
    }
}
{% endcodeblock %}
Then, I needed a way to actually call this plugin and do something with the results.  I was using a base controller for the 'football' module for my application, and after messing around, I figured out that the code interacting with my ACL plugin needed to go in the init() method of the controller:
{% codeblock lang:php %}
 // Now, let's hook up some ACL lovin'
 $acl = Xmlteam_Football_Acl::getInstance();
 $resource = 'football:' . $this->_request->controller;

 if ($acl->has($resource) && !$acl->isAllowed($this->userInfo['role'], $resource, $this->_request->action)) {
       $this->_flashMessenger->addMessage('You do not have the proper access level to view that page');
       $this->_redirect('/football/' . $this->league . '/standings');
 }
{% endcodeblock %}
This used to be a lot more crufty, but I slowly whittled away at the code until it has what I think is the simplest implementation.
</p>
<p>
Oh, I almost forgot.  Here are the tests I wrote for it.  I bet you thought I forgot to write tests, didn't you. ;)
{% codeblock lang:php %}
class FootballAclTest extends PHPUnit_Framework_TestCase 
{

    public function setUp()
    {
        $this->bootstrap = new Zend_Application(
            'testing',
            APPLICATION_PATH . '/configs/application.ini'
        );
        parent::setUp();
        $this->_acl = Xmlteam_Football_Acl::getInstance();
    }

    public function tearDown()
    {
        parent::tearDown();
    }

    public function testTransactions()
    {
        $resource = 'football:transactions';
        $this->assertTrue($this->_acl->has($resource), 'football:transactions resource exists');
        $this->assertTrue($this->_acl->isAllowed('captain', $resource, 'request'), 'Team captains can request transactions');
        $this->assertFalse($this->_acl->isAllowed('normal', $resource, 'request'), 'Normal team users cannot request transactions');
        $this->assertTrue($this->_acl->isAllowed(null, $resource, 'league'), 'Anyone can view league transactions');
    }

    public function testPhotos()
    {
        $resource = 'football:photos';
        $this->assertTrue($this->_acl->has($resource));
        $this->assertTrue($this->_acl->isAllowed(null, $resource, 'view'), 'Anyone can view photos');
        $this->assertTrue($this->_acl->isAllowed('admin', $resource, 'manage'), 'Admin can manage photos');
        $this->assertTrue($this->_acl->isAllowed('photoadmin', $resource, 'manage'), 'Photoadmin can manage photos');
        $this->assertFalse($this->_acl->isAllowed('captain', $resource, 'manage'), 'Captains cannot manage photos');
        $this->assertFalse($this->_acl->isAllowed('normal', $resource, 'manage'), 'Normal users cannot manage photos');
        $this->assertFalse($this->_acl->isAllowed('guest', $resource, 'manage'), 'Guests cannot manage photos');
    }
}
{% endcodeblock %}</p>
