--- 
layout: post
title: "Lazyweb Help: Busting out of frames"
---
<p>Normally I don't ask for time-sensitive help on my blog, but since my readers are such gracious bunch I thought I could count on them to help me out.</p>
<p>
I have a <a href='http://www.agatedepot.com'>site for work</a> that uses frames.  Oh yeah, it's <a href='http://www.cakephp.org'>CakePHP</a> application.  Frames are not my favourite thing in the world, but they are part of this particular site.  Now here is my problem:
<ol>
<li>Users must be authenticated to use the site, and when they log in from the front page a bunch of frames are loaded.  Then they can click around doing stuff.</li>
<li>When their session times out, meaning they need to get logged back in, I need for the frames to disappear and send them back to front page of the site.</li>
</ol>
</p>
<p>
So far, I have not been able to figure out how to do this.  I've been told by reliable sources on Twitter that I probably need some Javascript code that does something like this:

{% codeblock lang:javascript %}
<script type="text/javascript"> 
if (top !== self) top.location.replace(self.location.href); 
</script>
{% endcodeblock %}

but I cannot determine *where* to put that code.  Please help this frames n00b figure it out!
</p>
