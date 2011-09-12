--- 
layout: post
title: Multiple Form Defaults Using jQuery
---
<p>At <a href="http://www.xmlteam.com">work</a>, one of the projects I work on is an <a href="http://www.sportsstandards.org/sd/sportscaster">open source web service front end</a> for our Perl-based main application.  It has a front-end for it that uses Javascript to dynamically build a query to the web service.  I didn't write it, but I think it's kind of neat.  One of the things I was asked to do was create some code that allow users to define a series of default values for the (/me goes to count) 7 different forms that are in the front-end.  There had been some pre-existing code, but I decided it needed to be refactored to be a lot more simpler than the previous system.  After all, I was not writing this code for myself but for our clients.  They would definitely not be as familiar with the system as I would be, so simple is always better.
</p>
<p>
So, the trick was to figure out what pieces I was going to use to build this.  Since I am a <a href="http://jquery.com">jQuery</a> fan, I started searching for plugins to make it all work nice.  My research dug up the perfect tool: the <a href="http://www.keyframesandcode.com/resources/javascript/jQuery/demos/populate-demo.html">jQuery Form Population</a> plugin.  I know you'll follow the link and read it, but as a quick summary it is a plugin for allowing you to populate values in a form on the client side, meaning in Javascript, instead of the server side, which in this case would be everyone's favourite online whipping-boy PHP.</p>
<p>
Once I played around with the plugin (and actually read the documentation) I realized that the simple solution I wanted was at hand.  Let me show you what I did:
{% codeblock lang:javascript %}
function clearAllDefaults() {
	$('#searchDocumentsForm').clearForm();
	$('#searchDocumentsForm').populate(
		{
			'revision-control':'all',
			'priorities':'all',
			'content-returned':'metadata-only',
			'rendering-engine':'xslt',
			'query-debug':'false',
			'gateway-theme':'default',
			'stylesheet':''
			}, 
		{'reset-form':false, 'identifier':'name'}
		);

	$('#getDocumentsForm').clearForm();
	$('#getDocumentsForm').populate(
		{
			'rendering-engine':'xslt',
			'query-debug':'false',
			'gateway-theme':'default',
			'stylesheet':''
			}, 
		{'reset-form':false, 'identifier':'name'}
		);

	$('#searchEventsForm').clearForm();
	$('#searchEventsForm').populate(
		{
			'date-offset':0,
			'date-offset-span':1,
			'date-offset-midnight':1600,
			'sort-order':'asc',
			'content-returned':'metadata-and-scores',
			'rendering-engine':'xslt',
			'query-debug':'false',
			'gateway-theme':'default',
			'stylesheet':''
			}, 
		{'reset-form':false, 'identifier':'name'}
		);

	$('#getEventsForm').clearForm();
	$('#getEventsForm').populate(
		{
			'content-returned':'metadata-and-scores',
			'rendering-engine':'xslt',
			'query-debug':'false',
			'gateway-theme':'default',
			'stylesheet':''
			}, 
		{'reset-form':false, 'identifier':'name'}
		);
}

function setDefaults(defaultId) {
	for (var formId in defaults[defaultId]) {
		$('#' + formId).populate(defaults[defaultId][formId], {'reset-form':false, 'identifier':'name'});
	}	
}

function outputDefaultChoices() {
	document.write('<table width="200"><tr valign="top"><td width="100" nowrap><b>Default Selections:</b></td>');
	document.write('<td nowrap><input type="radio" name="defaultSet" value="none" checked onChange="clearAllDefaults();"/> none<br />');
	
	for (var myDefault in defaults) {
		document.write('<input type="radio" name="defaultSet" value="' + myDefault + '" onChange="clearAllDefaults();setDefaults(\'' + myDefault + '\');"/> ' + myDefault + '<br />');
	}

	document.write('</td></tr></table>');
}
{% endcodeblock %}
This is load-defaults.js.  It contains functions that I want to use to set the defaults.  I think it's pretty self-explanatory.  I would like a less-ugly way of implementing what I did in outputDefaultChoices(), so let me know if there is a better way.  
</p>
<p>
Up at the top of that code is where we are setting a bunch of defaults for when the form front-end is initially loaded.  The populate plugin accepts JSON containing not only the key-value pairs of form field name and value respectively, but also accepts a bunch of very useful options.  'reset-form':false tells the plugin to not simple reset the form when populating (we might not want to overwrite some existing values). 'identifier':'name' is a cool feature of the plugin that allows you to specify *how* you want the plugin to figure out how to map the field names you sent it already to the form itself.  Default is 'id' but much of the existing form did not have id fields for the form fields, so I figured it was less work for me to make the plugin figure it out. ;)
</p>
{% codeblock lang:javascript %}
/**
 * In order to create a set of defaults, you simply have to create
 * a JSON array of options in the following format
 *
 * defaults[<set name>] = {'<formid>':{<json pairs of fields and values>}}
 * 
 * defaults['favorites'] = {'searchDocumentsForm':{'team-keys':'l.mlb.com-t.18', 'fixture-keys':'general-news', 'date-window':'2400'}};
 * 
 * Adding in defaults for multiple forms is easy.  Here's an example
 * of setting the team-keys in both the searchDocuments and searchEvents forms
 *
 * defaults['multiple'] = {
 *	'searchDocumentsForm':{'team-keys':'l.mlb.com-t.17'},
 *	'searchEventsForm':{'team-keys':'l.mlb.com-t.17'}
 * }
 */

var defaults = new Array();

defaults['favorites'] = {
		'searchDocumentsForm':{
			'league-keys':'l.mlb.com', 
			'fixture-keys':'general-news', 
			'date-window':'2400',
			'publisher-keys':'sportsnetwork.com',
			'max-result-count':'5',
			'revision-control':'all',
			'priorities':'all',
			'content-returned':'metadata-only',
			'rendering-engine':'xslt',
			'query-debug':'false',
			'gateway-theme':'default',
			'stylesheet':''
			},

		'getDocumentsForm':{
			'doc-ids':'xt.9569941-recap', 
			'rendering-engine':'xslt',
			'query-debug':'false',
			'gateway-theme':'default',
			'stylesheet':''
			},

		'searchEventsForm':{
			'league-keys':'l.mlb.com', 
			'publisher-keys':'sportsnetwork.com',
			'max-result-count':'200',
			'date-offset':0,
			'date-offset-span':1,
			'date-offset-midnight':1600,
			'sort-order':'asc',
			'content-returned':'metadata-and-scores',
			'rendering-engine':'mvc-view',
			'query-debug':'false',
			'gateway-theme':'default',
			'stylesheet':'events'
			},

		'getEventsForm':{
			'event-keys':'l.mlb.com-2009-e.24850',
			'publisher-keys':'sportsnetwork.com',
			'content-returned':'metadata-and-scores',
			'rendering-engine':'mvc-view',
			'query-debug':'false',
			'gateway-theme':'default',
			'stylesheet':'events'
			}
		};
		
defaults['team-news'] = {
		'searchDocumentsForm':{
			'team-keys':'l.mlb.com-t.18', 
			'fixture-keys':'general-news,post-event-coverage,pre-event-coverage', 
			'date-window':'9600',
			'publisher-keys':'sportsnetwork.com',
			'max-result-count':'5',
			'revision-control':'latest-only',
			'priorities':'all',
			'content-returned':'metadata-only',
			'rendering-engine':'xslt',
			'query-debug':'false',
			'gateway-theme':'default',
			'stylesheet':'sportsml2html-listing'
			}
		};
		
defaults['standings'] = {
		'searchDocumentsForm':{
			'league-keys':'l.mlb.com', 
			'fixture-keys':'standings-by-division', 
			'date-window':4800,
			'max-result-count':1,
			'revision-control':'all',
			'priorities':'all',
			'content-returned':'all-content',
			'rendering-engine':'xslt',
			'query-debug':'false',
			'gateway-theme':'default',
			'stylesheet':'sportsmlt'
			}
		};
{% endcodeblock %}
<p>
This is the sample configuration file that we distribute with the application to show people how to use it.  Look, I even provided instructions at the top on how to use it!
</p>
<p>
Anyway, if you've been looking for a way to create multiple sets of defaults for your forms, switchable with the click of a button, I hope this code is useful to you.
</p></json></formid></set>
