
#!/usr/bin/env python3
"""
WNBA Shot Charts
"""
import logging
import requests
import csv
import json


# Create a custom logger
logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s: %(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')

# logging.disable(logging.CRITICAL)

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)...',
    'Accept': 'application/json, text/plain, */*',
    'x-nba-stats-origin': 'stats',
    'x-nba-stats-token': 'true',
    'Referer': 'https://stats.wnba.com/',
}

SEASON = 2025
PLAYER_ID = 1629483

"""Get player season gamelog."""
parameters = {
'LastNGames': '0',
'LeagueID': 10,
'MeasureType': 'Base',
'Month': '0',
'OpponentTeamID': '0',
'PORound': '0',
'PaceAdjust': 'N',
'PerMode': 'Totals',
'Period': '0',
'PlayerID': PLAYER_ID,
'PlusMinus': 'N',
'Rank': 'N',
'Season': SEASON,
'SeasonSegment': '',
'SeasonType': 'Regular Season'
}

endpoint = 'playergamelogs'
request_url = f'https://stats.wnba.com/stats/{endpoint}?'

r = requests.get(request_url,
                headers=HEADERS,
                params=parameters,
                timeout=10)

headers = json.loads(r.content.decode())['resultSets'][0]['headers']
data = json.loads(r.content.decode())['resultSets'][0]['rowSet']


# Open a file to write that heat
with open(f'data/player_gamelogs_{SEASON}_{PLAYER_ID}.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(headers) 
    writer.writerows(data)

logging.info('Data saved to CSV file.')
