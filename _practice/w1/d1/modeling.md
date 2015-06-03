---
title: Mathematical Modeling
---
## GameBot

Each team will create a Keeper and Kicker Bot, and each team will play every other team in a game once.  In the game, Team A's Kicker plays Team B's Keeper 100 times (resulting in a score A1-B1), and Team B's Kicker plays Team A's Keeper 100 times (resulting in a score A2-B2).  The winner of this game will be the greater score (A1+A2 or B1+B2), with a tie possible.  The winner of the tournament will win the greatest number of games (or have the best record W-L-T).  

Dictate a strategy for your Goalie and Kicker.  Each can "learn" from the opponent during the game (remembers the history up the the 100th kick), but enters each new game unaware of the new teams history. 

1. As the Goalie you can move L/R and try to CATCH/DEFLECT - with the assumption that CATCHing (or obtaining possession of the ball) is both riskier than DEFLECTing (the kicker is more likely to score) and better for your team (once you have possession, your team scores).
2. As the Kicker, you can shoot (kick the ball) L/R and POWER/CURVE (where POWER is the more accurate option with less reward).

K   G   | CATCH L | DEFLECT L | CATCH R | DEFLECT R
POWER L | ------- | --------- | ------- | ----------
CURVE L |
POWER R |
CURVE R |

