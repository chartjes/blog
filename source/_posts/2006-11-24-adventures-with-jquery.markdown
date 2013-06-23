--- 
layout: post
title: Adventures with jQuery
date: 2006-11-24
author: Chris Hartjes
---
Man, I never realized that I could actually learn to enjoy Javascript.  It looks just like PHP or even *gasp* Ruby code to me at times. :)

For my <a target="_blank" href="http://www.mustique-island.com">current paid side project</a> I've been using <a target="_blank" href="http://www.jquery.com">jQuery</a> to do some cool transformational effects.  On the page that shows the details for a villa, there's a little section, sort of a sidebar, that has things like the number of rooms, price, etc.  Visitors are then allowed to share the information by sending an email.

So, being a guy who always wants to learn I said "Hell, lemme whip up some Ajax goodness so that we don't have to do any page refreshes."  Then I said "How the hell do I do that with jQuery any way."  Long story short,  I got it to work.  I'm finally getting the hang of this stuff.  How easy was it?  Lemme show you:

First, I put all the different divs that will be displayed into the main page. Perhaps this is sloppy, but I'm just a beginner at this.  I then went to the style sheet for that particular page and added in:

{% codeblock lang:css %}
#email {
    display: none;
}

#email_thankyou {
    display: none;
}
{% endcodeblock %}
That made sure those two divs wouldn't show up until I turned them on.? Then, I created an href of the style <a xhref="javascript: foo();"> in a successful effort to avoid having the page scroll up to the top when they click on the link.? Then, we added in the following jQuery magic:

{% codeblock lang:javascript %}

function shareVilla() {

$("#details").hide("fast");

$("#email").fadeIn("slow"));

}

{% endcodeblock %}

Man, I love helper functions that actually read like English.

So then I made sure to hack an existing form validation script to then use some Ajax and post the data to an external PHP script that will send the email.? Here's what I added in, again in jQuery style:

{% codeblock lang:javascript %}

$.post("foo.php",
{ send_to: document.res_form.send_to.value,
email: document.res_form.email.value,
from: document.res_form.from.value,
your_email_address: document.res_form.your_email_address.value,
textarea: document.res_form.textarea.value,
villa_description: document.res_form.villa_description.value,
villa_url: document.res_form.villa_url.value},
function(){
$("#email").hide("fast");
$("#email_thanks").fadeIn("slow");
});

{% endcodeblock %}

Again, I find that code to be very readable which means I can actually go back to it later and figure out what it was doing. So, it works:? content fades in and out, data gets posted to an external script, so all that's left is to test to make sure that the emails actually do get sent out.

A tip of my hat to John Resig for creating a great, compact Javascript library.? Steal from the best, I always say.</a>
