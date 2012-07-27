---
layout: post
title: "Monkey-patching is for closers" 
author: Chris Hartjes
date: 2012-07-13
comments: true 
sharing: true 
---

My co-worker [Juan Treminio](http://jtreminio.com) brought to my attention this interesting
blog post by someone advocating [monkey-patching strtotime in order to test his code](http://antecedent.github.com/a-time-and-place-for-monkey-patching.html).

For those not familiar with the term, first I suggest you go read what [Wikipedia says about it](https://en.wikipedia.org/wiki/Monkey_patch)
and then try and understand why it is, in 99.999% of cases, a practice best left to 
real experts at dynamic languages that allow redefinition of methods at run time.
And definitely a terrible practice to recommend for testing purposes.

The use of monkey-patching is extremely prevalent in the Ruby community and
also to a certain extent in Python usage. I'm not going to go into length
about their use of it except to say that it seems quite common and I think
most developers are using it as a shortcut to counter what might be poor
code architecture decisions. Perhaps some Rubyists could provide me with
some good examples of why it is so popular amongst them. I don't hate
Ruby, let's be extremely clear about that.

So, our blog post author submits some code that needs testing:

{% codeblock lang=php %}
function deleteOldPosts()
{
    $threshold = strtotime("-1 year");
    # Fetch all posts older than $threshold from the database
    $oldPosts = Post::findAll(["timestamp" => ["<" => $threshold]]);
    foreach ($oldPosts as $oldPost) {
        $oldPost->delete();
    }
}
{% endcodeblock %}

Quite correctly he points out that this code would be difficult to test...so he
then goes on to explain that using [runkit](http://php.net/manual/en/book.runkit.php) to
monkey-patch strtotime and what is this I don't even...

I will start of by showing a subtle set of refactorings that would make this 
code testable, and then explode into a rant afterwards.

First, the threshold should be injected.

{% codeblock lang=php %}
function deleteOldPosts($threshold)
{
    # Fetch all posts older than $threshold from the database
    $oldPosts = Post::findAll(["timestamp" => ["<" => $threshold]]);
    foreach ($oldPosts as $oldPost) {
        $oldPost->delete();
    }
}
{% endcodeblock %}

Second, you replace the static method call with an object instantiation
and a normal method call.

{% codeblock lang=php %}
function deleteOldPosts($threshold)
{
    # Fetch all posts older than $threshold from the database
    $post = new Post();
    $oldPosts = $post->findAll(["timestamp" => ["<" => $threshold]]);
    foreach ($oldPosts as $oldPost) {
        $oldPost->delete();
    }
}
{% endcodeblock %}

Third, you inject your Post object into your function.

{% codeblock lang=php %}
function deleteOldPosts(Post $post, $threshold)
{
    $oldPosts = $post->findAll(["timestamp" => ["<" => $threshold]]);
    foreach ($oldPosts as $oldPost) {
        $oldPost->delete();
    }
}
{% endcodeblock %}

No runkit. No monkey-patching. No justification for doing stuff like this
instead of the correct, long, hard, difficult slog through a legacy code base
to do things the right way this time instead of compounding the problem.

The other day on Twitter I commented that I felt that any blogger who does
a post that contains code in ANY programming language needs to understand
a few things:

* your code might be wrong
* your approach might be wrong
* people will take your advice as being canonical or idiomatic

I am all for people sharing knowledge that they have gained. Hell, it's 
how I've made my entire career. But don't go advocating solutions to
problems when there are much more straight-forward solutions available.

The issue with that original method isn't that you need to monkey-patch
strtotime(). The issue is the coding decisions that led you to think that
monkey-patching ANYTHING was the way to do it.

There are no shortcuts to testing things. It's extra work during development 
to save you extra work at deployment. Unless you start off a project doing
TDD, you will have to refactor your code to make it work. Do not pretend
otherwise, and do not advocate the use of something that should only be
used in specific, well-understood circumstances as a shortcut for testing
your code without modifying it.

