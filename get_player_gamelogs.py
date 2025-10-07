
#!/usr/bin/env python3
"""
WNBA Shot Charts
"""
import logging
import requests
import csv
import json
import pandas as pd


# Create a custom logger
logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s: %(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')

# logging.disable(logging.CRITICAL)

# LEARN (2025-10-07): Do this in pySpark and use UDFs to make parallel requests.

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)...',
    'Accept': 'application/json, text/plain, */*',
    'x-nba-stats-origin': 'stats',
    'x-nba-stats-token': 'true',
    'Referer': 'https://stats.wnba.com/',
}

SEASON = 2025
PLAYER_ID = 1629483

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
# data = json.loads(r.content.decode())['resultSets'][0]['rowSet']

# Open a file to write headers
with open(f'data/player_gamelogs_{SEASON}.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(headers) 


# Read list of player IDs from csv file
df = pd.read_csv(f'data/all_players_{SEASON}.csv')
active_player_ids = df[df['ROSTER_STATUS'] == 1]['PERSON_ID']

for player_id in active_player_ids:
    logging.info(f'Requesting player game logs for player ID: {player_id}')

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
    'PlayerID': player_id,
    'PlusMinus': 'N',
    'Rank': 'N',
    'Season': SEASON,
    'SeasonSegment': '',
    'SeasonType': 'Regular Season'
    }    

    r = requests.get(request_url,
                    headers=HEADERS,
                    params=parameters,
                    timeout=10)

    # headers = json.loads(r.content.decode())['resultSets'][0]['headers']
    data = json.loads(r.content.decode())['resultSets'][0]['rowSet']

    # # Open a file to write headers
    # with open(f'data/player_gamelogs_{SEASON}.csv', 'w', newline='', encoding='utf-8') as file:
    #     writer = csv.writer(file)

    # Open a file to append data
    with open(f'data/player_gamelogs_{SEASON}.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        # writer.writerow(headers) 
        writer.writerows(data)

logging.info('Data saved to CSV file.')
