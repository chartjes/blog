--- 
layout: post
title: Testing Components In CakePHP
date: 2007-06-26
author: Chris Hartjes
---
<p>Since I was moaning to Larry about the lack of tests in CakePHP (even though there is a great test suite based on Simpletest) I felt obliged to add in some tests to my work on adding functionality to the Email component to allow it to send things via SMTP.</p>
<p>Using the test suite is actually quite easy:  drop <a href="http://www.lastcraft.com/simple_test.php">SimpleTest</a> into your cake/vendors directly and you're ready to start writing your tests.  Having written tests using SimpleTest before it wasn't going to be too hard for me to get them done.  But there was one little problem:  how do you test a component?</p>
<p>
Components are called via controllers, so there was no way for me to simply instantiate the component and test it out.  After much back-and-forth with Larry (aka PhpNut) via IM I got it working.
<br />
{% codeblock lang:php %}
require_once LIBS . '/controller/components/email.php';

class EmailTestController extends Controller {
	var $name = 'EmailTest';
	var $uses = null;
	var $components = array('Email');
}

class EmailTest extends CakeTestCase {
	var $name = 'Email';

	function setUp() {
		$this->Controller =& new EmailTestController();

		restore_error_handler();
		@$this->Controller->_initComponents();
		set_error_handler('simpleTestErrorHandler');

		$this->Controller->Email->startup($this->Controller);
		ClassRegistry::addObject('view', new View($this->Controller));
	}

	function testSmtpSend() {
		$this->Controller->Email->to = 'chartjes@localhost';
		$this->Controller->Email->subject = 'Cake SMTP test';
		$this->Controller->Email->replyTo = 'noreply@example.com';
		$this->Controller->Email->from = 'noreply@example.com';
		$this->Controller->Email->delivery = 'smtp';
		$this->Controller->Email->template = null;
		$this->assertTrue($this->Controller->Email->send("This is the body of the message"));
	}

}
?>
{% endcodeblock %}
</p>
<p>
The trick ended up being me not knowing to create an instantiation of the controller and then telling it to initialize all components.  Before I was doig that I woudl get all sorts of controller-related errors.  The internals of CakePHP are slowly being revealed to me, which is a good thing because working for <a href="http://www.cakedevelopment.com">CDC</a> pretty much guarantees I will need to understand them inside and out.
</p>
<p>
I know that testing isn't very glamourous but can you imagine how to debug an Email compnent that sends out email on a specific TCP port without a repeatable unit test?  Me neither.
</p>
