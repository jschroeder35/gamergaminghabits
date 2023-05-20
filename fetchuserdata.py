#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Aycan Katitas
Date: 05/19/2023
Description: Get info on owned games of users using Steam API
"""

import requests
import json
import os
from decouple import config
import numpy as np
import pandas as pd

# Show all columns 
pd.options.display.max_columns = 100

with open("myapikey.txt", "r") as file:
    myapikey=file.read()

os.environ["STEAM_API_KEY"] = myapikey
KEY = config("STEAM_API_KEY")

idlist = ['76561199505328285','76561197960435530','76561198119266856','76561198039393086']

# Function to connect with API 

final_df=pd.DataFrame()

for i in idlist:
    # For Owned Games
    # put in a request
    slink1 = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key="
    slink2 = "&steamid=" + i + "&format=json"
    slink = slink1 + KEY + slink2
    response = requests.get(slink)
    r = response.json()
    
    # Turn json file into data frame 
    try:
        df = pd.json_normalize(r,['response','games'],
                                [['response','game_count']])
        df['userid'] = i
        final_df=pd.concat([final_df,df])
    except KeyError:
        print("User ID", i, "has no information available.")
        