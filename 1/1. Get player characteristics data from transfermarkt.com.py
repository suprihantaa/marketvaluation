# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 19:49:34 2020

@author: Cynthia Suprihanta
"""

# Get the player identity and market value from transfermarkt.com

from lxml import html
import requests
import xlsxwriter

import os
os.chdir('C:/Users/Cynthia Suprihanta/OneDrive/Aston University/Business Project/data/per league/player identity')



def write_to_excel(nf, data):
  workbook = xlsxwriter.Workbook(nf)
  worksheet = workbook.add_worksheet()
  
  row = 0
  col = 0

  worksheet.write(row, col,     'Player Name')
  worksheet.write(row, col + 1, 'Club Name')
  worksheet.write(row, col + 2, 'Position')
  worksheet.write(row, col + 3, 'DoB(age)')
  worksheet.write(row, col + 4, 'Nationality')
  worksheet.write(row, col + 5, 'Height')
  worksheet.write(row, col + 6, 'Dominant foot')
  worksheet.write(row, col + 7, 'Contract Expired')
  worksheet.write(row, col + 8, 'Market Value')

  for d in data:
    row += 1
    col = 0
    
    for s in d:
      if col == 0:
        worksheet.write_string(row, col, d[col])
        col += 1
      else:
        worksheet.write_string(row, col, d[col])
        col += 1
  
  workbook.close()
  
def get_elements(link):
  page = requests.get(link, headers={'User-Agent':'Custom'})
  page_string = html.fromstring(page.content)
  odd_elements = page_string.xpath('//tr[@class="odd"]')
  even_elements = page_string.xpath('//tr[@class="even"]')
  elements = odd_elements + even_elements
  return elements

def get_data_by_xpath(element,xpath,attr,index):
  if attr == 'text':
    xpath += '/text()'
  data_list = element.xpath(xpath)
  if len(data_list) == 0:
    ret = ''
  else:
    if attr=='text':
      ret = data_list[index].strip()
    else:
      ret = data_list[index].get(attr)
  return ret

def get_data(element,club_name):
  player_name = get_data_by_xpath(element,".//a[@class='spielprofil_tooltip']/",'text',0)
  position = get_data_by_xpath(element,".//table[@class='inline-table']//td",'text',0)
  dob = get_data_by_xpath(element,".//td[@class='zentriert']",'text',0)
  nationality = get_data_by_xpath(element,".//img[@class='flaggenrahmen']",'title',0)
  height = get_data_by_xpath(element,".//td[@class='zentriert']",'text',1)
  foot = get_data_by_xpath(element,".//td[@class='zentriert']",'text',2)
  contract_exp = get_data_by_xpath(element,".//td[@class='zentriert']",'text',4)
  market_value = get_data_by_xpath(element,".//td[@class='rechts hauptlink']",'text',0)
  return [player_name, club_name, position, dob, nationality, height, foot, contract_exp, market_value]

data = []
link = "https://www.transfermarkt.com/CLUBNAME/kader/verein/CLUBCODE/saison_id/2018/plus/1"

clubs_code__name = {
    # premier_league_uk
    '281':'manchester-city',
    '631':'fc-chelsea',
    '31':'fc-liverpool',
    '985':'manchester-united',
    '148':'tottenham-hotspur',
    '11':'fc-arsenal',
    '29':'fc-everton',
    '1003':'leicester-city',
    '379':'west-ham-united',
    '180':'fc-southampton',
    '873':'crystal-palace',
    '931':'fc-fulham',
    '762':'newcastle-united',
    '1132':'fc-burnley',
    '989':'afc-bournemouth',
    '1237':'brighton-amp-hove-albion',
    '1010':'fc-watford',
    '543':'wolverhampton-wanderers',
    '1110':'huddersfield-town',
    '603':'cardiff-city', 
    #la_liga_spain
    '131':'fc-barcelona',
    '418':'real-madrid',
    '13':'atletico-madrid',
    '1049':'fc-valencia',
    '368':'fc-sevilla',
    '1050':'fc-villarreal',
    '621':'athletic-bilbao',
    '681':'real-sociedad-san-sebastian',
    '940':'celta-vigo',
    '150':'real-betis-sevilla',
    '1244':'cd-leganes',
    '714':'espanyol-barcelona',
    '12321':'fc-girona',
    '3368':'ud-levante',
    '1108':'deportivo-alaves',
    '3709':'fc-getafe',
    '367':'rayo-vallecano',
    '1533':'sd-eibar',
    '5358':'sd-huesca',
    '366':'real-valladolid',
    #serie_a_italy
    '506':'juventus-turin',
    '46':'inter-mailand',
    '5':'ac-mailand',
    '6195':'ssc-neapel',
    '12':'as-rom',
    '398':'lazio-rom',
    '800':'atalanta-bergamo',
    '430':'ac-florenz',
    '416':'fc-turin',
    '1038':'uc-sampdoria',
    '6574':'us-sassuolo',
    '410':'udinese-calcio',
    '1390':'cagliari-calcio',
    '252':'fc-genua-1893',
    '1025':'fc-bologna',
    '2722':'spal-2013',
    '130':'fc-parma',
    '862':'chievo-verona',
    '8970':'frosinone-calcio',
    '749':'fc-empoli',  
    #bundesliga_germany
    '27':'fc-bayern-munchen',
    '16':'borussia-dortmund',
    '15':'bayer-04-leverkusen',
    '23826':'rasenballsport-leipzig',
    '33':'fc-schalke-04',
    '18':'borussia-monchengladbach',
    '533':'tsg-1899-hoffenheim',
    '79':'vfb-stuttgart',
    '82':'vfl-wolfsburg',
    '24':'eintracht-frankfurt',
    '44':'hertha-bsc',
    '86':'sv-werder-bremen',
    '167':'fc-augsburg',
    '42':'hannover-96',
    '60':'sc-freiburg',
    '39':'1-fsv-mainz-05',
    '38':'fortuna-dusseldorf',
    '4':'1-fc-nurnberg',    
    #ligue1_france
    '583':'fc-paris-saint-germain',
    '162':'as-monaco',
    '1041':'olympique-lyon',
    '244':'olympique-marseille',
    '273':'fc-stade-rennes',
    '417':'ogc-nizza',
    '40':'fc-girondins-bordeaux',
    '995':'fc-nantes',
    '1082':'osc-lille',
    '618':'as-saint-etienne',
    '415':'fc-toulouse',
    '855':'ea-guingamp',
    '969':'hsc-montpellier',
    '667':'racing-strassburg',
    '1420':'sco-angers',
    '1162':'sm-caen',
    '2969':'fco-dijon',
    '1416':'sc-amiens',
    '1421':'stade-reims',
    '1160':'olympique-nimes',
    #eredivisie_netherlands
    '610':'ajax-amsterdam',
    '383':'psv-eindhoven',
    '234':'feyenoord-rotterdam',
    '1090':'az-alkmaar',
    '200':'fc-utrecht',
    '499':'vitesse-arnheim',
    '306':'sc-heerenveen',
    '202':'fc-groningen',
    '403':'willem-ii-tilburg',
    '1269':'pec-zwolle',
    '1268':'ado-den-haag',
    '1304':'heracles-almelo',
    '132':'nac-breda',
    '385':'fortuna-sittard',
    '1426':'vvv-venlo',
    '1283':'fc-emmen',
    '798':'excelsior-rotterdam',
    '642':'de-graafschap-doetinchem',
    #premier_liga_russia
    '964': 'zenit-st-petersburg',
    '232': 'spartak-moskau',
    '932': 'lokomotiv-moskau',
    '16704': 'fk-krasnodar',
    '2410': 'zska-moskau',
    '121': 'dinamo-moskau',
    '2698': 'rubin-kazan',
    '1083': 'fk-rostov',
    '3725': 'terek-grozny',
    '2696': 'krylya-sovetov-samara',
    '11127': 'ural-sverdlovskaya-oblast',
    '28095': 'fk-ufa',
    '3729': 'arsenal-tula',
    '3714': 'enisey-krasnoyarsk',
    '14589': 'gazovik-orenburg',
    '2700': 'anzhi-makhachkala',
    #liga_nos_portugal
    '720':'fc-porto',
    '294':'benfica-lissabon',
    '336':'sporting-lissabon',
    '1075':'sc-braga',
    '2420':'vitoria-guimaraes-sc',
    '7378':'portimonense-sc',
    '2425':'rio-ave-fc',
    '3325':'gd-chaves',
    '1301':'cs-maritimo',
    '1085':'vitoria-setubal-fc',
    '2457':'cf-belenenses-lissabon',
    '2503':'boavista-porto-fc',
    '979':'moreirense-fc',
    '7179':'cd-tondela',
    '3349':'cd-feirense',
    '2423':'cd-santa-clara',
    '982':'cd-nacional',
    '3336':'desportivo-aves',
    #jupiler_pro_belgium
    '58':'rsc-anderlecht',
    '2282':'fc-brugge',
    '157':'kaa-gent',
    '3057':'standard-luttich',
    '1184':'krc-genk',
    '172':'rsc-charleroi',
    '3508':'sv-zulte-waregem',
    '2861':'kv-oostende',
    '1096':'royal-fc-antwerpen',
    '498':'ksc-lokeren',
    '601':'kv-kortrijk',
    '1245':'kas-eupen',
    '520':'cercle-brugge',
    '475':'vv-st-truiden',
    '28643':'waasland-beveren',
    '29228':'mouscron-peruwelz',
    #superlig_turkey
    '36': 'fenerbahce-istanbul',
    '141': 'galatasaray-istanbul',
    '114': 'besiktas-istanbul',
    '6890': 'istanbul-buyuksehir-belediyespor',
    '449': 'trabzonspor',
    '11282': 'alanyaspor',
    '20': 'bursaspor',
    '126': 'caykur-rizespor',
    '1467': 'goztepe-izmir',
    '868': 'mke-ankaragucu',
    '2293': 'torku-konyaspor',
    '19789': 'yeni-malatyaspor',
    '2381': 'sivasspor',
    '10484': 'kasimpasa',
    '3205': 'kayserispor',
    '19771': 'akhisar-belediye-genclik-ve-spor',
    '589': 'medical-park-antalyaspor',
    '39722': 'erzurum-buyuksehir-belediyespor'
}

for club_code, club_name in clubs_code__name.items():
  club_link = link.replace('CLUBNAME', club_name)
  club_link = club_link.replace('CLUBCODE', club_code)
    
  new_data = [get_data(element,club_name) for element in get_elements(club_link)]  
  data += new_data
  
write_to_excel("Player Characteristics.xlsx", data)