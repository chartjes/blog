--- 
layout: post
title: Run-up To php|works and some AJAX fun
date: 2006-09-12
---
<p>
Ah, only one more day of work (today) then I'm off to <a href="http://www.phparch.com/works">php|works</a> for three days, and hopefully not embarassing myself during my talk "What Can PHP Learn From Rails".  I hope to run into some people I met before and make some new friends.  It's weird going to a conference where you really don't know anyone and no co-workers are coming with you.  Luckily I'm not shy, so I'm sure I'll make some friends while I'm there.
</p>
<p>
I spent some time yesterday adding some code to the stats reporting system I created for <a href="http://www.verticalscope.com">work</a> to display an animated graphic (stolen from <a href="http://ajaxpatterns.org">AjaxPatterns</a>, a site I find myself going to more and more as I expand my l33t skillz to include practical Ajax stuff).  Using the Yahoo YUI, here's all the javascript code I'm using to make it happen:
{% codeblock lang:javascript %}
<script type="text/javascript">

	// Object that handles response from XmlHttpRequest
	var responseObj = {
		success: function (o) {
			YAHOO.util.Dom.setStyle("progress", "visibility", "hidden");
			YAHOO.util.Dom.setStyle("hiddenDIV", "visibility", "visible");
			response = o.responseText;
			YAHOO.util.Dom.get ("hiddenDIV").innerHTML = response;
		},
		
		failure: function (o) {
			alert ("ERROR -- Could not get data for your report!");
		}
	}
	
	// process request to get page views information
		
	function getpageviews(field, start_date, finish_date) {
		YAHOO.util.Dom.setStyle("hiddenDIV", "visibility", "hidden");
		YAHOO.util.Dom.setStyle("progress", "visibility", "visible");
		YAHOO.util.Connect.asyncRequest('GET', "/verticalscope_stats/reports/getpageviews/" + field + "/" + start_date + "/" + finish_date, responseObj);
	}
	
	YAHOO.util.Dom.setStyle('progress", "visibility", "visible");
	getpageviews("page_views", "< ?php echo $start_date ?>", "< ?php echo $finish_date ?>");
	
</script>
{% endcodeblock %}
</p>
<p>
This example is from a report that scrapes Google Analytics and then presents the data.  I wish I could say I was smart enough to figure out the Google Analytics stuff on my own, but I wasn't.  It's a made-for-CakePHP solution and you can find it <a href="http://www.thinkingphp.org/2006/06/19/google-analytics-php-api-cakephp-model">here at ThinkingPHP</a>.  Man, I love it when people smarter than me have figured stuff out. ;)</p>
