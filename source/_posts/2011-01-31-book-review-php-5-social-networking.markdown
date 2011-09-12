--- 
layout: post
title: "Book Review: PHP 5 Social Networking"
---
<p>Back before Christmas I received an email from the folks at Pakt Publishing asking me if I was interested in reviewing a copy of <a href=" https://www.packtpub.com/php-create-powerful-dynamic-social-networking-website/book">PHP 5 Social Networking</a>.  Who am I to turn down a free e-book? 
</p>
<p>
I'm glad I decided to take a look at this book.  It's pretty dense at 450+ pages, but it really does work you through from start to finish how to build a small social networking site in PHP.  Okay, it's about dinosaurs, but let's not quibble.  I'm not into long-depth book reviews, so we can talk about what I liked about this book.
</p>
<p>
First, I admired the consistency in the approach.  While I may not agree with all the decisions that they've made, or the coding style (we all have our own way of wanting to do things), but the author was incredibly consistent in how they're putting things together.  It's all done in OOP, with attention paid on how to build on what you've already done.  I mean, let's be honest here:  most web apps of any significant size (meaning more than 10 lines of code) are very rarely internally consistent.  People learn how to do new things.  They start to hate how they've been implementing certain features in code.  They get bored and decide to try out one of these "design patterns" they've read about.
</p>
<p>
Not here.  I think this is a very valuable lesson to be learned by beginning programmers.  Once you've, you know, actually built a bunch of stuff that people other than your close friends use, you learn to refactor and improve your code.  Your task gets much more difficult if the application itself is internally inconsistent.  Like I said, I dunno if I would've made the same decisions as them, but damn it's slick looking code that looks the same no matter what they are doing.
</p>
<p>
It was also refreshing to see some attention paid to the concept of security in a web app.  Not trusting user input, not storing passwords as plaintext (they even mention using a salt for your password), stuff like that.  I still have some issues with there use of using $_SESSION as a totally trusted source, but I can admit there are limits to what you can do.
</p>
<p>
It's also rare to find a book that teaches you something while you are actually building something.  If you were to actually sit down and type in every single code example, my guess is that you would have 90% of a completely working site.  Building upon all that stuff you've learned by following the book along, it seems to me it would be easy to get it to 100%.
</p>
<p>
Just look at the sort of stuff you learn about:
<ul>
<li>the Model-View-Controller pattern</li>
<li>creating effective templates</li>
<li>proper use of a registry object</li>
<li>planning of relationships between data (along with use of binded parameters in your DB queries via PDO</li>
<li>post-coding tasks like deployment and figuring out how to get data from development into production</li>
</ul>
</p>
<p>But here's the part you were all waiting for: what did Chris not like about this book.  In a word: TESTING.  There are no tests for ANYTHING in here.  Yes, I know the testing vs. not testing flame war is on the same level as vim vs. emacs and mac vs. pc.  But damint, we're 2 years into the 21st century!  Integrating tests into your application isn't difficult any more.  Okay, so places like Facebook are apparently not using unit tests.  You are not Facebook, so don't give me that answer as an excuse.  Facebook is a perfect example of a spaghetti PHP application that grew out of control and they were able to hire some top-notch engineers to untangle it and produce an amazing application.  Slam 'em all you want, I have lots of respect for the people who continue to build and extend Facebook.
</p>
<p>
So, in summary, I highly recommend that beginning to intermediate developers check out "PHP 5 Social Networking".  It is a good example of a very cohesive application that covers a very large number of scenarios that you are pretty much guaranteed to run into.  Once you've had a chance to build something like this (many functions, cohesive architecture) you can then push your skills to the next level where you learn about refactoring and Demeter's Law and all design patterns.  Until then, use this book as a reference on one way to build stuff.
</p>
