#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Aycan Katitas
Date: 05/19/2023
Description: Getting information on games using steamspy api
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
import math

pd.options.display.max_columns = 100

with open ('./raw_data/aycan_pckfiles/ak_game_data_0.pkl', 'rb') as fp:
    loaded_data = pickle.load(fp)
    
loaded_data

# Turn json files into data frame 
df = pd.DataFrame(loaded_data, columns = ['userid', 'game_info'])

# Normalize the first dictionary and join it with the original data frame 
normalize = pd.json_normalize(df.pop('game_info'))
df_merge = df.join(normalize)

# games column is a list so explode the list - normalize games and merge it back with the original df
df_explode = df_merge.explode('games', ignore_index=True)
normalize2 = pd.json_normalize(df_explode.pop('games'))
df_fin = df_explode.join(normalize2)

appids = df_fin['appid'].values.tolist()
appids2 = [int(x) for x in appids if math.isnan(x) is False]

x = appids2[:4]
games = []
url = "https://steamspy.com/api.php"
# Fetch information about games using steamspy api 
for g in x: 
    parameters = {"request": "appdetails",
                  "appid": g}
    response = requests.get(url, parameters)
    temp = response.json()
    games.append(temp)

# tags are stored as dictionary in a columns     
games_df = pd.DataFrame.from_dict(games,orient="columns")

# If we want each tag to have its own row, we can do this 
#games_df2 = games_df.explode('tags')

