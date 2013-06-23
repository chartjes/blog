--- 
layout: post
title: CakePHP Pagination With A HABTM Relationship
date: 2007-12-11
author: Chris Hartjes
---
<p>There are usually lots of Has And Belongs To Many relationship questions on the CakePHP mailing list.  Since I am stupid about this stuff, I sought out Nate Abele and bugged him via IM until he agreed to give me an example of how to do this.  Thanks Nate!
{% codeblock lang:php %}
class Tag extends AppModel {
 
    var $hasAndBelongsToMany = 'Post';
   
    function paginate($conditions = null, $fields = null, $order = null, $limit = null, $page = 1, $recursive = null) {
        $tag = $conditions['tag'];
        unset($conditions['tag']);
 
        $this->hasAndBelongsToMany['Post'] = am(
            $this->hasAndBelongsToMany['Post'],
            compact('conditions', 'fields', 'order', 'limit', 'page')
        );
        return $this->findByName($tag);
    }
 
    function paginateCount($conditions = null) {
        $tag = $conditions['tag'];
        unset($conditions['tag']);
        $tmp = $this->hasAndBelongsToMany['Post'];
        $this->hasAndBelongsToMany['Post']['fields'] = array('id');
        $tag = $this->findByName($tag);
        $this->hasAndBelongsToMany['Post'] = $tmp;
        return count($tag['Post']);
    }
}
 
?>

<?php 
// Controller code
 
$data = $this->paginate('Tag', array('tag' => $tag));
// Where $tag = some tag name
{% endcodeblock %}
Okay, that's great but WHY does it work?  Normally, when you do pagination you have to pass it a bunch of different parameters so it knows what records you wish to include as part of the data set you want to paginate over.  In this example, you've already established that Tag HABTM Post.  In order for the pagination query to correctly pull out the Posts that are also associated with the Tag, you need to merge the parameters you passed in to your 'paginate' method so that the CakePHP data mapping functionality knows what associated records are to be included.  Then run your $this->findByName(...) and you're all set.</p>
