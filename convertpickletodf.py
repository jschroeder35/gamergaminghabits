#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Aycan Katitas
Date: 05/19/2023
Description: Convert pickle files into data frames
"""

import csv
import datetime as dt
import json
import os
import statistics
import time
import numpy as np
import pandas as pd
import requests
import pickle

pd.options.display.max_columns = 100

with open ('./raw_data/game_data_0.pkl', 'rb') as fp:
    loaded_data = pickle.load(fp)

# Turn json files into data frame 
df = pd.DataFrame(loaded_data, columns = ['userid', 'game_info'])

# Normalize the first dictionary and join it with the original data frame 
normalize = pd.json_normalize(df.pop('game_info'))
df_merge = df.join(normalize)

# games column is a list so explode the list - normalize games and merge it back with the original df
df_explode = df_merge.explode('games', ignore_index=True)
normalize2 = pd.json_normalize(df_explode.pop('games'))
df_fin = df_explode.join(normalize2)


    
    

