---
layout: post
title: Book Review -- Easy PHP Websites with the Zend Framework
---
Full disclosure: Jason Gilmore publishes my book
[Refactoring Legacy Applications Using CakePHP](http://www.wjgilmore.com/books/read/refactoring_legacy_applications_using_cakephp)
and also provided me with a free copy of his book (in both PDF and
MOBI formats) for me to review. While I consider Jason a friend, I
do not let my personal friendships interfere with an objective
review of a book.)

When you are going through the progress from beginner to mastery of
any web application framework, it is almost impossible to do unless
(a) you wrote the framework yourself or (b) there is excellent 3rd
party documentation available on how to use it. Even if the project
itself has really good extensive documentation (which Zend
Framework does) it is still essential that other people have
documented their usage of it in situations beyond the very limited
ones presented in the documentation provided by the project itself.
When you add to this the fact that Zend Framework is very large, is
component based, and often provides multiple solutions for the same
problem, it means that it is even more critical to find out how
other people are solving problems similar to the ones you are
facing.

Jason did provide me a copy of the previous version of this book as
well (it never hurts to ask people for favours...) and when he told
me at [CodeMash](http://codemash.org) that he was putting the
finishing touches on an updated version of the book I said (a) let
me know what tools you used to build it and (b) I'd be happy to
review it when it comes out. So when I saw the announcement that
[Easy PHP Websites with the Zend Framework](http://www.wjgilmore.com/books/read/easy_php_websites_with_the_zend_framework)
had been released I reminded Jason about my promise to review it.
Shortly thereafter an electronic copy of the book showed up in my
email.

At 240 pages I wouldn't say this is the type of book that you can
really read cover-to-cover at a rapid pace. I think it is more
suited as a very long and expanded HOWTO for building an
application from scratch. I was also pleased to see that Jason had
made the commitment to pushing Test Driven Development by having
the reader write tests for the site they were building as they went
along. The more people who come to understand the benefits of
writing and automating testing of the applications, the better the
applications people in the PHP community will produce.

In this book Jason guides you from start to finish on the creation
of GameNomad, a social networking application for console and PC
gaming enthusiasts. You start with nothing but a skeleton of a
project built using ZendTool and end up with an automated
deployment system for pushing your changes up into production. Oh,
you also end up learning how to integrate
[jQuery](http://jquery.org) into the project as well *and* learning
how to use Git, albeit at a very basic level) to keep things
organized.

I know what you're thinking: how could Jason have covered anything
of substance in 240 pages. I'm going to let you in on one of the
dirty secrets of the programming profession: a social networking
site is not as complicated to build as people think it is. Facebook
itself is not complicated, what is complicated is how it has
changed over time to handle the ridonkulous traffic levels it
handles. Trust me when I tell you that Jason shows you how to build
the features that are at the core of any decent social networking
site where members post items and send messages to each other.

In my opinion, this book works well as a resource for beginning and
intermediate users of Zend Framework. For beginners, it guides them
from creating the application from scratch and promotes some good
practices. For the intermediate level user, it shows you how to
accomplish common tasks needed by any website that relies on
user-generated content and adding unit testing, code coverage
reports, and automated deployment skills to your toolkit.

I've found this book to be a good resource, even for a grumpy
veteran PHP programmer like myself. Flipping through the chapters
quickly I can find some slightly different ways of doing things on
my projects, and I really like that Jason is also showing how to
take tools outside of the PHP ecosystem and embrace them. Tools
like Git and Capistrano are there to help you, why wouldn't you
want to use them?

Also pay close attention to how Jason shows you the proper places
to using the various helper and plugin architectures that Zend
Framework provides you. It has been my belief that any
well-designed framework should consist of as small a core as
possible, and then allow you to extend it through plugins. Zend
Framework allows you to do exactly that, and I've very quickly
embraced plugins as an easy way to keep customized code inside a
component that can be used anywhere in the application, instead of
dealing with the problem of cutting-and-pasting code all over the
place.

If you want to get serious about building a real application using
Zend Framework, I would recommend you pick up a copy of Jason's
book and take your time to go through it as your building your
project. When you've got an application full of tests providing
100% code coverage *and* can be automatically deployed, you'll be
able to sleep at night without worrying about the dreaded
late-night phone call "the site is broken and you have to fix it
RIGHT NOW!!!"

Also check out some of Jason's other books if you're fairly new to
PHP and are looking to get up to speed faster with things like
using MySQL with PHP and integrating PayPal into your web
applications.
