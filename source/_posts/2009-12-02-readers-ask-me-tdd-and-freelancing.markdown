--- 
layout: post
title: "Readers Ask Me: TDD and freelancing"
---
<p>Hendrick Daldrup writes:
<blockquote>I just saw your post regarding topic suggestions on your blog for Dec.

I actually have 2, but the first one might be better suited for a blog post.
So, here goes:

1. I started doing some freelance work to boost my portfolio and have been using CakePHP as my framework of choice in several cases.
I wanted to focus on TDD for the larger projects, thanks to Cake's nice tie in with SimpleTest, but found it impossible to market to clients.
The problem is that TDD causes an overhead on development time while reducing the bugs in the code. However, since bug fixes are basically included in the price, for the client it just translates to paying more for work that I would otherwise do for free anyway.
TDD makes sense for a company with full time developer(s), but those with a small budget/tight deadline or no technical understanding always translate it to an unnecessary additional cost & time.
Of course you could just add it to the development time and/or costs without mentioning it, but I prefer keeping my work transparent and was hoping that you or one of your readers might have been in a similar situation and have a tip on how to justify the use of TDD to a potential client.
</blockquote>
</p>
<p>The first thing that occurs to me when trying to answer this question is this:<i>TDD is not for the client, it is for the developer</i>.  In other words, the client should not care that you are using TDD to build this application for them.  They should care that you deliver something on-time, within budget, and meeting their application requirements.
</p>
<p>
TDD can be a powerful tool, especially if you are going in and reworking an existing application.  With work projects, every time a bug is reported I now create a test to (a) verify that the bug exists and (b) make sure that when I fix that bug, it has not broken anything else.  Scoff at the TDD crowd if you want, but there appears to be lots of evidence that including tests with your application goes a long way towards reducing bugs.  <a href="http://sites.google.com/site/yacoset/Home/how-to-avoid-writing-bugs">This article</a> speaks anecdotally about the value of TDD:
<blockquote>
 At first it wasn't clear what the benefits and trade-offs of TDD were, but an empirical study conducted on teams working at Microsoft and IBM2 found that teams practicing TDD could get up to 40% fewer bugs in their released code, but it came at a cost of taking up to 35% longer than a team developing the same software without TDD. It neither absolves TDD nor condemns it, but it can tell a product manager what he could get if he had the time to pay for it.
</blockquote>
</p>
<p>We have started to stray from Hendrik's question.  In my opinion, there is no need to sell the client on TDD.  As far as the client is concerned, TDD is simply part of the whole "building the application for you" process.  At this point, I could not imagine building a web application for someone else without including tests to make sure I don't break things.  Those tests are your first line of defence when fixing the bugs you inevitably introduce into an application.  No set of tests can cover everything, but even a limited set of tests are better than nothing.
</p>
<p>
Now, if someone can tell me how to test CodeIgniter controllers using <a href="http://jamierumbelow.net/2009/08/11/setting-up-the-perfect-codeigniter-tdd-environment/">this type of setup</a>, I'll be a much-less grumpier programmer.
</p>
