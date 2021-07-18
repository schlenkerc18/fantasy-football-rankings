# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 15:01:45 2021

@author: Schlenker18
"""

"""
The purpose of this file is just to get a better sense of what the data looks
like by messing around with some data visualizations.
"""
# importing relevant libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# Reading in csv files
qb_df_2018 = pd.read_csv("C:/Users/Schlenker18/Documents/GitHub/2021-Fantasy-Football-Rankings/WebScrapers/QbStats2018.csv")
qb_df_2019 = pd.read_csv("C:/Users/Schlenker18/Documents/GitHub/2021-Fantasy-Football-Rankings/WebScrapers/QbStats2019.csv")
qb_df_2020 = pd.read_csv("C:/Users/Schlenker18/Documents/GitHub/2021-Fantasy-Football-Rankings/WebScrapers/QbStats2020.csv")

# creating histogram to see distribution of data, 2018 stats
sns.set_style("white")
plt.figure(figsize = (12,8))
plt.hist(qb_df_2018['FPTS/G'].iloc[0:41], bins = 8, color = '#4F69C6') # removing outliers
plt.title("Distribution of QB Fpts/G in 2018", fontsize = 14, weight = 'bold')
plt.xlabel('Fpts/G', fontsize = 12, weight = 'bold')
plt.ylabel('Number of QBs', fontsize = 12, weight = 'bold')
sns.despine()
plt.show()

# creating histogram to see distribution of 2019 stats
sns.set_style("white")
plt.figure(figsize = (12,8))
plt.hist(qb_df_2019['FPTS/G'].iloc[0:42], bins = 8, color = '#4F69C6') # removing outliers
plt.title("Distribution of QB Fpts/G in 2019", fontsize = 14, weight = 'bold')
plt.xlabel('Fpts/G', fontsize = 12, weight = 'bold')
plt.ylabel('Number of QBs', fontsize = 12, weight = 'bold')
sns.despine()
plt.show()

# creating histogram to see distribution of 2020 stats
sns.set_style("white")
plt.figure(figsize = (12,8))
plt.hist(qb_df_2020['FPTS/G'].iloc[0:47], bins = 8, color = '#4F69C6') # removing outliers
plt.title("Distribution of QB Fpts/G in 2020", fontsize = 14, weight = 'bold')
plt.xlabel('Fpts/G', fontsize = 12, weight = 'bold')
plt.ylabel('Number of QBs', fontsize = 12, weight = 'bold')
sns.despine()
plt.show()