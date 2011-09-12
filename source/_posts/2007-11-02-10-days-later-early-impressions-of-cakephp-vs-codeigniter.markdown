--- 
layout: post
title: "10 Days Later:  Early Impressions of CakePHP vs. CodeIgniter"
date: 2007-11-02
author: Chris Hartjes
---
<p>
As loyal readers to my blog know, my <a href="http://www.xmlteam.com">employer</a> has committed to using <a href="http://codeigniter.com">CodeIgniter</a> for projects, although I hold out hope that new projects with my beloved <a href="http://www.cakephp.org">CakePHP</a>.  That's okay, I'm a big boy and can handle working with different things as clients (and bosses) demand.  So, after maybe a week and a bit of working with CodeIgniter I thought I'd talk about it.</p>
<p>
<b>Once you know one MVC framework, you know them all</b>.  My experience with CakePHP and <a href="http://framework.zend.com">Zend Framework</a> means that understanding how CodeIgniter works in the context of MVC is simple.</p>
<p><b>CodeIgniter mixes OOP and functions</b>.  CakePHP has a much, much stronger commitment to using objects to access core functionality.  A quick example is this is the way both frameworks handle forms in the views.
{% codeblock lang:php %}
// CakePHP
echo $form->create(...);
echo $form->input(...);
echo $form->select(...);
echo $form->submit(...);
echo $form->end();

// CodeIgniter
echo form_create(...);
echo form_input(...);
echo form_dropdown(...);
echo form_submit(...);
echo form_close();
{% endcodeblock %}
But within the controllers you are calling methods of objects to do things.
{% codeblock lang:php %}
$data = $this->defaultdata();
$this->load->model('Leagues');
$lookupResults = $this->Leagues->getLeagues();
$data['lookupResults'] = $lookupResults;
$data['mainview'] = 'league_browse';
$this->load->vars($data);
$this->load->view($data['layout']);
{% endcodeblock %}
Now, take this with a grain of salt because I am inheriting other people's code here so this might not be 'CodeIgniter best practices' but I think a little consistency would go a long way in the decision to use either functions or objects.
</p>
<p>
<b>Lack of conventions makes Chris sad</b>.  I am very used to CakePHP's habit of just knowing where things are supposed to be instead of me having to specify everything.  Yes, I understand that CodeIgniter is all about doing it your way, but I've grown to like the CakePHP way.  I like that my actions in the controller know where to find the view...as long as I've followed the conventions.</p>
<p>
<b>CodeIgniter's User Guide Is Awesome</b>.  Logical groupings, cool Web 2.0 features when you click on the table of contents.  Yes, we finally have some <a href="http://tempdoc.cakephp.org">documentation for CakePHP 1.2 available</a> but it is 'alpha with extreme prejudice' in it's current form.  I'm not saying CakePHP should copy what CodeIgniter is done.  I'm sure there will be an awesome final place for the CakePHP 1.2 documentation.  But for someone starting out with CodeIgniter, the user guide is an essential tool.</p> 
<p>
<b>No built-in associative data mapping makes Chris sad</b>.  But then again, I'm not really having to deal with much in the way of databases on this current project due to us using eXist.</p>
<p>
So, there you have it.  A very, very early look at my thoughts on CakePHP vs. CodeIgniter.  I'll post the more interesting things I come across along the way as my current project gets built out more...</p>
