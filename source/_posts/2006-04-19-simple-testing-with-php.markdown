--- 
layout: post
title: Simple Testing with PHP
---
I'm a guy who believes in the value of agile software development.  My former employers never seemed to quite grasp the concept fully.  My <a href="http://www.sexsearch.com">old project</a> started off agile, but it became a strictly big-design-up-front-all-decisions-from-the-top when things came to a head.  Now, they've gotten even more process intensive and I don't think I could be really productive in that sort of environment at this point in my career.

Anyhow, one of the smart things that we did was create unit tests for just about every single function we had.  We used the <a href="http://www.lastcraft.com/simple_test.php">SimpleTest</a> unit testing framework.  It works well, can produce output for both web browser and command line stuff.  I'm not sure if they are still using it.

As my interest in PHP security has grown, I started reading Chris Shiflett's <a href="http://shiflett.org">blog</a> and he had some great info on <a href="http://brainbulb.com/agile-php-testing.pdf">Agile Testing</a> with <a href="http://shiflett.org/code/test-more.php">test-more.php</a>, a PHP port of a Perl testing package called (oddly enough) Test::More.  It uses something called TAP (Test Anything Protocol).

Check out the site, check out the PDF, and you will see how easy it can be to implement testing for your PHP applications.
