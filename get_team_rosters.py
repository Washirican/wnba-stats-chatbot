
#!/usr/bin/env python3
"""
WNBA Shot Charts
"""
import logging
import requests
import json
import csv

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

# Create a custom logger
logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s: %(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')

logging.disable(logging.CRITICAL)
# FIXME (2025-10-02): 

def get_roster(self):
        """Get team roster for a specific season or current roster (?)."""

        logging.debug('Team class get_roster()')

        parameters = {
            'LeagueID': 10,
            'Season': season,
            'TeamID': id
        }

        endpoint = 'commonteamroster'
        request_url = f'https://stats.wnba.com/stats/{endpoint}?'

        r = requests.get(request_url,
                         headers=HEADERS,
                         params=parameters,
                         timeout=10)
        headers = json.loads(r.content.decode())['resultSets'][0]['headers']
        data = json.loads(r.content.decode())['resultSets'][0]['rowSet']

        # Define indices for data to print
        data_ids = [1, 3, 4, 6, 7, 8, 9, 10, 11, 12, 13]

        select_data = [[each_list[i] for i in data_ids] for each_list in data]
        select_headers = itemgetter(*data_ids)(headers)

        return select_headers, select_data