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
            headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.content, 'html.parser')
            
            tables = soup.find_all('table')
            # print(tables)  
            dfs = pd.read_html(str(tables))
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

    # V1 function without header no longer in use
    def getPlayerData(self, player_id=0):
        url = "https://stats.espncricinfo.com/ci/engine/player/{0}.html?{1}"
        encoded_params = urlencode(self.query_params)

        url = url.format(str(player_id), encoded_params)
        print('test')
        dfs = pd.read_html(url)
        cric_data = dfs[3]
        cric_data = cric_data.loc[:, ~cric_data.columns.str.startswith("Unnamed")]
        return cric_data
    
    # New funtion using requests instead of read_html directly on the url
    def getPlayerDataSoup(self, player_id=0):
        url = "https://stats.espncricinfo.com/ci/engine/player/{0}.html?{1}"
        # url = 'https://stats.espncricinfo.com/ci/engine/player/253802.html?class=2;template=results;type=allround'
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
        encoded_params = urlencode(self.query_params)
        
        url = url.format(str(player_id), encoded_params)
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        tables = soup.find_all('table')        
        
        player_data = tables[3]
        
        player_data = pd.read_html(str(player_data))[0]
        
        player_data = player_data.loc[:, ~player_data.columns.str.startswith("Unnamed")]
        
        return player_data    
    
    # New funtion using requests instead of read_html directly on the url
    def getPlayerAvgSoupData(self, player_id=0):
        url = "https://stats.espncricinfo.com/ci/engine/player/{0}.html?{1}"
        # url = 'https://stats.espncricinfo.com/ci/engine/player/253802.html?class=2;template=results;type=allround'
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
        encoded_params = urlencode(self.query_params)
        
        url = url.format(str(player_id), encoded_params)
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        tables = soup.find_all('table')        
        
        player_data = tables[2]
        
        player_data = pd.read_html(str(player_data))[0]
        
        player_data = player_data.loc[:, ~player_data.columns.str.startswith("Unnamed")]
        
        return player_data
    
    # V1 function without header no longer in use
    def getPlayerAvgData(self, player_id=0):
        url = "https://stats.espncricinfo.com/ci/engine/player/{0}.html?{1}"
        encoded_params = urlencode(self.query_params)
        
        url = url.format(str(player_id), encoded_params)
        dfs = pd.read_html(url)
        cric_data = dfs[2]
        cric_data = cric_data.loc[:, ~cric_data.columns.str.startswith("Unnamed")]
        return cric_data
