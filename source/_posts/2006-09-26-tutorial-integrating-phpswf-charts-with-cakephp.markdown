--- 
layout: post
title: "Tutorial: Integrating PHP/SWF Charts with CakePHP"
author: Chris Hartjes
date: 2006-09-26
---
<p>Many thanks to the CakePHP mailing list for pointing out some really dumb errors I made along the way getting this stuff to work.  It turns out that case-sensitivity does actually matter at time. :)
</p>
<p>
Okay, for a project at <a href="http://www.verticalscope.com">work</a> I was asked to add graphs to some of the reports I'd already created.  So I looked around for solutions for graphing in PHP and stumbled upon <a href="http://www.maani.us/charts/">PHP/SWF Charts</a> as a solution.  Basically, it comes in two parts:  a Flash movie that generates the charts for you and a PHP library that sends data to the Flash movie to create those great charts.
</p>
<p>
So, first thing I did was download the package from the PHP/SWF Charts site.  I then dumped everything into a /graphs directory in my web root.  Why?  Well, that's the only way I could get the thing working and I am a disciple who worships at the altar of Get It Done because there are other things I'd rather deal with.  I'm sure one of the CakePHP people who runs across this tutorial can correct things for me so it's all inside the framework itself.
</p>
<p>
Now, that the library is unzipped and in it's own directory, we go and start altering the code I need to make this work.   First thing I did was add a subdirectory to my app/views directory called graphs and added in users.thtml
{% codeblock lang:php %}
<?php
vendor('charts');
$chart['chart_data'] = array($header, $member_data, $visitor_data);
$chart['chart_type'] = 'stacked area';
$chart['axis_category'] = array('size' => 9);
$chart['chart_grid_h'] = array('thickness' => 1);
$chart['chart_grid_v'] = array('thickness' => 1);
SendChartData($chart);
?>
{% endcodeblock %} This code will pass the info I've passed to my view to the flash component.  This is the part that will spit out the chart, but I also had to add in some code to the main view for the report itself so the graph will show up

{% codeblock lang:php %}
<div align = "center">
	<br /><br />
	Users Online For Entire Network For Last 24 Hours
	<br /><br />
	< ?php vendor("charts") ?>
	< ?php echo InsertChart ('/verticalscope_stats/img/charts.swf', "/graphs/charts_library", '/verticalscope_stats/graphs/users/' . uniqid(rand(), true), 800, 250, 'FFFFFF') ?>
</div>
{% endcodeblock %}
As you can tell, I omitted a step above.  When I downloaded the charts package I stuck the charts.swf Flash movie in app/webroot/img so I can find it later.  The uniqid stuff is to make sure it doesn't get cached by your browser.
</p>
<p>
Okay, so now here's the code I created to pull results from our database, munge the data and pass it over to the view:
{% codeblock lang:php %}
class GraphsController extends AppController
{
	var $name = 'Graphs';
	var $uses = array('OnlineUser');
	
	public function users()
	{
		// create graph for charts based on users online for the past 24 hours
		$members = array();
		$visitors = array();
		$total_users = array();
		$header = array();
		$member_data = array();
		$visitor_data = array();
        
		$this->OnlineUser->recursive = -1;		
		$temp = $this->OnlineUser->findBySQL("SELECT MAX(ou_date) as max_ou_date FROM online_users");
		$max_ou_date = $temp[0][0]['max_ou_date'];		
		$result = $this->OnlineUser->findAll("DATE_SUB('$max_ou_date', INTERVAL 1 DAY) < = ou_date");
		
        foreach ($result as $data) {
            // Now we have to find the top value for each hour within
            // all the data for an hour
            $hour = date("H:00", strtotime($data['OnlineUser']['ou_date']));
            $site_id = $data['OnlineUser']['site_id'];

            if (!isset($members[$site_id][$hour])) {
                $members[$site_id][$hour] = 0; 
            }

            if ( $members[$site_id][$hour] < $data['OnlineUser']['members']) {
                $members[$site_id][$hour] = $data['OnlineUser']['members'];
            }

            if (!isset($visitors[$site_id][$hour])) {
                $visitors[$site_id][$hour] = 0;
            }

            if ( $visitors[$site_id][$hour] < $data['OnlineUser']['visitors']) {
                $visitors[$site_id][$hour] = $data['OnlineUser']['visitors'];
            }

		}

        // Phew, that's a lot of dating munging.  Okay, now we need to cycle through
        // the raw data and create totals for each hour
        $member_data = array( );
        $visitor_data = array( );

        foreach ($members as $site_id => $member) {
            foreach ($member as $hour => $count) {
                
                if (!isset($member_count[$hour])) $member_count[$hour] = 0;
                
                $member_count[$hour] += $members[$site_id][$hour];
            }
        }

        foreach ($visitors as $site_id => $visitor) {
            foreach ($visitor as $hour => $count) {
                if (!isset($visitor_count[$hour])) $visitor_count[$hour] = 0;
                
                $visitor_count[$hour] += $visitors[$site_id][$hour];
            }
        }

		$header[] = "";
		$member_data[] = "Members";
		$visitor_data[] = "Visitors";
        
        foreach ($member_count as $hour => $count) {
			$header[] = $hour;
			$member_data[] = $count;
			$visitor_data[] = $visitor_count[$hour];
		}

		$this->set('header', $header);
		$this->set('member_data', $member_data);
		$this->set('visitor_data', $visitor_data);
		$this->layout = 'ajax';
	}
}

?>
{% endcodeblock %}
</p>
<p>
So, I think that's all you need in order to get your code working and talking nicely with PHP/SWF charts.  I'll go over this stuff again to look for any errors and clear up anything that looks confusing.
</p>
