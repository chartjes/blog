--- 
layout: post
title: If It Walks Like A Duck...
---
I recently got my copy of the <a href="http://www.pragmaticprogrammer.com/titles/ruby/index.html">Pick Axe</a>, properly known "Progamming Ruby, 2nd Edition" and have been reading through it on the train ride to and from work mostly.  One of the more interesting chapters is called "Duck Typing".  It was referred to this because Ruby (and PHP to some extent) just "knows" what the variable or object is that you are using.  To paraphrase the book: "If it walks like a duck, and quacks like a duck, it is a duck."  This means that Ruby will let you do all sorts of things to an object or variable, and will let you know if what you're trying to do just won't work because of the type of thing it is.

Ruby and PHP share the same dynamic typing mechanism for variables.  For those who don't know what that means (or perhaps a reminder for some), it means that in order to use a variable or object you don't have to declare what type of thing it is in advance.  This is in stark contrast to how C, C++ and Java work.  That gives Ruby and PHP a lot of flexability when it comes time to refactor things.

Ruby and PHP will throw exceptions (or generate errors) if you try to use an object (in this case I mean either a real object or a variable) in a way that you just aren't allowed to.  This means throwing errors if you try to add two strings together in PHP, or if you try to treat a string as an object and use a method that doesn't exist in Ruby.

They even go on to explain an example where duck typing saved them.  A site for a client provided a CSV download that contained information about people participating in a contest.  Things worked well for a while, then the download started timing out.  When they looked at the code, it became obvious that the overhead involved in the algorithm they chose to build the CSV file has getting to be too high.  So, they changed ONE line in the code in question to build the CSV file (I'm serious, it was one line) and POOF, the problem went away.

That is the power of dynamic typing.  Since the variable receiving the information didn't care what the source was (thanks to duck typing), it was trivial to change how to get it.  Because the variable they were using to collect the information didn't care if you changed it from a string to an array, it was trivial to change.

Besides, it's such a cool name for a programming philosophy.  Duck typing. Quack.
