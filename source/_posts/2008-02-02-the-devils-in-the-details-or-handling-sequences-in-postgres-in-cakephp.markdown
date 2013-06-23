--- 
layout: post
title: The Devil's In The Details (or, Handling Sequences in Postgres in CakePHP)
date: 2008-02-02
author: Chris Hartjes
---
<p>I had been struggling with some weirdness that CakePHP has been displaying while trying to add some new features to the <a href="http://www.ibl.org">baseball league website</a>, where Cake + PHP 4.4 + Postgres were deciding to just be sulky and not work together well.</p>
<p>
So, I was trying to figure out how to make a test for this so I could file a bug (CakePHP not finding the proper name of the Postgres sequence for a table) when I tracked down <a href="http://cake.insertdesignhere.com/">nate</a> on IM to whine to him about this problem, he started bugging me about "not paying attention" when looking around in code to try and track down what I thought was a bug.  If I had looked at the API a little closer I would've been steered towards the solution he gave me.
</p>
<p>
Lucky for me, it turns out that the solution (for now) to the problem was to simply add the name of the sequence for that table as a variable to the model definition.
{% codeblock lang:php %}
<?php
class Vote extends AppModel {

	var $name = 'Vote';
	var $sequence = 'votes_id_seq'; // This is what I added in

	//The Associations below have been created with all possible keys, those that are not needed can be removed
	var $belongsTo = array(
			'BallotItem' => array('className' => 'BallotItem',
								'foreignKey' => 'ballot_item_id',
								'conditions' => '',
								'fields' => '',
								'order' => ''
			),
			'Franchise' => array('className' => 'Franchise',
								'foreignKey' => 'franchise_id',
								'conditions' => '',
								'fields' => '',
								'order' => ''
			)
	);
    var $validate = array('ballot_item_id' => array('rule' => 'numeric',
                                                    'required' => true),
                          'franchise_id' => array('rule' => 'numeric',
                                                  'required' => true),
                          'answer' => array('rule' => 'numeric',
                                            'required' => true,
                                            'message' => 'You must vote on this item')
                         );

}
?>
{% endcodeblock %}
</p>
<p>
This confirmed to me that my new-found respect for trying to come up with the simplest solution to a problem is the correct way to do so.  Since my head is full of all sorts of nonsense (work items, family life, baseball stats, old Dungeons & Dragons adventures from my teenage years) I find that at times I am better served by taking the time to think about the problem rather than start digging around.  Especially when it comes to code that was well-written an has been tested by lots of people, like the overwhelming majority of CakePHP's core code.
</p>
<p>
Thanks again to nate for proving to me that the Devil's in the details.  And continuing to make me feel stupid.
</p>
