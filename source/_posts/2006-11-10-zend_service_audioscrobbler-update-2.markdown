--- 
layout: post
title: Zend_Service_Audioscrobbler Update
author: Chris Hartjes
date: 2006-11-10
---
<p>
Work has been moving a lot slower on this than I would have liked for a number of reasons, mostly family related as my wife's return to the working world has meant a good portion of the time I used to devote to my various side projects is now devoted to doing things like making lunches for my daughter and helping to prepare dinner for the next day.  So I don't have the time I used to.
</p>
<p>
Any how, in a <href ="http://www.littlehart.net/atthekeyboard/2006/09/28/zend_service_audioscrobbler-update/">previous posting I had talked about how the work on my Last.fm/Audioscrobbler plugin had been going.  I've come a long way since then, and only have one more major category of functions to write the unit tests and accompanying code (notice that it's tests first, code second in true agile fashion).  After a bunch of suggestions, I've reworked the code and I think I've made it really simple for me to add new functionality.  Here's what I'm talking about:
</href></p>
{% codeblock lang:php %}
	/**
	*
	* Private method that queries REST service and returns SimpleXML response set
	* @param string $service name of Audioscrobbler service file we're accessing
	* @param string $params parameters that we send to the service if needded
	* @return SimpleXML result set
	*/
	private function getInfo($service, $params = NULL)
	{
		$service = (string) $service;
		$params = (string) $params;

		try {   
            $request = $this->_rest->restGet($service, $params);
            
			if ($request->isSuccessful()) {
				$response = simplexml_load_string($request->getBody());
				return $response;
            } else {
				if ($request->getBody() == 'No such path') {
					throw new Zend_Service_Exception('Could not find: ' . $dir);
				} else if ($request->getBody() == 'No user exists with this name.') {
					throw new Zend_Service_Exception('No user exists with this name.');
				} else {
					throw new Zend_Service_Exception('The REST service ' . $service . ' returned the following status code: ' . $request->getStatus());
				}
			}
		}
		catch (Zend_Service_Exception $e) {
			throw ($e);
		}
	}
{% endcodeblock %}
<p>
That bit of code is what does all the heavy lifting for me. It uses the Zend_Service_Rest component to talk to Audioscrobbler's web services, and returns the results as a SimpleXML object.  Nice and simple.  A perfect example of what Zend Framework is trying to accomplish.
</p>
<p>
So, how do I query the web service?  I think an example of one of my unit tests will show you again how simple I've tried to make it.
</p>
{% codeblock lang:php %}
<?php

/**
 * @package    Zend_Service_Audioscrobbler
 * @subpackage UnitTests
 */

/**
 * Zend_Service_Audioscrobbler
 */
require_once 'Zend/Service/Audioscrobbler.php';

/**
 * PHPUnit test case
 */
require_once 'PHPUnit/Framework/TestCase.php';

/**
 * @package    Zend_Service_Audioscrobbler
 * @subpackage UnitTests
 */
class Zend_Service_Audioscrobbler_TagDataTest extends PHPUnit_Framework_TestCase
{
    public function testGetTopTags()
    {
        try {
            $as = new Zend_Service_Audioscrobbler();
            $response = $as->tagGetTopTags();
            $this->assertNotNull($response->tag);
        } catch (Exception $e ) {
                $this->fail("Exception: [" . $e->getMessage() . "] thrown by test");
        }
    }
    
    public function testGetTopArtists()
    {
         try {
                $as = new Zend_Service_Audioscrobbler();
                $as->set('tag', 'Rock');
                $response = $as->tagGetTopArtists();
                $this->assertNotNull($response->artist);
                $this->assertEquals($response['tag'], strtolower($as->get('tag')));
            } catch (Exception $e ) {
                    $this->fail("Exception: [" . $e->getMessage() . "] thrown by test");
            }       
    }
    
    public function testGetTopTracks() 
    {
        try {
            $as = new Zend_Service_Audioscrobbler();
            $as->set('tag', 'Rock');
            $response = $as->tagGetTopTracks();
            $this->assertNotNull($response->track);
            $this->assertNotNull($response->artist);
            $this->assertEquals($response['tag'], strtolower($as->get('tag')));
        } catch (Exception $e) {
            $this->fail("Exception: [" . $e->getMessage() . "] thrown by test");
        }
    }
    
}

?>
{% endcodeblock %}
<p>
I can't stress enough that I've really come around to the idea of that simple is always better, and if you want people to actually use what you've written you need to make it easy to use.  I hope to get the unit tests all done in the next week, and then write up some documentation on how to use the component.  After that, I'll send something to the fw-general mailing list announcing the fruits of my labours and people should take a look at the component.
</p>
