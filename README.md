# Fantasy Football Rankings
This project aims to create a 2021 ranking of fantasy football players to help players during their fantasy football draft.

I plan to model my 2021 projections based on several factors including statistics from previous seasons, coaching staff, offensive-line ranking, etc.  I will then weight these numbers together to create a ranked list of players in 2021.

For the time being, I will only focus on offensive players.  Kickers and defenses will not be included in this ranked list.

QB Factors:
  1. 2019 Season
  2. Rating of WR's

RB Factors: 
  1. Past Two Seasons

WR Factors:
  1. Past Two Seasons

TE Factors:
  1. Past Two Seasons

Current state of project:
  So far, I have pulled statistics for the 2018, 2019, and 2020 seasons.  I have created simple linear regresssions and multiple linear regressions for each of the posistions listed above.  For the QB position and TE positions, recent seasons are not a reliable predictor of future output.  However, recent seasons for the RB, and WR positions seem to be a generally reliable predictor of future output, especially for the WR position.
  
r^2 for simple linear regressions for each position (2019 is used as input, 2020 is dependent variable)

    QB: .32    
    RB: .42
    WR: .31
    TE: .33
    
  
r^2 values for the multiple linear regressions for each position (Feautures of multiple linear regression are listed above for each position)

    QB: .25
    RB: .63
    WR: .46
    TE: .35
