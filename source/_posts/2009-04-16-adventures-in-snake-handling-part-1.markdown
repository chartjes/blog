--- 
layout: post
title: Adventures In Snake Handling, Part 1
---
<p>Those of you who are loyal readers and follow my blog do know that I am starting to learn Python, with an angle towards making it the language that earns me my paycheque.  But that is a story for another day (and full of unrequited whining by me).  So, I've been doing some Python stuff here and there at work and since I had to update the schedule for my <a href="http://www.ibl.org">simulation baseball league</a> for the upcoming season, I figured that I should create a tool using Python.
</p>
<p>
I did the following:
<ul>
<li>Decided to use <a href="http://www.sqlalchemy.org">SQLAlchemy</a> to talk to the database</li>
<li>Learned a ton about manipulating <a href="http://docs.python.org/tutorial/datastructures.html#dictionaries">Python dictionaries</a></li>
</ul>
</p>
<p>
I figured I would create a dictionary for each week of the schedule containing each of the series for that particular week.  Python handles associative arrays a little differently than PHP does in terms of syntax, but the concept is still the same.  Once I had those dictionaries in place, I would then iterate through each one and save a record in the schedule database.  After a few stops and starts, I got to work properly.
{% codeblock lang:python %}
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Schedule(Base):
    __tablename__ = 'sched2009'
    week = Column(Integer, primary_key=True)
    home = Column(String, primary_key=True)
    away = Column(String, primary_key=True)
    status = Column(Integer)

    def __init__(self, week, home, away, status):
        self.week = week
        self.home = home
        self.away = away
        self.status = status

    def __repr__(self):
        return "<schedule (%i, '%s', '%s', %i)>" %  (self.week, self.home, self.away, self.status)

engine = create_engine('postgres://user:pass@localhost:3333/ibl_stats')
Session = sessionmaker(bind=engine)
session = Session()
series = {}

series[1] = {'05':'01', '08':'02', '07':'03', '06':'04', '09':'05', '12':'06', '11':'07', '10':'08', '01':'09', '04':'10', '03':'11', '02':'12'}
series[2] = {'06':'01', '05':'02', '08':'03', '07':'04', '10':'05', '09':'06', '12':'07', '11':'08', '02':'09', '01':'10', '04':'11', '03':'12'}
series[3] = {'07':'01', '06':'02', '05':'03', '08':'04', '11':'05', '10':'06', '09':'07', '12':'08', '03':'09', '02':'10', '01':'11', '04':'12'}
series[4] = {'08':'01', '07':'02', '06':'03', '05':'04', '12':'05', '11':'06', '10':'07', '09':'08', '04':'09', '03':'10', '02':'11', '01':'12'}

series[8] = {'08':'01', '05':'02', '06':'03', '07':'04', '12':'05', '09':'06', '10':'07', '11':'08', '04':'09', '01':'10', '02':'11', '03':'12'}
series[9] = {'07':'01', '08':'02', '05':'03', '06':'04', '11':'05', '12':'06', '09':'07', '10':'08', '03':'09', '04':'10', '01':'11', '02':'12'}
series[10] = {'06':'01', '07':'02', '08':'03', '05':'04', '10':'05', '11':'06', '12':'07', '09':'08', '02':'09', '03':'10', '04':'11', '01':'12'}
series[11] = {'05':'01', '06':'02', '07':'03', '08':'04', '09':'05', '10':'06', '11':'07', '12':'08', '01':'09', '02':'10', '03':'11', '04':'12'}

series[17] = {'09':'01', '12':'02', '11':'03', '10':'04', '01':'05', '04':'06', '03':'07', '02':'08', '05':'09', '08':'10', '07':'11', '06':'12'}
series[18] = {'10':'01', '09':'02', '12':'03', '11':'04', '02':'05', '01':'06', '04':'07', '03':'08', '06':'09', '05':'10', '08':'11', '07':'12'}
series[19] = {'11':'01', '10':'02', '09':'03', '12':'04', '03':'05', '02':'06', '01':'07', '04':'08', '07':'09', '06':'10', '05':'11', '08':'12'}
series[20] = {'12':'01', '11':'02', '10':'03', '09':'04', '04':'05', '03':'06', '02':'07', '01':'08', '08':'09', '07':'10', '06':'11', '05':'12'}

series[21] = {'12':'01', '09':'02', '10':'03', '11':'04', '04':'05', '01':'06', '02':'07', '03':'08', '07':'09', '06':'10', '05':'11', '08':'12'}
series[22] = {'11':'01', '12':'02', '09':'03', '10':'04', '03':'05', '04':'06', '01':'07', '02':'08', '06':'09', '05':'10', '08':'11', '07':'12'}
series[23] = {'10':'01', '11':'02', '12':'03', '09':'04', '02':'05', '03':'06', '04':'07', '01':'08', '05':'09', '08':'10', '07':'11', '06':'12'}
series[24] = {'09':'01', '10':'02', '11':'03', '12':'04', '01':'05', '02':'06', '03':'07', '04':'08', '08':'09', '07':'10', '06':'11', '05':'12'}

series[5] = {'04':'01', '01':'02', '02':'03', '03':'04', '08':'05', '05':'06', '06':'07', '07':'08', '12':'09', '09':'10', '10':'11', '11':'12'}
series[6] = {'03':'01', '04':'02', '01':'03', '02':'04', '07':'05', '08':'06', '05':'07', '06':'08', '11':'09', '12':'10', '09':'11', '10':'12'}
series[7] = {'02':'01', '03':'02', '04':'03', '01':'04', '06':'05', '07':'06', '08':'07', '05':'08', '10':'09', '11':'10', '12':'11', '09':'12'}

series[14] = {'03':'01', '04':'02', '02':'03', '01':'04', '07':'05', '08':'06', '06':'07', '05':'08', '11':'09', '12':'10', '10':'11', '09':'12'}
series[15] = {'02':'01', '01':'02', '04':'03', '03':'04', '06':'05', '05':'06', '08':'07', '07':'08', '10':'09', '09':'10', '12':'11', '11':'12'}
series[16] = {'04':'01', '03':'02', '01':'03', '02':'04', '08':'05', '07':'06', '05':'07', '06':'08', '12':'09', '11':'10', '09':'11', '10':'12'}

series[25] = {'02':'01', '01':'02', '04':'03', '03':'04', '06':'05', '05':'06', '08':'07', '07':'08', '10':'09', '09':'10', '12':'11', '11':'12'}
series[26] = {'04':'01', '03':'02', '02':'03', '01':'04', '08':'05', '07':'06', '06':'07', '05':'08', '12':'09', '11':'10', '10':'11', '09':'12'}
series[27] = {'03':'01', '04':'02', '01':'03', '02':'04', '07':'05', '08':'06', '05':'07', '06':'08', '11':'09', '12':'10', '09':'11', '10':'12'}

for w, games in series.iteritems():
    for a, h in games.iteritems():
        for conf in 'n', 'a':
            home_team = conf + h
            away_team = conf + a
            new_series = Schedule(week=w, home=home_team, away=away_team, status=0)
            session.add(new_series)
            session.commit()
            print 'Added wk' + str(w) + ' ' + away_team + ' @ ' + home_team

# Now, let's do the interleague games
series = {}
series[12] = {'a08':'n08', 'a04':'n04', 'n03':'a04', 'a02':'n02', 'a12':'n12', 'a11':'n11', 'n02':'a03', 'a01':'n01', 'n01':'a02', 'n05':'a06', 'a10':'n10', 'n10':'a11', 'n08':'a05', 'n12':'a09', 'a07':'n07', 'n04':'a01', 'n06':'a07', 'a05':'n05', 'n11':'a12', 'a06':'n06', 'a03':'n03', 'n09':'a10', 'a09':'n09', 'n07':'a08'}
series[13] = {'a01':'n03', 'n02':'a01', 'a11':'n09', 'n09':'a12', 'a04':'n02', 'a07':'n05', 'n10':'a09', 'a10':'n12', 'a02':'n04', 'n05':'a08', 'n11':'a10', 'a05':'n07', 'a03':'n01', 'n04':'a03', 'n06':'a05', 'a08':'n06', 'a12':'n10', 'n08':'a07', 'n03':'a02', 'n01':'a04', 'a06':'n08', 'n12':'a11', 'a09':'n11', 'n07':'a06'}

for w, games in series.iteritems():
    for a, h in games.iteritems():
        new_series = Schedule(week=w, home=h, away=a, status=0)
        session.add(new_series)
        session.commit()
        print 'Added wk' + str(w) + ' ' + a + ' @ ' + h
{% endcodeblock %}
</schedule></p>
<p>
The code looks straightforward, but my only concern is am I writing idiomatic Python code, or does it still look like "Python written by a PHP guy".  I'd appreciate any feedback from pythonistas.
</p>
