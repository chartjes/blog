--- 
layout: post
title: A Simple CouchDB Datasource
---
<p>
Yes, my waffling continues.  But this time it is NOT with respect to what editor to use, as <a href="http://www.vim.org">the one true editor</a> has been configured in such a way to make my life easier.  I have a personal project that I have been waffling about building in Python (first as a Django app, now maybe as a web2py app) or in CakePHP, since I would probably be most productive building out something quickly using it.
</p>
<p>
Since I'm in a CakePHP phase right now, I decided to start building out some of the components I would need to make the side project work.  One of those components is the use of <a href="http://couchdb.apache.org">CouchDB</a> as the database.  Since non-relational databases are all the hawtness right now (and <a href="http://twitter.com/janl">Jan Lehnardt</a> is such an awesome guy) I decided the best way to learn it's use is to store search results by users to my site (no hints on what I'm doing).  I figured the best way to do this was to create a CouchDB datasource, add it to my application, and then create models that would use the datasource.  
</p>
<p>
While I suggest that you visit the CouchDB website for more info on what it is and how to use it, here's a quick summary:  CouchDB is a non-relational datastore that you communicate with using views written in Javascript, and it returns any records that match your view as JSON-formatted data.  Very simple when you think of it, but also very powerful.
</p>
<p>
I must emphasize that the code is very raw and not fully tested.  Written using PHP 5.2.9 and Cake 1.2.bleeding.edge. First, the data source:
{% codeblock lang:php %}
< ?php

/**
 * Datasource for connecting to CouchDB
 *
 * @author Chris Hartjes
 */
class CouchDbSource extends DataSource {
	public $description = 'CouchDB Data Source';
	public $host = 'localhost';
	public $port = 5984;
	public $error_number = null;
	public $error_message = null;
	public $headers = null;
	public $body = null;

	public function __construct($config) {
		parent::__construct($config);	

		if (!empty($this->config['host'])) {
			$this->host = $this->config['host'];	
		}

		if (!empty($this->config['port'])) {
			$this->post = $this->config['port'];
		}
	}

	public function fullTableName() {
		return false;
	}
	
	/**
	 * Method that sends data to the CouchDB server
	 *
	 * @param $method string GET, POST, PUT or DELETE
	 * @param $url string URL you are trying to send to
	 * @param $post_data string optional data to be posted
	 * @return string
	 */
	public function send($method, $url, $post_data = NULL) {
		$s = fsockopen($this->host, $this->port, $this->error_number, $this->error_message);

		if (!$s) {
			return false;
		}

		$request = "{$method} {$url} HTTP/1.0\r\nHost: {$this->host}\r\n";

		if ($post_data) {
			$request .= "Content-Length: " . strlen($post_data) . "\r\n\r\n";	
			$request .= "{$post_data}\r\n";
		} else {
			$request .= "\r\n";	
		}

		fwrite($s, $request);

		$response = "";

		while (!feof($s)) {
			$response .= fgets($s);	
		}

		list($this->headers, $this->body) = explode("\r\n\r\n", $response);

		return $this->body;
	}
}
?>
{% endcodeblock %}
I warned you that it was very simple.
</p>
<p>
So, if you want to use the datasource, the first thing to do is add an entry to your APP/config/database.php file with all the pertinent configuration info:
{% codeblock lang:php %}
< ?php
class DATABASE_CONFIG {

	var $couchdb = array(
		'datasource' => 'couchdb',
		'host' => 'localhost',
		'port' => 5984
	);
}
?>
{% endcodeblock %}
<br />
CouchDB by default runs on port 5984, but like most flexible applications it lets you change that port if you need to.  That's really all the configuration info you'll need.
</p>
<p>
So next up is configuring a model to use it. 
{% codeblock lang:php %}
< ?php

class Search extends AppModel {
	public $name = 'Search';
	public $useDbConfig = 'couchdb';	
	public $useTable = null;

	public function send($method, $url, $post_data = NULL) {
		return $this->getDataSource()->send($method, $url, $post_data);	
	}
}

?>
{% endcodeblock %}
Thanks to <a href="http://twitter.com/jperras">Joel Perras</a> for helping me dig through the CakePHP internals in order to figure out the best way to get my model to speak to the datasource.  And pointing out my stupid mistake that caused CakePHP's automodel magic to bite me in the ass.
</p>
<p>
So how do you actually use this thing.  Here's an example of asking CouchDB to give you a listing of all documents available on the server:
{% codeblock lang:php %}
APP/controllers/searches_controller.php
< ?php

class SearchesController extends AppController {
	public function show_all() {
		$this->layout = 'ajax';
		$response = $this->Search->send('GET', '/searches/_all_docs');
		$this->set(compact('response'));
	}
}

?>

APP/views/searches/show_all.ctp

< ?= $response ?>
{% endcodeblock %}
</p>
<p>
In my case, the view spit out a nice string that looked like this:
{% codeblock lang:javascript %}
{"total_rows":1,"offset":0,"rows":[ {"id":"e2ffaae4df81b66c3d8386b75be71aa3","key":"e2ffaae4df81b66c3d8386b75be71aa3","value":{"rev":"1-71594714"}} ]}
{% endcodeblock %}
</p>
<p>
So there you have it.  If you want to do more work with this datasource, I suggest you take a look at <a href="http://wiki.apache.org/couchdb/Getting_started_with_PHP">this link on the CouchDB wiki</a> about using PHP with CakePHP.   It could use some work to add in convenience methods for adding, deleting and finding specific records but it's a good start I think.
</p>
