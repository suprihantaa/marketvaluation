# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 19:51:32 2020

@author: Cynthia Suprihanta
"""

# Get the team ID

# import the library
import requests
import os
import pandas as pd
import json
from pandas.io.json import json_normalize 

league_code=[2,87,94,8,4,10,135,11,34,114]

all_team=[]

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "7d7db10d44mshf489ec15699a75ep19aa92jsnb2657cd7022a"
    }

    
for league_id in league_code:
    url = "https://api-football-v1.p.rapidapi.com/v2/teams/league/" + str(league_id)
    response = requests.request("GET", url, headers=headers)
    result=response.text
    resp=json.loads(result)
    #remove the bracket of the json
    team=resp['api']['teams']
    all_team+=team
    
df=json_normalize(all_team)
team_id=df[['name', 'team_id','country']].copy()

os.chdir('C:/Users/Cynthia Suprihanta/OneDrive/Aston University/Business Project/data/overall')
team_id.to_csv('all_league_id .csv', index=False)

# Get the Performance Data

# open the csv that contain league id 
df=pd.read_csv('all_league_id.csv')

headers = {
    'x-rapidapi-host': "api-football-v1.p.rapidapi.com",
    'x-rapidapi-key': "7d7db10d44mshf489ec15699a75ep19aa92jsnb2657cd7022a"
    }

################################### Premier League - England ############################

#get the list of team id 
premier_league_england=(df.loc[df['country'] == 'England'])
premier_league_england=premier_league_england['team_id'].to_list()

england= []
england += premier_league_england


#get the player stat in the team 
premier_league_player=[]



#get the data
for pl_england in england:
    url_player = "https://api-football-v1.p.rapidapi.com/v2/players/team/" +str(pl_england)+ "/2018-2019"
    response = requests.request("GET", url_player, headers=headers)
    player=json.loads(response.text)
    player=player['api']['players']
    premier_league_player += player
    
#remove unnecessary league and put the necessary league into csv
premier_league_player=json_normalize(premier_league_player)
premier_league_player=(premier_league_player.loc[premier_league_player['league'] == 'Premier League'])
premier_league_player.to_csv('1.premier_league_player.csv',index=False,encoding='utf-8-sig')


################################### La Liga - Spain #####################################


#get the list of team id 
la_liga_spain=(df.loc[df['country'] == 'Spain'])
la_liga_spain=la_liga_spain['team_id'].to_list()

spain= []
spain += la_liga_spain

#get the player stat in the team 
la_liga_player=[]

#get the data
for ll_spain in spain:
    url_player = "https://api-football-v1.p.rapidapi.com/v2/players/team/" +str(ll_spain)+ "/2018-2019"
    response = requests.request("GET", url_player, headers=headers)
    player=json.loads(response.text)
    player=player['api']['players']
    la_liga_player += player
    
#remove unnecessary league and put the necessary league into csv
la_liga_player=json_normalize(la_liga_player)
la_liga_player=(la_liga_player.loc[la_liga_player['league'] == 'La Liga'])
la_liga_player.to_csv('2.la_liga_player.csv',index=False,encoding='utf-8-sig')


################################### Serie A - Italy ######################################

#get the list of team id 
serie_a_italy=(df.loc[df['country'] == 'Italy'])
serie_a_italy=serie_a_italy['team_id'].to_list()

italy= []
italy += serie_a_italy

#get the player stat in the team 
serie_a_player=[]

#get the data
for sa_italy in italy:
    url_player = "https://api-football-v1.p.rapidapi.com/v2/players/team/" +str(sa_italy)+ "/2018-2019"
    response = requests.request("GET", url_player, headers=headers)
    player=json.loads(response.text)
    player=player['api']['players']
    serie_a_player += player
    
#remove unnecessary league and put the necessary league into csv
serie_a_player=json_normalize(serie_a_player)
serie_a_player=(serie_a_player.loc[serie_a_player['league'] == 'Serie A'])
serie_a_player.to_csv('3.serie_a_player.csv',index=False,encoding='utf-8-sig')

################################### Bundesliga - Germany #################################

#get the list of team id 
bundesliga_germany=(df.loc[df['country'] == 'Germany'])
bundesliga_germany=bundesliga_germany['team_id'].to_list()

germany= []
germany += bundesliga_germany

#get the player stat in the team 
bundesliga_player=[]

#get the data
for bl_germany in germany:
    url_player = "https://api-football-v1.p.rapidapi.com/v2/players/team/" +str(bl_germany)+ "/2018-2019"
    response = requests.request("GET", url_player, headers=headers)
    player=json.loads(response.text)
    player=player['api']['players']
    bundesliga_player += player

#remove unnecessary league and put the necessary league into csv
bundesliga_player=json_normalize(bundesliga_player)
bundesliga_player=(bundesliga_player.loc[bundesliga_player['league'] == 'Bundesliga'])
bundesliga_player.to_csv('4.bundesliga_player.csv',index=False,encoding='utf-8-sig')


################################### Ligue 1 - France ####################################

#get the list of team id 
ligue1_france=(df.loc[df['country'] == 'France'])
ligue1_france=ligue1_france['team_id'].to_list()

france= []
france += ligue1_france

#get the player stat in the team 
ligue1_player=[]

#get the data
for l1_france in france:
    url_player = "https://api-football-v1.p.rapidapi.com/v2/players/team/" +str(l1_france)+ "/2018-2019"
    response = requests.request("GET", url_player, headers=headers)
    player=json.loads(response.text)
    player=player['api']['players']
    ligue1_player += player
    
#remove unnecessary league and put the necessary league into csv
ligue1_player=json_normalize(ligue1_player)
ligue1_player=(ligue1_player.loc[ligue1_player['league'] == 'Ligue 1'])
ligue1_player.to_csv('5.ligue1_player.csv',index=False,encoding='utf-8-sig')

################################### Eredivisie - Netherlands ############################

#get the list of team id 
eredivisie_netherlands=(df.loc[df['country'] == 'Netherlands'])
eredivisie_netherlands=eredivisie_netherlands['team_id'].to_list()

netherlands= []
netherlands += eredivisie_netherlands

#get the player stat in the team 
eredivisie_player=[]

#get the data
for e_netherlands in netherlands:
    url_player = "https://api-football-v1.p.rapidapi.com/v2/players/team/" +str(e_netherlands)+ "/2018-2019"
    response = requests.request("GET", url_player, headers=headers)
    player=json.loads(response.text)
    player=player['api']['players']
    eredivisie_player += player
    
#remove unnecessary league and put the necessary league into csv
eredivisie_player=json_normalize(eredivisie_player)
eredivisie_player=(eredivisie_player.loc[eredivisie_player['league'] == 'Eredivisie'])
eredivisie_player.to_csv('6.eredivisie_player.csv',index=False,encoding='utf-8-sig')

################################### Premier Liga - Russia ############################

#get the list of team id 
premier_liga_russia=(df.loc[df['country'] == 'Russia'])
premier_liga_russia=premier_liga_russia['team_id'].to_list()

russia= []
russia += premier_liga_russia

#get the player stat in the team 
premier_liga_player=[]

#get the data
for pl_russia in russia:
    url_player = "https://api-football-v1.p.rapidapi.com/v2/players/team/" +str(pl_russia)+ "/2018-2019"
    response = requests.request("GET", url_player, headers=headers)
    player=json.loads(response.text)
    player=player['api']['players']
    premier_liga_player += player
    
#remove unnecessary league and put the necessary league into csv
premier_liga_player=json_normalize(premier_liga_player)
premier_liga_player=(premier_liga_player.loc[premier_liga_player['league'] == 'Premier League'])
premier_liga_player.to_csv('7.premier_liga_player.csv',index=False,encoding='utf-8-sig')

################################### Liga NOS - Portugal ##################################

#get the list of team id 
liga_nos_portugal=(df.loc[df['country'] == 'Portugal'])
liga_nos_portugal=liga_nos_portugal['team_id'].to_list()

portugal= []
portugal += liga_nos_portugal

#get the player stat in the team 
liga_nos_player=[]

#get the data
for ln_portugal in portugal:
    url_player = "https://api-football-v1.p.rapidapi.com/v2/players/team/" +str(ln_portugal)+ "/2018-2019"
    response = requests.request("GET", url_player, headers=headers)
    player=json.loads(response.text)
    player=player['api']['players']
    liga_nos_player += player

#remove unnecessary league and put the necessary league into csv
liga_nos_player=json_normalize(liga_nos_player)
liga_nos_player=(liga_nos_player.loc[liga_nos_player['league'] == 'Primeira Liga'])
liga_nos_player.to_csv('8.liga_nos_player.csv',index=False,encoding='utf-8-sig')

################################### Jupiler Pro - Belgium ################################

#get the list of team id 
jupiler_pro_belgium=(df.loc[df['country'] == 'Belgium'])
jupiler_pro_belgium=jupiler_pro_belgium['team_id'].to_list()

belgium= []
belgium += jupiler_pro_belgium

#get the player stat in the team 
jupiler_pro_player=[]

#get the data
for jp_belgium in belgium:
    url_player = "https://api-football-v1.p.rapidapi.com/v2/players/team/" +str(jp_belgium)+ "/2018-2019"
    response = requests.request("GET", url_player, headers=headers)
    player=json.loads(response.text)
    player=player['api']['players']
    jupiler_pro_player += player

#remove unnecessary league and put the necessary league into csv
jupiler_pro_player=json_normalize(jupiler_pro_player)
jupiler_pro_player=(jupiler_pro_player.loc[jupiler_pro_player['league'] =='First Division A'])
jupiler_pro_player.to_csv('9.jupiler_pro_player.csv',index=False,encoding='utf-8-sig')

################################### Super Lig - Turkey ###################################

#get the list of team id 
superlig_turkey=(df.loc[df['country'] == 'Turkey'])
superlig_turkey=superlig_turkey['team_id'].to_list()

turkey= []
turkey += superlig_turkey

#get the player stat in the team 
superlig_player=[]

#get the data
for sl_turkey in turkey:
    url_player = "https://api-football-v1.p.rapidapi.com/v2/players/team/" +str(sl_turkey)+ "/2018-2019"
    response = requests.request("GET", url_player, headers=headers)
    player=json.loads(response.text)
    player=player['api']['players']
    superlig_player += player

#remove unnecessary league and put the necessary league into csv
superlig_player=json_normalize(superlig_player)
superlig_player=(superlig_player.loc[superlig_player['league'] =='Süper Lig'])
superlig_player.to_csv('10.superlig_player.csv',index=False,encoding='utf-8-sig')