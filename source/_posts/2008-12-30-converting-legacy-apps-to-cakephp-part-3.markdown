--- 
layout: post
title: Converting Legacy Apps to CakePHP, Part 3
author: Chris Hartjes
date: 2008-12-30
---
<p>I hope everyone has had a good holiday season this winter of 2008/2009.  Me, I took two weeks of consecutive vacation time for the first time since my youngest was born.  This has given me time to relax, enjoy time with my family and think about 2009.  Due to time constraints I have been forced to start the process of handing over the Side Project That Will Not End to another developer who can give it the attention that it deserves and needs.  If you are well versed in CakePHP 1.2 and are looking for a side project that will push your skills, contact me.  The client is anxious to get it done and are awesome to work with.
</p>
<p>
Anyway, onto other matters.  As you saw in parts 1 and 2, a bug part in having a successful transition from legacy app to CakePHP is having an environment that is well suited to the use of a framework.  Having laid out the groundwork for that switchover, it's time to talk about the part of a refactoring or porting that is most difficult:  separating your business logic from your display logic.
</p>
<p>
In a post on this site, I talked about the concept of "fat models and skinny controllers".  Having worked with frameworks professionally for almost two years now, I can say that I think I can update that motto to be "fat models, skinny controllers, and flexible views".   So, just what do I mean about this.
</p>
<p>
The main reason people use a framework (other than to become a raving fanboi) is to provide structure to an application.  However, with this structure there comes some limitations.   Maybe limitations is the wrong word.  I prefer to borrow a term used a lot by the Rails world (and the Cake world as well), and that is "convention".  Every framework has it's conventions, and the culture and environment of the framework dictates what the rules are for the models, views and controllers.  Or models, views and templates if you're into Django.  Whatever you call them (data source, request responder, output?) any framework does its best to try and prevent you from doing harm to yourself while coding.
</p>
<p>
In what I call spaghetti PHP, you usually end up with applications that have their data source interactions, request responder and output mashed together.  The vast majority of my early code was of this type.  Nothing wrong with it, as long as it was cleanly written and easy to understand.  Frameworks say that this kind of thing leads to poorly written code and lack of flexibility.  Refactoring spaghetti PHP is not always easy, especially when you have to add new things into the mix.
</p>
<p>
So, as a result, it has become a common programming practice to make the effort to separate your business logic from your presentation logic.  I don't think this is a bad thing at all, framework fanboi that I am or not.  The goal in all this is to create an application that is easier to maintain going forward, and I truly believe that this can only be done through this separation.  But *how* do you do this?
</p>
<p>
Let's look at the first part of the new motto:  "fat models".  Now, I'm not talking about <a href="http:://http://en.wikipedia.org/wiki/Big_Beautiful_Woman">BBW</a> here, despite how many people end up on my site via a search along those lines.  The "fat model" is the concept of placing as much code in the data source interaction parts of your application as possible.  In Cake terms, this means creating methods in your models to do all the data crunching that you need, and then having your controllers simply call these model methods and pass the results to the view.
</p>
<p>
So, in our legacy app we had a structure that used "modules", which are really nothing more than a number of <a href="http://en.wikipedia.org/wiki/Front_controller">front controllers</a> that had request response processing via large switch-case blocks that did a lot of database calls.  Then, it would do a search-and-replace of tokens within a template based on the data retrieved and then display it.  While I had some issues with their "all-inclusive templates" that controlled the display of data via CSS calls that set "display:none" as needed, it did mean I had templates to work with.  
</p>
<p>
The next logical step then was to take a look at all the database calls that were being done within these modules and map them to a particular Cake model.  As I looked at the queries and what was being done with the results, I started breaking them done into one of two categories:
<ol>
<li>Results that could be obtained with the existing model methods like find('all') etc</li>
<li>Results that would require further manipulation of the data after using an existing model method call</li>
</ol>
</p>
<p>
Initially, I thought that I would be looking at a small number of the first category, but in the end it was the power of Cake's Associative Data Mapping capabilities that made me realize the number of custom model methods would be minimal.  Let me give you some examples.
</p>
<p>
Let's say that I need to get a list of all cases that belong to a particular firm.  Here's one way of doing that in Cake.
{% codeblock lang:php %}
<?php

// Given that we have a has-and-belongs-to-many relationship 
// established between LegalCase and Firm, and the ID of the firm 
// already stored in the session via the Auth component

$conditions = array(
     'LegalCase.archived' => 0,
     'Firm.id' => $this->Auth->user('firm_id')
);
$order = 'LegalCase.case_name';
$cases = $this->LegalCase->CaseFirm->find('all', compact('conditions', 'order'));

?>
{% endcodeblock %}
</p>
<p>
Very straightforward, and Cake would return to me an associative array containing all the cases that belong to the firm, ready to pass to the view.  If you were to look at the SQL generated by such a thing, you would see that it was using some SQL JOINS to link the cases, firms and cases_firms table to get my results.  I cannot recommend enough for people building things in CakePHP to use the awesome <a href="http://github.com/cakephp/debug_kit/tree/master">Debug Kit</a> to peer inside Cake as you develop.
</p>
<p>
In another part of the application, I had to get a list of orders that had been archived, count them, and group them by month.  Obviously this could not be done with just the existing model methods.  So I looked at the queries and then the code that followed those queries, then condensed them down into a method in the Order model:<br />
{% codeblock lang:php %}
	function archivedOrdersCount($user_id) {
		$fields = "DATE_FORMAT(date_completed, '%m') as month_completed, DATE_FORMAT(date_completed, '%M') as month_name, DATE_FORMAT(date_completed, '%Y') as year_completed";
		$conditions = array(
			'user_id' => $user_id,
			'OR' => array(
				'client_archive' => 1,
				'void' => 1)
		);
		$order = "year_completed, month_completed ASC";
		$results = $this->find('all', compact('fields', 'conditions', 'order'));
		$orders = array();

		foreach ($results as $result) {
			$key = "{$result[0]['month_name']} {$result[0]['year_completed']}";
			
			if (!isset($orders[$key])) {
				$orders[$key] = array(
					'year' => $result[0]['year_completed'],
					'month' => $result[0]['month_completed'],
					'label' => $key,
					'count' => 0
				);
			}

			$orders[$key]['count']++;
		}	
		
		return $orders;	
	}
{% endcodeblock %}
</p>
<p>
I think part of the problem a lot of people are faced with when converting a legacy app over to using *any* framework, is the idea that your problems are unique and not solvable via a framework.  In the context of using Cake's models, I think people would be really shocked to discover just how easy it really is now to take an existing query and make it work with Cake models.
</p>
<p>
I hope I've given you a little glimpse into some of the work involved in converting SQL calls in PHP over to using Cake's model objects.  In the next post in this series, I'll be showing what I mean by "skinny controllers".
</p>
