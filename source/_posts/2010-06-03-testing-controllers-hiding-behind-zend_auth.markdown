--- 
layout: post
title: Testing Controllers Hiding Behind Zend_Auth
---
<p>(Note, this example was using Zend Framework 1.10, so things might change going forwards).</p>
<p>As a lapsed tester, I've made the commitment to build out our Zend Framework powered application using tests going forward.  The first two modules for the app *should* have been done with tests, and for that I hang my head with shame.  Now that I've invested the work in creating a <a href="http://en.wikipedia.org/wiki/Continuous_integration">continuous integration</a> environment using <a href="http://hudson-ci.org">Hudson</a>, there is no longer an excuse to not write tests.  Especially when I can get tests run automatically every time I commit code.
</p>
<p>
Anyway, I was asked to implement a new feature for the application:  a list of all transactions for a fantasy baseball league, sorted by date.  What a perfect excuse to write some tests!  The initial problem though was how do I simulate logging in a user so I can see this page, which was protected by authentication using Zend_Auth.  So I started my scouring the internet for answers.
</p>
<p>
I found quite a few examples on how to test a controller, using the $this->dispatch('/path/to/action') method but found that I wasn't getting redirected properly to the post-login page.  I was passing proper credentials in and everything.  Then finally after deciding to go back to basics and read up on just how to test Zend_Auth.  After some swearing a few face-palms, I realized what I had been doing wrong.
</p>
<p>
The tl;dr version:  I was forgetting that the unit test itself needed to manually log in the user by speaking with Zend_Auth directly.  Here's the testing code for that particular controller:
{% codeblock lang:php %}
< ?php

require_once 'Zend/Test/PHPUnit/ControllerTestCase.php';
require_once 'Zend/Application.php';

// Define path to application directory
if (!defined('APPLICATION_PATH')) {
    define('APPLICATION_PATH', realpath(dirname(__FILE__) . '/../../../application'));
}

// Define application environment
if (!defined('APPLICATION_ENV')) {
    define('APPLICATION_ENV', (getenv('APPLICATION_ENV') ? getenv('APPLICATION_ENV') : 'test'));
}

// Ensure library/ is on include_path
set_include_path(implode(PATH_SEPARATOR, array(
        realpath(APPLICATION_PATH . '/../library'),
            get_include_path(),
        )));

class TransactionControllerTest extends Zend_Test_PHPUnit_ControllerTestCase 
{

    public function setUp()
    {
        $this->bootstrap = new Zend_Application(
            'testing',
            APPLICATION_PATH . '/configs/application.ini'
        );
        parent::setUp();
    }

    public function loginUser($login, $passwd, $shortLeague)
    {
        $authParams = array(
            'login' => $login,
            'password' => $passwd,
            'short_league' => $shortLeague 
        );
        $adapter = new Xmlteam_Auth($authParams);
        $auth = Zend_Auth::getInstance();
        $result = $auth->authenticate($adapter);
        $this->assertTrue($auth->hasIdentity());
    }

    public function tearDown()
    {
        parent::tearDown();
    }

    public function testOverallBaseballList()
    {
        $this->loginUser('test@test.com', '*****', 'bluejays2010');
        $this->dispatch('/baseball/bluejays2010/transactions/list');
        $this->assertModule('baseball', 'In baseball module');
        $this->assertController('transactions', 'In the transactions controller');
        $this->assertQuery('#tblTransactions', 'Transaction table exists');
    }
}
{% endcodeblock %}
</p>
<p>
I'm using a custom authentication adaptor with Zend_Auth, as we need to limit access for a user to a particular league.  Perhaps better to do it with Zend_Acl, and since the platform is likely to expand I will end up using that as well.  But I am drifting off topic here.
</p>
<p>
The magic is in that loginUser() method.  What I did not realize at the time was that running a test where I asked it to dispatch users to the login page and passed along what would've been entered in the form was not working.  Perhaps it was creating an authenticated session OUTSIDE the scope of the test environment.  Perhaps it is my sucky code.  Either way, it wasn't working.
</p>
<p>
So, by creating a authenticated login Zend_Auth *inside* the test, I could then safely dispatch my testing code to look at pages requiring authentication.  I hope this blog posts helps out others trying to write tests for controllers that are hidden behind Zend_Auth.
</p>
