# -*- coding: utf-8 -*-
"""
Author: Aycan Katitas
Date: 05/13/2023
Description: Learning how to use steam api
"""

import requests

#KEY = <YOUR_KEY_HERE>
ID = '76561199505328285'
ID = '76561197960435530'
ID = '76561198119266856'


# Get owned games 
slink1 = "http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key="
slink2 = "&steamid=" + ID + "&format=json"
slink = slink1 + KEY + slink2

r = requests.get(slink)
print(r.status_code)
steam=r.json()
print(steam)

# Get player summaries 
slink1 = "https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key="
slink2 = "&steamids=" + ID
slink= slink1 + KEY + slink2

r = requests.get(slink)
print(r.status_code)

# Get friend list 
slink1 = "http://api.steampowered.com/ISteamUser/GetFriendList/v001/?key="
slink2 = "&steamid=" +ID
slink = slink1 + KEY + slink2

r = requests.get(slink)
print(r.status_code)

steam=r.json()
print(steam)

slink1 = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key="
slink2 = "&steamid=" + ID + "&format=json"
slink = slink1 + KEY + slink2

r = requests.get(slink)
print(r.status_code)

steam = r.json()

print(steam)
