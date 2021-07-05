# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 19:20:43 2021

@author: Schlenker18
"""

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

rel_diff = {}

for x,y in off_line_ranks_19.items():
    if x in off_line_ranks_20:
        diff = off_line_ranks_19[x] - off_line_ranks_20[x]
        rel_diff[x] = diff