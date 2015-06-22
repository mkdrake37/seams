#!/usr/bin/python
import urllib2
from BeautifulSoup import BeautifulSoup

# This is not the finished version of this script; rather it's one that shows the incremental 
# chunks of code I wrote, and some of the checks that I did to convince myself that it was
# working properly

base_url = 'http://www.whatsthescore.com'
response = urllib2.urlopen('http://www.whatsthescore.com/football/ghana/ghana-premier-league/teams.html')
html = response.read()

# write out and inspect html to see if what we want is there
fo = open('league.html', 'w')
fo.write(html)
fo.close()

# Inspected teams.html in shell using 'less'.  Looks good, the data I saw in the web browser
# is there. Also looked for the smallest container that held the list of links for Ghana Premier League
# individual team pages.  Looks like it's a div with class=section . . .

parsed_html = BeautifulSoup(html)
for sec in parsed_html.body.findAll('div', attrs={'class':'section'}):
    # Did a bit of fiddling here until I got a command that pulled out the links, all the links, and
    # nothing but the links for the teams
    print base_url + sec.find('a').get('href')

# Okay, let's just look at one of those pages now . . .
team_response = urllib2.urlopen('http://www.whatsthescore.com/football/ghana/team-ba-stars-fc-213517.html')
team_html = team_response.read()

# write out and inspect html to see if what we want is there
fo = open('team.html', 'w')
fo.write(team_html)
fo.close()

# Again, looks good, although kind of ugly structure, involving different classes and crud we don't care about

team_parsed = BeautifulSoup(team_html)
table = team_parsed.body.find('div', attrs={'class':'tables'})  # grab the main table
for event in table.findAll('tr')[1:]:                           # skip the header, grab each subsequent row
    # and then grab text from the individual containers we care about
    print event.find('td', attrs={'class':'event-time'}).text,

    # something like this is needed (or a regex, which seems more complicated), because the container class 
    # is dependent on whether the home or away team won
    try:
        print event.find('td', attrs={'class':'event-home-team winner'}).text,
    except:
        print event.find('td', attrs={'class':'event-home-team '}).text,

    print event.find('span', attrs={'class':'event-score home-runningscore'}).text,
    try:
        print event.find('td', attrs={'class':'event-away-team winner'}).text,
    except:
        print event.find('td', attrs={'class':'event-away-team '}).text,

    print event.find('span', attrs={'class':'event-score away-runningscore'}).text

# Okay, that dumped lots of good stuff to the screen.  Let's build a DB for it.
conn = sqlite3.connect('ghana-premier.sqlite')
c = conn.cursor()
c.execute('DROP TABLE if exists match') # keep DB clean, in case we run this multiple times
# Unique statement on the following line prevents games from being inserted multiple times.
# Since we're parsing all league teams pages, every within-league game should be parsed twice.
c.execute('CREATE TABLE match (date text, home text, away text, hscore int, ascore int, unique(date, home, away))')

# Okay, all together now: For each team
for sec in parsed_html.body.findAll('div', attrs={'class':'section'}):
    team_url = base + sec.find('a').get('href')

    # Grab the HTML for the team's page
    team_response = urllib2.urlopen(team_url)
    team_html = team_response.read()

    team_parsed = BeautifulSoup(team_html)
    # Grab the match table
    table = team_parsed.body.find('div', attrs={'class':'tables'})
    matches = []
    for event in table.findAll('tr')[1:]:
        # Store the data in a list of tuples this time
        date = event.find('td', attrs={'class':'event-time'}).text

        try:
            home = event.find('td', attrs={'class':'event-home-team winner'}).text
        except:
            home = event.find('td', attrs={'class':'event-home-team '}).text

        try: 
            away = event.find('td', attrs={'class':'event-away-team winner'}).text
        except:
            away = event.find('td', attrs={'class':'event-away-team '}).text
         
        hscore = event.find('span', attrs={'class':'event-score home-runningscore'}).text
        ascore = event.find('span', attrs={'class':'event-score away-runningscore'}).text
        matches.append((date, home, away, hscore, ascore))
    # Insert everything that's not a duplicate into the DB
    c.executemany('INSERT OR IGNORE INTO match VALUES (?,?,?,?,?)', matches)
    # Commit the stuff
    conn.commit()

# Call it a day.
conn.close()

