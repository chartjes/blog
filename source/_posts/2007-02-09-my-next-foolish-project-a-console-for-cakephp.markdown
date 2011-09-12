--- 
layout: post
title: "My Next Foolish Project:  A console for CakePHP"
---
<p>On the <a href="http://www.cakephp.org">CakePHP</a> mailing list, somebody familiar with Ruby on Rails' console functionality asked "why isn't there one of these in Cake?".  I, of course, jumped right in and said "such a thing does not exist in PHP."  Nate, of course, quickly corrected me and pointed out that PHP has an interactive mode.  Which lets you do some stuff quickly for testing purposes, but this is not enough.  So I foolishly volunteered to work on a console.  Like I'm not busy enough.
</p>
<p>
So I got to thinking about how to do this.  On the surface, it seems the easiest way to do this is to write a PHP script that takes entries on the command line, run the input through an 'eval' statement.  Sounds easy enough, and I could write that in a hurry.  I think the trickiness comes in figuring out how to hook it into CakePHP so that you can access Models that already exist.  I guess this will be something that will bother me while I'm at the <a href="http://vancover.php.net">conference</a> on Monday and Tuesday.  I'll be sure to mention it during my talk.
</p>
