
#!/usr/bin/env python3
"""
WNBA Shot Charts
"""
import logging
import requests
import json
import csv

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)...',
    'Accept': 'application/json, text/plain, */*',
    'x-nba-stats-origin': 'stats',
    'x-nba-stats-token': 'true',
    'Referer': 'https://stats.wnba.com/',
}

# request_url = 'https://stats.wnba.com/stats/teamgamelogs?DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=10&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=Totals&Period=0&PlusMinus=N&Rank=N&Season=2025&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&VsConference=&VsDivision='
# r = requests.get(request_url, headers=HEADERS, timeout=10)

# Create a custom logger
logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s: %(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')

logging.disable(logging.CRITICAL)

SEASON = 1998

parameters = {
    'LastNGames': '0',
    'LeagueID': '10',
    'MeasureType': 'Base',
    'Month': '0',
    'OpponentTeamID': '0',
    'PORound': '0',
    'PaceAdjust': 'N',
    'PerMode': 'Totals',
    'Period': '0',
    'PlusMinus': 'N',
    'Rank': 'N',
    'Season': SEASON,
    'SeasonType': 'Regular Season',
    'TeamID': '0',
    'PlayerID': '0',
}

endpoint = 'teamgamelogs'
request_url = f'https://stats.wnba.com/stats/{endpoint}?'

r = requests.get(request_url,
                    headers=HEADERS,
                    params=parameters,
                    timeout=10)

headers = json.loads(r.content.decode())['resultSets'][0]['headers']
data = json.loads(r.content.decode())['resultSets'][0]['rowSet']

# Open a file to write that heat
with open(f'data/team_gamelogs_{SEASON}.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(headers) 
    writer.writerows(data)

print("CSV saved, you’re set!")