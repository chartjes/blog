---
layout: post
title: Building a Gimmebar Sidebar 
author: Chris Hartjes
date: 2011-11-07
comments: true 
sharing: true 
---
One of the interesting side effects of getting involved in your programming
language community of choice is that you often get access to cool projects
being done by your community buddies before the rest of the riffraff (aka 
the general public). One such project is [Gimme Bar](http://gimmebar.com),
a "capture anything you want and read later" web site. Created by the fine
folks at [Fictive Kin](http://fictivekin.com/), [Sean Coates](http://twitter.com/coates)
and [Ed Finkler](http://twitter.com/funkatron) were kind enough to not only
give me access to their application (My user type apparantly is "The Betanaut") but
also an early peek at their API.

Now, it's changed a bit since their earliest work but now they are starting to promote
not only the site but showing how easy it is to use their API to play around with
not only your content but other's public-facing content too. I fooled around with
the API and tried to write some Python stuff but lots patience when trying to work
with OAuth from the command line. Hey, it's not their fault that I couldn't be bothered
to slog through it all.

Funkatron was kind enough to put together a blog post about [building a Tumblelog with 
Gimmer Bar and PHP](http://funkatron.com/posts/building-a-tumblelog-with-gimme-bar-and-php.html)
so I told him I would write up what I did on my own blog.

One of my intents was to use the [Gimme Bar API](https://gimmebar.com/api/v0) to pull
in a list of my latest Gimmies for the sidebar on this blog. Ed had posted a very
simple example in Javascript (I cannot remember where it is) so I took it and ran with
it to modify it to work with [the blogging software](http://octopress.org) used here.

I went and asked some questions in the Freenode IRC channel for Octopress and found out
that they recommended the use of JS libraries that are compatible with [Ender.js](http://dustindiaz.com/ender).
Okay, so that was no problem. So what to use to make the actual AJAX request call to
the API? [Reqwest](https://github.com/ded/reqwest) was mentioned by some as the best
fit for using with Ender. Finally, I used [Underscore](https://github.com/documentcloud/underscore) to 
help with templating.

Even though I'm not much of a JS whiz, I was able to take Ed's example and very quickly
modify it to work exactly the way I wanted it to. Below is the code I used to putt in 
my 10 latest Gimmes and insert them into the DOM exactly where I wanted them.

{% codeblock lang:javascript %}
<section>
  <h1>My Latest Gimmies</h1>
  <ul id="gb_assets"></ul>
  <script type="text/javascript">
  reqwest({
      url: 'https://gimmebar.com/api/v0/public/assets/grumpycanuck.js?jsonp_callback=?',
      type: 'jsonp',
      success: function(data){
          var list_tpl = "<% _.each(records, function(record) { %> <li><a href='https://gimmebar.com/view/<%=record.id%>'><%=record.title%></li></a> <% }); %>";
          var list_html = _.template(list_tpl, data);
          $('#gb_assets').html(list_html);
      }
  });
  </script>                                                                                                                                                     
</section>
{% endcodeblock %}

For those who aren't JS-savvy, I'll explain what goes on here:
<ul>
    <li>Execute an AJAX call that...</li>
    <li>calls the Gimme Bar public API to get the latest 10 public posts...</li>
    <li>and on success generate an unordered list of posts...</li>
    <li>linking to the item on Gimme Bar and show the title...</li>
    <li>and insert it into the DOM where I asked it to</li>
</ul>

Easy peasy, lemon squeezy. Ender.js + Reqwest + Underscore + 15 lines of markup and JS
gives me the latest 10 posts. Hope this inspires you to play with the Gimme Bar API
yourself. 

