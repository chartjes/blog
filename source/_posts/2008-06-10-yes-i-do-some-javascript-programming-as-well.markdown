--- 
layout: post
title: Yes, I Do Some Javascript Programming As Well
author: Chris Hartjes
---
<p>(before I get into this I wanted to let people know that I will be going to <a href="http://www.zendcon.com/ZendCon08/public/content/home">ZendCon</a> to give my deployment talk.  I might be looking for a place to crash for a second night, so let me know if you're going and can hook me up)</p>
<p>
For a <a href="http://sportso.com">work project</a> I had to add in some Ajax functionality for a scoreboard feature, where users will enter scores for periods / quarters / innings and then the total score has to update automatically on the screen before the user wishes to save that scoring document.  So with some help from one of my online <a href="http://marcgrabanski.com/">javascript ninja associates</a> and Google searches, I got it all figured out, and thought I would share.
</p>
<p>
Here's a snapshot of the interface in question:
<img src="http://chrishartjes.com/sportso-scoreboard.png" alt="Sportso scoreboard interface" / width=532 height=183  />
</p><p>
The first thing I did was apply the same class name to the away "innings" and home "innings" form fields, so that $().serialize would be able to pull up all those fields.  That way, it wouldn't matter how many "inning" fields there might be.  The tricky thing I found out was that I need to wrap my $('.homePeriods').change() call in it's own function() call so that it would actually be loaded when the page was loaded as well.  I had no idea I needed to do that, and thanks to Marc for pointing it out.  If there is a better method, let me know.
<br />
{% codeblock lang:javascript %}
// Method used to automatically update total fields
// when editing individual periods
$(function(){ 
	$('.homePeriods').change(function(){
		var params = $('.homePeriods').serialize();
		var pArray = params.split('&');
		var homeTotal = 0;

		for (var i=0; i < pArray.length; i++) {
			var temp = pArray[i].split('=');
			var homePeriod = temp[1];
			// Cast value to an integer with this little hack
			homePeriod = homePeriod - 0;
			homeTotal += homePeriod;
		}

		$('#homeScoreTotal').replaceWith('<td class="period" id="homeScoreTotal"><input type="text" name="homeScoreTotal" value="' + homeTotal + '" maxlength="2" size="2" id="htotal" />');
	});

	$('.awayPeriods').change(function(){
		var params = $('.awayPeriods').serialize();
		var pArray = params.split('&');
		var awayTotal = 0;

		for (var i=0; i < pArray.length; i++) {
			var temp = pArray[i].split('=');
			var awayPeriod = temp[1];
			awayPeriod = awayPeriod - 0;
			awayTotal += awayPeriod;
		}

		$('#awayScoreTotal').replaceWith('<td class="period" id="awayScoreTotal"><input type="text" name="awayScoreTotal" value="' + awayTotal + '" maxlength="2" size="2" id="vtotal" />');
	});
});
{% endcodeblock %}
</p>
<p>
So, here's a small movie showing that in action.
<br />
<br />
[flv:http://www.archive.org/download/SportsoDynamicScoreboard/sportso-scoreboard.flv 533 400]
</p>
<p>I hope this helps out other people looking to add similar functionality to their site.</p>
