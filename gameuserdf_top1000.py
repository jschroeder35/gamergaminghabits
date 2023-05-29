#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 29 15:49:47 2023

@author: maria
"""

import glob
import pickle
import pandas as pd

myf=glob.glob("./raw_data/*/*.pkl")

users=[]

for filename in myf:
    with open (filename, 'rb') as file:
        users = users + pickle.load(file)
        
with open ('top1000games_may29_347pm.pkl', 'rb') as fp:
    games = pickle.load(fp)

games = list(map(int, games))
    
#dictionary to hold number of users 
gamesnusers=dict.fromkeys(games,0)

for user in users:
    for i in range(user[1]['game_count']):
        appid=user[1]['games'][i]['appid']
        if appid in games:
            gamesnusers[appid]+=1

#filter out games that have 0 owners

gamesnusersdf=pd.DataFrame(gamesnusers.values(),index=gamesnusers.keys(),columns=['Nusers'])
gamesnusersdf2=gamesnusersdf.loc[gamesnusersdf.Nusers>0]


