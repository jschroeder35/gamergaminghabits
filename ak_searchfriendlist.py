#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Author: Aycan Katitas
Date: 05/25/2023 
Description: Get collected user id's friends 
"""

from steam import Steam
from decouple import config
import random
from time import sleep
import pickle
import os
import sys
import pandas as pd
import traceback

pd.options.display.max_columns = 100


# Setting up the script
with open("myapikey.txt", "r") as file:
    myapikey=file.read()
    
os.environ["STEAM_API_KEY"] = myapikey
KEY = config("STEAM_API_KEY")
steam = Steam(KEY)


validid_txts = ['valid_ids.txt','ak_valid_ids.txt','ak_valid_ids2.txt']
validid_list = []

for i in validid_txts: 
    path_name = "raw_data/" + i
    with open(path_name, 'r') as file:
        valid=file.read().splitlines()
        validid_list.append(valid)
        
validid_list_l = [item for sublist in validid_list for item in sublist]     

#validid_list_l =  validid_list_l[:10]

validid_list_s = set(validid_list_l)


friend_ids = set()

# '76561198084324477' - this is a public user but it still raises an error 
for j in range(len(validid_list_l)):
    # some users raise "401 Unauthorized" error - some sites say it is the private users but when I checked that was
    # not the problem. The problematic user id is from Russia, so I don't know if it has to do with that
    # dealing with the problem with try/except
    try:
        temp = steam.users.get_user_friends_list(validid_list_l[j])
        temp2 = dict((item['steamid'], item) for item in temp['friends'])
        list_ids = list(temp2.keys())
        for k in list_ids:
            if k not in validid_list_s | friend_ids:
                friend_ids.add(k)
        #sleep(0.1)
    except Exception as exc:
        print(validid_list_l[j])
        print(exc)

friend_ids = list(friend_ids)

with open('raw_data/friendlist_ids.txt', 'a') as file:
    for id in friend_ids:
        file.write(id+"\n")

   
        
    
    
    
