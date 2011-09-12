--- 
layout: post
title: Creating Usable Forms With Zend Framework
---
<p><i>Note: These examples are using Zend Framework 1.9.5, with comes with Zend Server Community Edition 4.0.6 for OS-X</i></p>
<p>As I begin working on the admin area for a work application being built with <a href="http://framework.zend.com">Zend Framework</a>, I've been spending a lot of time starting and stopping on it.  Why?  Chalk it up to the extensibility of Zend Framework, who have clearly taken the "configuration" side of the "configuration vs. convention" philosophy when it comes to frameworks.  Before you get all worked up, remember that (a) I last used Zend Framework 3 years ago and (b) I got very used to relying on framework conventions to help me speed things up, a tactic used with great success in building <a href="http://cakephp.org">CakePHP</a> and <a href="http://codeigniter.com">CodeIgniter</a> applications.  Alas, those days are behind me and I am getting schooled in the wonders of "figuring everything out" and "object chaining is cool" and "why are there always more than one way to do something with this framework?!?".
</p>
<p>
So one of my first tasks is to create a form to allow people to create new leagues for a fantasy sports league.  Need a very simple form with three things in it: league name, sport and scoring period (which is how often we need to compile standings).  Sounds easy right? 
</p>
<p>
After searching around online for some examples of building simple forms, I was dismayed to discover there were two different ways of building the form.  I could (a) do it the long way and create specific instances of the form elements using Zend_Form_Element_X or (b) do it the short way and add them to the form by use of <a href="http://framework.zend.com/apidoc/1.9/Zend_Form/Zend_Form.html#addElement">Zend_Form::addElement()</a> and pass it the type of form element I want via an array.  For reasons I cannot explain initially, I decided to do things the long way.  Later on, I found out that doing it this way saved me from rewriting.
</p>
<p>
So, the approach I decided to use was to create a separate file that contains the form I want to use.  Why? Because I wanted to reuse this form for both "add a new league" functionality and "edit an existing league" functionality.  After figuring out that I needed to create a Bootstrap file for the module that the form was in (otherwise auto loading wouldn't work) here's what I cranked out:
{% codeblock lang:php %}
class Admin_Form_League extends Zend_Form
{
	public function __construct($options = null)
	{
		parent::__construct($options);
		$this->setAction($options['action'])->setMethod('post');
	
		$name = new Zend_Form_Element_Text('name', array('required' => true));
		$sport = new Zend_Form_Element_Select(
			'sport', 
			array(
				'required' => true,
				'multiOptions' => array('baseball' => 'Baseball', 'football' => 'Football')
			)
		);
		$scoringPeriod = new Zend_Form_Element_Select(
			'scoring_period',
			array(
				'required' => true,
				'multiOptions' => array('daily' => 'Daily', 'weekly' => 'Weekly', 'monthly' => 'Monthly')
			)
		);
		$submit = new Zend_Form_Element_Submit('submit', array('label' => $options['submitLabel']));

		if (isset($options['leagueId'])) {
			$leagueId = new Zend_Form_Element_Hidden('id', array('value' => $options['leagueId']));
			$this->addElement($leagueId);
		}

		$this->addElements(array($name, $sport, $scoringPeriod, $submit));
	}
}
{% endcodeblock %}
Perhaps you've noticed something different about this example compared to others you might have seen elsewhere?  Okay, I won't keep you in suspense about it.  I'm using the $options parameter when creating an instantiation of this particular form to pass some dynamic information.  Without this, it would be very difficult to reuse this form.  In this case, I pass in up to three different parameters:  the target for the form, the label I want on the submit button and (in the case where we're editing an existing record) the primary key of that league in the database.
</p>
<p>
So, then the next step is to tell my controller I want to use that form.  Ignore the database related stuff as I'm using <a href="http://www.doctrine-project.org/">Doctrine</a> and my use of that probably deserves it's own blog post down the line.
{% codeblock lang:php %}
class Admin_IndexController extends Zend_Controller_Action
{
	protected $_flashMessenger = null;

	public function init()
	{
		$this->_flashMessenger = $this->_helper->getHelper('FlashMessenger');
		$this->initView();
	}

	public function indexAction()
	{
		$leagues = Doctrine::getTable('Leagues');
		$form = new Admin_Form_League(array(
			'action' => '/admin/index', 
			'submitLabel' => 'Add New League'
		));

		if ($this->_request->getPost()) {
			$formData = $this->_request->getPost();

			if ($form->isValid($formData)) {
				$newLeague = new Leagues();
				$newLeague->fromArray($form->getValues(true));
				$newLeague->save();
			} else {
				$form->populate($formData);
			}
		}

		$this->view->leagues = $leagues->findAll()->toArray();
		$this->view->messages = $this->_flashMessenger->getMessages();
		$this->view->form = $form;
	}

}
{% endcodeblock %}
</p><p>Nice and simple, and effective.  I also have another action that is for the editing or deleting an existing league.  Here's the controller for that
{% codeblock lang:php %}
class Admin_LeaguesController extends Zend_Controller_Action
{
    public function init()
	{
		$this->_flashMessenger = $this->_helper->getHelper('FlashMessenger');
		$this->initView();
    }
	
	public function editAction()
	{
		$leagueId = $this->_getParam('id', 0);
		$leagues = Doctrine::getTable('Leagues');
		
		if ($this->_request->getPost()) {
			$formData = $this->_request->getPost();
			$form = new Admin_Form_League(array(
				'action' => '/admin/leagues/edit', 
				'submitLabel' => 'Update League',
				'leagueId' => $formData['id']
			));
			
			if ($form->isValid($formData)) {
				$updateLeague = $leagues->find($formData['id']);
				$updateLeague->name = $formData['name'];
				$updateLeague->sport = $formData['sport'];
				$updateLeague->scoring_period = $formData['scoring_period'];
				$updateLeague->save();
				$this->_flashMessenger->addMessage('Updated league');
				$this->_redirect('/admin');
				exit();
			} else {
				$form->populate($formData);
			}
		} else {
			$leagueId = $this->_getParam('id', 0);

			if ($leagueId == 0) {
				$this->_redirect('/admin');
				exit();
			} else {
				$form = new Admin_Form_League(array(
					'action' => '/admin/leagues/edit', 
					'submitLabel' => 'Update League',
					'leagueId' => $leagueId
				));
			}
		}
		
		$results = $leagues->findById($leagueId)->toArray();
		$formData = array(
			'name' => $results[0]['name'],
			'sport' => $results[0]['sport'],
			'scoring_period' => $results[0]['scoring_period']
		);
		$form->populate($formData);
		$this->view->form = $form;
	}

	public function deleteAction()
	{
		$leagueId = $this->_getParam('id', 0);

		if ($leagueId == 0) {
			$this->_redirect('/admin');
			exit();
		}

		$leagues = Doctrine::getTable('Leagues');
		$deleteLeague = $leagues->find($leagueId);
		
		if ($deleteLeague->delete()) {
			$deleteMessage = 'Deleted league';
		} else {
			$deleteMessage = 'Unable to delete league';
		}

		$this->_flashMessenger->addMessage($deleteMessage);
		$this->_redirect('/admin');	
		exit();
	}
}
{% endcodeblock %}
</p>
<p>Nothing too earth-shattering I would think.  Armed with this, I can now display my form in two different places:
{% codeblock lang:php %}
<h1>Admin home</h1>
<h2>Leagues</h2>
< ?php if (count($this->messages) > 0) : ?>
<ul>
< ?php foreach ($this->messages as $message) : ?>
<li>< ?php echo $message ?></li>
< ?php endforeach; ?>
</ul>
< ?php endif; ?>
<table border=1>
	<tr>
		<th>League Name</th>
		<th>Sport</th>
		<th>Scoring Period</th>
	</tr>
< ?php foreach ($this->leagues as $league) : ?>
	<tr>
		<td>< ?php echo $league['name'] ?></td>
		<td>< ?php echo $league['sport'] ?></td>
		<td>< ?php echo $league['scoring_period'] ?></td>
		<td><a href="/admin/leagues/edit/id/<?php echo $league['id'] ?>">Edit</a> <a href="/admin/leagues/delete/id/<?php echo $league['id'] ?>" onClick="return confirm('Are you sure you want to delete this league?');">Delete</a></td>	
	</tr>
< ?php endforeach; ?>
	<tr>
< ?php echo $this->form ?>
	</tr>
</table>
{% endcodeblock %}
{% codeblock lang:php %}
<h1>Edit league</h1>
</p><p>Use the form below to edit an existing league</p>
<table border=1>
	<tr>
		<th>League Name</th>
		<th>Sport</th>
		<th>Scoring Period</th>
	</tr>
	<tr>
< ?php echo $this->form ?>
	</tr>
</table>
{% endcodeblock %}

<p>So I do that, and load up the form and...what the?  Damn, the default decorator for these elements is ugly.  I want my form fields to line up nicely inside my table (shut up, I know I should use CSS but this is an admin panel and I am in a hurry) so after finding <a href="http://devzone.zend.com/article/3450">this article by Zend Framework architect MWOP</a> I figured out how to create the exact decorator I wanted.  Here's the final version of my reusable form.
{% codeblock lang:php %}
class Admin_Form_League extends Zend_Form
{
	public function __construct($options = null)
	{
		parent::__construct($options);
		$this->setAction($options['action'])->setMethod('post');
		$decoratorOptions = array(
			'ViewHelper',
			'Errors',
			array(array('data' => 'HtmlTag'), array('tag' => 'td', 'class' => 'element')),
		);
	
		$name = new Zend_Form_Element_Text('name', array('required' => true));
		$name->setDecorators($decoratorOptions);
		
		$sport = new Zend_Form_Element_Select(
			'sport', 
			array(
				'required' => true,
				'multiOptions' => array('baseball' => 'Baseball', 'football' => 'Football')
			)
		);
		$sport->setDecorators($decoratorOptions);
		
		$scoringPeriod = new Zend_Form_Element_Select(
			'scoring_period',
			array(
				'required' => true,
				'multiOptions' => array('daily' => 'Daily', 'weekly' => 'Weekly', 'monthly' => 'Monthly')
			)
		);
		$scoringPeriod->setDecorators($decoratorOptions);
		$submit = new Zend_Form_Element_Submit('submit', array('label' => $options['submitLabel']));
		$submit->setDecorators($decoratorOptions);

		if (isset($options['leagueId'])) {
			$leagueId = new Zend_Form_Element_Hidden('id', array('value' => $options['leagueId']));
			$this->addElement($leagueId);
		}

		$this->addElements(array($name, $sport, $scoringPeriod, $submit));
	}
}
{% endcodeblock %}
</p>
<p>
I'm pretty sure that if I dig around some more, I can find info on how to automatically apply that decorator to ALL my form elements if I needed that.  Maybe in the next revision.  Hope you find this example helps you to create your own reusable forms and to tweak the decorators yourself.
</p>
