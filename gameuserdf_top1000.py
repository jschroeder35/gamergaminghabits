#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 29 15:49:47 2023

@author: maria
"""

import glob
import pickle
import pandas as pd
import numpy as np

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

gamesnu_ser=pd.Series(gamesnusers.values(),index=gamesnusers.keys())
gamesnu_ser2=gamesnu_ser.loc[gamesnu_ser>0]

#gup = games,users,playtimes dataframe
#make game ids the rows
#make player ids the columns
#entries will be the total playtime in that game

gupdf=pd.DataFrame(index=gamesnu_ser2.index)

j=0
for user in users:
    print(j)
    usercol=pd.Series(np.nan,index=gupdf.index)
    for i in range(user[1]['game_count']):
        appid=user[1]['games'][i]['appid']
        if appid in gupdf.index:
            usercol[appid]=user[1]['games'][i]['playtime_forever']
        gupdf[int(user[0])]=usercol
    
    #to prevent warnings of defragmented dataframe
    defrag=gupdf.copy()
    del(gupdf)
    gupdf=defrag
    del(defrag)
    
    j=j+1

