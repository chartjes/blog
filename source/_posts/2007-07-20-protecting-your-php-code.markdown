--- 
layout: post
title: Protecting Your PHP Code
author: Chris Hartjes
date: 2007-07-20
---
<p><b>WARNING:  This post contains my own opinions and does not represent the views of my current employers</b></p>
<p>
In the July 2007 issue of <a href="http://www.phparch.com">php|architect magazine</a> there is an article called "Shell Shock" that advocates using products from Zend and IonCube to encode and protect your PHP applications.  Here are some of the nuggets of wisdom from that article:
<ul>
<li>"Serious business demands closed source"</li>
<li>"Maybe your friend will let it (<i>ed: meaning your code</i>) sit on his server for a few years, then dig it up, make some modifications and re-release it as his own script"</li>
<li>"You prevent would-be attackers from deceiving you by first deceiving them, and you do this by veiling your plain-text source code"</li>
</ul>
</p>
This paragraph is my favourite of the whole article, and it appears at the end:
<blockquote>
Many programmers are afraid of deception. They are 
accustomed to code that is open, and they feel safer 
around it. As a result, many programmers don?t even 
check for errors, refusing to entertain the possibility 
that the PHP functions they hold so dearly may betray 
them one day. Then that day comes, and there?s an in- 
explicable bug in the product that is the result of the 
programmer?s failure to let go of the illusion of perfec- 
tion. Perfection has a very high price. What you really 
want from your code is for it to work. You want it to 
keep working under varied conditions, and you want it 
to keep working next week, next month and after the 
next release of PHP. Give yourself all the help you can.
</blockquote>

<p>
First I laughed when I read this article.  Then I sighed.  Then I got mad.  Then I decided to write this blog post.
</p>
<p>
To start, I will focus on the paragraph above.  What I get out of that is that if only your source was closed and hidden from prying eyes, it would not have bugs in it.  Which is, of course, total nonsense.  Code has bugs because it's open and they feel safer?  There are two kinds of bugs:  application bugs (which is the code I would write) and system bugs (in this case, bugs that that appear from PHP itself).  I'm sorry, but there is nothing I can do if there is a bug in PHP that causes my application to crash except to point this bug out to the people who have the ability to fix it.  That paragraph I quoted doesn't seem to make sense to me at all.  I fail to see how encoding my code makes it somehow safer and less vulnerable to bugs from either the application level or system level.  Perhaps I'm reading something that isn't there, or have taken that paragraph out of context.</p>
<p>
Look, I understand that people want to make money off of the code that they create.  This is how I have been making my living for almost 10 years now, writing code for companies and they pay me for doing it.  Over time I have come to realize that what I am being paid for now is not just the code I create, but the knowledge that goes with that code as well.  Unless I've signed a non-compete agreement, I can pretty much reproduce any code I've written in the past and probably do it better now.
</p>
<p>
Having said that, I haven't been in the business of creating an application that I sell to other people.  Well, that's not entirely true.  Way back in the day I wrote a parser for use with a system run by Canada Post called eParcel.  You'd send it the size of the object you're trying to ship and it would spit back XML with data in it about what size box they recommend and how much it would cost to send the item where you were going.  I sold exactly one copy of it.  I created a license that said they could use my code on as many of their own sites as they wanted but they couldn't give the code to anyone else.  I got paid for the license and that was the end of it as far as I was concerned.</p>
<p>
Was I worried they would give my code to someone else?  Not really.  I figured if they wanted to do it bad enough, they would do it and no license would stop them from doing so.  How many unregistered copies of the various versions of Microsoft's operating systems are out there?  See my point?  Microsoft made all their money selling programs that ran on their operating system.  Did it matter that there were so many unauthorized copies running out there?  Sure, but not as much because they were making money elsewhere.</p>
<p>
So, encoding / encrypting / hiding your source code won't stop those who really want to get at it.  I'm pretty sure a quick search on google will let me find tools to break through the encryption and then I've got what I want.  And where does that leave you?  The same place as those who didn't encrypt their source code.  I know this will come as a blow to the ego of many programmers, but the stuff you've written probably isn't so earth-shattering as you think it is.  Besides, somebody out there probably already holds a patent on what you've dreamed up and also probably has a lawyer or two laying around. ;)</p>
<p>
Another reason I dislike encoding / encrypting is that it prevents you from fixing flaws in the software you've purchased if you are able to do so.  Real world example:  my previous employer Verticalscope purchased licenses of a mailing list manager that came highly recommended by an employee.  It was written in PHP.  There were some bugs in the application, bugs that could've fixed if they had access to the source code.   Bugs that could be seen in the error logs.  Instead, it was encrypted with IonCode's encoder and they were at the mercy of the creators of the application as to if and when bugs would be fixed.  Time and money wasted...a lot more money than what the product cost them.
</p>
<p>
If you charge money for your application and it is good, PEOPLE WILL PAY YOU FOR IT EVEN IF THEY COULD STEAL IT.  If you want to be like the record industry and treat all your customers like potential criminals, then you shouldn't be surprised when people get mad at you and do everything they can to steal your application and distribute it as far and wide as they can.  What you want people to do is pay you for what you know about getting that application running (otherwise known as a service contract) and let the people who want to do it themselves (for whatever reason) be on their own when it comes to support or changes.
</p>
<p>Some people will steal your stuff no matter what, so you can always build that into the price of your product (don't think Microsoft isn't doing that?) if you are so concerned.  I say don't worry about your "intellectual property" in the form of your PHP application being stolen if you are making it available to other people.  You're smart enough to find another ways to make money off it, right?</p> 
<p>
Now, I believe in respecting the "intellectual property rights" of others because ripping off someone's stuff and claiming it as your own is just about as dishonest an intellectual act as there is.  I just feel that deception gives you a false sense of security.  If your stuff is good, people will want it and many of them will pay you for it too.  Even if they can get the source code and fix it themselves if a problem occurs.
</p>
<p>
Trust me, even if my sole source of income was selling a PHP application that I had written I would feel the same. The author of that article probably makes his living selling applications he wrote, and has chosen the "security by obscurity" path when it comes to securing his application.  Encode your stuff if you want, but be aware that the minute you choose to do that you are telling your customers "I don't trust you" and I have a hard time understanding a business model that assumes people are going to want to steal the stuff you sell. My policy would be simple:  if you buy it from me, I'll be happy to give you as much support as I reasonable can.  If you steal it from me or can't prove that you bought a copy from me (which is pretty much the same thing) then you can expect a hearty "screw you, call me when you are willing to pay for your copy" in response to your requests.  I'm sure my regular visitors will agree that seems to be more in line with my personality.
</p>
