# -*- coding: utf-8 -*-
"""
Created on Mon Jun 21 12:43:32 2021

@author: Schlenker18
"""
# using https://www.codecademy.com/resources/blog/web-scraping-python-beautiful-soup-mlb-stats/
# as a guide to pull stats from fantasypros

import pandas as pd
import re
import requests
from bs4 import BeautifulSoup

# scraping 2020 Qb fantasy stats
url = requests.get('https://www.fantasypros.com/nfl/stats/qb.php?year=2020')
src = url.content
soup = BeautifulSoup(src, 'html.parser')

# create column names
columns = ['RANK', 'PLAYER', 'CMP', 'ATT', 'PCT', 'YDS', 'Y/A', 'TD', 'INT', 
          'SACKS', 'ATT', 'YDS', 'TD', 'FL', 'G', 'FPTS', 'FPTS/G', 'OWN']

# create an empty dataframe with column names
final_2020_df = pd.DataFrame(columns = columns)

# pull in player rows
players = soup.find_all('tr', attrs = {'class': re.compile('mpb-player-')})

for player in players:
        
    # get the stats for each player
    stats = [stat.get_text() for stat in player.find_all('td')]
    
    # create a dataframe for the single player's stats
    temp_df = pd.DataFrame(stats).transpose()
    temp_df.columns = columns
    
    # Join the single player's stats with the overall dataset
    final_2020_df = pd.concat([final_2020_df, temp_df], ignore_index = True)
    
# export to csv
final_2020_df.to_csv(r"QbStats2020.csv", 
                index = False, sep = ',', encoding = 'utf-8')

# repeat for 2018, 2019
# not using a for loop here because I want to save each season 
# as a separate csv file

# scraping 2018
url = requests.get('https://www.fantasypros.com/nfl/stats/qb.php?year=2018')
src = url.content
soup = BeautifulSoup(src, 'html.parser')

# create an empty dataframe with column names
final_2018_df = pd.DataFrame(columns = columns)

# pull in player rows
players = soup.find_all('tr', attrs = {'class': re.compile('mpb-player-')})

for player in players:
        
    # get the stats for each player
    stats = [stat.get_text() for stat in player.find_all('td')]
    
    # create a dataframe for the single player's stats
    temp_df = pd.DataFrame(stats).transpose()
    temp_df.columns = columns
    
    # Join the single player's stats with the overall dataset
    final_2018_df = pd.concat([final_2018_df, temp_df], ignore_index = True)
    
# export to csv
final_2018_df.to_csv(r"QbStats2018.csv", 
                index = False, sep = ',', encoding = 'utf-8')


# scraping 2019
url = requests.get('https://www.fantasypros.com/nfl/stats/qb.php?year=2019')
src = url.content
soup = BeautifulSoup(src, 'html.parser')

# create an empty dataframe with column names
final_2019_df = pd.DataFrame(columns = columns)

# pull in player rows
players = soup.find_all('tr', attrs = {'class': re.compile('mpb-player-')})

for player in players:
        
    # get the stats for each player
    stats = [stat.get_text() for stat in player.find_all('td')]
    
    # create a dataframe for the single player's stats
    temp_df = pd.DataFrame(stats).transpose()
    temp_df.columns = columns
    
    # Join the single player's stats with the overall dataset
    final_2019_df = pd.concat([final_2019_df, temp_df], ignore_index = True)
    
# export to csv
final_2019_df.to_csv(r"QbStats2019.csv", 
                index = False, sep = ',', encoding = 'utf-8')