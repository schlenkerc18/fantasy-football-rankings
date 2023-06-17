# -*- coding: utf-8 -*-
"""
Created on Thu Jun 24 12:14:31 2021

@author: Schlenker18
"""
import pandas as pd

# reading in all player CSVs
qb_2019 = pd.read_csv("C:/Users/Schlenker18/Documents/GitHub/2021-Fantasy-Football-Rankings/StatFiles/QbStats2019.csv")
qb_2020 = pd.read_csv("C:/Users/Schlenker18/Documents/GitHub/2021-Fantasy-Football-Rankings/StatFiles/QbStats2020.csv")

rb_2019 = pd.read_csv("C:/Users/Schlenker18/Documents/GitHub/2021-Fantasy-Football-Rankings/StatFiles/RbStats2019.csv")
rb_2020 = pd.read_csv("C:/Users/Schlenker18/Documents/GitHub/2021-Fantasy-Football-Rankings/StatFiles/RbStats2020.csv")

wr_2019 = pd.read_csv("C:/Users/Schlenker18/Documents/GitHub/2021-Fantasy-Football-Rankings/StatFiles/WrStats2019.csv")
wr_2020 = pd.read_csv("C:/Users/Schlenker18/Documents/GitHub/2021-Fantasy-Football-Rankings/StatFiles/WrStats2020.csv")

te_2019 = pd.read_csv("C:/Users/Schlenker18/Documents/GitHub/2021-Fantasy-Football-Rankings/StatFiles/TeStats2019.csv")
te_2020 = pd.read_csv("C:/Users/Schlenker18/Documents/GitHub/2021-Fantasy-Football-Rankings/StatFiles/TeStats2020.csv")

# function to return string representation of a player's team
def get_player_team(string):
    start = string.find('(')
    end = string.find(')')
    return string[start+1:end]

# function returns the player without the team
def get_player(string):
    end = string.find('(')
    return string[0:end-1]
    
# function that returns dictionary of players with their respective fantasy points
# for that season, only includes players who scored points
def get_player_season(df):
    my_dict = {get_player(df['PLAYER'].iloc[i]): [df['FPTS/G'].iloc[i]] for i in range(len(df))
           if df['FPTS/G'].iloc[i] > 0}
    return my_dict

# function takes a given dictionary and adds 2nd season to a player if they
# are already in the dictionary
def add_season(my_dict, df):
    for i in range(len(df)):
        if get_player(df['PLAYER'].iloc[i]) in my_dict:
            my_dict[get_player(df['PLAYER'].iloc[i])].append(df['FPTS/G'].iloc[i])
    return my_dict

# function removes players from a dictionary if they played less than amount 
# of given seasons
def clean_dictionary(my_dict, seasons):
    new_dict = {x:y for x,y in my_dict.items() if len(y) > seasons}
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

# this function was added to remove players who are backups from a dictionary
# the intent of this is to remove most players who are not starters for successive 
# seasons from the linear regression
def remove_backups(my_dict, num):
    new_dict = {}
    add_player = True
    for x,y in my_dict.items():
        for i in range(len(y)):
            if y[i] < num:
                add_player = False
        if add_player == True:
            new_dict[x] = y
        add_player = True
    
    return new_dict
    
    new_dict = {x:y for (x,y) in my_dict if my_dict[x] > 5}
    return new_dict

# same as dict_to_series function, but returns 4 series
def dict_to_series_2(my_dict):
    # r.strip() removes trailing whitespace
    keys = [x.rstrip() for x in my_dict]
    keys = pd.Series(keys)
    
    fpts_2018 = [x[0] for x in my_dict.values()]
    fpts_2018 = pd.Series(fpts_2018)
    
    fpts_2019 = [x[1] for x in my_dict.values()]
    fpts_2019 = pd.Series(fpts_2019)
    
    fpts_2020 = [x[2] for x in my_dict.values()]
    fpts_2020 = pd.Series(fpts_2020)
    
    return keys, fpts_2018, fpts_2019, fpts_2020