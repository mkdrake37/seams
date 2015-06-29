#!/usr/bin/python
import urllib2
from BeautifulSoup import BeautifulSoup
import sqlite3

base = 'http://www.whatsthescore.com'
response = urllib2.urlopen('http://www.whatsthescore.com/football/ghana/ghana-premier-league/teams.html')
html = response.read()

conn = sqlite3.connect('ghana-premier.sqlite')
c = conn.cursor()
c.execute('DROP TABLE if exists match')
c.execute('CREATE TABLE match (date text, home text, away text, hscore int, ascore int, unique(date, home, away))')

parsed_html = BeautifulSoup(html)
for sec in parsed_html.body.findAll('div', attrs={'class':'section'}):
    team_url = base + sec.find('a').get('href')

    team_response = urllib2.urlopen(team_url)
    team_html = team_response.read()

    team_parsed = BeautifulSoup(team_html)
    table = team_parsed.body.find('div', attrs={'class':'tables'})
    matches = []
    for event in table.findAll('tr')[1:]:
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
    c.executemany('INSERT OR IGNORE INTO match VALUES (?,?,?,?,?)', matches)
    conn.commit()

conn.close()
