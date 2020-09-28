# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 20:41:30 2020

@author: Cynthia Suprihanta
"""

# import the library

import pandas as pd
import os
import numpy as np

############################## COMBINE DATA SET ########################################

# import performance and id dataframe
os.chdir('C:/Users/Cynthia Suprihanta/OneDrive/Aston University/Business Project/data')
df_id_perf=pd.read_csv('final_df.csv')

# create query columns to use as index to combine with youtube
df_id_perf['Query'] = df_id_perf[['Player Name', 'Club Name']].agg(' '.join, axis=1)
df_id_perf[df_id_perf['Player Name'].isnull()]
df_id_perf.columns

# import youtube result
os.chdir('C:/Users/Cynthia Suprihanta/OneDrive/Aston University/Business Project/data/preprocess 01july/youtube/youtube_result')
df_youtube = pd.read_csv('youtube_result.csv')
df_youtube = df_youtube.drop('Unnamed: 0', 1)

# import twitter result
os.chdir('C:/Users/Cynthia Suprihanta/OneDrive/Aston University/Business Project/data/preprocess 01july/youtube/twitter_result')
df_twitter=pd.read_csv('twitter_result.csv')
df_twitter = df_twitter.drop('Unnamed: 0', 1)

# import google result
os.chdir('C:/Users/Cynthia Suprihanta/OneDrive/Aston University/Business Project/data/preprocess 01july/youtube/google_result')
df_google=pd.read_csv('google_result.csv')
df_google = df_google.drop('Unnamed: 0', 1)


# rename 'name' columns into 'Query'
df_youtube=df_youtube.rename(columns = {'name':'Query'})
df_twitter=df_twitter.rename(columns = {'Player Name':'Query'})
df_google=df_google.rename(columns = {'name':'Query'})


# combine performance, id, and popularity
df_id_perf.shape[0]
df_youtube.shape[0]
df_twitter.shape[0]
df_google.shape[0]



# combine the id, performance and youtube result
df1=pd.merge(df_id_perf,df_youtube, how='right',left_on=['Query'],right_on=['Query'])
df1


# combine with twitter result
df2=pd.merge(df_twitter,df1, how='right',left_on=['Query'],right_on=['Query'])
df2

# combine with google result
df=pd.merge(df_google,df2, how='right',left_on=['Query'],right_on=['Query'])
df.columns

############################## INSERT CLUB FEATURES ########################################
# insert club market value
os.chdir('C:/Users/Cynthia Suprihanta/OneDrive/Aston University/Business Project/data')
club_mv=pd.read_csv('club mv.csv')
club_mv.columns

df['club market value'] = df['Club Name'].map(club_mv.set_index('Club Name')['Club Market Value'])
df['club market value'].unique()
df.loc[df['club market value']==np.nan]

# remove the € and change it into real number

df['club market value'] = df['club market value'].str.replace('€', '')

df['club market value'] = (df['club market value'].replace(r'[bnm]+$', '', regex=True).astype(float) * \
                      df['club market value'].str.extract(r'[\d\.]+([bnm]+)', expand=False)
                      .fillna(1)
                      .replace(['bn','m'], [10**9, 10**6]).astype(int))
    
df['club market value']
df

# insert club game 
os.chdir('C:/Users/Cynthia Suprihanta/OneDrive/Aston University/Business Project/data')
club_game=pd.read_csv('club game.csv')
club_game.columns

df['club match played'] = df['Club Name'].map(club_game.set_index('Club Name')['Match Played'])
df['club match won'] = df['Club Name'].map(club_game.set_index('Club Name')['Match Won'])
df['club match draw'] = df['Club Name'].map(club_game.set_index('Club Name')['Match Draw'])
df['club match lose'] = df['Club Name'].map(club_game.set_index('Club Name')['Match Lose'])
df['club total goals'] = df['Club Name'].map(club_game.set_index('Club Name')['Total Goals'])
df['club goals conceded'] = df['Club Name'].map(club_game.set_index('Club Name')['Total Goals Conceded'])

############################## REMOVE UNNECESSARY COLUMNS ########################################
df.columns
# remove unnecessary columns
df.drop(['Query','birth_date','Height','birth_place',
         'birth_country','age','season','team_id'], axis=1, inplace=True)


############################## CHECK NATIONALITY ########################################
# check the difference between Nationality and nationality

df.loc[df['Nationality'] == df['nationality']]
diff_nationality = df.loc[df['Nationality'] != df['nationality']]
diff_nationality = diff_nationality[['Player Name','Nationality', 'nationality']].copy()

diff_nationality[0:50]
diff_nationality[50:100]
diff_nationality[100:150]
diff_nationality[150:200]
diff_nationality[200:244]

# change the similar nationality and Nationality
df.replace({'Nationality' : 
                          {'Korea, South' : 'Korea Republic', 
                           'Bosnia-Herzegovina' : 'Bosnia and Herzegovina', 
                           'DR Congo' : 'Congo DR',
                           'United States' : 'USA',
                           'The Gambia' : 'Gambia'},
                          'nationality' :
                              {'Republic of Ireland' : 'Ireland',
                              'Cape Verde Islands' : 'Cape Verde',
                              'China PR' : 'China',
                              'Kyrgyz Republic' : 'Kyrgyzstan'}},inplace=True)
    
# check the Nationality and nationality that completely different
    
diff_nationality = df.loc[df['Nationality'] != df['nationality']]
diff_nationality = diff_nationality[['Player Name','Nationality', 'nationality']].copy()
diff_nationality[0:54]
diff_nationality[54:108]

df.loc[df['Player Name'] == 'adrien tameze', 'Nationality'] = 'France'
df.loc[df['Player Name'] == 'pierre-yves polomat', 'Nationality'] = 'France'
df.loc[df['Player Name'] == 'neven subotic', 'Nationality'] = 'Serbia'
df.loc[df['Player Name'] == 'matis carvalho', 'Nationality'] = 'France'
df.loc[df['Player Name'] == 'sory doumbouya', 'Nationality'] = 'France'
df.loc[df['Player Name'] == 'hassane kamara', 'Nationality'] = 'Gambia'
df.loc[df['Player Name'] == 'dennis jastrzembski', 'Nationality'] = 'Germany'
df.loc[df['Player Name'] == 'senna miangue', 'Nationality'] = 'Belgium'
df.loc[df['Player Name'] == 'eric asomani', 'Nationality'] = 'Belgium'
df.loc[df['Player Name'] == 'loret sadiku', 'Nationality'] = 'Kosovo'
df.loc[df['Player Name'] == 'erman herman vardar', 'Nationality'] = 'Sweden'
df.loc[df['Player Name'] == 'gregoire defrel', 'Nationality'] = 'France'
df.loc[df['Player Name'] == 'iliass bel hassani', 'Nationality'] = 'Morocco'
df.loc[df['Player Name'] == 'kingsley ehizibue', 'Nationality'] = 'Netherlands'
df.loc[df['Player Name'] == 'ouasim bouy', 'Nationality'] = 'Netherlands'
df.loc[df['Player Name'] == 'dehninio muringen', 'Nationality'] = 'Suriname'
df.loc[df['Player Name'] == 'dogucan haspolat', 'Nationality'] = 'Netherlands'
df.loc[df['Player Name'] == 'carlito fermina', 'Nationality'] = 'Netherlands'
df.loc[df['Player Name'] == 'agil etemadi', 'Nationality'] = 'Netherlands'
df.loc[df['Player Name'] == 'anthony van den hurk', 'Nationality'] = 'Netherlands'
df.loc[df['Player Name'] == 'marko obradovic', 'Nationality'] = 'Montenegro'
df.loc[df['Player Name'] == 'alex dos santos', 'Nationality'] = 'Brazil'

diff_nationality = df.loc[df['Nationality'] != df['nationality']]
diff_nationality = diff_nationality[['Player Name','Nationality', 'nationality']].copy()

diff_nationality[0:43]
diff_nationality[43:86]

# remove 'nationality' since its no longer relevant
df.drop(['nationality'], axis=1, inplace=True)
df.columns
df



############################## CHECK POSITION ########################################

# check the difference between Position and position
df['Position'].unique()
df['position'].unique()

# check nan 
df['Position'].isna().sum()
df['position'].isna().sum()

# input the nan of 'position' with 'Position' value
df.position.fillna(df.Position, inplace=True)

# equalize the new value of Position from position
df.replace({'position':{'Attacking Midfield':'Midfielder'}},inplace=True)
df.replace({'position':{'Left Winger':'Attacker'}},inplace=True)

# remove 'Position' since its no longer relevant
df.drop(['Position'], axis=1, inplace=True)
df.columns
df['position'].unique()

############################## CHANGE MARKET VALUE ########################################

# change market value into real number
df['Market Value'].unique()

# change '-' into NaN
df.loc[df['Market Value']=='-']
df['Market Value'] = df['Market Value'].replace('-', np.nan)
df['Market Value'].unique()

df['Market Value'] = (df['Market Value'].replace(r'[Th.m]+$', '', regex=True).astype(float) * \
                      df['Market Value'].str.extract(r'[\d\.]+([Th.m]+)', expand=False)
                      .fillna(1)
                      .replace(['Th.','m'], [10**3, 10**6]).astype(int))

df['Market Value'].unique()

# drop the NaN in the 'market value'
df = df[df['Market Value'].notna()]
df.reset_index(drop=True, inplace=True)
df['Market Value'].max()
df['Market Value'].min()
df

############################## CHANGE CAPTAIN TO BOOL ########################################
# change captain into bool
df['captain'] = [int(i>0) for i in df['captain']]
df['captain']=df['captain'].astype(bool)

############################## DOB ########################################
# retrieve age per July 1st, 2018
df['DoB(age)'] = df['DoB(age)'].str.extract(r"\(([0-5][0-9]+)\)", expand=False)
df.rename({'DoB(age)':'Age'},axis=1,inplace=True)
df['Age']=df['Age'].astype('int64')

############################## CONTRACT EXPIRED ########################################
# change the format into date

df.loc[df['Contract Expired']=='-']
df.replace({'Contract Expired':{'-': np.NaN}},inplace=True)

df.columns
df['Contract Expired'] 
df['Contract Expired'] =  pd.to_datetime(df['Contract Expired'], infer_datetime_format=True)

# create new dataframe that contains the date when the market value data taken
marketvalue_taken = pd.DataFrame({'date':['2018-07-01']*5313})
marketvalue_taken['date'] = pd.to_datetime(marketvalue_taken['date'])

# find the duration (in years) from when contract taken to contract due date
a = df['Contract Expired'] - marketvalue_taken['date']
df['Contract Expired'] = a/np.timedelta64(1,'Y')

############################## HEIGHT AND WEIGHT #######################################################

# change height and weight into float64
df['height'] = df['height'].replace({'cm':''}, regex = True).astype(float)
df['weight'] = df['weight'].replace({'kg':''}, regex = True).astype(float)
df

################ PUT 0 INTO NP.NAN IN YOUTUBE AND TWITTER ##################################

# twitter
df.replace({'avgretweets':{np.NaN: 0}},inplace=True)
df.replace({'avglikes':{np.NaN: 0}},inplace=True)

# youtube
df.replace({'YoutubeAvgViewCount':{np.NaN: 0}},inplace=True)
df.replace({'YoutubeAvglikeCount':{np.NaN: 0}},inplace=True)
df.replace({'YoutubeAvgDislikeCount':{np.NaN: 0}},inplace=True)
df.replace({'YoutubeAvgCommentCount':{np.NaN: 0}},inplace=True)

df.info()

############################## CHANGE ALL COLUMNS INTO LOWER CASE ########################################
# change all columns into lower case
df.columns = [str(x).lower() for x in df.columns]
df.columns

######################### REMOVE UNNECESSARY COLUMNS AND ROWS ########################################

# remove 'penalty.commited' since its not relevant
df=df.drop('penalty.commited',1)
df.columns


# remove rows that has zero minute played since it will not be relevant
df.loc[df['games.minutes_played'] == 0]
df[np.isnan(df['games.minutes_played'])]
df=df.loc[(df[['games.minutes_played']] != 0).all(axis=1)]
df

############################## CHECK DUPLICATE PLAYER AGAIN ########################################
# group player again based on league
england=(df.loc[df['league'] == 'Premier League'])
spain=(df.loc[df['league'] == 'La Liga'])
italy=(df.loc[df['league'] == 'Serie A'])
germany=(df.loc[df['league'] == 'Bundesliga'])
france=(df.loc[df['league'] == 'Ligue 1'])
netherlands=(df.loc[df['league'] == 'Eredivisie'])
russia=(df.loc[df['league'] == 'Premier Liga'])
portugal=(df.loc[df['league'] == 'Primeira Liga'])
belgium=(df.loc[df['league'] == 'First Division A'])
turkey=(df.loc[df['league'] == 'Super Lig'])

# check duplicate on each league
england[england.duplicated(['player name'])]
spain[spain.duplicated(['player name'])]
italy[italy.duplicated(['player name'])]
germany[germany.duplicated(['player name'])]
france[france.duplicated(['player name'])]
netherlands[netherlands.duplicated(['player name'])]
russia[russia.duplicated(['player name'])]
portugal[portugal.duplicated(['player name'])]
belgium[belgium.duplicated(['player name'])]
turkey[turkey.duplicated(['player name'])]

# no duplicate found

############################## CHECK NAN ########################################
df.shape[0]
df.info()

# check the '-' 

df.loc[df['player name']=='-']
df.loc[df['club name']=='-']
df.loc[df['age']=='-']
df.loc[df['nationality']=='-']
df.loc[df['dominant foot']=='-']
df.loc[df['market value']=='-']
df.loc[df['position']=='-']
df.loc[df['league']=='-']
df.loc[df['captain']=='-']

# change - into np.NaN
df.replace({'dominant foot':{'-': np.NaN}},inplace=True)



################################## PUT COLUMN INTO ORDER ###########################
df.shape[1]
# put the column into order of independent variables
df = df[['market value', 'player name', 'age', 'nationality', 'club name',
         'club market value', 'club match played', 'club match won',
         'club match draw', 'club match lose', 'club total goals',
         'club goals conceded', 'league', 'contract expired', 'position',
         'dominant foot', 'height', 'weight', 'rating',
         'captain', 'shots.total', 'shots.on', 'goals.total',
         'goals.conceded', 'goals.assists', 'passes.total', 'passes.key', 'passes.accuracy', 
         'tackles.total', 'tackles.blocks', 'tackles.interceptions', 'duels.total', 'duels.won',
         'dribbles.attempts','dribbles.success', 'fouls.drawn', 'fouls.committed', 'cards.yellow',
         'cards.yellowred', 'cards.red', 'penalty.won', 'penalty.success',
         'penalty.missed', 'penalty.saved', 'games.appearences',
         'games.minutes_played', 'games.lineups', 'substitutes.in',
         'substitutes.out', 'substitutes.bench', 'google_search', 'avgretweets',
         'avglikes', 'youtubeavgviewcount', 'youtubeavglikecount',
         'youtubeavgdislikecount', 'youtubeavgcommentcount'
]]

df.rename({'market value':'market_value','player name': 'player_name',
           'club name': 'club_name','club market value':'club_mv',
           'club match played': 'club_match_played',
           'club match won':'club_match_won','club match draw': 'club_match_draw',
           'club match lose':'club_match_lose','club total goals':'club_total_goals',
           'club goals conceded': 'club_goals_conceded','contract expired': 'contract_expired',
           'dominant foot': 'dominant_foot','shots.total': 'shots_total','shots.on':'shots_on',
           'goals.total':'goals_total','goals.conceded':'goals_conceded', 'goals.assists': 'goals_assists',
           'passes.total':'passes_total','passes.key':'passes_key','passes.accuracy':'passes_accuracy',
           'tackles.total':'tackles_total','tackles.blocks': 'tackles_blocks',
           'tackles.interceptions':'tackles_interceptions',
           'duels.total':'duels_total','duels.won': 'duels_won',
           'dribbles.attempts':'dribbles_attempts',
           'dribbles.success':'dribbles_success',
           'fouls.drawn': 'fouls_drawn','fouls.committed':'fouls_committed',
           'cards.yellow':'cards_yellow','cards.yellowred':'cards_yellowred',
           'cards.red': 'cards_red','penalty.won':'penalty_won',
           'penalty.success': 'penalty_success','penalty.missed':'penalty_missed',
           'penalty.saved': 'penalty_saved','games.appearences':'games_appearences',
           'games.minutes_played': 'games_minutes_played','games.lineups':'games_lineups',
           'substitutes.in':'substitutes_in','substitutes.out': 'substitutes_out',
           'substitutes.bench': 'substitutes_bench','avgretweets': 'twitter_avgretweets',     
           'avglikes': 'twitter_avglikes',
           'youtubeavgviewcount': 'youtube_avgview','youtubeavglikecount':'youtube_avglike',
           'youtubeavgdislikecount': 'youtube_avgdislike','youtubeavgcommentcount':'youtube_avgcomment',
            },axis=1,inplace=True)

len(df.columns)



############################## TEST AND TRAIN SPLIT ########################################
############################## IMPUTE MISSING VALUE ####################################
############################## DUMMY VARIABLE ########################################
############################## EDA AND DESCRIPTIVE STATISTICS ########################################
############################## LOG TRANSFORM THE VARIABLE ########################################
############################## CORRELATION BEFORE FEATURE ENGINEERING ########################################
############################## FEATURE ENGINEERING ########################################
