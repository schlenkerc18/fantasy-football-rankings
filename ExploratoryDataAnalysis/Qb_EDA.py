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

# importing module with helper functions
import Helper_Functions as hf

# reading in CSV files
df_2019 = pd.read_csv("C:/Users/Schlenker18/Documents/GitHub/2021-Fantasy-Football-Rankings/WebScrapers/QbStats2019.csv")
df_2020 = pd.read_csv("C:/Users/Schlenker18/Documents/GitHub/2021-Fantasy-Football-Rankings/WebScrapers/QbStats2020.csv")

# create dictionary for qbs who played in 2019
# only want to add qbs who scored fantasy points
qb_dict = hf.get_player_season(df_2019)

# since I want to create a linear regression, I will need players to have stats
# for the 2019 season, so I only want to add players stats who are already in the dictionary
# adding 2020 ftps/g to dictionary        
qb_dict = hf.add_season(qb_dict, df_2020)
        
# create new dictionary that only holds data for players with more than one season
new_qb_dict = hf.clean_dictionary(qb_dict)

# turning dictionary back into series in order to create a pandas dataframe
players, fpts_2019, fpts_2020 = hf.dict_to_series(new_qb_dict)
   
# creating dataframe 
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