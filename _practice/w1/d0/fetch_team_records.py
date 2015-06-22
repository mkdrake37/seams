#!/usr/bin/python
import urllib2
from BeautifulSoup import BeautifulSoup

base = 'http://www.whatsthescore.com'
response = urllib2.urlopen('http://www.whatsthescore.com/football/ghana/ghana-premier-league/teams.html')
html = response.read()

parsed_html = BeautifulSoup(html)
for sec in parsed_html.body.findAll('div', attrs={'class':'section'}):
    team_url = base + sec.find('a').get('href')

    team_response = urllib2.urlopen(team_url)
    team_html = team_response.read()

    team_parsed = BeautifulSoup(team_html)
    table = team_parsed.body.find('div', attrs={'class':'tables'})
    for event in table.findAll('tr')[1:]:
        print event.find('td', attrs={'class':'event-time'}).text,

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
