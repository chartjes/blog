--- 
layout: post
title: CakePHP Application RFC Follow-Up
---
<p>Holy moley, has it been almost a year since I <a href="http://www.littlehart.net/atthekeyboard/2008/05/16/cakephp-application-deployment-rfc">blogged about a potential CakePHP deployment task</a>.  Since a few people have hit me up in Twitter and in the comments for that blog post, I thought I would share my progress on this task.  To be blunt, I decided it was a waste of time to do it.</p>
<p>
Why?  Well, there plenty of options out there to help you with application deployment already.  I talked about many of them in the talk I gave at PHPQuebec back in March.  In the end, there is no reason to NOT use an existing tool to handle this other than you cannot (or in some cases will not) use one of these tools.  I picked <a href="http://www.capify.org">Capistrano</a> because:
<ul>
<li>it is command-line based and therefore it's use could be easily automated in my development and production environments</li>
<li>deployment instructions are written in code, not XML.  Sure it's Ruby but don't be like that and sneer at me.  I work with XML all day long and know when it's good to use it and when it's not good to use it.  In my opinion, using it as a configuration file to tell you where to deploy your stuff is a misuse of it.  Why not do it in JSON then?  Hrm, there's an idea what will rattle around in my brain for a while.</li>
<li>it doesn't care what you are trying to deploy, which I think is such an understated feature of Capistrano that I tell it to EVERYONE who asks me about it.</li>
</ul>
</p>
<p>
Sure, being able to type 'cake deploy' would be nice for those people who are using Cake and have things setup completely according to the default configuration, but one little change and the whole thing might just blow up.  Capistrano and <a href="http://phing.info/trac/">Phing</a> are the two tools I would recommend to any PHP devs trying to work out automated deployment.
</p>
<p>Given the number of permutations that can be part of an install, I am not confident that 'cake deploy' would be up to the task.  When I think about all the stuff I have to deploy that is not just PHP code at work, I can't imagine making it all work in a CakePHP task.  That's not to say that someone smarter than me can't figure it out.
</p>
