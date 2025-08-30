# -*- coding: utf-8 -*-
"""
Created on Wed Jun 23 13:13:27 2021

@author: Schlenker18
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
sns.set()

from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import f_regression

import Helper_Functions as hf
import Pos_Group_Rankings as pgr

# reading in CSV files
df_2018 = pd.read_csv("C:/Users/Schlenker18/Documents/GitHub/2021-Fantasy-Football-Rankings/StatFiles/WrStats2018.csv")
df_2019 = pd.read_csv("C:/Users/Schlenker18/Documents/GitHub/2021-Fantasy-Football-Rankings/StatFiles/WrStats2019.csv")
df_2020 = pd.read_csv("C:/Users/Schlenker18/Documents/GitHub/2021-Fantasy-Football-Rankings/StatFiles/WrStats2020.csv")

# creating dictionary for wrs who scored fantasy points in 2019
wr_dict = hf.get_player_season(df_2019)

# since I want to create a linear regression, I will need players to have stats
# for the 2019 season, so I only want to add players stats who are already in the dictionary
# adding 2020 ftps/g to dictionary
wr_dict = hf.add_season(wr_dict, df_2020)
        
# create new dictionary that only holds data for players with more than one season
new_wr_dict = hf.clean_dictionary(wr_dict, 1)

# removing players who scored less than 3 fantasy ppg in any season
new_wr_dict = hf.remove_backups(new_wr_dict, 3)

# turning dictionary back into series in order to create a pandas dataframe
players, fpts_2019, fpts_2020 = hf.dict_to_series(new_wr_dict)

data = {'Players': players, '2019 Fpts/G': fpts_2019, '2020 Fpts/G': fpts_2020}
df = pd.DataFrame(data)

# running simple linear regression
# creating the regression
x = data['2019 Fpts/G'] # x is the feauture var
y = data['2020 Fpts/G'] # y is the output

x_matrix = x.values.reshape(-1,1)

# running the regression
reg = LinearRegression()

reg.fit(x_matrix, y)

# r-squared
reg_score = reg.score(x_matrix, y)

# Intercept
reg_intercept = reg.intercept_

# making predctions
def predict_ppg(x):
    score = np.array([[x]])
    print(reg.predict(score))


# plotting regression line
plt.scatter(x,y)
yhat = reg.coef_ * x + reg_intercept
fig = plt.plot(x, yhat, lw = 2, c = 'orange')
plt.xlabel('2019 Fpts/G', fontsize = 15, fontweight = 'bold')
plt.ylabel('2020 Fpts/G', fontsize = 15, fontweight = 'bold')
plt.show()

# creating new regression using both 2018, 2019 seasons as inputs
# creating dictionary with 2018 wrs who scored more than 0 points
test_wr_dict = hf.get_player_season(df_2018)

# adding 2019, 2020 seasons to dictionary
test_wr_dict = hf.add_season(test_wr_dict, df_2019)
test_wr_dict = hf.add_season(test_wr_dict, df_2020)

# removing players who played less than 3 seasons
test_wr_dict = hf.clean_dictionary(test_wr_dict, 2)

# removing players who scored less than 3 points per game, these are generally
# backups
test_wr_dict = hf.remove_backups(test_wr_dict, 3)

# turning dictionary back into series in order to create a pandas dataframe
players, fpts_2018, fpts_2019, fpts_2020 = hf.dict_to_series_2(test_wr_dict)

# finding corresponding 2019 team for each player in our series
player_teams = []
for player in players:
    for i in range(len(df_2019)):
        if player == hf.get_player(df_2019.loc[i].PLAYER):
            player_teams.append(hf.get_player_team(df_2019.loc[i].PLAYER))
            
# finding corresponding 2020 team for each player in our series
player_teams_20 = []
for player in players:
    for i in range(len(df_2020)):
        if player == hf.get_player(df_2020.loc[i].PLAYER):
            player_teams_20.append(hf.get_player_team(df_2020.loc[i].PLAYER))
        

# turning list of player teams into series
player_teams = pd.Series(player_teams)      
player_teams_20 = pd.Series(player_teams_20)  

# creating dataframe 
test_data = {'Players': players, '19 TM': player_teams, '20 TM': player_teams_20,
             '2018 Fpts/G': fpts_2018, '2019 Fpts/G': fpts_2019,
             '2020 Fpts/G': fpts_2020}
test_df = pd.DataFrame(test_data)

# running multiple linear regression
# creating the regression 
x = test_df[['2018 Fpts/G', '2019 Fpts/G']] # x is the feauture var
y = test_data['2020 Fpts/G'] # y is the output

# running the regression
test_reg = LinearRegression()

test_reg.fit(x, y)

# r-squared
test_reg_score = test_reg.score(x, y)

# Intercept
test_reg_intercept = reg.intercept_

# determining effect of each of the regressors
f_regression(x,y)

p_vals = f_regression(x,y)[1]

# creating summary table for coefficients and p-values
reg_summary = pd.DataFrame(data = x.columns.values, columns = ['Features'])

reg_summary['Coefficients'] = test_reg.coef_
reg_summary['p-values'] = p_vals.round(5)