# 2021-Fantasy-Football-Rankings
This project aims to create a 2021 ranking of fantasy football players to help players during their fantasy football draft.

I plan to model my 2021 projections based on several factors including statistics from previous seasons, coaching staff, offensive-line ranking, etc.  I will then weight these numbers together to create a ranked list of players in 2021.

For the time being, I will only focus on offensive players.  Kickers and defenses will not be included in this ranked list.

QB Factors:
  1. Recent seasons
  2. Rating of WR's
  3. Rating of offensive line
  4. Rating of offensive play caller

RB Factors: 
  1. Recent seasons
  2. Rating of offensive line
  3. Rating of QB
  4. Rating of offensive play caller

WR Factors:
  1. Recent seasons
  2. Rating of QB
  3. Rating of offensive line
  4. Rating of offensive play caller

TE Factors:
  1. Recent Seasons
  2. Rating of QB
  3. Rating of WRs
  4. Rating of offensive player-caller
  5. Rating of offensive line

Current state of project:
  So far, I have pulled statistics for the 2018, 2019, and 2020 seasons.  I have created simple linear regresssions and multiple linear regressions for each of the posistions listed above.  For the QB position and TE positions, recent seasons are not a reliable predictor of future output.  However, recent seasons for the RB, and WR positions seem to be a generally reliable predictor of future output, especially for the WR position.
  
r^2 for simple linear regressions for each position (2019 is used as input, 2020 is dependent variable)

    QB: .32    
    RB: .42
    WR: .31
    TE: .33
    
  
r^2 values for the multiple linear regressions for each position (2018 and 2019 are used as input variables, 2020 is the dependent variable)

    QB: .32
    RB: .63
    WR: .46
    TE: .35
    
    
To-Do List:
  1. Create regression equations for each regression
  2. Fix overfitting problem (regressions are ran on all data, need to run regressions on ~80% of data to avoid overfitting problem)
  3. Add more features to multiple linear regression equations
