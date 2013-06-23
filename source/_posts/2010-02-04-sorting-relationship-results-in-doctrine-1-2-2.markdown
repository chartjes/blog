--- 
layout: post
title: Sorting Relationship Results In Doctrine 1.2
---
<p>
I've been building an admin panel for a work project dealing with fantasy sports, and one of the failings of the old version of the overall application was that, well, sometimes it didn't retain the desired display order of players grouped by position.  Sometimes it worked, sometimes it didn't.  A classic case of "software working by accident" maybe?  So I've set out to fix that part of it.
</p>
<p>
I've been using <a href="http://www.doctrine-project.org">Doctrine</a> 1.2 for the project (integrated with <a href="http://framework.zend.com">Zend Framework</a>), and I found it quite easy to setup the relationships I needed between my models.  Oh, except for finding out that I really needed a field called 'id' in one table in order to make a relationship work properly.  Sometimes convention triumphs over configuration. ;)
So I thought to myself "I wonder if I can configure things so that when we're pulling in the related results, it is sorted?"
</p>
<p>
So I started digging around via search engine.  Took me about an hour to find the solution.  First, it took me half the time to dive deep enough to find out WHERE I can define the default sort order.  Surprisingly, it was in an area that made total sense but I could not find before.  Weird.  Probably due to me not fulling understanding the API.
</p>
{% codeblock lang:php %}
class Team extends Doctrine_Record 
{
	public function setUp() 
	{
                ...

		$this->hasMany('Player as Players', array(
			'local' => 'team_id',
			'foreign' => 'player_id',
			'refClass' => 'PlayersTeams',
			'orderBy' => 'FIELD(position, "C","1B", "2B" ,"3B", "SS", "OF", "P")'
		));
	}
}
{% endcodeblock %}

<p>
Oh, what's all that other stuff?  That's what took the other half of the hour to figure out.  See, I couldn't use any sort of natural sorting order.  I had a specific order that they needed to be displayed in.  As usual <a href="http://stackoverflow.com/questions/134379/returning-query-results-in-predefined-order">StackOverflow came to my rescue</a>.  I'm pretty sure that what I am doing is MySQL-specific but I imagine you can figure it out for other RDBMS'.
</p>
<p>
So now when I pull in info about a Team, I get the associated Player records sorted to my heart's desire.  Awesome.  This does raise a question:  how would you accomplish this sort of trick if you were using a non-relational database like <a href="http://couchdb.apache.org">CouchDB</a>.  Research for another day I guess.
</p>
