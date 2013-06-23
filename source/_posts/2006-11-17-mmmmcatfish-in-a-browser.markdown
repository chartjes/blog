--- 
layout: post
title: Mmmm...catfish in a browser
---
No, I'm not talking about the delicious fish, I'm talking about <a href="http://www.sitepoint.com/blogs/2005/10/18/the-catfish-part-1/">The Catfish</a>, a Javascript pop-up that sits at the bottom of the browser window and follows you as you scroll through the site.? The above-linked SitePoint uses the Catfish to show ads for their books (which I think are some of the best books for programmers just getting started).

Before I point out an example at my work, why is it called The Catfish?? Well, catfish like to swim at the bottom of whatever body of water they are in...and the javascript Catfish sits at the bottom of your browser window.? Makes sense to me, but it sounds cool too.? "Hey guys, I just got the catfish working.? Can you check it out in IE?"

Anyhow, I've been tasked with trying to fix our current catfish implementation (you can find ours at <a href="http://www.footballforum.com">FootballForum</a> where we use it to entice people to sign up for a membership to the site) because it was having some problems.? So I dug around and found <a href="http://www.gen-x-design.com/archives/ajax-activity-indicators-make-them-global-and-unobtrusive">this posting</a> that showed me how I could create a catfish using the <a href="http://prototype.conio.net/">Prototype javascript library</a>.? Now I can do some cool effects and such (like fade the catfish in, and will experiment with some other effects.

However, the problem with the catfish right now isn't that it's not working, because the window is popping up at the bottom and it's staying at the bottom like it's supposed to.? I think the problem is CSS and DOM related, because we're layering two images over top of a tiled background.? It requires nasty hacks in CSS for IE in order to make it happen.? Not being a CSS guru I've passed those implementation details off to? the CSS guru here at work and he is confident he'll have it all worked out.

Once that gets worked out I'll do a follow-up posting where I show the Javascript side of things that helped make it happen for us.
