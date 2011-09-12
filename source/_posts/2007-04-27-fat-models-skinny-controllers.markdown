--- 
layout: post
title: Fat Models, Skinny Controllers
date: 2007-04-27
author: Chris Hartjes
---
<p>I've become a convert to the design concept that says when you build something with an MVC pattern, you should have fat models and skinny controllers.  What does this really mean?  It means that you put as much of your business logic as you can into your models and all the controller should be doing is retrieving data from the model and passing it to the view.  Nice and simple, but a very powerful concept once you start doing it.</p>
<p>So, despite my problems using the RADAR concept for the <a href="http://www.ibl.org">Internet Baseball League</a> web site, I did do the models and controllers the way I wanted.  Here's what I'm talking about:
<br />
(Note the use of overriding the default table and database names.  CakePHP lets you use legacy databases, and don't let anyone tell you otherwise)
{% codeblock lang:php %}
/**
 * Model for accessing schedule table
 *
 * @author Chris Hartjes
 */

class Schedule extends AppModel
{
    var $name = 'Schedule';
    var $useTable = 'sched2007';
    var $useDbConfig = 'stats';

    function get($week) {
        $scheduledGames = array();
        $team = array("a01" => "BUF", "a02" => "COU", "a03" => "HAG", "a04" => "TRI",
                    "a05" => "BOW", "a06" => "MCM", "a07" => "PHI", "a08" => "WMS",
                    "a09" => "LAW", "a10" => "PAD", "a11" => "POR", "a12" => "STL",
                    "n01" => "CSP", "n02" => "COL", "n03" => "MIN", "n04" => "SDQ",
                    "n05" => "BUZ", "n06" => "CAJ", "n07" => "DTR", "n08" => "SCS",
                    "n09" => "CRE", "n10" => "MAD", "n11" => "SEA", "n12" => "SPO");
        $results = $this->findAll("home LIKE 'a%' AND week = " . (int)$week);
        $data = array();

        foreach ($results as $result) {
            $home = $team[$result['Schedule']['home']];
            $away = $team[$result['Schedule']['away']];
            $data[$home] = array('home' => $home, 'away' => $away);
        }

        asort($data);

        foreach ($data as $home => $matchup) {
            $scheduledGames[$home] = $matchup;
        }

        $results = $this->findAll("home LIKE 'n%' AND week = " . (int)$week);
        $data = array();

        foreach ($results as $result) {
            $home = $team[$result['Schedule']['home']];
            $away = $team[$result['Schedule']['away']];
            $data[$home] = array('home' => $home, 'away' => $away);
        }

        asort($data);

        foreach ($data as $home => $matchup) {
            $scheduledGames[$home] = $matchup;
        }
        
        return $scheduledGames;
    }
}
{% endcodeblock %}
</p>
<p>
Now *that* is a fat model.  I'm manipulating all the business logic within my model and returning it.  Now, here's what the controller looks like:
<br />
<br />
{% codeblock lang:php %}
/**
 * Controller for displaying individual weeks
 * of the IBL schedule
 *
 * @author Chris Hartjes
 */

class ScheduleController extends AppController
{
    var $name = 'Schedule';
    var $uses = array('Schedule', 'Game');
    var $layout = 'rosters';
    var $cacheAction = "1 day";

    function index($week)
    {
        $game = new Game();
        $week = (int)$week;

        if ($week == 0) {
            $week = $game->getMaxWeek();
        }

        $schedule = new Schedule();
        $this->set('schedule', $schedule->get($week));
        $this->set('week', $week);
        $this->set('maxWeek', $game->getMaxWeek());
        $this->set('scheduleWeek', $week);
    }

}
{% endcodeblock %}
</p><p>See, the schedule controller is nice and thin.  All it does is get the week as a parameter passed into it via the URL and then tells the model to give me all me the schedule for the week.  Simple, easy to understand and even easier to maintain.</p>
<p>
I know that sometimes these things don't make sense at first but once you actually use them...and then have to go and modify something you quickly realize just what advantage you are getting from it.  Try seeing if you can refactor your MVC-based app (CakePHP or otherwise) to have Fat Models and Thin Controllers.
</p>
