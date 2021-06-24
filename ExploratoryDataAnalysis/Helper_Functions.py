# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 12:14:31 2021

@author: Schlenker18
"""
import pandas as pd

# reading in all player CSVs
qb_2019 = pd.read_csv("C:/Users/Schlenker18/Documents/GitHub/2021-Fantasy-Football-Rankings/WebScrapers/QbStats2019.csv")
qb_2020 = pd.read_csv("C:/Users/Schlenker18/Documents/GitHub/2021-Fantasy-Football-Rankings/WebScrapers/QbStats2020.csv")

rb_2019 = pd.read_csv("C:/Users/Schlenker18/Documents/GitHub/2021-Fantasy-Football-Rankings/WebScrapers/RbStats2019.csv")
rb_2020 = pd.read_csv("C:/Users/Schlenker18/Documents/GitHub/2021-Fantasy-Football-Rankings/WebScrapers/RbStats2020.csv")

wr_2019 = pd.read_csv("C:/Users/Schlenker18/Documents/GitHub/2021-Fantasy-Football-Rankings/WebScrapers/WrStats2019.csv")
wr_2020 = pd.read_csv("C:/Users/Schlenker18/Documents/GitHub/2021-Fantasy-Football-Rankings/WebScrapers/WrStats2020.csv")

te_2019 = pd.read_csv("C:/Users/Schlenker18/Documents/GitHub/2021-Fantasy-Football-Rankings/WebScrapers/TeStats2019.csv")
te_2020 = pd.read_csv("C:/Users/Schlenker18/Documents/GitHub/2021-Fantasy-Football-Rankings/WebScrapers/TeStats2020.csv")

# final 2020 o-line rankings according to ProFootballFocus(PFF)
off_line_ranks = {'CLE': 1, 'GB': 2, 'LAR': 3, 'NE': 4, 'TB': 5, 'WAS': 6, 'IND': 7,
                  'NO': 8, 'SF': 9, 'BUF': 10, 'KC': 11, 'ARI': 12, 'DET': 13, 
                  'SEA': 14, 'TEN': 15, 'BAL': 16, 'PIT': 17, 'CAR': 18, 'PHI': 19,
                  'CHI': 20, 'ATL': 21, 'JAC': 22, 'HOU': 23, 'LV': 24, 'DEN': 25,
                  'MIN': 26, 'DAL': 27, 'MIA': 28, 'NYJ': 29, 'CIN': 30, 'NYG':31,
                  'LAC': 32, 'FA': 33}

# function to return string representation of a player's team
def get_player_team(string):
    start = string.find('(')
    end = string.find(')')
    return string[start+1:end]

# function that returns dictionary of players with their respective fantasy points
# for that season, only includes players who scored points
def get_player_season(df):
    my_dict = {df['PLAYER'].iloc[i]: [df['FPTS/G'].iloc[i]] for i in range(len(df))
           if df['FPTS/G'].iloc[i] > 0}
    return my_dict

# function takes a given dictionary and adds 2nd season to a player if they
# are already in the dictionary
def add_season(my_dict, df):
    for i in range(len(df)):
        if df['PLAYER'].iloc[i] in my_dict:
            my_dict[df['PLAYER'].iloc[i]].append(df['FPTS/G'].iloc[i])
    return my_dict

# function removes players from a dictionary if they played only one season
def clean_dictionary(my_dict):
    new_dict = {x:y for x,y in my_dict.items() if len(y) > 1}
    return new_dict

# function takes keys and values and returns pandas Series
# these series can then easily be converted into dataframe
def dict_to_series(my_dict):
    # r.strip() removes trailing whitespace
    keys = [x.rstrip() for x in my_dict]
    keys = pd.Series(keys)
    
    fpts_2019 = [x[0] for x in my_dict.values()]
    fpts_2019 = pd.Series(fpts_2019)
    
    fpts_2020 = [x[1] for x in my_dict.values()]
    fpts_2020 = pd.Series(fpts_2020)
    
    return keys, fpts_2019, fpts_2020
    
# filling o_line list with ratings
# off_line_rank = []
# for i in range(len(players)):
#     p = get_player_team(players[i])
#     if (off_line_ranks[p] <= 16):
#         off_line_rank.append(1)
#     else:
#         off_line_rank.append(0)