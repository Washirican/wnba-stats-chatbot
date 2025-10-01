
#!/usr/bin/env python3
"""
WNBA Shot Charts
"""
import json
import logging

import requests

HEADERS = {
    'Host': 'www.wnba.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0',
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br, zstd',
    'x-nba-stats-origin': 'stats',
    'x-nba-stats-token': 'true',
    'Connection': 'keep-alive',
    'Referer': 'https://www.wnba.com/',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

# complete_url = 'https://www.wnba.com/api/schedule?season=2025&regionId=1'

parameters = {
            'season': '2025',
            'regionId': '1',
        }

endpoint = 'schedule'
request_url = f'https://www.wnba.com/api/{endpoint}?'

# Create a custom logger
logging.basicConfig(level=logging.DEBUG,
                    format='%(levelname)s: %(asctime)s - %(message)s',
                    datefmt='%d-%b-%y %H:%M:%S')

logging.disable(logging.CRITICAL)

r = requests.get(request_url, headers=HEADERS, params=parameters, timeout=10)
data = json.loads(r.content.decode())
