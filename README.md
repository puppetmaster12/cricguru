<h2 align="center">Cricguru</h2>

## Overview
Cricguru is a data extraction module for extracting data from the Statsguru data query on Cricinfo. I was inspired to build a simple tool to extract dataframes from statsguru for analyzing cricket data and was finding it difficult to obtain overall figures from the website as they did not have an API for it. Cricinfo has a large variety of cricket data for all classes of cricket matches and also in-depth player data. However without an API it is impossible to extract any useful information from it. Hence this module has functions to easily get the cricket data we want without having to manually scrape the website. The data output is currently returned in the form of Pandas dataframes. You can find the full documentation <a href="https://cricguru.readthedocs.io/en/stable/overview.html" target="_blank">here</a>.

## Team Data
Data by team can be obtained for the three main classes of cricket formats which are <b>Test</b>, <b>One-day</b> and <b>T20</b>. Excluding the class argument would return the overall data. In order to filter by teams and opposition you must provide one of the following ids to the team and opposition arguments respectively for some popular teams.

{"all teams": "", "Afghanistan": "40", "Australia": "2", "Bangladesh": "25", "England": "1", "ICC World XI": "140", "India": "6", "Ireland": "29", "New Zealand": "5", "Pakistan": "7", "South Africa": "3", "Sri Lanka": "8", "West Indies": "4", "Zimbabwe": "9"}

## Player Data
Data by player can be obtained for the same classes mentioned above. The player class however requires a player id which can be obtained from Cricinfo by selecting a team followed by a player from that team. For example <a href="https://www.espncricinfo.com/player/angelo-mathews-49764">Angelo Mathew's</a> id is 49764 which can be found appended to the url of the player's stats page on Cricinfo.

## Built With
This project primarily uses Python 3.8 in combination with Pandas. Pandas is used to get the tables directly from the Statsguru query pages and convert them to dataframes. Urllib is used to format the url and append the query parameters. Poetry is used for packaging and publishing.

## Getting Started
You can install the package using the following command.
```sh
pip install cricguru
```

## Usage
You can get overall figures for all teams with the following. You must pass in the query parameters in a dictionary as shown. The "template" key with a "results" value is required along with the "class" variable which specifies which format of cricket you require data from. The classes for each format are as follows.
<br>
1 - Test
<br>2 - ODI
<br>3 - T20
<br>11 - All
<br>10 - Women's T20i
<br>8 - Women's Test
<br>9 - Women's ODI
<br>20 - Youth Test
<br>21 - Youth ODI
<br>22 - Youth T20
```sh
from cricguru import team

team = team.Team()
query_params = {"template": "results", "class": "2"}
cric_data = team.overall(query_params)

#Returns a pandas dataframe
cric_data.head()
```
For player data you have to provide the player id to initialize the player object and then call the function for the type of data you require. You have to specify what type of player data you need such as allround, batting or bowling.

```sh
from cricguru import player

player = player.Player(49764)
query_params = {
    'class' : '1',
    'type' : 'allround'
}

cric_data = player.career_summary(query_params)
print(cric_data.head())
```

## Contributing
This is an amateur project at best and I am still a complete beginner to Python and would greatly welcome any suggestions, advice, constructive criticism, best practices or contributions to the project.  Simply open a pull request or issue and I will check it out.

## Contact
You can also contact me at pavithranthilakanathan@gmail.com or on twitter - <a href="https://twitter.com/pavin_v1">@pavin_v1</a>

## License
Distributed under the MIT license. See `LICENSE.md' for more information.

## Acknowledgements
<ul>
  <li><a href="https://www.espncricinfo.com/">ESPN Cricinfo</a></li>
</ul>

## Todo
<ul>
  <li>100% code coverage</li>
  <li>Additional data formats</li>
</ul>
