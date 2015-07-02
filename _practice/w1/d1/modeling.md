---
title: Mathematical Modeling
---
## GameBot

Each team will create a Keeper and Kicker Bot, and each team will play every other team in a game once.  In the game, Team A's Kicker plays Team B's Keeper 100 times (resulting in a score A1-B1), and Team B's Kicker plays Team A's Keeper 100 times (resulting in a score A2-B2).  The winner of this game will be the greater score (A1+A2 or B1+B2), with a tie possible.  The winner of the tournament will win the greatest number of games (or have the best record W-L-T).  

Dictate a strategy for your Goalie and Kicker.  Each can "learn" from the opponent during the game (remembers the history up the the 100th kick), but enters each new game against a new opponent unaware of the opponent's history. 

1. As the Goalie you can move to deflect L/C/R. 
2. As the Kicker, you can shoot (kick the ball) L/C/R.

Ki/Ke   |  L  |  C  |  R 
------- | --- | --- | ---
 L      | 0.1 | 0.6 | 0.9
 C      | 0.7 | 0.2 | 0.7 
 R      | 0.9 | 0.8 | 0.1
 
Each team should submit a KEEPER and a KICKER object...

See code [here](https://gist.github.com/c6324b6bdd9b5352e641)
