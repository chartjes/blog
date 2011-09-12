---
layout: post
title: Book Review -- CakePHP 1.3 Application Development Cookbook
---
(Note: Packt Publishing provided me with a copy of this book in PDF
and MOBI formats for the purpose of me doing a review)

Once again, the fine folks at
[Packt Publishing](http://packtpub.com) have asked me to review a
book. I must confess that I had mixed feelings reviewing
[CakePHP 1.3 Application Development Cookbook](http://www.packtpub.com/cakephp-1-3-application-development-cookbook/book).
First, the only CakePHP work I do these days is maintaining an old,
old CakePHP web site (not even version 1.2) and it's being
re-written in Python + Django. Second, I know the author personally
and I like Mariano so I was worried about what would happen if I
read the book and didn't like it. So I took the approach that most
fit what my current status with CakePHP is: someone who has used it
in the past, but hasn't used it for a while and is looking for
practical examples of how to accomplish specific tasks with the
framework.

I personally find the "cookbook" style of books to be the most
helpful. They enable me to quickly find answers to the problem
"show me how to do something realistic using your tool". Hello
World doesn't cut it for the tools I need to use. A common workflow
for me is finding an example of how to do something, and then start
tweaking it to meet by particular needs. I certainly cannot be the
only one who learns how to do things this way. So Mariano can rest
easy since I found his book to be exactly the type of guide an
experienced programmer who is not familiar with a specific tool can
use.

Like any well-thought-out book, they cover the main components of
CakePHP. One of the thing I liked was that you didn't have to
necessarily read the book from front-to-back in order to get
something from it. Within each chapter, you will find info on
accomplishing common generic tasks using framework-specific code. A
lot of it didn't look too foreign to me, so I'm comfortable that
1.3 is not a huge leap forward in terms of compatibility. Of
course, your mileage may vary.

I was also extremely happy to see a chapter dedicated to showing
people how to use the CLI shells available to you via CakePHP. Back
in the day I wrote a really crappy attempt to create a
read-eval-print loop for people choosing to use CakePHP. I called
it "the testing shell" and I did a really crappy job of promoting
it. It never got a lot of traction because of PHP's focus on the
web and lack of testing culture. Which dovetails nicely into a
chapter in this book on writing tests.

While it's not great that CakePHP ended up not using PHPUnit to
begin with, but having SOME testing is better than NO testing.
Congrats to Mariano for sticking his neck out and making sure
people understand why testing is important and how easy it is to
add in tests. Honestly, it's good that you can also see the tests
written for the framework as well. If you tweak things and try to
extend CakePHP, you have a pretty comprehensive test suite to find
out if you've broken anything else.

So I will recommend "CakePHP 1.3 Application Development Cookbook"
for the intermediate to advanced programmer who is looking to learn
how to accomplish specific tasks using CakePHP 1.3. I think
beginning developers are much better off actually learning some PHP
before trying to use a book like this. YOu should not be just
cut-and-pasting code without being able to understand what the code
itself is doing.

