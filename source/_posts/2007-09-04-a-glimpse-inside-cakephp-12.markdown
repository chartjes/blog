--- 
layout: post
title: A Glimpse Inside CakePHP 1.2
author: Chris Hartjes
date: 2007-09-04
---
<p>One of my co-workers over at <a href="http://www.cakedevelopment.com">CDC</a> (the mighty <a href="http://rd11.com/">gwoo</a>) gave a talk to the Orange Country PHP group about CakePHP 1.2 and some of the features that it contains.  One of the more interesting items, well interesting to *me* anyway, is the addition of a convenience feature to "has and belongs to many" associations called "with".  Stolen directly from gwoo's slides, here's an example of it:
{% codeblock lang:php %}
<?php 
class Post extends AppModel { 
var $hasAndBelongsToMany = array( 
 ?Tag? => array( 
 ?className? => ?Tag?, 
 ?with? => ?TaggedPost?, 
 ) 
 ); 

    function beforeSave() { 
         if(!empty($this->data[?Tag?])) { 
$this->TaggedPost->save($this->data[?Tag?]); 
         } 
    } 
} 
?>
{% endcodeblock %}
So what is the "with" parameter really for?  It's nothing more than a convenience parameter that lets you apply a label to the name of your join table, so you don't have to call it by it's ugly name, in this case PostTags.  Want to see it in action?
{% codeblock lang:php %}
<?php 
class PostsController extends AppController { 
var $name = ?Posts?; 
function tags() { 
$this->set(?tags?, $this->Post->TaggedPost->findAll()); 
} 
} 
?>
 
<?php 
foreach ($tags as $tag) : 
echo $tag[?Post?][?title?]; 
echo $tag[?Tag?][?name?]; 
echo $tag[?TaggedPost?][?date?]; 
endforeach; 
?>
{% endcodeblock %}
It's little touches like that, unseen by a lot of developers, that makes CakPHP just a little bit easier to use with each passing day.  You can download gwoo's slides <a href="http://www.cakephp.org/files/OCPHP.pdf">here</a>.</p>
