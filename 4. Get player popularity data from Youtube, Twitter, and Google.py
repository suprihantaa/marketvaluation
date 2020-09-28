# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 21:20:40 2020

@author: Cynthia Suprihanta
"""

import pandas as pd
import numpy as np
import os
os.chdir('C:/Users/Cynthia Suprihanta/OneDrive/Aston University/Business Project/data')


# import player data
df = pd.read_csv('Final Performance and ID data.csv')

club_name = {# England
            'manchester-city':'Manchester City',
             'manchester-united':'Manchester United',
             'fc-everton':'Everton',
             'fc-southampton':'Southampton',
             'newcastle-united':'Newcastle United',
             'brighton-amp-hove-albion':'Brighton & Hove Albion',
             'wolverhampton-wanderers':'Wolverhampton Wanderers',
             'fc-chelsea':'Chelsea',
             'tottenham-hotspur':'Tottenham Hotspur',
             'leicester-city':'Leicester City',
             'crystal-palace':'Crystal Palace',
             'fc-burnley':'Burnley',
             'fc-watford':'Watford',
             'huddersfield-town':'Huddersfield Town',
             'fc-liverpool':'Liverpool',
             'fc-arsenal':'Arsenal',
             'west-ham-united':'West Ham United',
             'fc-fulham':'Fulham',
             'afc-bournemouth':'Bournemouth',
             'cardiff-city':'Cardiff City',
             # Spain
             'real-sociedad-san-sebastian':'Real Sociedad',
             'real-betis-sevilla':'Real Betis',
             'athletic-bilbao':'Athletic Bilbao',
             'cd-leganes':'Leganés',
             'sd-eibar':'Eibar',
             'fc-girona':'Girona',
             'sd-huesca':'Huesca',
             'deportivo-alaves':'Alavés',
             'fc-villarreal':'Villarreal',
             'fc-sevilla':'Sevilla',
             'real-valladolid':'Valladolid',
             'fc-getafe':'Getafe',
             'atletico-madrid':'Atlético Madrid',
             'real-madrid':'Real Madrid',
             'espanyol-barcelona':'Espanyol',
             'fc-valencia':'Valencia',
             'rayo-vallecano':'Rayo Vallecano',
             'ud-levante':'Levante',
             'fc-barcelona':'Barcelona',
             'celta-vigo':'Celta Vigo',
             # Italy
             'ac-mailand':'AC Milan',
             'frosinone-calcio':'Frosinone',
             'juventus-turin':'Juventus',
             'ssc-neapel':'Napoli',
             'ac-florenz':'Fiorentina',
             'fc-genua-1893':'Genoa',
             'fc-bologna':'Bologna',
             'fc-empoli':'Empoli',
             'fc-parma':'Parma',
             'us-sassuolo':'Sassuolo',
             'atalanta-bergamo':'Atalanta',
             'spal-2013':'SPAL',
             'cagliari-calcio':'Cagliari',
             'udinese-calcio':'Udinese',
             'inter-mailand':'Inter Milan',
             'chievo-verona':'Chievo',
             'lazio-rom':'Lazio',
             'uc-sampdoria':'Sampdoria',
             'fc-turin':'Torino',
             'as-rom':'AS Roma',
             # Germany
             'fc-bayern-munchen':'Bayern Munich',
             'borussia-dortmund':'Borussia Dortmund',
             'bayer-04-leverkusen':'Bayer Leverkusen',
             'rasenballsport-leipzig':'RB Leipzig',
             'fc-schalke-04':'FC Schalke 04',
             'borussia-monchengladbach':'Borussia Monchengladbach',
             'tsg-1899-hoffenheim':'1899 Hoffenheim',
             'vfb-stuttgart':'VfB Stuttgart',
             'vfl-wolfsburg':'VfL Wolfsburg',
             'eintracht-frankfurt':'Eintracht Frankfurt',
             'hertha-bsc':'Hertha Berlin',
             'sv-werder-bremen':'Werder Bremen',
             'fc-augsburg':'FC Augsburg',
             'hannover-96':'Hannover 96',
             'sc-freiburg':'SC Freiburg',
             '1-fsv-mainz-05':'FSV Mainz 05',
             'fortuna-dusseldorf':'Fortuna Dusseldorf',
             '1-fc-nurnberg':'FC Nurnberg',
             # France
             'fc-paris-saint-germain':'Paris Saint Germain',
             'as-monaco':'AS Monaco',
             'olympique-lyon':'Lyon',
             'olympique-marseille':'Marseille',
             'fc-stade-rennes':'Rennes',
             'ogc-nizza':'Nice',
             'fc-girondins-bordeaux':'Bordeaux',
             'fc-nantes':'Nantes',
             'osc-lille':'Lille',
             'as-saint-etienne':'Saint Etienne',
             'fc-toulouse':'Toulouse',
             'ea-guingamp':'Guingamp',
             'hsc-montpellier':'Montpellier',
             'racing-strassburg':'Strasbourg',
             'sco-angers':'Angers',
             'sm-caen':'Caen',
             'fco-dijon':'Dijon',
             'sc-amiens':'Amiens',
             'stade-reims':'Reims',
             'olympique-nimes':'Nimes',
             # Netherlands
             'ajax-amsterdam':'Ajax',
             'psv-eindhoven':'PSV Eindhoven',
             'feyenoord-rotterdam':'Feyenoord',
             'az-alkmaar':'AZ Alkmaar',
             'fc-utrecht':'Utrecht',
             'vitesse-arnheim':'Vitesse',
             'sc-heerenveen':'Heerenveen',
             'fc-groningen':'Groningen',
             'willem-ii-tilburg':'Willem II',
             'pec-zwolle':'PEC Zwolle',
             'ado-den-haag':'ADO Den Haag',
             'heracles-almelo':'Heracles',
             'nac-breda':'NAC Breda',
             'fortuna-sittard':'Fortuna Sittard',
             'vvv-venlo':'VVV Venlo',
             'fc-emmen':'Emmen',
             'excelsior-rotterdam':'Excelsior',
             'de-graafschap-doetinchem':'De Graafschap',
             # Russia
             'zenit-st-petersburg':'Zenit St. Petersburg',
             'spartak-moskau':'Spartak Moscow',
             'lokomotiv-moskau':'Lokomotiv Moscow',
             'fk-krasnodar':'Krasnodar',
             'zska-moskau':'CSKA Moscow',
             'dinamo-moskau':'Dynamo Moscow',
             'rubin-kazan':'Rubin Kazan',
             'fk-rostov':'FC Rostov',
             'terek-grozny':'Akhmat Grozny',
             'krylya-sovetov-samara':'Krylya Sovetov',
             'ural-sverdlovskaya-oblast':'Ural FC',
             'fk-ufa':'FC UFA',
             'arsenal-tula':'Arsenal Tula',
             'enisey-krasnoyarsk':'FC Enisey',
             'gazovik-orenburg':'FC Orenburg',
             'anzhi-makhachkala':'Anzhi',
             # Portugal
             'fc-porto':'FC Porto',
             'benfica-lissabon':'Benfica',
             'sporting-lissabon':'Sporting CP',
             'sc-braga':'SC Braga',
             'vitoria-guimaraes-sc':'Vitoria SC',
             'portimonense-sc':'Portimonense',
             'rio-ave-fc':'Rio Ave',
             'gd-chaves':'GD Chaves',
             'cs-maritimo':'Maritimo',
             'vitoria-setubal-fc':'Vitoria Setubal',
             'cf-belenenses-lissabon':'Belenenses',
             'boavista-porto-fc':'Boavista',
             'moreirense-fc':'Moreirense',
             'cd-tondela':'Tondela',
             'cd-feirense':'Feirense',
             'cd-santa-clara':'Santa Clara',
             'cd-nacional':'C.D. Nacional',
             'desportivo-aves':'Desportivo Aves',
             # Belgium
             'standard-luttich':'Standard Liege',
             'royal-fc-antwerpen':'Royal Antwerp F.C.',
             'krc-genk':'K.R.C. Genk',
             'rsc-anderlecht':'RSC Anderlecht',
             'fc-brugge':'Club Brugge',
             'kaa-gent':'KAA Gent',
             'kv-kortrijk':'KV Kortrijk',
             'sv-zulte-waregem':'Zulte Waregem',
             'waasland-beveren':'Waasland-beveren',
             'vv-st-truiden':'St. Truiden',
             'cercle-brugge':'Cercle Brugge',
             'kv-oostende':'KV Oostende',
             'mouscron-peruwelz':'Royal Excel Mouscron',
             'kas-eupen':'AS Eupen',
             'rsc-charleroi':'RSC Charleroi',
             'ksc-lokeren':'KSC Lokeren',
             # Turkey 
             'kayserispor':'Kayserispor',
             'medical-park-antalyaspor':'Antalyaspor',
             'trabzonspor':'Trabzonspor',
             'sivasspor':'Sivasspor',
             'bursaspor':'Bursaspor',
             'torku-konyaspor':'Konyaspor',
             'yeni-malatyaspor':'Yeni Malatyaspor',
             'fenerbahce-istanbul':'Fenerbahce',
             'akhisar-belediye-genclik-ve-spor':'Akhisar Belediye',
             'caykur-rizespor':'Rizespor',
             'erzurum-buyuksehir-belediyespor':'Erzurum BB',
             'besiktas-istanbul':'Besiktas',
             'alanyaspor':'Alanyaspor',
             'mke-ankaragucu':'Ankaragucu',
             'galatasaray-istanbul':'Galatasaray',
             'goztepe-izmir':'Goztepe',
             'kasimpasa':'Kasimpasa',
             'istanbul-buyuksehir-belediyespor':'Istanbul Basaksehir',
             }


df['Club Name'] = df['Club Name'].map(club_name)
df['Club Name'].unique()

x = df.select_dtypes(include=[np.object]).columns
df[x] = df[x].apply(lambda x: x.str.normalize('NFKD').str.encode('ascii', errors='ignore').str.decode('utf-8'))
df['Club Name'].unique()

# divide data based on each league
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


# split the data into 100 rows dataframe
def split(df, chunkSize = 100):
    return np.array_split(df, chunkSize)


# england
england_split = split(england, 6)
england_1=england_split[0]
england_2=england_split[1]
england_3=england_split[2]
england_4=england_split[3]
england_5=england_split[4]
england_6=england_split[5]

england_1[england_1.duplicated(['Player Name'])]

england_2[england_2.duplicated(['Player Name'])]

england_3=england_3.drop(england_3[(england_3['Player Name'] == 'stuart armstrong') & (england_3['position'] == 'Goalkeeper')].index)
england_3[england_3.duplicated(['Player Name'])]

england_4[england_4.duplicated(['Player Name'])]
england_5[england_5.duplicated(['Player Name'])]

england_6=england_6.drop(england_6[(england_6['Player Name'] == 'lee peltier') & (england_6['position'] == 'Goalkeeper')].index)
england_6[england_6.duplicated(['Player Name'])]

df_england=pd.concat([england_1, england_2, england_3,
                          england_4, england_5 , england_6],
                          ignore_index=True)


# spain
spain_split = split(spain, 7)
spain_1=spain_split[0]
spain_2=spain_split[1]
spain_3=spain_split[2]
spain_4=spain_split[3]
spain_5=spain_split[4]
spain_6=spain_split[5]
spain_7=spain_split[6]

spain_7.to_csv('spain_7.csv')

spain_1=spain_1.drop(spain_1[(spain_1['Player Name'] == 'cristian rodriguez') & (spain_1['position'] == 'Defender')].index)
spain_1[spain_1.duplicated(['Player Name'])]

spain_2=spain_2.drop(spain_2[(spain_2['Player Name'] == 'jose gaya') & (spain_2['position'] == 'Attacker')].index)
spain_2=spain_2.drop(spain_2[(spain_2['Player Name'] == 'david zurutuza') & (spain_2['birth_country'] == 'France')].index)
spain_2=spain_2.drop(spain_2[(spain_2['Player Name'] == 'luis muriel') & (spain_2['position'] == 'Goalkeeper')].index)
spain_2[spain_2.duplicated(['Player Name'])]

spain_3[spain_3.duplicated(['Player Name'])]

spain_4[spain_4.duplicated(['Player Name'])]

spain_5=spain_5.drop(spain_5[(spain_5['Player Name'] == 'sergio garcia') & (spain_5['position'] == 'Defender')].index)
spain_5=spain_5.drop(spain_5[(spain_5['Player Name'] == 'daniel torres') & (spain_5['position'] == 'Attacker')].index)
spain_5[spain_5.duplicated(['Player Name'])]

spain_6=spain_6.drop(spain_6[(spain_6['Player Name'] == 'miguel de la fuente') & (spain_6['birth_place'] == 'Cadiz')].index)
spain_6[spain_6.duplicated(['Player Name'])]

spain_7[spain_7.duplicated(['Player Name'])]
spain_7=spain_7.drop(spain_7[(spain_7['Player Name'] == 'javier almerge') & (spain_7['birth_place'] == 'Huesca')].index)
spain_7=spain_7.drop(spain_7[(spain_7['Player Name'] == 'juan aguilera') & (spain_7['birth_place'] == 'Valencia')].index)
spain_7=spain_7.drop(spain_7[(spain_7['Player Name'] == 'juan aguilera') & (spain_7['birth_place'] == 'Pereira')].index)
spain_7=spain_7.drop(spain_7[(spain_7['Player Name'] == 'juan aguilera') & (spain_7['birth_place'] == 'Caracas')].index)
spain_7=spain_7.drop(spain_7[(spain_7['Player Name'] == 'jose pozo') & (spain_7['birth_place'] == 'Malaga')].index)


os.chdir('C:/Users/Cynthia Suprihanta/OneDrive/Aston University/Business Project/data/preprocess 01july')
spain_7.to_csv('df_spain_7.csv')


df_spain=pd.concat([spain_1, spain_2, spain_3,
                          spain_4, spain_5, spain_6, spain_7],
                          ignore_index=True)

spain_7[spain_7.duplicated(['Player Name'])]
df_spain.to_csv('df_spain.csv',index=False,encoding='utf-8-sig')

# italy
italy_split = split(italy, 7)
italy_1=italy_split[0]
italy_2=italy_split[1]
italy_3=italy_split[2]
italy_4=italy_split[3]
italy_5=italy_split[4]
italy_6=italy_split[5]
italy_7=italy_split[6]


italy_1=italy_1.drop(italy_1[(italy_1['Player Name'] == 'franck kessie') & (italy_1['position'] == 'Attacker')].index)
italy_1=italy_1.drop(italy_1[(italy_1['Player Name'] == 'marco brescianini') & (italy_1['position'] == 'Midfielder')].index)
italy_1=italy_1.drop(italy_1[(italy_1['Player Name'] == 'lucas biglia') & (italy_1['birth_country'] == 'Brazil')].index)
italy_1[italy_1.duplicated(['Player Name'])]

italy_2[italy_2.duplicated(['Player Name'])]

italy_3=italy_3.drop(italy_3[(italy_3['Player Name'] == 'christian koffi') & (italy_3['birth_country'] == 'France')].index)
italy_3=italy_3.drop(italy_3[(italy_3['Player Name'] == "nicolas n'koulou") & (italy_3['birth_country'] == 'Argentina')].index)
italy_3[italy_3.duplicated(['Player Name'])]

italy_4[italy_4.duplicated(['Player Name'])]

italy_5[italy_5.duplicated(['Player Name'])]

italy_6=italy_6.drop(italy_6[(italy_6['Player Name'] == 'giacomo poluzzi') & (italy_6['position'] == 'Defender')].index)
italy_6[italy_6.duplicated(['Player Name'])]

italy_7=italy_7.drop(italy_7[(italy_7['Player Name'] == 'lorenzo ariaudo') & (italy_7['position'] == 'Attacker')].index)
italy_7=italy_7.drop(italy_7[(italy_7['Player Name'] == 'andrea beghetto') & (italy_7['age'] == 18)].index)
italy_7[italy_7.duplicated(['Player Name'])]


df_italy=pd.concat([italy_1, italy_2, italy_3,
                          italy_4, italy_5, italy_6, italy_7],
                          ignore_index=True)

df_italy[df_italy.duplicated(['Player Name'])]

df_italy.to_csv('df_italy.csv',index=False,encoding='utf-8-sig')

#germany
germany_split = split(germany, 6)
germany_1=germany_split[0]
germany_2=germany_split[1]
germany_3=germany_split[2]
germany_4=germany_split[3]
germany_5=germany_split[4]
germany_6=germany_split[5]

germany_1=germany_1.drop(germany_1[(germany_1['Player Name'] == 'roman burki') & (germany_1['position'] == 'Defender')].index)
germany_1=germany_1.drop(germany_1[(germany_1['Player Name'] == 'eric oelschlagel') & (germany_1['age'] == 25)].index)
germany_1=germany_1.drop(germany_1[(germany_1['Player Name'] == 'manuel akanji') & (germany_1['position'] == 'Midfielder')].index)
germany_1=germany_1.drop(germany_1[(germany_1['Player Name'] == 'omer toprak') & (germany_1['position'] == 'Attacker')].index)
germany_1=germany_1.drop(germany_1[(germany_1['Player Name'] == 'thomas delaney') & (germany_1['age'] == 31)].index)
germany_1=germany_1.drop(germany_1[(germany_1['Player Name'] == 'mario gotze') & (germany_1['age'] == 24)].index)
germany_1=germany_1.drop(germany_1[(germany_1['Player Name'] == 'jacob bruun larsen') & (germany_1['age'] == 31)].index)
germany_1=germany_1.drop(germany_1[(germany_1['Player Name'] == 'raphael guerreiro') & (germany_1['age'] == 21)].index)
germany_1=germany_1.drop(germany_1[(germany_1['Player Name'] == 'christian pulisic') & (germany_1['age'] == 26)].index)
germany_1=germany_1.drop(germany_1[(germany_1['Player Name'] == 'lukas hradecky') & (germany_1['position'] == 'Midfielder')].index)
germany_1=germany_1.drop(germany_1[(germany_1['Player Name'] == 'thorsten kirschbaum') & (germany_1['age'] == 21)].index)
germany_1=germany_1.drop(germany_1[(germany_1['Player Name'] == 'panagiotis retsos') & (germany_1['age'] == 22)].index)
germany_1=germany_1.drop(germany_1[(germany_1['Player Name'] == 'lars bender') & (germany_1['age'] == 26)].index)
germany_1=germany_1.drop(germany_1[(germany_1['Player Name'] == 'lars bender') & (germany_1['rating'] == 7.007692)].index)
germany_1=germany_1.drop(germany_1[(germany_1['Player Name'] == 'jonathan tah') & (germany_1['age'] == 25)].index)
germany_1=germany_1.drop(germany_1[(germany_1['Player Name'] == 'ibrahima konate') & (germany_1['age'] == 22)].index)
germany_1=germany_1.drop(germany_1[(germany_1['Player Name'] == 'sergio gomez') & (germany_1['age'] == 20)].index)
germany_1=germany_1.drop(germany_1[(germany_1['Player Name'] == 'lukas klostermann') & (germany_1['age'] == 29)].index)

germany_1[germany_1.duplicated(['Player Name'])]


germany_2=germany_2.drop(germany_2[(germany_2['Player Name'] == 'stefan ilsanker') & (germany_2['age'] == 26)].index)
germany_2=germany_2.drop(germany_2[(germany_2['Player Name'] == 'tom krau') & (germany_2['age'] == 30)].index)
germany_2=germany_2.drop(germany_2[(germany_2['Player Name'] == 'jean-kevin augustin') & (germany_2['age'] == 20)].index)
germany_2=germany_2.drop(germany_2[(germany_2['Player Name'] == 'marcel halstenberg') & (germany_2['age'] == 23)].index)
germany_2=germany_2.drop(germany_2[(germany_2['Player Name'] == 'alexander nubel') & (germany_2['age'] == 35)].index)
germany_2=germany_2.drop(germany_2[(germany_2['Player Name'] == 'benjamin stambouli') & (germany_2['age'] == 21)].index)
germany_2=germany_2.drop(germany_2[(germany_2['Player Name'] == 'abdul rahman baba') & (germany_2['age'] == 23)].index)
germany_2=germany_2.drop(germany_2[(germany_2['Player Name'] == 'suat serdar') & (germany_2['age'] == 30)].index)
germany_2=germany_2.drop(germany_2[(germany_2['Player Name'] == 'nassim boujellab') & (germany_2['age'] == 20)].index)
germany_2=germany_2.drop(germany_2[(germany_2['Player Name'] == 'alessandro schopf') & (germany_2['age'] == 23)].index)
germany_2=germany_2.drop(germany_2[(germany_2['Player Name'] == 'philip fontein') & (germany_2['age'] == 27)].index)
germany_2=germany_2.drop(germany_2[(germany_2['Player Name'] == 'cedric teuchert') & (germany_2['age'] == 26)].index)
germany_2=germany_2.drop(germany_2[(germany_2['Player Name'] == 'hamza mendyl') & (germany_2['age'] == 24)].index)
germany_2=germany_2.drop(germany_2[(germany_2['Player Name'] == 'steven skrzybski') & (germany_2['age'] == 29)].index)
germany_2=germany_2.drop(germany_2[(germany_2['Player Name'] == 'yann sommer') & (germany_2['age'] == 21)].index)
germany_2=germany_2.drop(germany_2[(germany_2['Player Name'] == 'moritz nicolas') & (germany_2['age'] == 21)].index)
germany_2=germany_2.drop(germany_2[(germany_2['Player Name'] == 'mamadou doucoure') & (germany_2['age'] == 32)].index)
germany_2=germany_2.drop(germany_2[(germany_2['Player Name'] == 'tobias strobl') & (germany_2['birth_place'] == 'Hoyerswerda')].index)
germany_2=germany_2.drop(germany_2[(germany_2['Player Name'] == 'jonas hofmann') & (germany_2['age'] == 33)].index)
germany_2=germany_2.drop(germany_2[(germany_2['Player Name'] == 'laszlo benes') & (germany_2['age'] == 26)].index)
germany_2=germany_2.drop(germany_2[(germany_2['Player Name'] == 'raffael') & (germany_2['age'] == 29)].index)
germany_2[germany_2.duplicated(['Player Name'])]



germany_3=germany_3.drop(germany_3[(germany_3['Player Name'] == 'ron-robert zieler') & (germany_3['age'] == 35)].index)
germany_3=germany_3.drop(germany_3[(germany_3['Player Name'] == 'timo baumgartl') & (germany_3['age'] == 33)].index)
germany_3=germany_3.drop(germany_3[(germany_3['Player Name'] == 'antonis aidonis') & (germany_3['age'] == 22)].index)
germany_3=germany_3.drop(germany_3[(germany_3['Player Name'] == 'emiliano insua') & (germany_3['age'] == 25)].index)
germany_3=germany_3.drop(germany_3[(germany_3['Player Name'] == 'benjamin pavard') & (germany_3['age'] == 20)].index)
germany_3=germany_3.drop(germany_3[(germany_3['Player Name'] == 'daniel didavi') & (germany_3['age'] == 33)].index)
germany_3=germany_3.drop(germany_3[(germany_3['Player Name'] == 'david kopacz') & (germany_3['age'] == 26)].index)
germany_3=germany_3.drop(germany_3[(germany_3['Player Name'] == 'marc oliver kempf') & (germany_3['age'] == 32)].index)
germany_3[germany_3.duplicated(['Player Name'])]

germany_4=germany_4.drop(germany_4[(germany_4['Player Name'] == 'jiri pavlenka') & (germany_4['age'] == 29)].index)
germany_4=germany_4.drop(germany_4[(germany_4['Player Name'] == 'luca plogmann') & (germany_4['position'] == 'Attacker')].index)
germany_4=germany_4.drop(germany_4[(germany_4['Player Name'] == 'luca plogmann') & (germany_4['age'] == 26)].index)
germany_4=germany_4.drop(germany_4[(germany_4['Player Name'] == 'milos veljkovic') & (germany_4['age'] == 26)].index)
germany_4=germany_4.drop(germany_4[(germany_4['Player Name'] == 'theodor gebre selassie') & (germany_4['age'] == 35)].index)
germany_4=germany_4.drop(germany_4[(germany_4['Player Name'] == 'felix beijmo') & (germany_4['age'] == 33)].index)
germany_4=germany_4.drop(germany_4[(germany_4['Player Name'] == 'philipp bargfrede') & (germany_4['age'] == 24)].index)
germany_4=germany_4.drop(germany_4[(germany_4['Player Name'] == 'thanos petsos') & (germany_4['age'] == 22)].index)
germany_4=germany_4.drop(germany_4[(germany_4['Player Name'] == 'davy klaassen') & (germany_4['age'] == 33)].index)
germany_4=germany_4.drop(germany_4[(germany_4['Player Name'] == 'florian kainz') & (germany_4['age'] == 25)].index)
germany_4=germany_4.drop(germany_4[(germany_4['Player Name'] == 'claudio pizarro') & (germany_4['age'] == 30)].index)
germany_4[germany_4.duplicated(['Player Name'])]


germany_5=germany_5.drop(germany_5[(germany_5['Player Name'] == 'michael esser') & (germany_5['age'] == 35)].index)
germany_5=germany_5.drop(germany_5[(germany_5['Player Name'] == 'samuel sahin-radlinger') & (germany_5['age'] == 24)].index)
germany_5=germany_5.drop(germany_5[(germany_5['Player Name'] == 'waldemar anton') & (germany_5['age'] == 30)].index)
germany_5=germany_5.drop(germany_5[(germany_5['Player Name'] == 'julian korb') & (germany_5['age'] == 26)].index)
germany_5=germany_5.drop(germany_5[(germany_5['Player Name'] == 'jonathas') & (germany_5['age'] == 31)].index)
germany_5=germany_5.drop(germany_5[(germany_5['Player Name'] == 'hendrik weydandt') & (germany_5['age'] == 20)].index)
germany_5=germany_5.drop(germany_5[(germany_5['Player Name'] == 'benjamin hadzic') & (germany_5['age'] == 27)].index)
germany_5[germany_5.duplicated(['Player Name'])]

germany_6=germany_6.drop(germany_6[(germany_6['Player Name'] == 'florian muller') & (germany_6['age'] == 30)].index)
germany_6=germany_6.drop(germany_6[(germany_6['Player Name'] == 'finn dahmen') & (germany_6['age'] == 26)].index)
germany_6=germany_6.drop(germany_6[(germany_6['Player Name'] == 'ahmet gurleyen') & (germany_6['age'] == 25)].index)
germany_6=germany_6.drop(germany_6[(germany_6['Player Name'] == 'aaron martin') & (germany_6['age'] == 25)].index)
germany_6=germany_6.drop(germany_6[(germany_6['Player Name'] == 'giulio donati') & (germany_6['birth_country'] == 'Romania')].index)
germany_6=germany_6.drop(germany_6[(germany_6['Player Name'] == 'danny latza') & (germany_6['age'] == 27)].index)
germany_6=germany_6.drop(germany_6[(germany_6['Player Name'] == 'jose rodriguez') & (germany_6['age'] == 24)].index)
germany_6=germany_6.drop(germany_6[(germany_6['Player Name'] == 'moussa niakhate') & (germany_6['age'] == 32)].index)
germany_6=germany_6.drop(germany_6[(germany_6['Player Name'] == 'gaetan bussmann') & (germany_6['age'] == 27)].index)
germany_6=germany_6.drop(germany_6[(germany_6['Player Name'] == 'pierre kunde malong') & (germany_6['age'] == 24)].index)
germany_6=germany_6.drop(germany_6[(germany_6['Player Name'] == 'leandro barreiro') & (germany_6['age'] == 27)].index)
germany_6[germany_6.duplicated(['Player Name'])]


df_germany=pd.concat([germany_1, germany_2, germany_3,
                          germany_4, germany_5, germany_6],
                          ignore_index=True)

df_germany[df_germany.duplicated(['Player Name'])]


# france
france_split = split(france, 7)
france_1=france_split[0]
france_2=france_split[1]
france_3=france_split[2]
france_4=france_split[3]
france_5=france_split[4]
france_6=france_split[5]
france_7=france_split[6]



france_1=france_1.drop(france_1[(france_1['Player Name'] == 'thiago silva') & (france_1['position'] == 'Midfielder')].index)
france_1[france_1.duplicated(['Player Name'])]

france_2[france_2.duplicated(['Player Name'])]

france_3[france_3.duplicated(['Player Name'])]

france_4[france_4.duplicated(['Player Name'])]

france_5=france_5.drop(france_5[(france_5['Player Name'] == 'anthony mandrea') & (france_5['position'] == 'Midfielder')].index)
france_5[france_5.duplicated(['Player Name'])]

france_6[france_6.duplicated(['Player Name'])]

france_7[france_7.duplicated(['Player Name'])]


df_france=pd.concat([france_1, france_2, france_3,
                          france_4, france_5, france_6, france_7],
                          ignore_index=True)

df_france[df_france.duplicated(['Player Name'])]


# netherlands
netherlands_split = split(netherlands, 6)
netherlands_1=netherlands_split[0]
netherlands_2=netherlands_split[1]
netherlands_3=netherlands_split[2]
netherlands_4=netherlands_split[3]
netherlands_5=netherlands_split[4]
netherlands_6=netherlands_split[5]

netherlands_1[netherlands_1.duplicated(['Player Name'])]
netherlands_2[netherlands_2.duplicated(['Player Name'])]

netherlands_3=netherlands_3.drop(netherlands_3[(netherlands_3['Player Name'] == 'tim freriks') & (netherlands_3['position'] == 'Defender')].index)
netherlands_3[netherlands_3.duplicated(['Player Name'])]

netherlands_4[netherlands_4.duplicated(['Player Name'])]

netherlands_5=netherlands_5.drop(netherlands_5[(netherlands_5['Player Name'] == 'tom hendriks') & (netherlands_5['position'] == 'Defender')].index)
netherlands_5[netherlands_5.duplicated(['Player Name'])]

netherlands_6[netherlands_6.duplicated(['Player Name'])]


df_netherlands=pd.concat([netherlands_1, netherlands_2, netherlands_3,
                          netherlands_4, netherlands_5, netherlands_6],
                          ignore_index=True)

df_netherlands[df_netherlands.duplicated(['Player Name'])]

# russia
russia_split = split(russia, 6)
russia_1=russia_split[0]
russia_2=russia_split[1]
russia_3=russia_split[2]
russia_4=russia_split[3]
russia_5=russia_split[4]
russia_6=russia_split[5]

russia_1[russia_1.duplicated(['Player Name'])]
russia_2[russia_2.duplicated(['Player Name'])]
russia_3[russia_3.duplicated(['Player Name'])]

russia_4=russia_4.drop(russia_4[(russia_4['Player Name'] == 'gennadi kiselev') & (russia_4['games.minutes_played'] == 0)].index)
russia_4=russia_4.drop(russia_4[(russia_4['Player Name'] == 'denis polyakov') & (russia_4['age'] == 34)].index)
russia_4[russia_4.duplicated(['Player Name'])]

russia_5=russia_5.drop(russia_5[(russia_5['Player Name'] == 'aleksandr zotov') & (russia_5['age'] == 34)].index)
russia_5[russia_5.duplicated(['Player Name'])]

russia_6[russia_6.duplicated(['Player Name'])]


df_russia=pd.concat([russia_1, russia_2, russia_3,
                          russia_4, russia_5, russia_6],
                          ignore_index=True)

df_russia[df_russia.duplicated(['Player Name'])]


# portugal
portugal_split = split(portugal, 6)
portugal_1=portugal_split[0]
portugal_2=portugal_split[1]
portugal_3=portugal_split[2]
portugal_4=portugal_split[3]
portugal_5=portugal_split[4]
portugal_6=portugal_split[5]


portugal_1=portugal_1.drop(portugal_1[(portugal_1['Player Name'] == 'bruno gaspar') & (portugal_1['age'] == 21)].index)
portugal_1=portugal_1.drop(portugal_1[(portugal_1['Player Name'] == 'bruno gaspar') & (portugal_1['age'] == 31)].index)
portugal_1=portugal_1.drop(portugal_1[(portugal_1['Player Name'] == 'bruno gaspar') & (portugal_1['age'] == 26)].index)
portugal_1=portugal_1.drop(portugal_1[(portugal_1['Player Name'] == 'miguel luis') & (portugal_1['position'] == 'Goalkeeper')].index)
portugal_1[portugal_1.duplicated(['Player Name'])]


portugal_2=portugal_2.drop(portugal_2[(portugal_2['Player Name'] == 'ricardo ferreira') & (portugal_2['age'] == 27)].index)
portugal_2=portugal_2.drop(portugal_2[(portugal_2['Player Name'] == 'ricardo ferreira') & (portugal_2['age'] == 26)].index)
portugal_2=portugal_2.drop(portugal_2[(portugal_2['Player Name'] == 'joao palhinha') & (portugal_2['age'] == 27)].index)
portugal_2=portugal_2.drop(portugal_2[(portugal_2['Player Name'] == 'bruno viana') & (portugal_2['age'] == 23)].index)
portugal_2=portugal_2.drop(portugal_2[(portugal_2['Player Name'] == 'andre almeida') & (portugal_2['age'] == 31)].index)
portugal_2=portugal_2.drop(portugal_2[(portugal_2['Player Name'] == 'jean felipe') & (portugal_2['birth_place'] == 'Toledo')].index)
portugal_2=portugal_2.drop(portugal_2[(portugal_2['Player Name'] == 'bruno reis') & (portugal_2['age'] == 23)].index)
portugal_2=portugal_2.drop(portugal_2[(portugal_2['Player Name'] == 'paulinho') & (portugal_2['age'] == 22)].index)
portugal_2=portugal_2.drop(portugal_2[(portugal_2['Player Name'] == 'lucas fernandes') & (portugal_2['age'] == 26)].index)

portugal_2[portugal_2.duplicated(['Player Name'])]


portugal_3=portugal_3.drop(portugal_3[(portugal_3['Player Name'] == 'paulo vitor') & (portugal_3['age'] == 32)].index)
portugal_3=portugal_3.drop(portugal_3[(portugal_3['Player Name'] == 'carlos jr.') & (portugal_3['age'] == 21)].index)
portugal_3=portugal_3.drop(portugal_3[(portugal_3['Player Name'] == 'joao kuspiosz') & (portugal_3['age'] == 26)].index)
portugal_3=portugal_3.drop(portugal_3[(portugal_3['Player Name'] == 'filipe brigues') & (portugal_3['age'] == 23)].index)
portugal_3=portugal_3.drop(portugal_3[(portugal_3['Player Name'] == 'filipe brigues') & (portugal_3['age'] == 31)].index)
portugal_3=portugal_3.drop(portugal_3[(portugal_3['Player Name'] == 'hugo basto') & (portugal_3['age'] == 23)].index)
portugal_3=portugal_3.drop(portugal_3[(portugal_3['Player Name'] == 'ruben macedo') & (portugal_3['age'] == 29)].index)
portugal_3=portugal_3.drop(portugal_3[(portugal_3['Player Name'] == 'pedro mateus') & (portugal_3['age'] == 20)].index)
portugal_3=portugal_3.drop(portugal_3[(portugal_3['Player Name'] == 'leandro barrera') & (portugal_3['age'] == 21)].index)

portugal_3[portugal_3.duplicated(['Player Name'])]


portugal_4=portugal_4.drop(portugal_4[(portugal_4['Player Name'] == 'andre sousa') & (portugal_4['age'] == 23)].index)
portugal_4=portugal_4.drop(portugal_4[(portugal_4['Player Name'] == 'nuno valente') & (portugal_4['position'] == 'Defender')].index)
portugal_4=portugal_4.drop(portugal_4[(portugal_4['Player Name'] == 'nuno tomas') & (portugal_4['age'] == 33)].index)
portugal_4=portugal_4.drop(portugal_4[(portugal_4['Player Name'] == 'diogo calila') & (portugal_4['age'] == 30)].index)
portugal_4=portugal_4.drop(portugal_4[(portugal_4['Player Name'] == 'goncalo silva') & (portugal_4['age'] == 29)].index)
portugal_4=portugal_4.drop(portugal_4[(portugal_4['Player Name'] == 'eduardo henrique') & (portugal_4['age'] == 29)].index)
portugal_4=portugal_4.drop(portugal_4[(portugal_4['Player Name'] == 'fabio espinho') & (portugal_4['age'] == 24)].index)
portugal_4=portugal_4.drop(portugal_4[(portugal_4['Player Name'] == 'rafael bracali') & (portugal_4['age'] == 29)].index)
portugal_4[portugal_4.duplicated(['Player Name'])]


portugal_5=portugal_5.drop(portugal_5[(portugal_5['Player Name'] == 'pedro nuno') & (portugal_5['age'] == 32)].index)
portugal_5=portugal_5.drop(portugal_5[(portugal_5['Player Name'] == 'ruben barros') & (portugal_5['age'] == 31)].index)
portugal_5=portugal_5.drop(portugal_5[(portugal_5['Player Name'] == 'ricardo costa') & (portugal_5['age'] == 32)].index)
portugal_5=portugal_5.drop(portugal_5[(portugal_5['Player Name'] == 'ricardo costa') & (portugal_5['age'] == 29)].index)
portugal_5=portugal_5.drop(portugal_5[(portugal_5['Player Name'] == 'david bruno') & (portugal_5['age'] == 23)].index)
portugal_5=portugal_5.drop(portugal_5[(portugal_5['Player Name'] == 'david bruno') & (portugal_5['age'] == 36)].index)
portugal_5=portugal_5.drop(portugal_5[(portugal_5['Player Name'] == 'joao jaquite') & (portugal_5['birth_country'] == 'Portugal')].index)
portugal_5=portugal_5.drop(portugal_5[(portugal_5['Player Name'] == 'bruno brigido') & (portugal_5['position'] == 'Midfielder')].index)
portugal_5=portugal_5.drop(portugal_5[(portugal_5['Player Name'] == 'bruno brigido') & (portugal_5['position'] == 'Defender')].index)
portugal_5=portugal_5.drop(portugal_5[(portugal_5['Player Name'] == 'jose valencia') & (portugal_5['age'] == 23)].index)
portugal_5=portugal_5.drop(portugal_5[(portugal_5['Player Name'] == 'tiago gomes') & (portugal_5['age'] == 30)].index)
portugal_5=portugal_5.drop(portugal_5[(portugal_5['Player Name'] == 'tiago gomes') & (portugal_5['age'] == 27)].index)
portugal_5=portugal_5.drop(portugal_5[(portugal_5['Player Name'] == 'joao tavares') & (portugal_5['age'] == 30)].index)
portugal_5[portugal_5.duplicated(['Player Name'])]

portugal_6=portugal_6.drop(portugal_6[(portugal_6['Player Name'] == 'joao pedro') & (portugal_6['age'] == 24)].index)
portugal_6=portugal_6.drop(portugal_6[(portugal_6['Player Name'] == 'joao camacho') & (portugal_6['age'] == 27)].index)
portugal_6=portugal_6.drop(portugal_6[(portugal_6['Player Name'] == 'jorge fellipe') & (portugal_6['age'] == 25)].index)
portugal_6=portugal_6.drop(portugal_6[(portugal_6['Player Name'] == 'rodrigo') & (portugal_6['age'] == 34)].index)
portugal_6=portugal_6.drop(portugal_6[(portugal_6['Player Name'] == 'ricardo rodrigues') & (portugal_6['age'] == 22)].index)
portugal_6=portugal_6.drop(portugal_6[(portugal_6['Player Name'] == 'vitor costa') & (portugal_6['age'] == 33)].index)
portugal_6=portugal_6.drop(portugal_6[(portugal_6['Player Name'] == 'bruno lourenco') & (portugal_6['age'] == 24)].index)
portugal_6=portugal_6.drop(portugal_6[(portugal_6['Player Name'] == 'bruno lourenco') & (portugal_6['age'] == 37)].index)
portugal_6[portugal_6.duplicated(['Player Name'])]

df_portugal=pd.concat([portugal_1, portugal_2, portugal_3,
                          portugal_4, portugal_5, portugal_6],
                          ignore_index=True)

df_portugal[df_portugal.duplicated(['Player Name'])]

# belgium 
belgium_split = split(belgium, 5)
belgium_1=belgium_split[0]
belgium_2=belgium_split[1]
belgium_3=belgium_split[2]
belgium_4=belgium_split[3]
belgium_5=belgium_split[4]

belgium_1[belgium_1.duplicated(['Player Name'])]

belgium_2=belgium_2.drop(belgium_2[(belgium_2['Player Name'] == 'mehdi carcela-gonzalez') & (belgium_2['nationality'] == 'Belgium')].index)
belgium_2[belgium_2.duplicated(['Player Name'])]

belgium_3[belgium_3.duplicated(['Player Name'])]

belgium_4=belgium_4.drop(belgium_4[(belgium_4['Player Name'] == 'hannes van der bruggen') & (belgium_4['position'] == 'Defender')].index)
belgium_4=belgium_4.drop(belgium_4[(belgium_4['Player Name'] == 'miguel van damme') & (belgium_4['position'] == 'Defender')].index)
belgium_4[belgium_4.duplicated(['Player Name'])]

belgium_5=belgium_5.drop(belgium_5[(belgium_5['Player Name'] == 'dimitri mohamed') & (belgium_5['birth_place'] == 'Dakar')].index)
belgium_5[belgium_5.duplicated(['Player Name'])]

df_belgium=pd.concat([belgium_1, belgium_2, belgium_3,
                          belgium_4, belgium_5],
                          ignore_index=True)

df_belgium[df_belgium.duplicated(['Player Name'])]


# turkey
turkey_split = split(turkey, 6)
turkey_1=turkey_split[0]
turkey_2=turkey_split[1]
turkey_3=turkey_split[2]
turkey_4=turkey_split[3]
turkey_5=turkey_split[4]
turkey_6=turkey_split[5]

turkey_1=turkey_1.drop(turkey_1[(turkey_1['Player Name'] == 'fernando muslera') & (turkey_1['age'] == 29)].index)
turkey_1=turkey_1.drop(turkey_1[(turkey_1['Player Name'] == 'fernando muslera') & (turkey_1['age'] == 33)].index)
turkey_1=turkey_1.drop(turkey_1[(turkey_1['Player Name'] == 'martin linnes') & (turkey_1['age'] == 25)].index)
turkey_1=turkey_1.drop(turkey_1[(turkey_1['Player Name'] == 'mugdat celik') & (turkey_1['age'] == 35)].index)
turkey_1=turkey_1.drop(turkey_1[(turkey_1['Player Name'] == 'serdar aziz') & (turkey_1['Club Name'] == 'galatasaray-istanbul')].index)
turkey_1[turkey_1.duplicated(['Player Name'])]

turkey_2=turkey_2.drop(turkey_2[(turkey_2['Player Name'] == 'arda turan') & (turkey_2['age'] == 36)].index)
turkey_2=turkey_2.drop(turkey_2[(turkey_2['Player Name'] == 'muhammed sengezer') & (turkey_2['age'] == 18)].index)
turkey_2[turkey_2.duplicated(['Player Name'])]

turkey_3=turkey_3.drop(turkey_3[(turkey_3['Player Name'] == 'lamine gassama') & (turkey_3['age'] == 33)].index)
turkey_3=turkey_3.drop(turkey_3[(turkey_3['Player Name'] == 'halil akbunar') & (turkey_3['age'] == 34)].index)
turkey_3=turkey_3.drop(turkey_3[(turkey_3['Player Name'] == 'thomas heurtaux') & (turkey_3['age'] == 32)].index)
turkey_3[turkey_3.duplicated(['Player Name'])]

turkey_4=turkey_4.drop(turkey_4[(turkey_4['Player Name'] == 'stelios kitsiou') & (turkey_4['age'] == 26)].index)
turkey_4=turkey_4.drop(turkey_4[(turkey_4['Player Name'] == 'ricardo faty') & (turkey_4['age'] == 22)].index)
turkey_4=turkey_4.drop(turkey_4[(turkey_4['Player Name'] == 'wilfred moke') & (turkey_4['Club Name'] == 'torku-konyaspor')].index)
turkey_4=turkey_4.drop(turkey_4[(turkey_4['Player Name'] == 'murat akca') & (turkey_4['age'] == 33)].index)
turkey_4[turkey_4.duplicated(['Player Name'])]




turkey_5=turkey_5.drop(turkey_5[(turkey_5['Player Name'] == 'eray birnican') & (turkey_5['age'] == 35)].index)
turkey_5[turkey_5.duplicated(['Player Name'])]



turkey_6[turkey_6.duplicated(['Player Name'])]

df_turkey=pd.concat([turkey_1, turkey_2, turkey_3,
                          turkey_4, turkey_5, turkey_6],
                          ignore_index=True)

df_turkey=df_turkey.drop(df_turkey[(df_turkey['Player Name'] == 'serdar aziz') & (df_turkey['Club Name'] == 'Galatasaray')].index)
df_turkey=df_turkey.drop(df_turkey[(df_turkey['Player Name'] == 'emre akbaba') & (df_turkey['Club Name'] == 'Alanyaspor')].index)
df_turkey=df_turkey.drop(df_turkey[(df_turkey['Player Name'] == 'aurelien chedjou') & (df_turkey['Club Name'] == 'Istanbul Basaksehir')].index)
df_turkey=df_turkey.drop(df_turkey[(df_turkey['Player Name'] == 'wilfred moke') & (df_turkey['Club Name'] == 'Ankaragucu')].index)
df_turkey=df_turkey.drop(df_turkey[(df_turkey['Player Name'] == 'omer bayram') & (df_turkey['Club Name'] == 'Akhisar Belediye')].index)
df_turkey=df_turkey.drop(df_turkey[(df_turkey['Player Name'] == 'mevlut erdinc') & (df_turkey['Club Name'] == 'Istanbul Basaksehir')].index)


df_turkey[df_turkey.duplicated(['Player Name'])]
len(df_turkey['Club Name'].unique())

os.chdir('C:/Users/Cynthia Suprihanta/OneDrive/Aston University/Business Project/data/preprocess 01july')


df_england.to_csv('df_england.csv',index=False,encoding='utf-8-sig')
df_spain.to_csv('df_spain.csv',index=False,encoding='utf-8-sig')
spain_7.to_csv('df_spain_7.csv',index=False,encoding='utf-8-sig')
df_italy.to_csv('df_italy.csv',index=False,encoding='utf-8-sig')
df_germany.to_csv('df_germany.csv',index=False,encoding='utf-8-sig')
df_france.to_csv('df_france.csv',index=False,encoding='utf-8-sig')
df_netherlands.to_csv('df_netherlands.csv',index=False,encoding='utf-8-sig')
df_russia.to_csv('df_russia.csv',index=False,encoding='utf-8-sig')
df_portugal.to_csv('df_portugal.csv',index=False,encoding='utf-8-sig')
df_belgium.to_csv('df_belgium.csv',index=False,encoding='utf-8-sig')
df_turkey.to_csv('df_turkey.csv',index=False,encoding='utf-8-sig')

final_df=pd.concat([df_england, df_spain, df_italy, df_germany,
                    df_france, df_netherlands, df_russia, df_portugal,
                    df_belgium, df_turkey],
                          ignore_index=True)

os.chdir('C:/Users/Cynthia Suprihanta/OneDrive/Aston University/Business Project/data')
final_df.to_csv('final_df.csv',index=False,encoding='utf-8-sig')


############################## SPLIT DATA INTO PER 100 ######################


# import player data
df = pd.read_csv('final_df.csv')

england=pd.read_csv('df_england.csv')
spain=pd.read_csv('df_spain.csv')
italy=pd.read_csv('df_italy.csv')
germany=pd.read_csv('df_germany.csv')
france=pd.read_csv('df_france.csv')
netherlands=pd.read_csv('df_netherlands.csv')
russia=pd.read_csv('df_russia.csv')
portugal=pd.read_csv('df_portugal.csv')
belgium=pd.read_csv('df_belgium.csv')
turkey=pd.read_csv('df_turkey.csv')

# create youtube query based on name and club
df['Query'] = df[['Player Name', 'Club Name']].agg(' '.join, axis=1)
df['Query'].head()


# split the df into per 100 rows
def split(df, chunkSize = 100):
    return np.array_split(df, chunkSize)



os.chdir('C:/Users/Cynthia Suprihanta/OneDrive/Aston University/Business Project/data/preprocess 01july/youtube')

df = split(df, 55)


df0=df[0]
df1=df[1]
df2=df[2]
df3=df[3]
df4=df[4]
df5=df[5]
df6=df[6]
df7=df[7]
df8=df[8]
df9=df[9]
df10=df[10]
df11=df[11]
df12=df[12]
df13=df[13]
df14=df[14]
df15=df[15]
df16=df[16]
df17=df[17]
df18=df[18]
df19=df[19]
df20=df[20]
df21=df[21]
df22=df[22]
df23=df[23]
df24=df[24]
df25=df[25]
df26=df[26]
df27=df[27]
df28=df[28]
df29=df[29]
df30=df[30]
df31=df[31]
df32=df[32]
df33=df[33]
df34=df[34]
df35=df[35]
df36=df[36]
df37=df[37]
df38=df[38]
df39=df[39]
df40=df[40]
df41=df[41]
df42=df[42]
df43=df[43]
df44=df[44]
df45=df[45]
df46=df[46]
df47=df[47]
df48=df[48]
df49=df[49]
df50=df[50]
df51=df[51]
df52=df[52]
df53=df[53]
df54=df[54]


os.chdir('C:/Users/Cynthia Suprihanta/OneDrive/Aston University/Business Project/data/preprocess 01july/youtube')



df0.to_csv('df0.csv',index=False,encoding='utf-8-sig')
df1.to_csv('df1.csv',index=False,encoding='utf-8-sig')
df2.to_csv('df2.csv',index=False,encoding='utf-8-sig')
df3.to_csv('df3.csv',index=False,encoding='utf-8-sig')
df4.to_csv('df4.csv',index=False,encoding='utf-8-sig')
df5.to_csv('df5.csv',index=False,encoding='utf-8-sig')
df6.to_csv('df6.csv',index=False,encoding='utf-8-sig')
df7.to_csv('df7.csv',index=False,encoding='utf-8-sig')
df8.to_csv('df8.csv',index=False,encoding='utf-8-sig')
df9.to_csv('df9.csv',index=False,encoding='utf-8-sig')
df10.to_csv('df10.csv',index=False,encoding='utf-8-sig')
df11.to_csv('df11.csv',index=False,encoding='utf-8-sig')
df12.to_csv('df12.csv',index=False,encoding='utf-8-sig')
df13.to_csv('df13.csv',index=False,encoding='utf-8-sig')
df14.to_csv('df14.csv',index=False,encoding='utf-8-sig')
df15.to_csv('df15.csv',index=False,encoding='utf-8-sig')
df16.to_csv('df16.csv',index=False,encoding='utf-8-sig')
df17.to_csv('df17.csv',index=False,encoding='utf-8-sig')
df18.to_csv('df18.csv',index=False,encoding='utf-8-sig')
df19.to_csv('df19.csv',index=False,encoding='utf-8-sig')
df20.to_csv('df20.csv',index=False,encoding='utf-8-sig')
df21.to_csv('df21.csv',index=False,encoding='utf-8-sig')
df22.to_csv('df22.csv',index=False,encoding='utf-8-sig')
df23.to_csv('df23.csv',index=False,encoding='utf-8-sig')
df24.to_csv('df24.csv',index=False,encoding='utf-8-sig')
df25.to_csv('df25.csv',index=False,encoding='utf-8-sig')
df26.to_csv('df26.csv',index=False,encoding='utf-8-sig')
df27.to_csv('df27.csv',index=False,encoding='utf-8-sig')
df28.to_csv('df28.csv',index=False,encoding='utf-8-sig')
df29.to_csv('df29.csv',index=False,encoding='utf-8-sig')
df30.to_csv('df30.csv',index=False,encoding='utf-8-sig')
df31.to_csv('df31.csv',index=False,encoding='utf-8-sig')
df32.to_csv('df32.csv',index=False,encoding='utf-8-sig')
df33.to_csv('df33.csv',index=False,encoding='utf-8-sig')
df34.to_csv('df34.csv',index=False,encoding='utf-8-sig')
df35.to_csv('df35.csv',index=False,encoding='utf-8-sig')
df36.to_csv('df36.csv',index=False,encoding='utf-8-sig')
df37.to_csv('df37.csv',index=False,encoding='utf-8-sig')
df38.to_csv('df38.csv',index=False,encoding='utf-8-sig')
df39.to_csv('df39.csv',index=False,encoding='utf-8-sig')
df40.to_csv('df40.csv',index=False,encoding='utf-8-sig')
df41.to_csv('df41.csv',index=False,encoding='utf-8-sig')
df42.to_csv('df42.csv',index=False,encoding='utf-8-sig')
df43.to_csv('df43.csv',index=False,encoding='utf-8-sig')
df44.to_csv('df44.csv',index=False,encoding='utf-8-sig')
df45.to_csv('df45.csv',index=False,encoding='utf-8-sig')
df46.to_csv('df46.csv',index=False,encoding='utf-8-sig')
df47.to_csv('df47.csv',index=False,encoding='utf-8-sig')
df48.to_csv('df48.csv',index=False,encoding='utf-8-sig')
df49.to_csv('df49.csv',index=False,encoding='utf-8-sig')
df50.to_csv('df50.csv',index=False,encoding='utf-8-sig')
df51.to_csv('df51.csv',index=False,encoding='utf-8-sig')
df52.to_csv('df52.csv',index=False,encoding='utf-8-sig')
df53.to_csv('df53.csv',index=False,encoding='utf-8-sig')
df54.to_csv('df54.csv',index=False,encoding='utf-8-sig')








############################### GET THE YOUTUBE DATA ########################

# The code only works for around 50 - 80 queries per API Keys (DEVELOPER KEYS) daily
# Therefore, the key will be changed if the quota is running out
# The code run through every file from df1 to df54


from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import pandas as pd
import numpy as np


def storeResults(response):

    #create variables to store your values
    title = []
    channelId = []
    channelTitle = []
    categoryId = []
    videoId = []
    viewCount = []
    likeCount = []
    dislikeCount = []
    commentCount = []
    favoriteCount = []
    category = []
    tags = []
    videos = []

    for search_result in response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            #append title and video for each item
            title.append(search_result['snippet']['title'])
            videoId.append(search_result['id']['videoId'])
            #then collect stats on each video using videoId
            stats = youtube.videos().list(
                part='statistics, snippet',
                id=search_result['id']['videoId']).execute()

            channelId.append(stats['items'][0]['snippet']['channelId'])
            channelTitle.append(stats['items'][0]['snippet']['channelTitle'])
            categoryId.append(stats['items'][0]['snippet']['categoryId'])
            favoriteCount.append(stats['items'][0]['statistics']['favoriteCount'])
            viewCount.append(stats['items'][0]['statistics']['viewCount'])

            #Not every video has likes/dislikes enabled so they won't appear in JSON response
            try:
                likeCount.append(stats['items'][0]['statistics']['likeCount'])
            except:
       #Good to be aware of Channels that turn off their Likes
                print("Video titled {0}, on Channel {1} Likes Count is not available".format(stats['items'][0]['snippet']['title'],
                                                                                             stats['items'][0]['snippet']['channelTitle']))
                print(stats['items'][0]['statistics'].keys())
        #Appends "Not Available" to keep dictionary values aligned
                likeCount.append(np.nan)

            try:
                dislikeCount.append(stats['items'][0]['statistics']['dislikeCount'])
            except:
                #Good to be aware of Channels that turn off their Likes
                print("Video titled {0}, on Channel {1} Dislikes Count is not available".format(stats['items'][0]['snippet']['title'],
                                                                                                stats['items'][0]['snippet']['channelTitle']))
                print(stats['items'][0]['statistics'].keys())
                dislikeCount.append(np.nan)

            if 'commentCount' in stats['items'][0]['statistics'].keys():
                commentCount.append(stats['items'][0]['statistics']['commentCount'])
            else:
                commentCount.append(np.nan)


    #Break out of for-loop and if statement and store lists of values in dictionary
    youtube_dict = {'title':title,
                    'videoId':videoId,
                    'viewCount':viewCount,
                    'likeCount':likeCount,
                    'dislikeCount':dislikeCount,
                    'commentCount':commentCount,}

    return youtube_dict

def get_player_data(name):
    search_response = youtube.search().list(
        q=name,
        type="video",
        pageToken=None,
        order = 'viewCount',
        part="id,snippet",
        publishedAfter= '2018-07-31T00:00:00Z' ,
        publishedBefore='2019-06-01T00:00:00Z' ,
        maxResults=5,
        location=None,
        locationRadius=None).execute()
    return pd.DataFrame(storeResults(search_response))

DEVELOPER_KEY = """insert developer key from Google API"""
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)



os.chdir('C:/Users/Cynthia Suprihanta/OneDrive/Aston University/Business Project/data/preprocess 01july/youtube')
df=pd.read_csv('df50.csv')
df=df['Query'].to_list()
# df=df[0:50]
df=df[50:99]


data=[]
for name in df:
    d = get_player_data(name)

    data.append(
            {"name": name,
             "YoutubeAvgViewCount": pd.to_numeric(d["viewCount"], errors='coerce').mean(),
             "YoutubeAvglikeCount": pd.to_numeric(d["likeCount"], errors='coerce').mean(),
             "YoutubeAvgDislikeCount": pd.to_numeric(d["dislikeCount"], errors='coerce').mean(),
             "YoutubeAvgCommentCount": pd.to_numeric(d["commentCount"], errors='coerce').mean()}
        )
    
    
df = pd.DataFrame(data)


os.chdir('C:/Users/Cynthia Suprihanta/OneDrive/Aston University/Business Project/data/preprocess 01july/youtube/youtube_result')
df.to_csv("df50_result.csv", index=False)


# combine all of youtube result into one grand csv

cwd = os.path.abspath('C:/Users/Cynthia Suprihanta/OneDrive/Aston University/Business Project/data/preprocess 01july/youtube/youtube_result') 
files = os.listdir(cwd)  
df_youtube = pd.DataFrame()
for file in files:
    if file.endswith('.csv'):
        df_youtube = df_youtube.append(pd.read_csv(file), ignore_index=True) 
        
        
df_youtube.to_csv('youtube_result.csv')


############################## GET THE TWITTER DATA ########################

# The key and token only worked around 150 queries / 40 mins
# Therefore, the code will run through every file from df1 to df54


import tweepy

CONSUMER_KEY = """insert consumer key from Twitter API"""
CONSUMER_SECRET = """insert consumer secret from Twitter API"""
ACCESS_TOKEN = """insert access token from Twitter API"""
ACCESS_TOKEN_SECRET = """insert access token secret from Twitter API"""


# Authenticate to Twitter
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
# test authentication
try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")
    
    

def get_tweet(query):
    tweets = api.search(q=query, count=20,result_type='popular')
    text_tweets = [[query,
                tw.retweet_count,
                tw.favorite_count] for tw in tweets]
    df= pd.DataFrame(text_tweets, columns = ['Player Name','Retweets','Favorites'])
    new_df = pd.DataFrame ({'Player Name':[query],
                            'avgretweets': df['Retweets'].mean(),
                            'avglikes': df['Favorites'].mean()
    })
    return new_df


os.chdir('C:/Users/Cynthia Suprihanta/OneDrive/Aston University/Business Project/data/preprocess 01july/youtube')
df = pd.read_csv('df9.csv')
df=df['Query'].to_list()
# df=df[0:50]
# df=df[50:100]


newdf = pd.DataFrame()

for name in df:
    df = get_tweet(name)
    newdf = newdf.append(df, ignore_index=True)
    

os.chdir('C:/Users/Cynthia Suprihanta/OneDrive/Aston University/Business Project/data/preprocess 01july/youtube/twitter_result')


newdf.to_csv("df9_result.csv", index=False)

# combine all of youtube result into one grand csv

cwd = os.path.abspath('C:/Users/Cynthia Suprihanta/OneDrive/Aston University/Business Project/data/preprocess 01july/youtube/twitter_result') 
files = os.listdir(cwd)  
df_twitter = pd.DataFrame()
for file in files:
    if file.endswith('.csv'):
        df_twitter = df_twitter.append(pd.read_csv(file), ignore_index=True) 
        
        
df_twitter.to_csv('twitter_result.csv')

############################## GET THE GOOGLE DATA ########################

# The google data approached using API
# The data will be acquired per country/league

import requests
import json


headers = { 'apikey': """insert API key from ZENSERP API""" }



os.chdir('C:/Users/Cynthia Suprihanta/OneDrive/Aston University/Business Project/data/preprocess 01july')
england=pd.read_csv('df_england.csv')
spain=pd.read_csv('df_spain.csv')
italy=pd.read_csv('df_italy.csv')
germany=pd.read_csv('df_germany.csv')
france=pd.read_csv('df_france.csv')
netherlands=pd.read_csv('df_netherlands.csv')
russia=pd.read_csv('df_russia.csv')
portugal=pd.read_csv('df_portugal.csv')
belgium=pd.read_csv('df_belgium.csv')
turkey=pd.read_csv('df_turkey.csv')

england['Query']=england[['Player Name', 'Club Name']].agg(' '.join, axis=1)
spain['Query']=spain[['Player Name', 'Club Name']].agg(' '.join, axis=1)
italy['Query']=italy[['Player Name', 'Club Name']].agg(' '.join, axis=1)
germany['Query']=germany[['Player Name', 'Club Name']].agg(' '.join, axis=1)
france['Query']=france[['Player Name', 'Club Name']].agg(' '.join, axis=1)
netherlands['Query']=netherlands[['Player Name', 'Club Name']].agg(' '.join, axis=1)
russia['Query']=russia[['Player Name', 'Club Name']].agg(' '.join, axis=1)
portugal['Query']=portugal[['Player Name', 'Club Name']].agg(' '.join, axis=1)
belgium['Query']=belgium[['Player Name', 'Club Name']].agg(' '.join, axis=1)
turkey['Query']=turkey[['Player Name', 'Club Name']].agg(' '.join, axis=1)

print(england.shape[0])
print(spain.shape[0])
print(italy.shape[0])
print(germany.shape[0])
print(france.shape[0])
print(netherlands.shape[0])
print(russia.shape[0])
print(portugal.shape[0])
print(belgium.shape[0])
print(turkey.shape[0])


data=[]

# england
df=england['Query']


for q in df :
    params = (
        ("q",q),
        );
    response = requests.get('https://app.zenserp.com/api/v2/search', headers=headers, params=params)
    result=response.text
    result=json.loads(result)
    total_results=result['number_of_results']      
    data.append(
            {"name": q,
             "google_search": total_results
             })
    
england_google = pd.DataFrame(data)
england_google



os.chdir('C:/Users/Cynthia Suprihanta/OneDrive/Aston University/Business Project/data/preprocess 01july/youtube/google_result')


england_google.to_csv("england_google.csv", index=False)

# spain

df=spain['Query']
df
data_spain=[]


for q in df :
    params = (
        ("q",q),
        );
    response = requests.get('https://app.zenserp.com/api/v2/search', headers=headers, params=params)
    result=response.text
    result=json.loads(result)
    total_results=result['number_of_results']      
    data_spain.append(
            {"name": q,
             "google_search": total_results
             })
    
spain_google = pd.DataFrame(data_spain)



os.chdir('C:/Users/Cynthia Suprihanta/OneDrive/Aston University/Business Project/data/preprocess 01july/youtube/google_result')


spain_google.to_csv("spain_google.csv", index=False)

# italy

df=italy['Query']
df
data_italy=[]


for q in df :
    params = (
        ("q",q),
        );
    response = requests.get('https://app.zenserp.com/api/v2/search', headers=headers, params=params)
    result=response.text
    result=json.loads(result)
    total_results=result['number_of_results']      
    data_italy.append(
            {"name": q,
             "google_search": total_results
             })
    
italy_google = pd.DataFrame(data_italy)



os.chdir('C:/Users/Cynthia Suprihanta/OneDrive/Aston University/Business Project/data/preprocess 01july/youtube/google_result')


italy_google.to_csv("italy_google.csv", index=False)

# germany

df=germany['Query']

data_germany=[]


for q in df :
    params = (
        ("q",q),
        );
    response = requests.get('https://app.zenserp.com/api/v2/search', headers=headers, params=params)
    result=response.text
    result=json.loads(result)
    total_results=result['number_of_results']      
    data_germany.append(
            {"name": q,
             "google_search": total_results
             })
    
germany_google = pd.DataFrame(data_germany)



os.chdir('C:/Users/Cynthia Suprihanta/OneDrive/Aston University/Business Project/data/preprocess 01july/youtube/google_result')


germany_google.to_csv("germany_google.csv", index=False)

# france

df=france['Query']

data_france=[]


for q in df :
    params = (
        ("q",q),
        );
    response = requests.get('https://app.zenserp.com/api/v2/search', headers=headers, params=params)
    result=response.text
    result=json.loads(result)
    total_results=result['number_of_results']      
    data_france.append(
            {"name": q,
             "google_search": total_results
             })
    
france_google = pd.DataFrame(data_france)



os.chdir('C:/Users/Cynthia Suprihanta/OneDrive/Aston University/Business Project/data/preprocess 01july/youtube/google_result')


france_google.to_csv("france_google.csv", index=False)

# netherlands

df=netherlands['Query']

data_netherlands=[]


for q in df :
    params = (
        ("q",q),
        );
    response = requests.get('https://app.zenserp.com/api/v2/search', headers=headers, params=params)
    result=response.text
    result=json.loads(result)
    total_results=result['number_of_results']      
    data_netherlands.append(
            {"name": q,
             "google_search": total_results
             })
    
netherlands_google = pd.DataFrame(data_netherlands)


os.chdir('C:/Users/Cynthia Suprihanta/OneDrive/Aston University/Business Project/data/preprocess 01july/youtube/google_result')


netherlands_google.to_csv("netherlands_google.csv", index=False)

# russia

df=russia['Query']
data_russia=[]


for q in df :
    params = (
        ("q",q),
        );
    response = requests.get('https://app.zenserp.com/api/v2/search', headers=headers, params=params)
    result=response.text
    result=json.loads(result)
    total_results=result['number_of_results']      
    data_russia.append(
            {"name": q,
             "google_search": total_results
             })
    
russia_google = pd.DataFrame(data_russia)


os.chdir('C:/Users/Cynthia Suprihanta/OneDrive/Aston University/Business Project/data/preprocess 01july/youtube/google_result')


russia_google.to_csv("russia_google.csv", index=False)

# portugal

df=portugal['Query']
data_portugal=[]


for q in df :
    params = (
        ("q",q),
        );
    response = requests.get('https://app.zenserp.com/api/v2/search', headers=headers, params=params)
    result=response.text
    result=json.loads(result)
    total_results=result['number_of_results']      
    data_portugal.append(
            {"name": q,
             "google_search": total_results
             })
    
google_portugal = pd.DataFrame(data_portugal)


os.chdir('C:/Users/Cynthia Suprihanta/OneDrive/Aston University/Business Project/data/preprocess 01july/youtube/google_result')


google_portugal.to_csv("portugal_google.csv", index=False)

# belgium

df=belgium['Query']
data_belgium=[]


for q in df :
    params = (
        ("q",q),
        );
    response = requests.get('https://app.zenserp.com/api/v2/search', headers=headers, params=params)
    result=response.text
    result=json.loads(result)
    total_results=result['number_of_results']      
    data_belgium.append(
            {"name": q,
             "google_search": total_results
             })
    
google_belgium = pd.DataFrame(data_belgium)


os.chdir('C:/Users/Cynthia Suprihanta/OneDrive/Aston University/Business Project/data/preprocess 01july/youtube/google_result')


google_belgium.to_csv("belgium_google.csv", index=False)

# turkey

df=turkey['Query']
data_turkey=[]

for q in df :
    params = (
        ("q",q),
        );
    response = requests.get('https://app.zenserp.com/api/v2/search', headers=headers, params=params)
    result=response.text
    result=json.loads(result)
    total_results=result['number_of_results']      
    data_turkey.append(
            {"name": q,
             "google_search": total_results
             })
    
google_turkey= pd.DataFrame(data_turkey)


os.chdir('C:/Users/Cynthia Suprihanta/OneDrive/Aston University/Business Project/data/preprocess 01july/youtube/google_result')


google_turkey.to_csv("turkey_google.csv", index=False)


# combine all result
cwd = os.path.abspath('C:/Users/Cynthia Suprihanta/OneDrive/Aston University/Business Project/data/preprocess 01july/youtube/google_result') 
files = os.listdir(cwd)  
df_google = pd.DataFrame()
for file in files:
    if file.endswith('.csv'):
        df_google = df_google.append(pd.read_csv(file), ignore_index=True) 
        
        
df_google.to_csv('google_result.csv')