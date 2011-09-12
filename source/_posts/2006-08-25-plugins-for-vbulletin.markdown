--- 
layout: post
title: Plugins for vBulletin
---
For the stats system I built at work, there is a component that tracks clicks (meaning we track IP addresses who have visited the site) and track "raw clicks" and "unique clicks".  I was trying to think of the easiest way to do it, and a co-worker (who has a ton more experience with <a href="http://www.vbulletin.com">vBulletin</a> than myself) suggested I do it as a plugin.
<br /><br />
Now, I'm pretty sure I'm not giving anything away by showing you guys the plugin.  After all, it only works with vBulletin and you need the other half (the puller) to make use of the data.  So, here's a nice, open source contribution to the world:
<br /><br />
<a href="http://www.littlehart.net/product-vs-clicktracking.xml">Clicktracking plugin</a>
<br /><br />
It's pretty straightforward, and the only trick was finding some code that works well with people hiding behind proxies and other places.  That I borrowed from a posting about how <a href="http://www.oscommerce.com>osCommerce</a> does it.
