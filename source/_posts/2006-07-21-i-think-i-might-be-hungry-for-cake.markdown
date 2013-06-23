--- 
layout: post
title: I Think I Might Be Hungry For Cake...
---
Alpha version of my stats app using <a href=http://framework.zend.com>Zend Framework</a> was looked at...and deemed as having "implemented basic functionality".  Well, not exactly resounding praise but it is an alpha.  Next up?  Pulling in data by date range and then making the data sortable by column, which leads me to my next thought.

<a href=http://derekmartin.ca>Derek</a> emailed me yesterday saying that his work was considering using a framework called Xoop.  I took a like at it, and didn't like what I saw.  Neither did Derek.  So he asked me what framework they should consider using.  I know he was expecting me to say Zend Framework...but I told him to use <a href=http://cakephp.org>CakePHP</a>.

Why?  Well, for starters, ZF isn't even remotely close to being stable.  While I am perfectly willing to use unstable versions of software (I'm an attention-deficit-disorder programmer that always likes the new and shiny) if it's going to be live on the internet where people other than your company are going to use it, well, stick with stable because it's less likely to blow up.

I like ZF, but it is still missing some features I'd like to see.  I was trying to do some Javascript stuff with ZF and it was just pissing me off.  Now, I'm a Javascript n00b and what I wanted to do was pretty simple...but the view helpers in ZF wouldn't let me do what I wanted.  Now, who's fault is that?  Probably mine since I'm such a beginner at it.  But providing helpers so that people like me can quickly hack together Javascript stuff is invaluable.

CakePHP, on the other hand, has implemented all the Rails goodness that I like:  ActiveRecord database module, javascript helpers, and gobs of documentation on how to do things.  If the point is rapid application development, well, having someone else do all the hard work for me and I just use their labours to build my neato-keen site is just fine by me.

Part of me is saying "wait until ZF is more stable for doing work-related projects and instead use CakePHP".  And to be honest, I can't really argue with that.  I'm early enough in the project that I could switch (it would require some grunt work but at a manageable level) and it wouldn't be that painfull.  I think that ZF is going to be rock-solid when it hits 1.0 (and I'm not going to ignore it while it works towards that) but at this time I think CakePHP simply fits my needs better.

On a totally unrelated note, <a href=http://www.phparch.com>php|architect</a> has asked me to write another magazine article for them.  The topic?  "What Can PHP Learn From Ruby on Rails?".  Heh.  I imagine that it will be in the issue of the magazine that comes out in September during php|works.  I find it funny that not only am I getting paid to give a talk on that topic, I'm also getting paid to actually *write* the talk.  Doing the article will basically entail putting my presentation down onto paper, since I already have an outline (and slides) finished. 

So, I'm off to read the CakePHP documentation and start moving stuff over.
