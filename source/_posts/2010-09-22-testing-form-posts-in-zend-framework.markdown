--- 
layout: post
title: Testing Form Posts in Zend Framework
---
<p>Man, did I ever blaze through a bunch of anger to figure this stuff out.  Why?  Same thing that bugs me about the Zend Framework in general:  multiple ways to accomplish something, and examples in the documentation that does NOT work as advertised.  Maybe, just maybe, I'm an idiot and did not understand the subtle nuances involved in making these tests work.  I doubt it though.
</p>
<p>
As I explained to the small group at the <a href="http://www.meetup.com/GTA-PHP-User-Group-Toronto/">PHP user's group meeting</a> I went to, I am not so dogmatic about TDD.  I tend to be pragmatic in that I am using tests and continuous integration to find things that are broken.  When I find something that is broken or not functioning as expected, I write a test for the expected behaviour and codes gets written and/or mangled until the test pass.
</p>
<p>
In this case, I had done a refactoring of the way a model was pulling in stats for running backs and receivers for a fantasy game.  As a result, in production (you suck Chris) you could not see results for those players.  The data was there, I had not properly tested things.  A familiar situation.  So, I fixed the code and wrote my more-specific-than-before unit tests, but I decided I also wanted to make sure that the output on the page itself worked correctly.  This began the descent into madness.</p>
<p>
I found MANY examples on how you allegedly send a POST request to something inside a PHPUnit-powered Zend Framework controller test.  Some said use $this->request.  Some said use $this->getRequest().  Some said to use object chaining (you know, $this->foo->setBar('fizz')->setFoo('buzz').  None of them worked.
</p>
<p>
Cue the sounds of Chris cursing loudly.  Eventually I figured it out.  What did I learn?  Object chaining did not work. And $this->getRequest() was the ticket.  Behold the code!
<br />
{% codeblock lang:php %}
public function testShowRbStatsPage()
{
    $this->loginUser('admin@xmlteam.com');
    $this->getRequest()->setMethod('POST');
    $this->getRequest()->setPost(array(
        'range' => '2009-09-10 to 2010-01-01',
        'position' => 'rb',
        'leagueName' => 'nflcanada2010'
    ));
    $this->dispatch('/football/nflcanada2010/stats');
    $this->assertQuery('td .rettd', 'Checking we have return TD stats');
}
{% endcodeblock %}
[/php]
</p>
<p>$this->loginUser() is a convenience method I created that authenticates a given user because to access the site you must have a username and password.
</p>
<p>
So what did I decide to look for?  I noticed in the templates that every running back, when displayed, would have a table cell that had the style .rettd.  Since that was unique to running backs (and receivers) I felt that was a sufficient check that we were actually displaying running back stats.
</p>
<p>One thing to take back from all this is that choosing a more pragmatic approach to testing can yield some interesting results.  It's my belief that by doing up a test every time something is broken or not behaving as expected makes for a more realistic set of tests.  You'll have tests that reflect how the application is really supposed to work, and you haven't wasted a lot of time on what you could call boilerplate testing, meaning tests that confirm stuff you already knew.  Edge cases are the first killer in any application, and then unexpected behaviour comes right after that.
</p>
<p>
If your tests reveal things that you or your users found by actually using the application, I think you are in much better shape than strict adherence to TDD.  Yes, having the tests are good.  Having tests that mean something are even better.
</p>
