# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 19:20:43 2021

@author: Schlenker18
"""

# final 2019 rankings according to ProFootballFocus
# https://www.pff.com/news/nfl-offensive-line-rankings-following-2019-regular-season
off_line_ranks_19 = {'PHI':1, 'BAL':2, 'IND':3, 'DAL':4, 'NO':5, 'GB':6,
                     'TB':7, 'TEN':8, 'PIT':9, 'NE':10, 'DET':11, 'DEN':12,
                     'WAS':13, 'SF':14, 'LV':15, 'KC':16, 'NYG':17, 'CAR':18,
                     'MIN':19, 'HOU':20, 'BUF':21, 'ARI':22, 'CLE':23, 'ATL':24,
                     'CHI':25, 'JAC':26, 'SEA':27, 'NYJ':28, 'LAC':29, 'CIN':30,
                     'LAR':31, 'MIA':32, 'FA':33}

# final 2020 o-line rankings according to ProFootballFocus(PFF)
# https://www.pff.com/news/nfl-final-2020-offensive-line-rankings
off_line_ranks_20 = {'CLE':1, 'GB':2, 'LAR':3, 'NE':4, 'TB':5, 'WAS':6, 'IND':7,
                  'NO':8, 'SF':9, 'BUF':10, 'KC':11, 'ARI':12, 'DET':13, 
                  'SEA': 14, 'TEN': 15, 'BAL': 16, 'PIT': 17, 'CAR': 18, 'PHI': 19,
                  'CHI': 20, 'ATL': 21, 'JAC': 22, 'HOU': 23, 'LV': 24, 'DEN': 25,
                  'MIN': 26, 'DAL': 27, 'MIA': 28, 'NYJ': 29, 'CIN': 30, 'NYG':31,
                  'LAC': 32, 'FA': 33}

# WR group ranking entering the 2019 season according to PFF
# https://www.pff.com/news/pro-nfl-receiving-corps-rankings-all-32-teams-entering-2019
wr_group_ranks_19 = {'PHI':1, 'ATL':2, 'LAR':3, 'KC':4, 'HOU':5, 'CLE':6,
                     'TB':7, 'MIN':8, 'LAC':9, 'CIN':10, 'CHI':11, 'LV':12,
                     'NO':13, 'PIT':14, 'DET':15, 'DEN':16, 'TEN':17, 'SF': 18,
                     'DAL':19, 'GB':20, 'IND':21, 'CAR':22, 'BUF':23, 'ARI':24,
                     'SEA':25, 'NE':26, 'NYG':27, 'WAS':28, 'NYJ':29, 'MIA':30,
                     'BAL':31, 'JAC':32, 'FA': 33}

# WR group ranking entering the 2020 season according to PFF
# https://www.pff.com/news/nfl-2020-nfl-season-receiving-corps-rankings
wr_group_ranks_20 = {'TB':1, 'KC':2, 'DAL':3, 'NO':4, 'BUF':5, 'DET':6, 'LAC':7,
                     'CAR':8, 'CLE':9, 'DEN':10, 'CIN': 11, 'ARI':12, 'ATL':13,
                     'PHI':14, 'LAR':15, 'SF':16, 'SEA':17, 'PIT':18, 'LV':19,
                     'HOU':20, 'NYG':21, 'IND':22, 'TEN':23, 'MIN':24, 'BAL':25,
                     'GB':26, 'CHI':27, 'NYJ':28, 'MIA':29, 'NE':30, 'JAC':31,
                     'WAS':32, 'FA':33}
        
# function returns difference in o-line ranking from 2019 to 2020
def get_oline_diff(s1, s2):
    return off_line_ranks_19[s1] - off_line_ranks_20[s2]

# function returns difference in wr group rank from 2019 to 2020
def get_wr_diff(s1, s2):
    return wr_group_ranks_19[s1] - wr_group_ranks_20[s2]