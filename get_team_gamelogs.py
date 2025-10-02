
#!/usr/bin/env python3
"""
WNBA Shot Charts
"""
import logging
import requests
import json
import csv

# HEADERS = {
#     'Host': 'stats.wnba.com',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0',
#     'Accept': 'application/json, text/plain, */*',
#     'Accept-Language': 'en-US,en;q=0.9',
#     'Accept-Encoding': 'gzip, deflate, br, zstd',
#     'x-nba-stats-origin': 'stats',
#     'x-nba-stats-token': 'true',
#     'Connection': 'keep-alive',
#     'Referer': 'https://stats.wnba.com/teams/',
#     'Pragma': 'no-cache',
#     'Cache-Control': 'no-cache',
# }

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)...',
    'Accept': 'application/json, text/plain, */*',
    'x-nba-stats-origin': 'stats',
    'x-nba-stats-token': 'true',
    'Referer': 'https://stats.wnba.com/teams/',
}

# request_url = 'https://stats.wnba.com/stats/teamgamelogs?DateFrom=&DateTo=&GameSegment=&LastNGames=0&LeagueID=10&Location=&MeasureType=Base&Month=0&OpponentTeamID=0&Outcome=&PORound=0&PaceAdjust=N&PerMode=Totals&Period=0&PlusMinus=N&Rank=N&Season=2025&SeasonSegment=&SeasonType=Regular+Season&ShotClockRange=&VsConference=&VsDivision='
# r = requests.get(request_url, headers=HEADERS, timeout=10)

# Create a custom logger
logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s: %(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')

logging.disable(logging.CRITICAL)

"""Get player season gamelog."""
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
    'Season': '2025',
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
with open('data/team_gamelogs.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(headers) 
    writer.writerows(data)

print("CSV saved, you’re set!")