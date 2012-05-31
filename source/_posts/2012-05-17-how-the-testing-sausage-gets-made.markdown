---
layout: post
title: "How The Testing Sausage Gets Made" 
author: Chris Hartjes
date: 2012-05-17
comments: true 
sharing: true 
---
So how does the Grumpy Programmer write code, TDD style? It starts with 
using a set of tools that reduce the amount of friction required.

First, I do almost all my work from a terminal. On my Macbook I use
[iTerm 2](http://www.iterm2.com/#/section/home) instead of the stock
Terminal.app. Until recently you could not get 256 colours without
some external hacking and since I like my editor to have purty colours
I needed a terminal to match it. I might take a look at Terminal.app
again, but iTerm 2 fits the bill.

Why the terminal? PHPUnit is a CLI application. Yes, many popular
editors and IDE's can do things like execute PHPUnit for you, but they
are limited in what flexibility they provide. At Kaplan we have several
different configurations under which we can run our tests. Again, reduce
the friction between the tools and you using them.

Then we have the [One True Editor](http://www.vim.org). While I do use
other editors from time to time (I do like [Sublime Text 2](http://www.sublimetext.com/2) 
a lot because it has Vim bindings), I stick with Vim. Why? The plugins.

Here's what I use:

* [Pathogen](https://github.com/tpope/vim-pathogen) to make loading other plugins easy
* [DiffDir](http://www.vim.org/scripts/script.php?script_id=102) for making code review and test reviews easier 
* [Gist.vim](http://www.vim.org/scripts/script.php?script_id=2423)
* [closetag](http://www.vim.org/scripts/script.php?script_id=13)
* [inline_edit.vim](https://github.com/AndrewRadev/inline_edit.vim)
* [nerdtree](https://github.com/scrooloose/nerdtree)
* [supertab](https://github.com/ervandew/supertab)
* [surround.vim](https://github.com/vim-scripts/surround.vim) - it has ruined me for using other editors
* [Tabular.vim](http://vimcasts.org/episodes/aligning-text-with-tabular-vim/)
* [tagbar](https://github.com/majutsushi/tagbar) - INDISPENSABLE
* [vim-repeat](https://github.com/tpope/vim-repeat)
* [vim-taglist](https://github.com/thisivan/vim-taglist)
* [vim-unimpaired](https://github.com/tpope/vim-unimpaired)

There is nothing specific to doing TDD in these plugins, but what they
do for me is allow me to slice and dice text as quickly as possible, along
with providing me with easy ways to navigate through the code base. Remember,
reducing friction is a big thing to me. If the tool makes it tough for me
to do what I want, it will be the target of grumpy ranting.

One of the reasons I like Sublime Text 2 is that you can jump all over the
place in the code base in similar ways. If you editor doesn't allow you to
do that, you need to get rid of that editor and use something that does.
NO EXCUSES. 

A typical coding session has me using two terminal windows. One has Vim running
in it, the other is used to run PHPUnit or other testing framework of choice as
I venture in the world of BDD and testing in other languages. Then I do the 
following:

* figure out HOW to test the code I'm writing
* write the tests required
* write code until the tests pass
* refactor code as required 
* refactor tests as required.

That's really all their is to it. The actual work flow of when you are using
TDD isn't magical. I will admit that experience is the only teacher for how
to actually write the tests, but luckily I have an awesome [co-worker](https://twitter.com/FreshWillisms)
who bellows obscenities at me while guiding me down the path to total testing
mastery. I know Will, you only hate me because you love me.

Every time I make a change to a test or the code, I re-run the tests. I find that
this lets me get more done while actually slowing down the pace. You end up
more focussed on the bit of code that really needs your attention, instead of
getting drawn into blind alleys.

I also frequently run code-coverage reports to make sure that I'm getting
maximum coverage for my efforts, while ignoring writing tests specifically
for methods with very low CRAP indexes. Again, I'm making sure that I am
targeting the parts of my code that need to be tested.

I know I've written about this before, but when you approach things from a
TDD perspective, you find that using things like dependency injection
become second nature. 

If there is a lesson to be learned from this, it's to make sure that every
tool that you use reduces the friction that is generated when building
your application using TDD. 

