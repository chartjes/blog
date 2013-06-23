---
layout: post
title: A Day in the Life At Moontoast
date: 2011-08-09
author: Chris Hartjes
---
I had jokingly asked on Twitter for topics for blog posts for this
week, planning on blogging something last night too, but I ran out
of time before I headed out to play softball. Let's here it for
dedication to task! [Matthew Turland](http://twitter.com/elazar)
had suggested I talk about the day in the life of your grumpy
programmer at [Moontast](http://www.moontoast.com). Not missing an
opportunity to be a smartass, I asked Matthew if he really wanted
to know before [my boss](http://twitter.com/ramsey) piped up that
it involved lots of "blood, sweat and swear". Thanks to
[Terry Chay](http://terrychay.com/) for that awesome quote.

Given that Moontoast is
[currently hiring](http://www.moontoast.com/company/jobs) some PHP
developers (ahem, Server Side Engineers) to either work in our
offices in Nashville, Boston or remotely in North America, perhaps
this is a very timely post. Don't worry, I'm not going to reveal
any trade secrets or ask you to peer review the code I've written.
I'll save that punishment for those folks we actually hire.
Instead, I want to focus a bit on work flow and our
infrastructure.

With most of the team in Nashville, that means they are on Central
time. Since I'm in the Eastern timezone, that gives me the first
hour of the day to focus on planning my day. Yes, I'm sure you
shocked that I actually make notes and try to plan ahead of time
the things I want to work on that day. Lately I've been working on
a SOAP-powered API. Don't worry, I can hear you snickering while
you read that. It's meant to be compatible with
[Magento's](http://www.magentocommerce.com/wiki/doc/webservices-api/api/)
for strategic business purposes.

As part of my tasks I also identify who on the team I need to speak
to if they are a potential block. Being a remote worker means that
communication is incredibly important, and quick turnaround time is
essential to avoid me sitting in my basement wasting my time. With
my list of potential targets for my anger secured, I connect to the
dev environment I'll be using and start coding away.

At Moontoast all our stuff is up in the cloud. EC2, S3, ELB, MySQL
on RDS and MongoHQ. My two dev environments are up there too, so I
spend pretty much all day using Vim. I did try using
[Expandrive](http://expandrive.com) to mount remote directories and
then edit things via MacVim (as I do prefer it) but I found that it
was impossible to use my most essential
[Vim plugin](https://wincent.com/products/command-t) to find the
files I needed to work on. So I instead duplicated my Vim setup on
my two dev instances and away I go.

I end up learning a lot of devops stuff while I build the
applications. Specifically learning how to make all the different
pieces talk nicely to each other, and then creating configurations
that allow me to pull in data for testing purposes from pretty much
any environment we are using. If you have not learned the power of
tunnelling database connections over SSH you have missed out on
some powerful tools.

We also use Git for our version control. It took me a few months to
get comfortable using it (still run into the odd problem but they
are fixable with a little research or swearing until someone helps)
and I think I'm okay with it now. I don't do anything fancy like
cherry-picking commits to build artisanal pushes that are a thing
of beauty. We keep things simple and stick to
[this workflow](http://nvie.com/posts/a-successful-git-branching-model/),
with the added change of using a stage branch.

Oh, and if that wasn't confusing enough, the two different products
we have use two different branching structures. Fixing that AND
getting rid of the stage branch are high on the list of system
integration tasks I want to do. That and fixing our current
deployment system.

Right now we use something that is actually quite awesome called
[Whiskey Disk](https://github.com/flogic/whiskey_disk), a tool that
(almost) delivers on the promise of "embarrassingly fast
deployments". I do like it but I feel that we're moving to a system
that needs to be more tailored to my goals of continuous delivery
of code. We have a cron job setup that monitors for changes to
several branches, and then triggers a deployment if it notices a
change. It *is* cool, but I would prefer some more control.
Sometimes I feel like waiting 10 minutes for changes to show up is
unacceptable. Some of my objections are also of a philosophical
nature. They are doing deploys using in-place updates of code
instead of copying code into a directory, swapping symlinks, and
then flushing the opcode cache. A minor detail to some, but if you
start relying on pieces like this you really need to do it right.

Magical deployments is cool, but I feel like we are moving towards
a scenario where we need more control of what gets deployed where.
One thing I do like is the concept of separate repositories for the
application and the config files for the application, allowing for
pushing just config changes out instead of the whole app. I find it
handy, but again, I have a desire for more control on what goes
where. My perfect tool is a cross between
[WePloy](https://github.com/rlerdorf/WePloy) and the
recently-released
[Deployinator](https://github.com/etsy/deployinator). Etsy's tool
looks the closest to what I like, but we shall see. Something in
PHP is more comfortable as Deployinator is a Sinatra app and my
Ruby is WAY out of date.

So, when I work I am either doing coding in a 'hotfix' branch to
fix a bug or a 'feature' branch when creating new things. For
example, my SOAP API work is in the 'feature-api' branch. I commit
my stuff often, usually after I've tested stuff out (more on that
later) and I also push to my branch quite often as well. Mostly
because it provides proof to the team that I am working on stuff as
all pushes are tracked and a bot emails the dev team AND posts a
message in our IRC channel that code has been pushed.

You notice I talked about tests. The amount of tests we have on
what is a fairly complex set of products is appallingly low. I do
feel shame, and while building the API I've been using
[PHPSpec](http://www.phpspec.net/) as the testing tool. While I've
been a big believer in unit testing in the past, it seems to me
that a Behaviour Driven Development approach is likely to achieve
better results overall. BDD lets me talk to our product managers
and very easily convert their criteria for a feature successfully
working into tests. I'm in the early days of PHPSpec and BDD so I'm
sure I'll have more thoughts on this in the future. Either way, the
time to commit to tests is now. I've been through the death march
of watching a team trying to write tests after the fact for a large
application. Not pretty.

To be perfectly honest, having good tests is like having
[six-pack abs](http://www.wikihow.com/Get-Six-Pack-Abs) --
everybody wants them but nobody wants to do the work to get them.
Tests are the first step down the continuous delivery path, because
if you write tests then you can have the running of those tests
automated via continuous integration. I've spoken about CI before,
so I won't waste any more time on it.

So, I have code I'm writing in Git branches and are writing tests
for all new features I'm doing. Next step is to figure out how to
complement the work I'm doing with PHPSpec with the use of
[Cucumber](http://cukes.info/) to let me test the rest of the site.
There are some challenges due to the use of Facebook Connect for
authentication, and heavy use of Ajax in the applications. They are
great from a user perspective, but a pain in the fucking ass to try
and write automated tests for. While Cucumber is aimed more at Ruby
folks, Cucumber is also able to test non-Ruby apps. Again, it will
be an uphill struggle but one that I think will pay off in allowing
increased delivery speed.

Now, we do have meetings every single day. We are using some
scrum-like system, but it basically boils down to talking to each
other for 5 to 10 minutes every day to go over what we're working
on to see if anyone needs help or to tell them if you're done early
and can tackle another problem. Yes, sometimes I get stuff done
ahead of schedule and then declare my desire to spend time on a
another task, usually something related to infrastructure work. Our
meetings are usually just before my lunch time, and often they
result in my slightly modifying what I'm working on in the day. I
have some lunch and then get back to work.

So there you have it: a day in my life at Moontoast. There are a
lot of cool challenges to make the whole infrastructure better, but
they are the type of challenges that I think will not kill you but
really make you stronger. Wish me luck!
