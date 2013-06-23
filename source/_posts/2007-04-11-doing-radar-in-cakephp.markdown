--- 
layout: post
title: Doing RADAR in CakePHP
date: 2007-04-11
author: Chris Hartjes
---
<p>Okay, time for some code samples to boost traffic to my site.  In a previous posting I talked about the idea of <a href="http://www.littlehart.net/atthekeyboard/2007/04/04/keep-an-eye-on-your-radar/">RADAR</a>, or RESTful Application, Dumb-Ass Recipient.  So, wanting to see if I could put it into use, I decided to do the following for a new application:
<ul>
<li>Have the core of the application provide data via a REST service</li>
<li>For the web part of it, create controller / action pairs that call the REST service and pass the output onto the views</li></ul>
I'm hoping that some of the other programmers in the league (there are a few) get interested in using the REST API I've put together and build off of it.  The API is in place, so they can build their own apps around it.  Should be an interesting experiment anyway.
</p>
<p>
So, some code examples of building CakePHP apps the RADAR way:
{% codeblock lang:php %}
class IndexController extends AppController
{
    var $name = 'Index';
    var $uses = array('Game', 'Schedule');

    function index()
    {
        uses('XML');
        $game = new Game();
        $week = $game->getMaxWeek();

        // Pass these variables to the view
        $standings =& new XML($this->requestAction('/rest/standings/' . $week , array('return')));
        $schedule =& new XML($this->requestAction('/rest/schedule/' . $week, array('return')));
        $results =& new XML($this->requestAction('/rest/results/' . $week, array('return')));
        $this->set('results', $results);
        $this->set('schedule', $schedule);
        $this->set('standings', $standings);
        $this->set('week', $week);
    }
}
{% endcodeblock %}
This is the controller for the "portal" page of the new web site I'm working on.  Since I don't have access to PHP 5 for this project, I have to use the built-in XML object instead of SimpleXML (curse you, PHP 4).  The key here is the use of requestAction to hit my REST API and return the response, and then pipe that response into an XML object, that in turn gets passed to the view.  Since I like my clean URL's, I'm using the same trick I used before in the REST controller's so I can do http://host/rest/results and get it to spit back XML:
{% codeblock lang:php %}
    /**
     * REST service for return games for the requested week
     *
     * @param integer $week
     */
    function results($week)
    {
        $games = new Game();
        $this->set('results', $games->getWeeklyResult($week));
        $this->set('week', $week);
    }

    /**
     * REST service for returning schedule for particular week
     *
     * @param integer $week
     */
    function schedule($week) {
        $team = array("a01" => "COU", "a02" => "CAP", "a03" => "TRI", "a04" => "BUF",
              "a05" => "MCM", "a06" => "WMS", "a07" => "PHI", "a08" => "BOW",
              "a09" => "STL", "a10" => "PAD", "a11" => "POR", "a12" => "LAW",
              "n01" => "SDQ", "n02" => "CSP", "n03" => "MIN", "n04" => "CAJ",
              "n05" => "BUZ", "n06" => "HAG", "n07" => "DTR", "n08" => "COL",
              "n09" => "SPO", "n10" => "SEA", "n11" => "MAD", "n12" => "CRE");

        $schedule = new Schedule();
        $this->set(compact('week', 'team'));
        $this->set('results', $schedule->get($week));
    }

    /**
     * Output standings based on the week passed into it
     *
     * @param integer $week
     */
    function standings($week)
    {
        $divisions = array('AC West' => array("STL" => "St. Louis Rivermen", "PAD" => "Palo Alto Devils", "POR" => "Portland Gryphons", "LAW" => "Los Angeles Wildmen"),
                          'AC Central' => array("MCM" => "Motor City Marauders", "WMS" => "Williamstown Thunder", "PHI" => "Philadelphia Phantasm", "BOW" => "Bowling Green Bandits"),
                          'AC East' => array("COU" => "Chicago Cougars", "CAP" => "Capital City Fruit Bats", "TRI" => "Tri-State Traffic", "BUF" => "Buffalo Thunderherd"),
                          'NC West' => array("MAD" => "Monrovia Madness", "SEA" => "Seattle Rainers", "SPO" => "Spokane Chiefs", "CRE" => "Crescent City Redwoods"),
                          'NC Central' => array("BUZ" => "Boston Buzzards", "COL" => "Colorado Corsairs", "HAG" => "Habana Gigantes", "DTR" => "Detroit Rangers"),
                          'NC East' => array("CSP" => "Casper Ghosts", "MIN" => "Minnesota Snow Bears", "SDQ" => "San Diego Quakes", "CAJ" => "Carolina Cajuns")
                          );
        $standings = new Standings();
        $standings->getData($week);

        foreach ($divisions as $divisionName => $divisionTeams) {
            $divisionStandings[$divisionName] = $standings->getDivisionalStandings($divisionTeams);
        }

        $this->set('divisionStandings', $divisionStandings);
    }
{% endcodeblock %}
I'm planning on making the index action for the REST controller point to documentation on how to actually use it, which I think is a nice touch.
</p>
<p>
Okay, so now one of the views using the XML object.  Again, I think it's such an ugly hack because I can't use SimpleXML.  Nate has discussed with me the possibility of trying to make something built-in to CakePHP that uses a SimpleXML-like interface so that it will work in PHP 4 as well.  We shall see...
{% codeblock lang:php %}
<br /><br />
<center>Standings as of week < ?php echo $week ?><br /><br /></center>
<?php
$standings = $standings->child('standings');
$divisionalStandings = $standings->children('division');
?>
<center>
<table>
    <tr>
        <td>< ?php echo $this->renderElement('divisional_standings', array('division' => $divisionalStandings[0])) ?></td>
        <td>< ?php echo $this->renderElement('divisional_standings', array('division' => $divisionalStandings[3])) ?></td>
    </tr>
    <tr>
        <td>< ?php echo $this->renderElement('divisional_standings', array('division' => $divisionalStandings[1])) ?></td>
        <td>< ?php echo $this->renderElement('divisional_standings', array('division' => $divisionalStandings[4])) ?></td>
    </tr>
    <tr>
        <td>< ?php echo $this->renderElement('divisional_standings', array('division' => $divisionalStandings[2])) ?></td>
        <td>< ?php echo $this->renderElement('divisional_standings', array('division' => $divisionalStandings[5])) ?></td>
    </tr>
</table>
</center>
{% endcodeblock %}
That's the main view for doing the standings, and it's done as an element called in my main index view.  Now, here's the view that actually generates the standings for a particular division:
{% codeblock lang:php %}
<table>
    <tr>
        <th><b>< ?php echo $division->attributes['name'] ?></b></th>
        <th><b>W</b></th>
        <th><b>L</b></th>
        <th><b>Pct</b></th>
        <th><b>GB</b></th>
    </tr>
<?php foreach ($division->children('team') as $team) : ?>
    <?php
    $name = $team->child('name');
    $w = $team->child('w');
    $l = $team->child('l');
    $gb = $team->child('gb');
    $pct = $team->child('pct');
    ?>
    <tr>
        <td>< ?php echo $name->value ?></td>
        <td align='right'>< ?php echo $w->value ?></td>
        <td align='right'>< ?php echo $l->value ?></td>
        <td align='right'>< ?php echo sprintf("%0.3f", $pct->value) ?></td>
        <td align='right'>< ?php echo $gb->value ?></td>
    </tr>
<?php endforeach; ?>
</table>
{% endcodeblock %}
</p>
<p>
So, there you have it!  Remember, the idea of RADAR is that you have a REST service at the core of your application, and then you provide a "proxy" for dumb clients like browsers that only understand HTML natively.  That way you make your application it's own API, and everything else is just clients that hang off the API.  As an example, I could build a plugin for the sidebar of my <a href="http://www.littlehart.net/attheballpark">baseball blog</a> that shows the standings for the division my team is in.  I could hit the REST service, then manipulate the results via XML and spit it out.  
</p>
<p>
I hope the example above gives you a different perspective on putting together your application.
</p>

