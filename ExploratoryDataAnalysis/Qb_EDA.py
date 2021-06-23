# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 14:21:53 2021

@author: Schlenker18
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
sns.set()

from sklearn.linear_model import LinearRegression

# reading in CSV files
df_2019 = pd.read_csv("C:/Users/Schlenker18/Documents/GitHub/2021-Fantasy-Football-Rankings/WebScrapers/QbStats2019.csv")
df_2020 = pd.read_csv("C:/Users/Schlenker18/Documents/GitHub/2021-Fantasy-Football-Rankings/WebScrapers/QbStats2020.csv")

# dictionary comprehension for 2019 qbs
# only want to add qbs who scored fantasy points
qb_dict = {df_2019['PLAYER'].iloc[i]: [df_2019['FPTS/G'].iloc[i]] for i in range(len(df_2019))
           if df_2019['FPTS/G'].iloc[i] > 0}

# since I want to create a linear regression, I will need players to have stats
# for the 2019 season, so I only want to add players stats who are already in the
# dictionary
# adding 2020 ftps/g to dictionary
for i in range(len(df_2020)):
    if df_2020['PLAYER'].iloc[i] in qb_dict:
        qb_dict[df_2020['PLAYER'].iloc[i]].append(df_2020['FPTS/G'].iloc[i])
        
# create new dictionary that only holds data for players with more than one season
new_qb_dict = {x:y for x,y in qb_dict.items() if len(y) > 1}

# turning dictionary back into lists in order to create a pandas dataframe
# turn keys in qb_dict into list, remove trailing whitespace
players = [x.rstrip() for x in new_qb_dict]
players = pd.Series(players)

fpts_2019 = [x[0] for x in new_qb_dict.values()]
fpts_2019 = pd.Series(fpts_2019)

fpts_2020 = [x[1] for x in new_qb_dict.values()]
fpts_2020 = pd.Series(fpts_2020)
   
# creating data to be put into dataframe 
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

# plotting regression line
plt.scatter(x,y)
yhat = reg.coef_ * x + reg_intercept
fig = plt.plot(x, yhat, lw = 2, c = 'orange')
plt.xlabel('2019 Fpts/G', fontsize = 15, fontweight = 'bold')
plt.ylabel('2020 Fpts/G', fontsize = 15, fontweight = 'bold')
plt.show()
