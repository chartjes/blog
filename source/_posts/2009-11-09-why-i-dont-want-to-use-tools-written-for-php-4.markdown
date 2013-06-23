--- 
layout: post
title: Why I Don't Want To Use Tools Written For PHP 4
---
<p>
I was engaged in a lively discussion on Twitter this morning sparked by someone grumbling that people should not be writing frameworks that target PHP 4.  In the course of that discussion, I offered my opinion on a couple of things:
<ul>
<li><a href="http://codeigniter.com">My least favourite framework</a> suffers from having code that detects whether or not you are using PHP 4</li>
<li>PHP 5 has been out long enough that pandering (I do not know if there is a better word for that) to the crowd that does not want to update to it is counter-productive.</li>
</ul>
</p><p>It was pointed out to me that CodeIgniter has 23 lines of code in it dedicated to detecting what version of PHP you are running.  In my opinion, that is 23 too many.  
</p>
<p>
Of course, it isn't as simple as that.  If you have customers who are paying you for your application and they are running PHP 4, well, you have a tough decision:  keep supporting them and your application becomes more and more convoluted as the language changes or be bold and tell them "from this point forward new versions of my application will be PHP 5 only."  I think the truth is that very few people are willing to make that sort of stand, and that's okay.  In the end, you really should use whatever tools you are comfortable with.  But it's important to understand why those tools are, in the big picture, substandard.
</p>
<p>
My personal opinion is that PHP 5 has enough new features that either replace existing functionality in PHP 4 or give you features that were not available before, only sheer apathy prevents you from creating a PHP 5-specific version of your application.  Not to mention that PHP 5 itself runs faster than PHP 4. If you have to turn on E_STRICT so your application stops spitting out errors all over the place, you are doing it wrong.
</p>
<p>
What I think would be very interesting is to see how <a href="http://www.rubyonrails.org">Ruby on Rails</a> and <a href="http://www.djangoproject.com">Django</a> handle this problem:  what sort of contortions do they go through when Ruby and Python (respectively) make changes and perhaps break backwards compatibility.  Is PHP the only programming language for the web where the people running older versions hold onto it kicking and screaming, despite gobs of evidence that newer stable versions of the language have fixed bugs, perform better, and offer new useful features?  Enquiring minds want to know!
</p>
