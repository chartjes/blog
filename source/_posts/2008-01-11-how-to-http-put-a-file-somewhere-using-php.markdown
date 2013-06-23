--- 
layout: post
title: How To HTTP-PUT A File Somewhere Using PHP
date: 2008-01-11
author: Chris Hartjes
---
<p>
A work project is getting close to 0.1 status.  Pretty underwhelming, I know.  One of the last 'milestones' for 0.1 is taking these wonderful XML documents that my web app creates (and stores in <a href='http://www.exist-db.org/'>eXist</a> and sends them to an internal web service that reads in the XML and breaks it apart for use by a wide variety of other company applications.  This web service will accept documents via an HTTP PUT (you know, GET, POST and it's neglected siblings PUT and DELETE) so I dug around a bit on the web (ignoring one cranky co-worker's complaints that real programmers read RFC's, or at least *know* what an RFC is) and put together some code</p>
<br /><br />
{% codeblock lang:php %}
	function _publish($service, $doc) {
		$params = array(
			'http' => array(
				'method' => 'PUT'));
		$context = stream_context_create($params);
		$fp = fopen($service, 'rb', false, $context);
		$response = fwrite($fp,file_get_contents($doc));
		
		if ($response === false) {
			return false;
		}

		// Pull out the status code from the header
		$metaData = stream_get_meta_data($fp);
		preg_match_all("/HTTP\/1\.[1|0]\s(\d{3})/", $metaData['wrapper_data'][0], $matches);
		$code = end($matches[1]);

		if ($code == 200) {
			return true;
		} else {
			return false;
		}
	}
{% endcodeblock %}
<p>
The only tricky thing here really is the use of the <a href="http://www.php.net/end">end</a> function to grab that last match of the status codes.  I got the code for doing the preg_match from <a href"http://www.jellyandcustard.com/2006/05/31/determining-if-a-url-exists-with-curl/">this site</a> and it seems to work just fine.  The reason to use end(...) as far as I can tell is to make sure that I only get the last match of the group.  Neat little trick and the link I posted demonstrates it.
</p>
<p>
I'm also quite proud that it's cURL free, as cURL seems to be the first option that most people use when doing this kind of thing.  There is some existing code that is using cURL that I *might* refactor to use the streams-driven stuff that I've been playing with.
</p>
