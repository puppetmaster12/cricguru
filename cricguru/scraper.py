import requests
from bs4 import BeautifulSoup
import pandas as pd
from dotenv import load_dotenv
import os
from urllib.parse import urlencode
from collections import OrderedDict

load_dotenv()

# Get all data for given query parameters
# ------------- Note -------------
# Default row limit set to 200 | 12/03/2022
class Scraper:
    def __init__(self, query_params):
        self.query_params = query_params

    def getTeamData(self, limit=100):
        encoded_params = urlencode(self.query_params)
        # URLS
        url = 'https://stats.espncricinfo.com/ci/engine/stats/index.html?{0}&page={1}'

        page_counter = 0
        row_limit = 0
        cric_data_pages = []

        # Scraper loop
        while True:
            page_counter += 1
            
            url = url.format(encoded_params, str(page_counter))
            
            dfs = pd.read_html(url)
            print(page_counter)
            row_limit += len(dfs[2])

            if row_limit < limit:
                cric_data_pages.append(dfs[2])
            elif page_counter == 1 and len(dfs[2]) > limit:
                cric_data_pages.append(dfs[2].iloc[:limit])
                break
            else:
                cric_data_pages.append(dfs[2].iloc[:limit-len(dfs[2])])
                break

        cric_data = pd.concat(cric_data_pages)
        cric_data = cric_data.loc[:, ~cric_data.columns.str.startswith('Unnamed')]
        return cric_data

    def getPlayerData(self, player_id=0):
        url = 'https://stats.espncricinfo.com/ci/engine/player/{0}.html?{1}'
        encoded_params = urlencode(self.query_params)

        url = url.format(str(player_id), encoded_params)
        dfs = pd.read_html(url)
        cric_data = dfs[3]
        cric_data = cric_data.loc[:, ~cric_data.columns.str.startswith('Unnamed')]
        return cric_data