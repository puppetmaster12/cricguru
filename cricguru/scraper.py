import os
from collections import OrderedDict
from urllib.parse import urlencode

import pandas as pd
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()

# Get all data for given query parameters
# ------------- Note -------------
# Default row limit set to 200 | 12/03/2022
class Scraper:
    def __init__(self, query_params):
        self.query_params = query_params
        self.page_counter = 0

    def getTeamData(self, limit=30):
        encoded_params = urlencode(self.query_params)
        # URLS
        host_url = (
            "https://stats.espncricinfo.com/ci/engine/stats/index.html?{0}&page={1}"
        )

        row_limit = 0
        cric_data_pages = []

        # Scraper loop
        while True:
            self.page_counter += 1
            url = host_url.format(encoded_params, str(self.page_counter))
            dfs = pd.read_html(url)
            row_limit += len(dfs[2])

            if (
                dfs[2].iloc[dfs[2].index.get_loc(0), 0]
                == "No records available to match this query"
            ):
                break

            if row_limit < limit:
                cric_data_pages.append(dfs[2])
            elif self.page_counter == 1 and len(dfs[2]) > limit:
                cric_data_pages.append(dfs[2].iloc[:limit])
                break
            else:
                cric_data_pages.append(dfs[2].iloc[: limit - len(dfs[2])])
                break

        cric_data = pd.concat(cric_data_pages)
        cric_data = cric_data.loc[:, ~cric_data.columns.str.startswith("Unnamed")]
        return cric_data

    def getPlayerData(self, player_id=0):
        url = "https://stats.espncricinfo.com/ci/engine/player/{0}.html?{1}"
        encoded_params = urlencode(self.query_params)

        url = url.format(str(player_id), encoded_params)
        dfs = pd.read_html(url)
        cric_data = dfs[3]
        cric_data = cric_data.loc[:, ~cric_data.columns.str.startswith("Unnamed")]
        return cric_data
    
    def getPlayerAvgData(self, player_id=0):
        url = "https://stats.espncricinfo.com/ci/engine/player/{0}.html?{1}"
        encoded_params = urlencode(self.query_params)
        
        url = url.format(str(player_id), encoded_params)
        dfs = pd.read_html(url)
        cric_data = dfs[2]
        cric_data = cric_data.loc[:, ~cric_data.columns.str.startswith("Unnamed")]
        return cric_data
