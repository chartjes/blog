--- 
layout: post
title: True Tales From The Internet
date: 2005-10-05
author: Chris Hartjes
---
11:03:17 AM 6161180: One of my personal projects coming up is a PHP5 web framework...prelude to a supersecret open source project
11:04:06 AM sp1ffar1ff1c: oh noes
11:04:08 AM sp1ffar1ff1c: a framework
11:04:31 AM 6161180: Yes, an evil framework
11:04:40 AM sp1ffar1ff1c: 99% of frameworks are
11:04:42 AM sp1ffar1ff1c: evil
11:04:51 AM 6161180: It's a tool to allow me to pimp myself out to various PHP conferences
11:05:00 AM 6161180: "How to build a PHP 5 framework that is not Evil"
11:05:09 AM sp1ffar1ff1c: step 1: download Cake.
11:05:14 AM sp1ffar1ff1c: there is no step 2!
11:05:50 AM 6161180: Cake is not ready
11:06:00 AM 6161180: it doesn't have any frosting yet
11:06:16 AM sp1ffar1ff1c: on the flip side, it mimics the best framework yet. <img src="//www.littlehart.net/atthekeyboard/templates/default/img/emoticons/smile.png"" alt="-)"" />
11:06:27 AM sp1ffar1ff1c: mmm cake. now i'm hungry.
11:06:28 AM 6161180: There is some truth to that
11:06:35 AM 6161180: <strong>rummages around for a snack</strong>
11:06:43 AM sp1ffar1ff1c: the beauty of ruby on rails is how it is loosely coupled
11:06:55 AM 6161180: I dunno...a lot of stuff I do now are exercises to expand my own programming skillz
11:06:58 AM sp1ffar1ff1c: it doesn't make doing things a different way any harder
11:07:11 AM 6161180: maybe it's time I looked at cake closely
11:07:20 AM 6161180: and abandoned my crazy dreams
11:07:39 AM sp1ffar1ff1c: i'm not convinced that php's design as a language really allows the creation of a good framework
11:07:58 AM sp1ffar1ff1c: it's missing a lot of important higher-level language features
11:07:58 AM 6161180: I don't see why not
11:08:03 AM sp1ffar1ff1c: meta-programming's practically impossible 
11:08:20 AM 6161180: what do you mean by "meta-programming" in this instance?
11:08:28 AM sp1ffar1ff1c: writing code which writes code on the fly
11:08:40 AM 6161180: you're talking about the generator scripts?
11:08:45 AM sp1ffar1ff1c: no.
11:08:47 AM sp1ffar1ff1c: let me show you.
11:10:03 AM sp1ffar1ff1c:    {:up =&gt; :move_higher, :down =&gt; :move_lower, :top =&gt; :move_to_top, :bottom =&gt; :move_to_bottom}.each do |action, list_method|
   define_method(action) do
        if params['id']
              @section = Section.find(params['id'])
              @section.send(list_method)
        end
        redirect_to :action =&gt; 'list'
      end
    end  
11:10:30 AM sp1ffar1ff1c: this bit of code writes methods when the class is invoked. it's not inside another method, it's just in the class. 
11:10:46 AM sp1ffar1ff1c: the fancy thing is a closure
11:10:57 AM sp1ffar1ff1c: closures + metaprogramming = simplicity
11:11:12 AM sp1ffar1ff1c: it was paul graham who really made me see that ther ereally is a huge power difference between languages
11:11:28 AM sp1ffar1ff1c: he of course pushes lisp, but ruby has most of the features which make lisp great, without the horrible dialects. <img src="//www.littlehart.net/atthekeyboard/templates/default/img/emoticons/smile.png"" alt="-)"" />
11:12:26 AM 6161180: I guess the biggest problem is that PHP grew so fast
11:12:32 AM 6161180: hard to go back after the fact and clean up the mess
11:12:47 AM sp1ffar1ff1c: the biggest problem is that it was made by a guy who hates to program and design things. <img src="//www.littlehart.net/atthekeyboard/templates/default/img/emoticons/smile.png"" alt="-)"" /> php is a sledgehammer.
11:12:51 AM sp1ffar1ff1c: but sometimes you need finer tools
11:13:06 AM sp1ffar1ff1c: it's still the best out there vs eveyrthing but ruby
11:13:07 AM sp1ffar1ff1c: for web dev
