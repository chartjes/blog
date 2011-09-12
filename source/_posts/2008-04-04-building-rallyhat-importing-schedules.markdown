--- 
layout: post
title: "Building Rallyhat: Importing Schedules"
author: Chris Hartjes
---
<p>I continue to be impressed with <a href="http://www.djangoproject.com">Django</a> as I build out Rallyhat.  I have an extreme alpha version working on my laptop, minus the Yahoo! Maps stuff I've been playing around with.  The biggest task was populating my database with the schedules for all the baseball teams.  I thought I'd share what the import script looks like:
</p>
<p>
{% codeblock lang:python %}
#!/usr/bin/env python
from django.core.management import setup_environ
import settings
setup_environ(settings)
from rallyhat.www.models import Team
from rallyhat.www.models import Game
from rallyhat.www.models import Location
from rallyhat.www.models import Sport

from datetime import date

import csv, urllib, time

s = Sport.objects.get(name='Major League Baseball')
teamSchedules = Team.objects.all()

for teamSchedule in teamSchedules:
    scheduleFile = teamSchedule.schedule
    print "Importing games for " + str(teamSchedule.name)

    if scheduleFile != "":
        reader = csv.reader(urllib.urlopen(scheduleFile))

        for row in reader:
            teams = row[3].split(' at ')

            if len(teams) == 2:
                if Team.objects.filter(name=teams[1]).count() == 0:
                    print "Adding new team: " + teams[1]
                    homeTeam = Team(name=teams[1], sport=s)
                    homeTeam.save()
                else:
                    homeTeam = Team.objects.get(name=teams[1])

                if Team.objects.filter(name=teams[0]).count() == 0:
                    print "Adding new team: " + teams[0]
                    awayTeam = Team(name=teams[0], sport=s)
                    awayTeam.save()
                else:
                    awayTeam = Team.objects.get(name=teams[0])

                gameDate = time.strftime("%Y-%m-%d", time.strptime(row[0], "%m/%d/%Y"))
                startTime = time.strftime("%H:%M", time.strptime(row[2], "%I:%M %p"))

                # If this game doesn't exist, add it to the system
                if Game.objects.filter(home_team=homeTeam, away_team=awayTeam, game_date=gameDate, start_time=startTime).count() == 0:
                    locationCheck = Location.objects.filter(name=row[4]).count()

                    if locationCheck == 0:
                        print "Adding new location: " + row[4]
                        l = Location(name=row[4])
                        l.save()
                    else:
                        l = Location.objects.get(name=row[4])

                    locationId = l.id
                    g = Game(home_team=homeTeam, away_team=awayTeam, location=l, game_date=gameDate, start_time=startTime)
                    g.save()
{% endcodeblock %}
</p>
<p>
It's interesting to treat everything as an object after so many years of being in the PHP world where you can mix and match depending on what's been going on in your application.  I'm also amazed at how clear the code is.  There is some non-intuitive stuff in there, especially when dealing with the saving of model records.  It took me a while to figure out I could pass the object containing the model  as a parameter when saving a record for a model that it is associated with.
</p>
