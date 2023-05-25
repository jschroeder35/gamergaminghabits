#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 24 17:22:09 2023

@author: maria
"""

import pandas as pd
import glob
import pickle

myf=glob.glob("./raw_data/*/*.pkl")

loaded_data=[]

for filename in myf:
    with open (filename, 'rb') as file:
        loaded_data = loaded_data + pickle.load(file)
           
firstuser=loaded_data[0]

appids=[]

playtimes=[]

for i in range(firstuser[1]['game_count']):
    appids.append(firstuser[1]['games'][i]['appid'])
    playtimes.append(firstuser[1]['games'][i]['playtime_forever'])
    
#gup = games,users,playtimes dataframe
#make game ids the rows
#make player ids the columns
#entries will be the total playtime in that game
#This is for easier entry into the dataframe, then we can transpose (hopefully)

gupdf=pd.DataFrame({int(firstuser[0]):playtimes},index=appids) #initialize the df

for j in range(1,len(loaded_data)):
    appidstemp=[]
    playtimestemp=[]
    usertemp=loaded_data[j]
    
    for i in range(usertemp[1]['game_count']):
        appidstemp.append(usertemp[1]['games'][i]['appid'])
        playtimestemp.append(usertemp[1]['games'][i]['playtime_forever'])
       
    gupdf[int(usertemp[0])]='NO' #preemptively sets all games already in the df to 'NO - Not Owned'
        
    playtimestemp=pd.Series(playtimestemp,index=appidstemp,dtype='Int32')
    
    #Now loop to figure out which games have already been added, if not, add a new
    # entry.  Should also go back and add 'Not Owned' or something to games 
    # not owned.
        
    for appid in appidstemp:
        if appid in gupdf.index:
            #enter the playtime if game alreaady exists in df
            gupdf[int(usertemp[0])][appid]=playtimestemp[appid]
        else: #create the entry in the df
            newrow=['NO']*(len(gupdf.columns)-1) #assigns No('not owned' to previous ids)
            newrow.append(playtimestemp[appid])
            gupdf.loc[appid]=newrow
            
    defrag=gupdf.copy()
    del(gupdf)
    gupdf=defrag
    del(defrag)
    
    print(j)
            