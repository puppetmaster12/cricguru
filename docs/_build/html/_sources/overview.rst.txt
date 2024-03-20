Overview
========

Cricguru is a data extraction module for extracting data from the
Statsguru data query on Cricinfo. I was inspired to build a simple tool
to extract dataframes from statsguru for analyzing cricket data and was
finding it difficult to obtain overall figures from the website as they
did not have an API for it. Cricinfo has a large variety of cricket data
for all classes of cricket matches and also in-depth player data.
However without an API it is impossible to extract any useful
information from it. Hence this module has functions to easily get the
cricket data we want without having to manually scrape the website. The
data output is currently returned in the form of Pandas dataframes.

Team Data
---------

Data by team can be obtained for the three main classes of cricket
formats which are Test, One-day and T20. Excluding the class argument
would return the overall data. In order to filter by teams and
opposition you must provide one of the following ids to the team and
opposition arguments respectively for some popular teams.

.. code-block:: json

    {
        "all teams": "", 
        "Afghanistan": "40",
        "Australia" : "2",
        "Bangladesh" : "25",
        "England" : "1",
        "ICC World XI" : "140",
        "India" : "6",
        "Ireland" : "29",
        "New Zealand" : "5",
        "Pakistan" : "7",
        "South Africa" : "3",
        "Sri Lanka" : "8", 
        "West Indies" : "4",
        "Zimbabwe" : "9"
    }

The following are ids for all grounds available in Statsguru.

.. code-block:: json

    {
        "all grounds": "",
        "Adelaide Oval": "131",
        "Bellerive Oval, Hobart": "905",
        "Brisbane Cricket Ground, Woolloongabba, Brisbane": "209",
        "Cazaly's Stadium, Cairns": "1066",
        "Exhibition Ground, Brisbane": "188",
        "Manuka Oval, Canberra": "757",
        "Melbourne Cricket Ground": "61",
        "Perth Stadium": "3404",
        "Sydney Cricket Ground": "132",
        "TIO Stadium, Darwin": "1155",
        "W.A.C.A. Ground, Perth": "213",
        "Bangabandhu National Stadium, Dhaka": "475",
        "Khan Shaheb Osman Ali Stadium, Fatullah": "1844",
        "MA Aziz Stadium, Chattogram": "476",
        "Shaheed Chandu Stadium, Bogra": "1925",
        "Sheikh Abu Naser Stadium, Khulna": "1930",
        "Shere Bangla National Stadium, Mirpur, Dhaka": "2025",
        "Sylhet International Cricket Stadium": "1564",
        "Zahur Ahmed Chowdhury Stadium, Chattogram": "1931",
        "Bramall Lane, Sheffield": "62",
        "Edgbaston, Birmingham": "164",
        "Headingley, Leeds": "179",
        "Kennington Oval, London": "45",
        "Lord's, London": "10",
        "Old Trafford, Manchester": "75",
        "Riverside Ground, Chester-le-Street": "1039",
        "Sophia Gardens, Cardiff": "644",
        "The Rose Bowl, Southampton": "1184",
        "Trent Bridge, Nottingham": "34",
        "Arun Jaitley Stadium, Delhi": "333",
        "Barabati Stadium, Cuttack": "442",
        "Bharat Ratna Shri Atal Bihari Vajpayee Ekana Cricket Stadium, Lucknow": "3355",
        "Brabourne Stadium, Mumbai": "393",
        "Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium, Visakhapatnam": "1896",
        "Eden Gardens, Kolkata": "292",
        "Gandhi Stadium, Jalandhar": "461",
        "Green Park, Kanpur": "419",
        "Gymkhana Ground, Mumbai": "189",
        "Himachal Pradesh Cricket Association Stadium, Dharamsala": "1920",
        "Holkar Cricket Stadium, Indore": "1055",
        "JSCA International Stadium Complex, Ranchi": "2575",
        "K.D.Singh 'Babu' Stadium, Lucknow": "580",
        "Lal Bahadur Shastri Stadium, Hyderabad": "376",
        "M.Chinnaswamy Stadium, Bengaluru": "683",
        "MA Chidambaram Stadium, Chepauk, Chennai": "291",
        "Maharashtra Cricket Association Stadium, Pune": "2677",
        "Narendra Modi Stadium, Motera, Ahmedabad": "840",
        "Nehru Stadium, Madras": "491",
        "Punjab Cricket Association IS Bindra Stadium, Mohali, Chandigarh": "1015",
        "Rajiv Gandhi International Cricket Stadium, Dehradun": "3416",
        "Rajiv Gandhi International Stadium, Uppal, Hyderabad": "1981",
        "Saurashtra Cricket Association Stadium, Rajkot": "2401",
        "Sawai Mansingh Stadium, Jaipur": "664",
        "Sector 16 Stadium, Chandigarh": "621",
        "University Ground, Lucknow": "464",
        "Vidarbha C.A. Ground, Nagpur": "367",
        "Vidarbha Cricket Association Stadium, Jamtha, Nagpur": "2399",
        "Wankhede Stadium, Mumbai": "713",
        "The Village, Malahide, Dublin": "974",
        "AMI Stadium, Christchurch": "152",
        "Basin Reserve, Wellington": "116",
        "Bay Oval, Mount Maunganui": "2524",
        "Carisbrook, Dunedin": "155",
        "Eden Park, Auckland": "283",
        "Hagley Oval, Christchurch": "93",
        "McLean Park, Napier": "453",
        "Seddon Park, Hamilton": "504",
        "University Oval, Dunedin": "769",
        "Arbab Niaz Stadium, Peshawar": "879",
        "Bagh-e-Jinnah, Lahore": "301",
        "Bahawal Stadium, Bahawalpur": "454",
        "Gaddafi Stadium, Lahore": "545",
        "Ibn-e-Qasim Bagh Stadium, Multan": "494",
        "Iqbal Stadium, Faisalabad": "639",
        "Jinnah Stadium, Gujranwala": "844",
        "Jinnah Stadium, Sialkot": "455",
        "Multan Cricket Stadium": "1597",
        "National Stadium, Karachi": "487",
        "Niaz Stadium, Hyderabad": "574",
        "Peshawar Club Ground": "402",
        "Pindi Club Ground, Rawalpindi": "337",
        "Rawalpindi Cricket Stadium": "1001",
        "Sheikhupura Stadium": "1061",
        "Southend Club Cricket Stadium, Karachi": "959",
        "Buffalo Park, East London": "931",
        "Ellis Park, Johannesburg": "428",
        "Kingsmead, Durban": "302",
        "Lord's, Durban": "212",
        "Mangaung Oval, Bloemfontein": "949",
        "Newlands, Cape Town": "174",
        "Old Wanderers, Johannesburg": "183",
        "Senwes Park, Potchefstroom": "1367",
        "St George's Park, Gqeberha": "173",
        "SuperSport Park, Centurion": "902",
        "The Wanderers Stadium, Johannesburg": "508",
        "Asgiriya Stadium, Kandy": "726",
        "Colombo Cricket Club Ground": "339",
        "Galle International Stadium": "847",
        "P Sara Oval, Colombo": "416",
        "Pallekele International Cricket Stadium": "2503",
        "R.Premadasa Stadium, Khettarama, Colombo": "1004",
        "Sinhalese Sports Club Ground, Colombo": "679",
        "Tyronne Fernando Stadium, Moratuwa": "835",
        "Dubai International Cricket Stadium": "2439",
        "Sharjah Cricket Stadium": "848",
        "Sheikh Zayed Stadium, Abu Dhabi": "1965",
        "Antigua Recreation Ground, St John's, Antigua": "547",
        "Arnos Vale Ground, Kingstown, St Vincent": "680",
        "Bourda, Georgetown, Guyana": "169",
        "Daren Sammy National Cricket Stadium, Gros Islet, St Lucia": "1697",
        "Kensington Oval, Bridgetown, Barbados": "199",
        "National Cricket Stadium, St George's, Grenada": "1131",
        "Providence Stadium, Guyana": "1986",
        "Queen's Park Oval, Port of Spain, Trinidad": "208",
        "Sabina Park, Kingston, Jamaica": "200",
        "Sir Vivian Richards Stadium, North Sound, Antigua": "1985",
        "Warner Park, Basseterre, St Kitts": "576",
        "Windsor Park, Roseau, Dominica": "629",
        "Bulawayo Athletic Club": "459",
        "Harare Sports Club": "260",
        "Queens Sports Club, Bulawayo": "261"
    }

Player Data
-----------

Data by player can be obtained for the same classes mentioned above. The
player class however requires a player id which can be obtained from
Cricinfo by selecting a team followed by a player from that team. For
example Angelo Mathew’s id is 49764 which can be found appended to the
url of the player’s stats page on Cricinfo.

Built With
----------

This project primarily uses Python 3.8 in combination with Pandas and Beautiful Soup.
Requests and Beautiful Soup are used primarily to scrape and organize the tables and Pandas Dataframes are the main data structures. 
Urllib is used to format the url and append the query parameters. Poetry is used for packaging and publishing.

Contributing
------------

All contrinbutions are greatly welcome with any suggestions, advice, constructive
criticism, best practices or contributions to the project. Simply open a
pull request or issue and I will check it out.

Contact
-------

You can also contact me at pavithranthilakanathan@gmail.com or on
twitter - @pavin_v1

License
-------

Distributed under the MIT license. See \`LICENSE.md’ for more
information.

Acknowledgements
----------------

.. raw:: html

   <ul>

.. raw:: html

   <li>

ESPN Cricinfo

.. raw:: html

   </li>

.. raw:: html

   </ul>

Todo
----

.. raw:: html

   <ul>

.. raw:: html

   <li>

100% code coverage

.. raw:: html

   </li>

.. raw:: html

   <li>

Additional data formats

.. raw:: html

   </li>

.. raw:: html

   </ul>
