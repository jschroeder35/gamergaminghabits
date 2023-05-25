#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 24 23:21:31 2023

@author: maria
"""

import steamspypi
import glob
import pickle

myf=glob.glob("./raw_data/maria_test1/*.pkl")

users=[]

for filename in myf:
    with open (filename, 'rb') as file:
        users = users + pickle.load(file)
                
genres=['Action','Strategy','RPG','Indie','Adventure','Sports','Simulation','MMO','Casual','Racing']
        
dict_template={
    "action_playtime":0,
    "strategy_playtime":0,
    "rpg_playtime":0,
    "indie_playtime":0,
    "adventure_playtime":0,
    "sports_playtime":0,
    "simulation_playtime":0,
    "mmo_playtime":0,
    "casual_playtime":0,
    "racing_playtime":0
    } 

game_genres={}

spy_request=dict()
spy_request['request']='appdetails'

for j in range(len(users)):
    
    print(j)
    users[j].append(dict_template)
    
    for i in range(users[j][1]['game_count']): 
        
        tempgameid=users[j][1]['games'][i]['appid']
        tempgameplaytime=users[j][1]['games'][i]['playtime_forever']
        
        if tempgameid not in game_genres.keys():
            spy_request['appid']=tempgameid
            spy_return=steamspypi.download(spy_request)
            game_genres[tempgameid]=spy_return['genre'].split(", ")
            
        for genre in game_genres[tempgameid]:
            match genre:
                case "Action":
                    users[j][2]["action_playtime"]+=tempgameplaytime
                case "Strategy":
                    users[j][2]["strategy_playtime"]+=tempgameplaytime
                case "RPG":
                    users[j][2]["rpg_playtime"]+=tempgameplaytime
                case "Indie":
                    users[j][2]["indie_playtime"]+=tempgameplaytime
                case "Adventure":
                    users[j][2]["adventure_playtime"]+=tempgameplaytime       
                case "Sports":
                    users[j][2]["sports_playtime"]+=tempgameplaytime
                case "Simulation":
                    users[j][2]["simulation_playtime"]+=tempgameplaytime
                case "Massively Multiplayer":
                    users[j][2]["mmo_playtime"]+=tempgameplaytime
                case "Casual":
                    users[j][2]["casual_playtime"]+=tempgameplaytime
                case "Racing":
                    users[j][2]["casual_playtime"]+=tempgameplaytime
     
    dict_template2={"total_playtime":0}               
     
    users[j].append(dict_template2)
    
    users[j][3]['total_playtime']=sum(users[j][2].values())
    
    users[j][3]['topgenre1']=max(users[j][2],key=users[j][2].get)
    
    users[j][3]['topgenre2']=list(users[j][2].keys())[list(users[j][2].values()).index(sorted(users[j][2].values(),reverse=True)[1])]
    
    users[j][3]['topgenre3']=list(users[j][2].keys())[list(users[j][2].values()).index(sorted(users[j][2].values(),reverse=True)[2])]
                    
