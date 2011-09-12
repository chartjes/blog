--- 
layout: post
title: Socket Servers Redux
---
<p>
It's always nice to beat a deadline at work, and I beat one by 2 hours for getting the alpha version of my <a href=http://www.pa-sportsticker.com/en/index.html>Sportsticker</a> XML stream parser done.  Looking back, I wasted a lot of time on a complicated procedure for parsing the stream when I should've kept it simple.  Luckily, I set it aside for a few hours on Wednesday and then spent Thursday looking for a simpler way to do it.  I found another example on <a href="http://www.devshed.com/c/a/PHP/Socket-Programming-With-PHP/">creating socket servers over at DevShed</a> and that did the trick.  Here's the quick algorithm for what I did.
</p>
<p>
<ul>
<li>Read in the stream one line at a time</li>
<li>If the current line is the start of a properly-formed XML block then grab what we've buffered and pass it to SimpleXML, then clear the buffer and start processing the string</li>
<li>If it's not the start of a properly-formed XML block then keep adding the data to the buffer</li>
</ul>
</p>
<p>Once I've got the XML, I parse through it and check the attributes to see if I've got the data I'm actually looking for, which is baseball boxscores from the AL and the NL.  I'll post the code early next week as I can't access if from home, cleaned up and free of any info that would compromise the company.  I take the info from the XML document (again, I can't say enough about how easy SimpleXML makes these things) and store them in a database. </p>
<p>The second part of the system are two scripts that spit out XML info based on the stuff I've stored in the database, and another developer at work is creating a Flash component that will read in that XML and display the info on our forum sites.  Should be very slick stuff.</p>
