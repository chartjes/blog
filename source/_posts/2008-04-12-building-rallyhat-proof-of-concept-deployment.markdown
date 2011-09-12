--- 
layout: post
title: "Building Rallyhat:  Proof-of-concept Deployment"
---
<p>Well, that went relatively well.  As a proof-of-concept for Google App Engine I decided to see what I could whip together today in between domestic duties, looking after the kids and praying that my wife gets better from her massive cold because I'm off to Vancouver tomorrow.
</p>
<p>So, I pushed the database for Rallyhat up into the cloud and wrote a super-simple front end just to see if I could do it.  You can take a quick peek at http://chrishartjes.appspot.com.  To get it to spit something out, you need 3 parameters:
<ul>
<li>home_team -- nickname for a baseball team (i.e. Yankees, Red Sox, Padres).  Don't forget to urlencode the spaces with a +</li>
<li>begin_date -- date in YYYY-MM-DD format</li>
<li>end_date -- date in YYYY-MM-DD format</li>
</ul>
</p>
<p>
It's a small start, but a start nonetheless.  Next step is to configure my app to use the dev version of Django, not the built in version.
</p>
