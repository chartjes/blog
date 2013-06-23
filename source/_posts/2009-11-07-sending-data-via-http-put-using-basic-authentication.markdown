--- 
layout: post
title: Sending data via HTTP-PUT using Basic Authentication
---
<p>(This is another problem I solved with the help of <a href="http://stackoverflow.com"</a>Stack Overflow</a> and some <a href="http://en.wikipedia.org/wiki/Rubber_duck_debugging">rubber duck debugging</a>)
</p>
<p>
While cleaning up some code I noticed a function that was sending data via an HTTP-PUT had stopped working.  A classic example of code "accidentally working".  So, this was the perfect opportunity to (a) write a test to verify that it worked and (b) clean up the code so that it was doing the job properly.  It had been using cURL, but I was using PHP streams elsewhere so I decided to be consistent.
</p>
<p>
So here's what we had to do:
<ul>
<li>Pass the code a URL of where the file was going to end up on the eXist DB server</li>
<li>Pass the name of the temporary file that contained the info</li>
<li>Send the file via HTTP-PUT to eXist, along with the username and password it requires.</li>
</ul>
</p>
<p>
The old code was sending the username and password as part of the URL, but that simply was not working any more.  Why it stopped working isn't all that important except to say that passing the username and password the *proper* way, which is via the HTTP header in the request, is the correct way to go.
</p>
<p>
So, I googled around, looked at my existing code (including an <a href="http://www.littlehart.net/atthekeyboard/2008/01/11/how-to-http-put-a-file-somewhere-using-php/">old blog post</a>) I tried a few things and just couldn't get it to work.  The problem?  I kept getting a "401 Authorization denied" message.  I was positive I was sending the header in the correct format.  So, I asked Stack Overflow to help me while I looked at the code with my trusty stuffed Grumpy Dwarf doll (you know, from the Disney Movie) in my lap looking at the screen while I went over the code.
</p>
<p>
You know, I never figured that "rubber duck debugging" worked, but in this instance by explaining what I'm doing I figured out a few things:
<ul>
<li>Don't blindly trust code examples you find on the internet</li>
<li>Sometimes taking the time to explain how something is supposed to work someone actually makes it easier for you to figure it out.</li>
</ul>
</p>
<p>
Lo and behold, I <a href="http://stackoverflow.com/questions/1691530/sending-a-file-via-http-put-in-php">figured it out</a>.  I'll repost the code here too:
<br />
{% codeblock lang:php %}
$params = array(
    'http' => array(
        'method' => 'PUT',
        'header' => "Authorization: Basic " . base64_encode($this->ci->config->item('ws_login') . ':' . $this->ci->config->item('ws_passwd')) . "\r\nContent-type: text/xml\r\n",
        'content' => file_get_contents($tmpFile)
             )
         );
$ctx = stream_context_create($params);
$response = @file_get_contents($url, false, $ctx);

return ($response == '');
{% endcodeblock %}
</p><p>
My mistake?  For some reason unbeknownst to me I was passing an array of values as the header.  Dunno why I did it, must've got it from an example somewhere.  Now I have code that successfully sends my file to eXist via HTTP-PUT.  The only thing I do not like is that I have to suppress the output of file_get_contents() because it throws a warning while also reporting the successful 201 HTTP response code.  Perhaps there is another way to do it, but I know with 100% certainty that this code does work.
</p>
