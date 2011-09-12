--- 
layout: post
title: "Twitter Asks:  Continuous Integration Landscape for PHP Developers"
---
<p>Thanks to my loyal followers on The Twitter, who suggested this topic.</p>
<p>For those not familiar with the concept of <a href="http://en.wikipedia.org/wiki/Continuous_integration">Continuous Integration</a>, I can sum it up with one very glib phrase:  it lets you break your code before you buy it.  By this I mean, when combined with other programming practices like automated deployment and Test Driven Development, you get a chance to see if the code you've written *today* breaks anything you wrote *yesterday*.</p>
<p>
If I were to design a Continuous Integration (hereafter referred to as CI) system, what would it look like? Setting aside the one I use already (details on that later), I believe there are some key features it requires:
<ul>
<li>Ability to integrate with your version control system</li>
<li>Web interface for cross-platform access to results of build</li>
<li>Ability to run your unit test suite and view the results</li>
<li>Ability to deploy code wherever you want</li>
<li>Ability to email results of test builds</li>
<li>Must be able to automate all of this for you</li>
</ul>
</p>
<p>This is what I would call a non-trivial set of requirements.</p>
<p>
It also illustrates what became the biggest realization for me:  you cannot have CI without writing tests (whether they are unit tests or integration tests), and you cannot have CI without the process of creating a "build" being triggered without any further action by the developer.  Without a commitment to writing meaningful tests it definitely won't work.  It is my firm feeling that there *is* such a thing as pointless tests, and to me getting to 100% code coverage is often more about programmer ego.
</p>
<p>
So, there are a few choices for PHP developers.  You could use <a href="http://phpundercontrol.org/">phpUnderControl</a>, which is a plugin for <a href="http://cruisecontrol.sourceforge.net/">CruiseControl</a>, a Java-based tool.  I took a look at it, saw all those XML configuration files and said "no thanks."  If you like screwing around with XML configuration files, then maybe this is the right tool for you.  Me, I like my pointy-clicky interfaces.  Or plain-text configuration files.  Also targeted mostly at Java developers.  My project was using PHP *and* Python, and needed to be able to support Java as well for a non-web project another developer was working on.
</p>
<p>If you prefer the cool ideology of a PHP-powered solution, you could look at <a href="http://code.google.com/p/xinc/">Xinc</a>.  Installs via PEAR (which is always a good idea), but drags a few other PHP components in with it.  I dunno, doing it PHP-only held no special appeal to me.
</p>
<p>In the end, I settled on <a href="http://hudson-ci.org">Hudson</a>.  Much like CruiseControl, it's Java based, but that was no big deal as we already have Java in our infrastructure at work with more little bits being moved to it.  Also, Hudson has the type of architecture I like:  a small, tight core with lots of plugins to add the functionality I wanted.  Using Subversion?  Add the plugin.  Need to run <a href="http://codespeak.net/py/dist/test/">py.test</a> scripts?  There's a plugin for that.  Want to be able to see the results of your PHPUnit tests?  There's a plugin for that.
</p>
<p>
So, not only that, but I could also write a shell script that is run when a build is triggered.  In this case, I was using a post-commit trigger to start builds, but if I wanted to be dogmatic about it I would use a pre-commit trigger, and fail the commit attempt if the tests broke.   I remember how the younger, angrier me flew into a rage at a previous employer when a hook was put into place in our CVS repository (yes, I've been around long enough to have actually used CVS) that ran a syntax checker on any code that got checked in.  Predictably, something was broken because the version of PHP running on the CVS server was *different* from what we were using both in development and production, and a difference in extensions caused a problem.  That is a story for another time.
</p>
<p>
I also find that using a post-commit hook allows me to look at the code in the staging environment to find bugs that are caused by subtle differences between the development environment and staging.  Today, I fixed one bug by using the new ternary shortcut available in PHP 5.3.  Learn something new every day, is my motto.
</p>
<p>
So, how does a build actually work?  Here's how I've set things up:
<ol>
<li>A developer commits code to the trunk of the SVN repository.  We don't currently use branches, so I'd have to tweak things if we did work in branches and then merged things into trunk.</li>
<li>Hudson wakes up when it sees a commit, and checks the code out into a workspace.</li>
<li>Hudson then runs a list of shell script commands to do a bunch of things:  run my Doctrine migration scripts, run my PHPUnit tests, run my py.test tests, then copy the code into place on the staging server.</li>
<li>Create a bunch of test reports that can be viewed in Hudson itself</li>
<li>Send out an email to our tech mailing list telling people that a build has been triggered along with the results</li>
</ol>
</p>
<p>I have to say there is nothing that puts a smug feeling of satisfaction in my heart like seeing that a build was successful...and nothing that makes me curse quite as much as seeing that a build failed.  But without those tests in place, then I would not find bugs that would've gone into production.  *Any* bug making it into production is BAD, and although I often use gallows humour at work to try and deflect my internal anger at such a thing, it IS possible to production pushes of new code that contain no errors.
</p>
<p>
As a follow-up to this idea, I now have a policy that whenever a bug does get found in staging or production, I write a test to recreate the bug, and then put code into place to fix it.  I have found that this has the interesting effect of giving you a bunch of unit *and* integration tests (thank you for the ability to test the output of controllers in Zend_Framework PHPUnit tests) that cover edge cases found by real users.  Besides, you can get really lost going deep into the "we need to create fixtures so I can test stuff that manipulates dynamically-generated content" rabbit hole.  I saw a test today that could benefit from the use of fixtures, instead of simply assuming that data will always be there.  Your mileage will vary, but you have to understand that slavish devotion to testing does you no good if you're not accomplishing the goal of producing a working application that meets the goals of the people who are actually, you know, using it.
</p>
<p>
I hope this post helps you if you're trying to decide whether or not to take the CI plunge.  I have no regrets at the length of time it took me to get things to a happy place in terms of Hudson's configuration.  The benefits of automated builds with the goal of protecting you from yourself more than outweighs a few afternoons of scratching your head and trying to figure out what is going on with Hudson itself.
</p>
