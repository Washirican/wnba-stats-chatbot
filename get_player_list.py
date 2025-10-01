
#!/usr/bin/env python3
"""
WNBA Shot Charts
"""
import logging
import requests
import json

HEADERS = {
    'Host': 'stats.wnba.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'x-nba-stats-origin': 'stats',
    'x-nba-stats-token': 'true',
    'Connection': 'keep-alive',
    'Referer': 'https://stats.wnba.com/',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

PLAYER_INDEX_URL = 'https://stats.wnba.com/js/data/ptsd/stats_ptsd.js' # 'https://stats.nba.com/stats/playerindex?LeagueID=10&Season=2025&Historical=1' # 'https://stats.wnba.com/js/data/ptsd/stats_ptsd.js' # 

# Create a custom logger
logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s: %(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')

logging.disable(logging.CRITICAL)

r = requests.get(PLAYER_INDEX_URL, timeout=10)

# Cleanup string
dict_str = r.content.decode()[17:-1]

# Turns string into dictionary
data = json.loads(dict_str)
players = data['data']['players']
teams = data['data']['teams']
data_date = data['generated']

# TODO (2025-10-01): Save this to DB table
# for player in players:
    # print(player[1])
    