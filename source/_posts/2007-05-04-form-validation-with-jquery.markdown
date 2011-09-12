--- 
layout: post
title: Form Validation with jQuery
date: 2007-05-04
author: Chris Hartjes
---
<p>Now that I have to actually design interfaces for other people, I am learning the finer details of Javascript.  Specifically, I'm using <a href="http://jquery.org">JQuery</a> as my library of choice.  I won't go into why I'm using, just go to the site and see it for yourself.  One of the things I've had to build recently is a playlist editor for the IPTV project.  I decided to be user-friendly for once, and make it Ajax-powered.  So this meant a lot of work creating small little actions in my Zend Framework code to accept form posts, etc.  Still cleaning things up, but I wanted to share some of the coolness from using a <a href="http://www.malsup.com/jquery/form/">jQuery form plugin </a>.</p>
<p>
So, never having really done any Javascript form validation (I know you're shocked) I unleashed my inner "programmer" to go and hack away at it so I can figure it out, then call back my inner "developer" to make the code elegant and compact.  It took me all morning but I figured it out thanks to Google and just hacking away at it.  One of the neat things about Javascript is that it supports the ability to dynamically define functions in your code.  With it's extensive use of callbacks, jQuery leverages this to the hilt. I believe this is what the Ruby crowd refers to as "blocks and closures".  Please correct me if I'm wrong.  Okay, so here's some code that illustrates how I was doing validation of the form:
<br />
{% codeblock lang:javascript %}
function saveBinary(playlist) {
    var options = {
        beforeSubmit: validateBinary,
        success: function() {
            $("div#media").load("/elostv/getBinaries/playlist/" + playlist);
            $("div#editMedia").html('<div align = "center"><br />Added media </div>'
                + '<a onclick="addBinaries(\'' + playlist + '\')">Add media</a>');
        }
    }

    $("#addMedia").ajaxSubmit(options);
}
{% endcodeblock %}
</p>
<p>
Isn't that nice?  Compact, simple, readable.  All the things a developer strives for.  In summary, the .ajaxSubmit() method lets you define a bunch of callback functions as part of the submission process.  The 'beforeSubmit' is used to handle validation, while the 'success' is stuff that gets triggered if the form submission comes back ok.  Here's the validation code (again, very simple and I'll save the advanced regex matching for the beta).  Here's the validation callback:
<br />
{% codeblock lang:javascript %}
function validateBinary(formData, jqForm, options) {
    var allFields = true;

    for (var i=0; i < formData.length; i++) {
        if (!formData[i].value) {
            allFields = false;
        }
    }

    if (!allFields) {
        alert('Please fill out every field in the form!');
        return false;
    }
}
{% endcodeblock %}
</p>
<p>
Now that I've done this once, I imagine the second time around will be much easier.  Trying to keep things simple when you're on a very tight schedule can be difficult, and I think I've done that despite a few missteps while trying to figure out what jQuery plugin to use to handle my form stuff.</p>
