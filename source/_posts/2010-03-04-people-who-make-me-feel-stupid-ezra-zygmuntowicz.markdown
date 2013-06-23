--- 
layout: post
title: "People Who Make Me Feel Stupid: Ezra Zygmuntowicz"
---
<p><i>This is the 4th out of 5 blog posts about programmers who I find make me feel stupid when I read what they write or hear them speak.  Stupid because what they say is so obvious I cannot believe I missed it.  See my thoughts on <a href="http://www.littlehart.net/atthekeyboard/2010/03/01/people-who-make-me-feel-stupid-geoffrey-grosenbach/">Geoffrey Grosenbach</a>, <a href="http://www.littlehart.net/atthekeyboard/2010/03/02/people-who-make-me-feel-stupid-antirez/">Antirez</a> and <a href="http://www.littlehart.net/atthekeyboard/2010/03/03/people-who-make-me-feel-stupid-rich-hickey/">Rich Hickey</a>.</i>
</p>
<p>
Next up is another prominent member of the Ruby community, one that I feel truly deserves the label "Renaissance Programmer".  He is <a href="http://brainspl.at/">Ezra Zygmuntowicz</a>, co-founder of <a href="http://www.engineyard.com">Engine Yard</a>, probably the leader in helping people deploy Rails applications of all shapes and sizes.  Ezra seems to have done it all, from Rails work, to <a href="http://merbivore.com/">Merb</a>, to the Ruby VM <a href="http://rubini.us/">Rubinus</a>.
</p>
<p>
If I remember correctly, I first encountered Ezra and his work (and his awesome last name) during my Ruby on Rails research.  Realizing that Rails was the dominate framework in that space, I wondered what the alternatives were.  That lead me to Merb.  Unfortunately at the time it was not well-documented, so I drifted into other things (like so many other times, I'm sensing a pattern here).  Then I started hearing about the efforts to create an alternative to the standard Ruby virtual machine, with the goal of creating, I imagine, a faster Ruby environment.
</p>
<p>Much as I cannot imagine writing my own programming language, I could not imagine creating a virtual machine based on running code in an already-established language.  Then I saw <a href="http://www.youtube.com/watch?v=TcMklv40YMY">this talk</a> Ezra gave about Merb, Rubinus and the stack that Engine Yard uses.  What blew me away was when he started explaining *how* he was going about implementing Rubinus.  It made so much sense.
</p>
<p>
See, in the Ruby world you can use what they call Matz' Ruby Interpreter, or CRuby as a reference point.  Since there is no official spec, the MRI is used.  So if you want to create your own Ruby virtual machine, it's as simple as looking at how the MRI implements functionality and then copy it in your own VM.  Repeat until your own virtual machine passes all the tests in the <a href="http://rubyspec.org/">RubySpec</a> project and bingo!  You have a (hopefully as close to compatible with the MRI) virtual machine for running Ruby.  It seems that <a href="http://en.wikipedia.org/wiki/YARV">YARV</a> is a virtual machine (I believe it is a bytecode interpreter) that is included with the latest version of Ruby at this writing, 1.9.
</p>
<p>
So why does Ezra make me feel stupid: <b>He has fully immersed himself in the Ruby world from the virtual machine to the language implementation to frameworks that sit on top of it.  Like most of the people I talk about in this series, he also knows how to explain these things to people in such a way that you do not realize what awesome work he is doing.</b>
</p>
<p>
I may not be doing anything with Ruby any more, but how can you not get interested in the nuts-and-bolts of a language and virtual machines in general when someone like Ezra explains it to you?!?  In the PHP world, Facebook recently announced the release and open sourcing of <a href="http://wiki.github.com/facebook/hiphop-php/">Hip Hop for PHP</a>.  This project takes PHP code, parses it and generates C++ executables.  This is a big deal for Facebook, who is the largest user of PHP out there.  It lets them use approximately 50% fewer servers when delivering PHP-results.  They did the same thing I talked about above:  looked at how PHP implemented functions at the lowest level, and then figured out how to do it in C++.  It's a very unique project, and obviously not for everyone.  But again, an awesome case study on creating virtual machines / alternate runtimes for an existing programming language.
</p>
