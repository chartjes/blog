--- 
layout: post
title: "A New Way Of Judging Frameworks:  Where are the tests?"
---
<p>
As a <a href="http://sportso.com">project for work</a> gets ready for an alpha release, I've managed to eliminate all the serious bugs and now have some time for what should've been part of the project from the beginning:  writing tests. As a lapsed tester, I always feel guilty about not writing tests when things start to get complicated with an application.  Whenever you make a change, you have to point-and-click your way through the application to make sure that nothing has broken.  I got tired of pointing-and-clicking, so I decided it was time to shut up and write some tests.  Since I'm using Code Igniter instead of CakePHP for this project (did I mention that I inherited the project and couldn't switch?) I started looking into the culture of testing surrounding Code Igniter.  It's weaker than a newborn baby.
</p>
<p>
The built-in testing system is some weird mishmash of unit testing and "you have to create your own test results template".  WTF?  You can't be serious.  So I quickly ignored that.  Besides, the first set of tests were going to be using <a href="http://phpunit.de">PHPUnit</a> combined with <a href="http://selenium.openqa.org/">Selenium</a> so I could make the "acceptance testing" automated.  As an aside to this, I remember speaking with Sebastian Bergmann (the driving force behind PHPUnit) at a conference maybe 3 years ago and him telling me that he knew someone was working on getting Selenium and PHPUnit to play nicely together.  Anyway, it's working just fine.
</p>
<p>
So, next step was to see if I could use something else than the incredibly lame testing tools that Code Igniter came with.  I found something called <a href="/www.foostack.com/foostack/">fooStack</a>, that contained CIUnit.  It lets you use PHPUnit with Code Igniter.  Now we're talking!  Lickety split I had some unit tests for my models written.  Well, after spending quite a lot of time screwing around with the tests and finding out the difference in relative paths between the application running via Apache and trying to test the models via the command line.  Thanks to all those on Twitter who yelled "use php_sapi_name to figure out what environment you are in, you idiot!" at me.
</p>
<p>
But all this got me to thinking:  how do some other PHP frameworks stack up in terms of having tests?
<ul>
<li>Code Igniter has ZERO tests for the framework itself.  Perhaps I will mention this to my boss next time I'm asked to create a project from scracth.  Hrm, guess I'll have to trust that their code actually works the way it's supposed to.</li>
<li>Zend Framework (full disclosure: I was one of the original authors of the Zend_Service_Audioscrobbler component) has huge amounts of tests for the framework itself.  In fact, any new contributions MUST have working tests submitted with it.</li>
<li>CakePHP has lots of tests for the core, and I believe that I saw something in the changelog for CakePHP 1.2RC3 that indicated they were at 80% code coverage in terms of testing for the CakePHP core.  Bug submissions for CakePHP are supposed to come with tests to prove that there is a repeatable problem.</li>
<li>Symfony recently rewrote it's core tests and created their own testing framework for it.</li>
</ul></p>
<p>So now when you start comparing frameworks to each other, I think it's important you also consider how much effort has gone into creating tests for the core functionality of that framework.  A well tested framework should mean far less surprises when using it.  Given how many tools are out there to assist you in testing, I don't think there are any excuses other than being totally lazy to not create tests for the core functionality of any application.  Pay now, or pay later, but you will PAY to fix bugs in your application.  Paying now is simply cheaper.
</p>
<p>
Would you stake your project on complex code written by someone else that is simply not testable by you?  Perhaps I am not looking at from the proper distance because I am inside the framework-creator culture, but I can't see why you wouldn't want to provide tests to prove your stuff actually works the way you claim it does.  Tests prove that the code is *behaving* the way you expect, and code that is testable is also usually easier to modify as time goes on.  There is some sort of sick joy in making a change to code, running the unit tests, and seeing that you didn't break anything. 
</p>


