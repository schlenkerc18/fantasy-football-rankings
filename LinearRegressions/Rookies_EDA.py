# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 11:43:48 2021

@author: Schlenker18
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

import Helper_Functions as hf

rb_df_18 = pd.read_csv("C:/Users/Schlenker18/Documents/GitHub/2021-Fantasy-Football-Rankings/WebScrapers/RbStats2018.csv")
rb_df_19 = pd.read_csv("C:/Users/Schlenker18/Documents/GitHub/2021-Fantasy-Football-Rankings/WebScrapers/RbStats2019.csv")
rb_df_20 = pd.read_csv("C:/Users/Schlenker18/Documents/GitHub/2021-Fantasy-Football-Rankings/WebScrapers/RbStats2020.csv")
# Analyzing jump from 1st year to 2nd year for RBs
rookie_rbs_18 = ['Saquon Barkley ', 'Nick Chubb ', 'Phillip Lindsay ', 
                 'Kerryon Johnson ', 'Sony Michel ', 'Royce Freeman ',
                 'Nyheim Hines ', 'Rashaad Penny ', 'Ito Smith ',
                 'Jordan Wilkins ', 'Josh Adams ', 'Ronald Jones II ']

rookie_rbs_19 = ['David Montgomery ', 'Darrell Henderson ', 'Josh Jacobs ',
                 'Devin Singletary ', 'Benny Snell Jr. ', 'Damien Harris ',
                 'Miles Sanders ', 'Alexander Mattison ']

rook_rb18_dict = {}
for i in range(len(rookie_rbs_18)):
    for j in range(len(rb_df_18)):
        if hf.get_player(rb_df_18['PLAYER'].iloc[j]) == rookie_rbs_18[i]:
            rook_rb18_dict[rookie_rbs_18[i]] = [rb_df_18['FPTS/G'].iloc[j]]
            
rook_rb18_dict = hf.add_season_2(rook_rb18_dict, rb_df_19)
rook_rb18_dict = hf.add_season_2(rook_rb18_dict, rb_df_20)

rook_rb19_dict = {}
for i in range(len(rookie_rbs_19)):
    for j in range(len(rb_df_19)):
        if hf.get_player(rb_df_19['PLAYER'].iloc[j]) == rookie_rbs_19[i]:
            rook_rb19_dict[rookie_rbs_19[i]] = [rb_df_19['FPTS/G'].iloc[j]]

rook_rb19_dict = hf.add_season_2(rook_rb19_dict, rb_df_20)       