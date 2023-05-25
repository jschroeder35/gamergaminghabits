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

#initial test of 3 people
#testflids=['76561198009190429','76561198048895718','76561198014795926']

#whole friend list 
testflids=[]

for i in range(len(testfl['friends'])):
    testflids.append(testfl['friends'][i]['steamid'])

testgamelist=steam.users.get_owned_games(testid)

appids=[]

playtimes=[]

for i in range(testgamelist['game_count']):
    appids.append(testgamelist['games'][i]['appid'])
    playtimes.append(testgamelist['games'][i]['playtime_forever'])
    
#make game ids the rows
#make player ids the columns
#entries will be the total playtime in that game
#This is for easier entry into the dataframe, then we can transpose (hopefully)

testdf=pd.DataFrame({int(testid):playtimes},index=appids) #initialize the df

for j in range(len(testflids)):
    appidstemp=[]
    playtimestemp=[]
    gamelisttemp=steam.users.get_owned_games(testflids[j])
    
    #in case of empty game list
    if gamelisttemp=={}:
        continue
    
    for i in range(gamelisttemp['game_count']):
        appidstemp.append(gamelisttemp['games'][i]['appid'])
        playtimestemp.append(gamelisttemp['games'][i]['playtime_forever'])
       
    testdf[int(testflids[j])]='NO' #preemptively sets all games already in the df to 'NO - Not Owned'
        
    playtimestemp=pd.Series(playtimestemp,index=appidstemp)
    
    #Now loop to figure out which games have already been added, if not, add a new
    # entry.  Should also go back and add 'Not Owned' or something to games 
    # not owned.
        
    for appid in appidstemp:
        if appid in testdf.index:
            #enter the playtime if game alreaady exists in df
            testdf[int(testflids[j])][appid]=playtimestemp[appid]
        else: #create the entry in the df
            newrow=['NO']*(len(testdf.columns)-1) #assigns No('not owned' to previous ids)
            newrow.append(playtimestemp[appid])
            testdf.loc[appid]=newrow
    
    