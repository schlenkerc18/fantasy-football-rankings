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
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

# Reading in csv files
qb_df_2018 = pd.read_csv("C:/Users/Schlenker18/Documents/GitHub/2021-Fantasy-Football-Rankings/StatFiles/QbStats2018.csv")
qb_df_2019 = pd.read_csv("C:/Users/Schlenker18/Documents/GitHub/2021-Fantasy-Football-Rankings/StatFiles/QbStats2019.csv")
qb_df_2020 = pd.read_csv("C:/Users/Schlenker18/Documents/GitHub/2021-Fantasy-Football-Rankings/StatFiles/QbStats2020.csv")

rb_df_2018 = pd.read_csv("C:/Users/Schlenker18/Documents/GitHub/2021-Fantasy-Football-Rankings/StatFiles/RbStats2018.csv")
rb_df_2019 = pd.read_csv("C:/Users/Schlenker18/Documents/GitHub/2021-Fantasy-Football-Rankings/StatFiles/RbStats2019.csv")
rb_df_2020 = pd.read_csv("C:/Users/Schlenker18/Documents/GitHub/2021-Fantasy-Football-Rankings/StatFiles/RbStats2020.csv")

wr_df_2018 = pd.read_csv("C:/Users/Schlenker18/Documents/GitHub/2021-Fantasy-Football-Rankings/StatFiles/WrStats2018.csv")
wr_df_2019 = pd.read_csv("C:/Users/Schlenker18/Documents/GitHub/2021-Fantasy-Football-Rankings/StatFiles/WrStats2019.csv")
wr_df_2020 = pd.read_csv("C:/Users/Schlenker18/Documents/GitHub/2021-Fantasy-Football-Rankings/StatFiles/WrStats2020.csv")

te_df_2018 = pd.read_csv("C:/Users/Schlenker18/Documents/GitHub/2021-Fantasy-Football-Rankings/StatFiles/TeStats2018.csv")
te_df_2019 = pd.read_csv("C:/Users/Schlenker18/Documents/GitHub/2021-Fantasy-Football-Rankings/StatFiles/TeStats2019.csv")
te_df_2020 = pd.read_csv("C:/Users/Schlenker18/Documents/GitHub/2021-Fantasy-Football-Rankings/StatFiles/TeStats2020.csv")

# creating histogram to see distribution of data, 2018 qb stats
sns.set_style("white")
plt.figure(figsize = (12,8))
plt.hist(qb_df_2018['FPTS/G'].iloc[0:41], bins = np.arange(6,31,4), color = '#4F69C6') # removing outliers
plt.title("Distribution of QB Fpts/G in 2018", fontsize = 14, weight = 'bold')
plt.xlabel('Fpts/G', fontsize = 12, weight = 'bold')
plt.ylabel('Number of QBs', fontsize = 12, weight = 'bold')
plt.xticks(np.arange(6,31,4))
plt.yticks(np.arange(1,15))
sns.despine()
plt.show()

# creating histogram to see distribution of 2019 qb stats
sns.set_style("white")
plt.figure(figsize = (12,8))
plt.hist(qb_df_2019['FPTS/G'].iloc[0:42], bins = np.arange(6,31,4), color = '#4F69C6') # removing outliers
plt.title("Distribution of QB Fpts/G in 2019", fontsize = 14, weight = 'bold')
plt.xlabel('Fpts/G', fontsize = 12, weight = 'bold')
plt.ylabel('Number of QBs', fontsize = 12, weight = 'bold')
plt.xticks(np.arange(6,31,4))
plt.yticks(np.arange(1,20))
sns.despine()
plt.show()

# creating histogram to see distribution of 2020 qb stats
sns.set_style("white")
plt.figure(figsize = (12,8))
plt.hist(qb_df_2020['FPTS/G'].iloc[0:47], bins = np.arange(6,31,4), color = '#4F69C6') # removing outliers
plt.title("Distribution of QB Fpts/G in 2020", fontsize = 14, weight = 'bold')
plt.xlabel('Fpts/G', fontsize = 12, weight = 'bold')
plt.ylabel('Number of QBs', fontsize = 12, weight = 'bold')
plt.xticks(np.arange(6,31,4))
plt.yticks(np.arange(1,15))
sns.despine()
plt.show()

# creating histogram to see distribution of 2018 rb stats
sns.set_style('white')
plt.figure(figsize = (12,8))
plt.hist(rb_df_2018['FPTS/G'].iloc[0:41], bins = np.arange(5,24,3), color = '#4F69C6')
plt.title('Distribution of RB Fpts/G in 2018', fontsize = 14, weight = 'bold')
plt.xlabel('Fpts/G', fontsize = 12, weight = 'bold')
plt.xticks(np.arange(5,24,3))
plt.yticks(np.arange(1,18))
sns.despine()
plt.show()

# creating histogram to see distribution of 2019 rb stats
sns.set_style('white')
plt.figure(figsize = (12,8))
plt.hist(rb_df_2019['FPTS/G'].iloc[0:41], bins = np.arange(5,24,3), color = '#4F69C6')
plt.title('Distribution of RB Fpts/G in 2019', fontsize = 14, weight = 'bold')
plt.xlabel('Fpts/G', fontsize = 12, weight = 'bold')
plt.xticks(np.arange(5,24,3))
plt.yticks(np.arange(1,17))
sns.despine()
plt.show()

# creating histogram to see distribution of 2020 rb stats
sns.set_style('white')
plt.figure(figsize = (12,8))
plt.hist(rb_df_2020['FPTS/G'].iloc[0:41], bins = np.arange(5,24,3), color = '#4F69C6')
plt.title('Distribution of RB Fpts/G in 2020', fontsize = 14, weight = 'bold')
plt.xlabel('Fpts/G', fontsize = 12, weight = 'bold')
plt.xticks(np.arange(5,24,3))
plt.yticks(np.arange(1,14))
sns.despine()
plt.show()

# creating histogram to see distribution of 2018 wr stats
sns.set_style('white')
plt.figure(figsize = (12,8))
plt.hist(wr_df_2018['FPTS/G'].iloc[0:51], bins = np.arange(5,18,2.5), color = '#4F69C6')
plt.title('Distribution of WR Fpts/G in 2018', fontsize = 14, weight = 'bold')
plt.xlabel('Fpts/G', fontsize = 12, weight = 'bold')
plt.xticks(np.arange(5,18,2.5))
plt.yticks(np.arange(1,19))
sns.despine()
plt.show()

# creating histogram to see distribution of 2019 wr stats
sns.set_style('white')
plt.figure(figsize = (12,8))
plt.hist(wr_df_2019['FPTS/G'].iloc[0:51], bins = np.arange(5,16,2.5), color = '#4F69C6')
plt.title('Distribution of WR Fpts/G in 2019', fontsize = 14, weight = 'bold')
plt.xlabel('Fpts/G', fontsize = 12, weight = 'bold')
plt.xticks(np.arange(5,16,2.5))
plt.yticks(np.arange(1,22))
sns.despine()
plt.show()

# creating histogram to see distribution of 2020 wr stats
sns.set_style('white')
plt.figure(figsize = (12,8))
plt.hist(wr_df_2020['FPTS/G'].iloc[0:51], bins = np.arange(5,18,2.5), color = '#4F69C6')
plt.title('Distribution of WR Fpts/G in 2020', fontsize = 14, weight = 'bold')
plt.xlabel('Fpts/G', fontsize = 12, weight = 'bold')
plt.xticks(np.arange(5,20,2.5))
plt.yticks(np.arange(1,22))
sns.despine()
plt.show()

# creating histogram to see distribution of 2018 te stats
sns.set_style('white')
plt.figure(figsize = (12,8))
plt.hist(te_df_2018['FPTS/G'].iloc[0:21], bins = np.arange(3,14,2.5), color = '#4F69C6')
plt.title('Distribution of TE Fpts/G in 2018', fontsize = 14, weight = 'bold')
plt.xlabel('Fpts/G', fontsize = 12, weight = 'bold')
plt.xticks(np.arange(3,14,2.5))
plt.yticks(np.arange(1,9))
sns.despine()
plt.show()

# creating histogram to see distribution of 2019 te stats
sns.set_style('white')
plt.figure(figsize = (12,8))
plt.hist(te_df_2019['FPTS/G'].iloc[0:21], bins = np.arange(4,11,2), color = '#4F69C6')
plt.title('Distribution of TE Fpts/G in 2019', fontsize = 14, weight = 'bold')
plt.xlabel('Fpts/G', fontsize = 12, weight = 'bold')
plt.xticks(np.arange(4,11,2))
plt.yticks(np.arange(1,12))
sns.despine()
plt.show()

# creating histogram to see distribution of 2019 te stats
sns.set_style('white')
plt.figure(figsize = (12,8))
plt.hist(te_df_2020['FPTS/G'].iloc[0:21], bins = np.arange(4,15,2.5), color = '#4F69C6')
plt.title('Distribution of TE Fpts/G in 2020', fontsize = 14, weight = 'bold')
plt.xlabel('Fpts/G', fontsize = 12, weight = 'bold')
plt.xticks(np.arange(4,15,2.5))
plt.yticks(np.arange(1,12))
sns.despine()
plt.show()
