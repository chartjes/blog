--- 
layout: post
title: CakePHP Mythbusters!
---
<p>I ran across an article <a href="http://www.isolani.co.uk/blog/web/PhpFrameworksComparingCakePhpAndSymfony">comparing CakePHP and Symfony</a> and found that the writer had a number of preconceived ideas about CakePHP.  These same ideas keep popping up everywhere, used by people looking to get their hate on about CakePHP.  I sent a very well-reasoned email to the writer clearing up some of those misconceptions, and (to his credit) he replied to me saying:

<blockquote>"Thanks for a brilliant email reply to my blog post about CakePHP and
symfony - and taking the time out to send it. Thanks so much for the
pointers and corrections."</blockquote>
So, in the interest of clarifying things about CakePHP I thought I would share that email, slightly rewritten for this blog posting, but the content is roughly the same.
</p>
<h3>Lack of Documentation</h3>
<p>
Man, this one will just not die.  One complaint seems to be the lack of documentation similar to what Symfony has.  I think that's totally fair in that there are very few *detailed* books out there explaining how to use Cake.  However, I feel that there is more than enough information on people's blogs on how to build things using CakePHP.  So, perhaps it requires time to search around via Google or your other favourite search engine, so I can understand how people are unable to find one unified source for this info.  I don't think you could ever have one definitive source for info about Cake, and the majority of contributors to Cake blog about it.  If I had to pick what I would call the definitive source out of the crowd, it would be <a href="http://book.cakephp.org">the CakePHP Cookbook</a>.
</p>
<h3>Scaffolding</h3>
<p>While I think scaffolding is a great idea to show off the strength of CakePHP, it is a toy and I have never used the scaffolding to build anything other than a throw-away prototype.  I use 'cake bake' to generate the "scaffolding"  for my application and then edit those files.  In fact, I'd say that 'cake bake' is the essential tool that anyone who uses CakePHP needs to start using RIGHT NOW if they are not already.
</p>
<p>It is my personal opinion that showing people the scaffolding stuff that Cake uses by default is counter-productive and a waste of time.  It just confuses them and leads to frustration, which is clearly what has happened to you here.  So if you want to use CakePHP, just don't use the scaffolding at all.</p>
<h3>Models are tied to controllers in a 1:1 relationship</h3>
<p>Nothing could be further from the truth.  Here's a sample of some code from a project I was working on that shows this</p>
{% codeblock lang:php %}
class CalendarController extends AppController {
	var $name = 'Calendar';
	var $uses = array('UserClient', 'CalendarPending', 'LegalCase');

	function admin_index() {
		$results = $this->UserClient->Location->findByLocationId($this->Auth->user('location_id'));
		$pending_depositions = $this->CalendarPending->find('all', array('conditions' => array('location' => $results['Location']['name'])));
		$cases = $this->LegalCase->groupByDepositionType();

		$this->set('pending_depositions', $pending_depositions);
		$this->set('cases', $cases);
	}
{% endcodeblock %}
<p>For those keeping score at home, that's one controller interacting with 4 different models.  You can have controllers that don't have any associated models.  You can also have controllers that don't talk to any model at all by default by setting the uses array to equal null.  So the idea of  Cake only being for simple "one table = one view" is simply wrong.  Again, I'd like to find a way to get rid of this idea that you can only have one model per controller.</p>
<h3>Cake's Ajax and Javascript helpers do not support graceful degradation</h3>
<p>I don't use the Ajax helper but a quick look at the online documentation shows that this myth might actually be true.  Core contributor Mark Story has a post showing you an example<a href="http://mark-story.com/posts/view/providing-contextual-form-help-with-mootools">how to make that happen</a> in CakePHP, but it requires a little bit of work.  Maybe Symfony is the only "mainstream" framework out there that has put effort into implementing that.  Personally, I don't use the Ajax helpers in Cake as I prefer to use jQuery.</p>
<h3>Cake's HTML and Form helpers produces bad markup</h3>
<p>I don't feel that's true at all.  The form helper can produce legends and fieldsets...and those can be turned off via parameters in the calls to that particular helper.  Again, more work needs to be done to clue people in about this stuff.  The online documentation does show what all the parameters that the helpers take do, so check them out to find out exactly how to bend if to your will.</p>
<h3>Unit tests are an afterthought</h3>
<p>Definitely not true.  When you use the 'cake bake' utility to create the outlines of models and controllers it also creates the empty unit tests that go along with it as well.  Cake also has a very extensive set of unit tests for the framework itself and code coverage that is up past 85% last that I had seen.  Testing is important, and it's good to see that Symfony also has a commitment to that.
</p>
<h3>CakePHP is not an "enterprise capable framework"</h3>
<p>
Could someone please tell me what this actually means?  Cake is used by Mozilla for their Add-ons site, so I think that's about as enterprisy a use as you're going to see out there.
</p>
<p>
So, a few myths about CakePHP busted I hope.  The thing I wish to emphasize to those who are looking at Cake to make sure they look at the <a href="http://book.cakephp.org">CakePHP Cookbook</a> and the <a href="http://api.cakephp.org/">online API documentation</a> in order to fully understand how to use the various helpers.
</p>
