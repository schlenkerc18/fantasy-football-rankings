# -*- coding: utf-8 -*-
"""
Created on Tue Jun 22 11:12:50 2021

@author: Schlenker18
"""

# using https://www.codecademy.com/resources/blog/web-scraping-python-beautiful-soup-mlb-stats/
# as a guide to pull stats from fantasypros

import pandas as pd
import re
import requests
from bs4 import BeautifulSoup

# create column names
columns = ['RANK', 'PLAYER', 'REC', 'TGT', 'YDS', 'Y/R', 'LG', '20+', 'TD', 
          'ATT', 'YDS', 'TD', 'FL', 'G', 'FPTS', 'FPTS/G', 'OWN']

def scrape_data(year):
    url = requests.get(f'https://www.fantasypros.com/nfl/stats/te.php?year={year}')
    src = url.content
    soup = BeautifulSoup(src, 'html.parser')
    
    final_df = pd.DataFrame(columns = columns)

    # pull in player rows
    players = soup.find_all('tr', attrs = {'class': re.compile('mpb-player-')})
    
    for player in players:
            
        # get the stats for each player
        stats = [stat.get_text() for stat in player.find_all('td')]
        
        # create a dataframe for the single player's stats
        temp_df = pd.DataFrame(stats).transpose()
        temp_df.columns = columns
        
        # Join the single player's stats with the overall dataset
        final_df = pd.concat([final_df, temp_df], ignore_index = True)
        
    csv_name = 'TeStats' + year + '.csv'
    # export to csv
    final_df.to_csv(csv_name, 
                    index = False, sep = ',', encoding = 'utf-8')
    
# create list of years to scrape, then call function on each year
years_to_scrape = ['2018', '2019', '2020', '2021']

for year in years_to_scrape:
    scrape_data(year)