--- 
layout: post
title: Namespaces in PHP?  Why *wouldn't* you want them?
---
<p>
Earlier today I say the following tweet on the-often-down-but-always-interested Twitter from <a href="http://weierophinney.net/matthew/">Matthew Weier-O'Phinney</a>:
<br /><br />
"What issues to _you_ see with using namespaces in PHP? Start blogging!"
<br /><br />
Since I am one who likes to share his opinion on a wide variety of topics, I thought this is a good one to prompt discussion.
</p>
<p>
<a href="http://en.wikipedia.org/wiki/Namespaces">Namespaces</a> are expected to be a feature in future releases of PHP.  I'm an outsider when it comes to tracking the going-on in the world of PHP internals.  So, because of that, I'm not going to comment on the actual syntax of how namespaces will be implemented or it's impact on internals.  That's not really important as far as this particular discussion goes.
</p>
<p>
Imagine if you will that you are the user of a <a href="http://cakephp.org">web application framework</a> that allows you to easily use third-party libraries by dropping them into a specific location in your application structure.  You go to use it and...what the fuck?!? Class name conflicts?!?!? ARRRRRRGGGGGGGHHH.  You proceed to post to  the mailing list for said framework, complaining bitterly about how you cannot use your favourite library with this stupid framework.  Some grumpy guy from Canada flames you in response and it spirals down from there into oblivion.
</p>
<p>
There are many programming languages that support namespaces, but PHP was not one of them.  Why are namespaces so important?  They can help to solve the exact problem mentioned in the paragraph above.  Why *wouldn't* you want such a thing?!?!  You can have 5 classes with the same name in 5 different namespaces and everything will be just fine.  Except for the fact you have 5 classes with the same name.  That's not good design, but namespaces would let you do that.
</p>
<p>
So, to go back to our little framework example for a minute, the framework could assign itself a namespace (oh, I dunno, like 'Cake') and if you happen to want to use a 3rd-party library with your application that has a class with the same name, it's all good...as long as you didn't put your own code in the same namespace.
</p>
<p>
So, to answer Matthew's original question:  I cannot think of any reason to NOT have namespaces in PHP.
</p>
