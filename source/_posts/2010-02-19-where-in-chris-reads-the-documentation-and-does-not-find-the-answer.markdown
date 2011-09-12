--- 
layout: post
title: Where In Chris Reads The Documentation...and Does Not Find The Answer
---
<p>If you follow me on Twitter you've seen me pissing and moaning about not being able to figure stuff out as I build out my first <a href="http://framework.zend.com">Zend Framework</a> project in a LONG time.  3 years to be exact.  I had two things that I wanted to add to the project:  (1) a new custom controller to base some other controllers off of and (2) create custom routes for it.  Sounds simple, right?
</p>
<p>
I have stared into the belly of the beast that is the Zend Framework documentation and have discovered the following truth:  there always seems to be two ways to do something.  For someone just starting out learning a framework (never mind their actual level of experience with PHP itself) this is not a good thing.  For example, let's look at creating a new base controller to extend controllers off of.  Via twitter I found the following ways:
<ul>
<li>no, don't do that, use custom action helpers</li>
<li>sure, just put it somewhere and use autoloading to find it</li>
</ul>
</p>
<p>
So I proceeded to start digging around and figure things out.  Hrm, an action helper is not what I need, so let's create that new base controller.  Oh, you mean you can have more than one way to lay out your project, even if you are using Zend_Application?  How come it's not finding the new controller even though I put it in a common place.  Why won't this work?!?  DAMNIT, I AM GOING TO QUIT PROGRAMMING AND RUN A DADDY DAY CARE OUT OF MY HOME.
</p>
<p>Fortunately the custom routing thing was easier to figure out.   Hey, here's an example of adding code to your bootstrap.  Oh wait, I'm using Zend_Application so things are different.  WTF, I am overriding my existing routes and everything is broken?!?  You can put this stuff in XML?!?!  But I am using the .ini format....  Nice, <a href="http://weierophinney.net/matthew/">MWOP</a> pointed me in the right direction.  Good thing he's on twitter.
</p>
<p>
Look, I've talked about this before.  It's awesome to have lots of documentation.  The Zend Framework documentation is awesome...but seems to only have 80% of the solutions I was looking for.  Digging around using Google just seemed to point me at the same 80%-complete documentation.
</p>
<p>
Writing documentation is a thankless task, so do not interpret my comments as a slam against those who are contributing.  I work best when I see FULL examples on how to do something, and then I can "extend and embrace" that to produce the customized solutions I always end up needing.  My complaints are solely my own, which is why I usually blog the solutions when I come up them.  I certainly cannot be the only one having problems sifting through the documentation.
</p>
<p>
As someone who had invested a lot of time in another framework, I am painfully aware of how much you take for granted when using a familiar tool, and then try to help people solve a problem.  My own experiences have ranged from "you are most definitely doing it wrong" to "I've never done it that way, and I can see how that will work".
</p><p>
Special thanks to @weierophinney, @elazar and @andriesss for their actual help and offers of help as I stumble around using Zend Framework.
</p>
