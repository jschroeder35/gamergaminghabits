# -*- coding: utf-8 -*-
"""
Created on Fri May 19 13:25:23 2023

@author: Maria
"""

from steam import Steam
from decouple import config
import pandas as pd

with open("myapikey.txt", "r") as file:
    myapikey=file.read()
    
import os
os.environ["STEAM_API_KEY"] = myapikey
KEY = config("STEAM_API_KEY")
steam = Steam(KEY)

testid='76561198039393086'

testfl=steam.users.get_user_friends_list(testid)

testgamelist=steam.users.get_owned_games(testid)

appids=[]

playtimes=[]

for i in range(testgamelist['game_count']):
    appids.append(testgamelist['games'][i]['appid'])
    playtimes.append(testgamelist['games'][i]['playtime_forever'])
    
#make player ids be the index
#game ids be the columns
#entries will be the playtime
#oh god do we have to do a loop
