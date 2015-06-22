---
title: IO - Why, What, When, Where, and sometimes How
---

The goal:
Write a web scraper that collects data about outcomes (final scores) of Ghana
Premier League football matches and writes them to a file on your computer.

In order to achieve this within ~90 minutes, you will need to either already
know how to do it, or you will need to use a search engine extensively!

Rough outline:
This website has links to team pages with match outcomes:
http://www.whatsthescore.com/football/ghana/ghana-premier-league/teams.html

Write a program that fetches the content from that page and extracts the links
to the team pages.

Modify the progam to go to each of the team pages, fetch that content, and
extract the date, the home and away team, and the final score.

Write the match data to disk.

If you have time, modify the program to write the data to an SQLite database.
