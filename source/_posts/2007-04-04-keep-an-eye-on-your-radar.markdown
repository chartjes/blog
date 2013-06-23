--- 
layout: post
title: Keep An Eye On Your RADAR
---
<p>Over at the PragDave blog (written by Dave Thomas of the Pragmatic Programmers) he has a very interesting article about a <a href="http://pragdave.pragprog.com/pragdave/2007/03/the_radar_archi.html">new architecture for web applications</a> that he calls RADAR for RESTful Application, Dumb-Ass Recipient.  Why do I think this is important?  Because it makes so much sense. :)</p>
<p>
In a nutshell, he is advocating that you build the core of your web application to supply information via a REST application server, then create a proxy server that can serve up the information in HTML format for clients that can't easily speak REST's language of XML responses, like a web browser.  He has a great section in there:

<blockquote>
Does that mean I'm down on the RESTful, CRUD based approach to application development? Not at all. For some categories of application, I think it's a great way of structuring your code. But REST isn't designed for talking to people. So let's accept that fact when creating applications. And, while we're at it, let's take advantage of the fact that HTTP is such a flexible transport. Rather than trying to design one monolithic application than has both the CRUD functionality and the smarts to be able to talk HTML to end users, why not split it into two smaller and simpler applications?
</blockquote>

So, you can still serve up your data with REST for "smart clients" that can directly manipulate the XML resulting from a REST call, but why not filter the REST response through some code that can then output a much-easier-for-humans-to-read version in HTML?
</p>
<p>
This isn't really a radical concept, as most people are doing something similar to this already in their code.  He is just advocating doing this on a more defined level instead of just in your code.  See, in Ruby on Rails you have the ability to specify what controller / action pair you want for different output types using something called 'respond_to'.  Now, I've used it a tiny bit and while it is a very neat bit of code, it does look kind of hackish to me as well.
</p>
<p>
Instead, continue to use a REST service as the core application server and then have, for example, an HTML application server that will read data from the REST service and manipulating so it looks real-pretty-like for display purposes.  Ironically, before I read this article I had been structuring the new IBL web site along these lines.  That site is kicking me in the ass because it's PHP 4 only, and PHP 4's XML parsing is just terrible.  Give me SimpleXML or give me death!  Nate has been helping me figure out how to use the XML object in CakePHP, but I have to do a lot of work on the data before it's in a presentable format.  Maybe I will do as Nate suggested and try pushing the XML stuff into the new Set object and see what happens.  You never know.
</p>
<p>
Anyhow, check out the article on RADAR and see what sort of ideas it gives you in terms of restructuring the architecture of your application.  Simple is good, and this looks like a very simple architecture to understand.
</p>
