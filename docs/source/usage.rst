Usage
=====

In order to use the package you need to import either the team or player submodule 
which contain the classes.

Parameters
----------

Statsguru uses a specific set of parameters in its search queries. The following are all the
parameters necessary to use the functions implemented in both the team and player submodules.
These must be supplied in the form of a dictionary to any function used. All parameters are
to be in string format.

class
~~~~~
The format of the matches. For team data this parameter is mandatory. Values: Test - 1, One-day - 2, T20 - 3, All - 11

team
~~~~
The team for which you need to filter by. This parameter is optional. Excluding this will give
overall results. Most of the team ids can be found in the overview section of the docs. The rest
will be updated soon.

opposition
~~~~~~~~~~
The opposing team played against the team specified in the team parameter. This again is an optional
parameter. The same ids team ids apply here.

home_or_away
~~~~~~~~~~~~
Whether the team was playing in home, away or in a neutral ground. The values are 1,2 and 3 respectively.

results
~~~~~~~
The results of the match. The values are 1,2,3 and 5 for win, loss, tie and n/r respectively.

season
~~~~~~
This is the season the matches were played. The parameter value will simply be the starting year of the
season. For example, 1973 for 1973/4 season.

spanmax1
~~~~~~~~
The date upto which you require records. This must be a string in the format DD-Mon-YYYY - "10 Dec 2021".

spanmin1
~~~~~~~~
This is the minimum date from which you require the records. The format is the same as spanmax1.

ground
~~~~~~
The ground on which the matches were played. All ground ids are available in the overview.

Player Parameters
-----------------

These parameters are specific to the player class functions and would not work with the team class.

type
~~~~
The type of data about the player that you require. The values are allround, batting, bowling and fielding.

Examples
--------

You can get overall figures for all teams with the following. You must
pass in the query parameters in a dictionary as shown.

.. code:: python

   from cricguru import team

   team = team.Team()
   query_params = {"template": "results"}
   cric_data = team.overall(query_params)

   print(cric_data.head())

For player data you have to provide the player id to initialize the
player object and then call the function for the type of data you
require. You have to specify what type of player data you need such as
allround, batting or bowling.

.. code:: python

   from cricguru import player

   player = player.Player(49764)
   query_params = {
       'class' : '1',
       'type' : 'allround'
   }

   cric_data = player.career_summary(query_params)
   print(cric_data.head())
