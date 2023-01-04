from .scraper import Scraper


class Player:
    """
    The Player class contains all the functions that extract data related to players

    Attributes
    ----------
    player_id : int
        ID of the player obtained from Cricinfo

    Methods
    -------
    career_summary(query_params)
        Returns the career summary stats of the player.

    inn_list(query_params)
        Returns the list of innings played by the player and stats.

    match_list(query_params)
        Returns the list of matches played by the player and stats.

    cumulative_avg(query_params)
        Returns the cumulative average of all matches played.

    reverse_cumulative(query_params)
        Returns the reverse cumulative average of all matches played.

    series_avg(query_params)
        Returns the average scores and bowling stats for each series.

    ground_avg(query_params)
        Returns the average scores and bowling stats in each ground played.

    match_results(query_params)
        Returns the results of all matches played.

    match_awards(query_params)
        Returns the awards earned in all matches.

    series_awards(query_params)
        Returns the awards earned in all series.

    partnership_summary(query_params)
        Returns the summary stats of all partnerships.

    partnership_list(query_params)
        Returns the list of all partnerships and stats.

    dismissal_summary(query_params)
        Returns the summary of all batting dismissals under various groupings.

    bowler_summary(query_params)
        Returns the summary of stats against all bowlers faced.

    fielder_summary(query_params)
        Returns the summary of stats and dismissals against fielding players.

    dismissal_list(query_params)
        Returns the list of all dismissals.

    dism_summary(query_params)
        Returns the summary of all wickets by the player.

    batsman_summary(query_params)
        Returns the summary stats of all batters dismissed.

    fielder_summary(query_params)
        Returns the summary stats dismissals by fielders.

    wickets_list(query_params)
        Returns the list of all wickets taken.
    """

    def __init__(self, player_id):
        """
        Parameters
        ----------
        player_id : int
            ID of the player obtained from Cricinfo
        """
        # Default results parameter required by cricinfo in all queries
        self.query = {"template": "results"}
        self.player_id = player_id
        self.cric_data = []

    def career_summary(self, query_params):
        """Returns the career summary stats of the player.

        Parameters
        ----------
        query_params (dict of str) : str
            A dictionary containing all the query parameters.

        Returns
        -------
        pandas.Dataframe
            A dataframe containing the query results
        """
        # Update default query dict with query_params dict
        self.query.update(query_params)
        scraper = Scraper(self.query)
        cric_data = scraper.getPlayerData(self.player_id)

        return cric_data

    def inn_list(self, query_params):
        """Returns the list of innings played by the player and stats.

        Parameters
        ----------
        query_params (dict of str) : str
            A dictionary containing all the query parameters.

        Returns
        -------
        pandas.Dataframe
            A dataframe containing the query results
        """
        self.query.update(query_params)
        self.query["view"] = "innings"
        scraper = Scraper(self.query)
        cric_data = scraper.getPlayerData(self.player_id)

        return cric_data

    def match_list(self, query_params):
        """Returns the list of matches played by the player and stats.

        Parameters
        ----------
        query_params (dict of str) : str
            A dictionary containing all the query parameters.

        Returns
        -------
        pandas.Dataframe
            A dataframe containing the query results
        """
        self.query.update(query_params)
        self.query["view"] = "match"
        scraper = Scraper(self.query)
        cric_data = scraper.getPlayerData(self.player_id)

        return cric_data

    def cumulative_avg(self, query_params):
        """Returns the cumulative average of all matches played.

        Parameters
        ----------
        query_params (dict of str) : str
            A dictionary containing all the query parameters.

        Returns
        -------
        pandas.Dataframe
            A dataframe containing the query results
        """
        self.query.update(query_params)
        self.query["view"] = "cumulative"
        scraper = Scraper(self.query)
        cric_data = scraper.getPlayerData(self.player_id)

        return cric_data

    def reverse_cumulative(self, query_params):
        """Returns the reverse cumulative average of all matches played.

        Parameters
        ----------
        query_params (dict of str) : str
            A dictionary containing all the query parameters.

        Returns
        -------
        pandas.Dataframe
            A dataframe containing the query results
        """
        self.query.update(query_params)
        self.query["view"] = "reverse_cumulative"
        scraper = Scraper(self.query)
        cric_data = scraper.getPlayerData(self.player_id)

        return cric_data

    def series_avg(self, query_params):
        """Returns the average scores and bowling stats for each series.

        Parameters
        ----------
        query_params (dict of str) : str
            A dictionary containing all the query parameters.

        Returns
        -------
        pandas.Dataframe
            A dataframe containing the query results
        """
        self.query.update(query_params)
        self.query["view"] = "series"
        scraper = Scraper(self.query)
        cric_data = scraper.getPlayerData(self.player_id)

        return cric_data

    def ground_avg(self, query_params):
        """Returns the average scores and bowling stats in each ground played.

        Parameters
        ----------
        query_params (dict of str) : str
            A dictionary containing all the query parameters.

        Returns
        -------
        pandas.Dataframe
            A dataframe containing the query results
        """
        self.query.update(query_params)
        self.query["view"] = "ground"
        scraper = Scraper(self.query)
        cric_data = scraper.getPlayerData(self.player_id)

        return cric_data

    def match_results(self, query_params):
        """Returns the results of all matches played.

        Parameters
        ----------
        query_params (dict of str) : str
            A dictionary containing all the query parameters.

        Returns
        -------
        pandas.Dataframe
            A dataframe containing the query results
        """
        self.query.update(query_params)
        self.query["view"] = "results"
        scraper = Scraper(self.query)
        cric_data = scraper.getPlayerData(self.player_id)

        return cric_data

    def match_awards(self, query_params):
        """Returns the awards earned in all matches.

        Parameters
        ----------
        query_params (dict of str) : str
            A dictionary containing all the query parameters.

        Returns
        -------
        pandas.Dataframe
            A dataframe containing the query results
        """
        self.query.update(query_params)
        self.query["view"] = "awards_match"
        scraper = Scraper(self.query)
        cric_data = scraper.getPlayerData(self.player_id)

        return cric_data

    def series_awards(self, query_params):
        """Returns the awards earned in all series.

        Parameters
        ----------
        query_params (dict of str) : str
            A dictionary containing all the query parameters.

        Returns
        -------
        pandas.Dataframe
            A dataframe containing the query results
        """
        self.query.update(query_params)
        self.query["view"] = "awards_series"
        scraper = Scraper(self.query)
        cric_data = scraper.getPlayerData(self.player_id)

        return cric_data

    # BATTING
    def partnership_summary(self, query_params):
        """Returns the summary stats of all partnerships.

        Parameters
        ----------
        query_params (dict of str) : str
            A dictionary containing all the query parameters.

        Returns
        -------
        pandas.Dataframe
            A dataframe containing the query results

        Raises
        ------
        Exception
            Functions that return batting data will not work with bowling parameters
        """
        self.query.update(query_params)
        self.query["view"] = "fow_summary"
        if self.query["type"] == "batting":
            scraper = Scraper(self.query)
            cric_data = scraper.getPlayerData(self.player_id)

            return cric_data
        raise Exception("Partnership summary is only available for batting data")

    def partnership_list(self, query_params):
        """Returns the list of all partnerships and stats.

        Parameters
        ----------
        query_params (dict of str) : str
            A dictionary containing all the query parameters.

        Returns
        -------
        pandas.Dataframe
            A dataframe containing the query results

        Raises
        ------
        Exception
            Functions that return batting data will not work with bowling parameters
        """
        self.query.update(query_params)
        self.query["view"] = "fow_list"
        if self.query["type"] == "batting":
            scraper = Scraper(self.query)
            cric_data = scraper.getPlayerData(self.player_id)

            return cric_data
        raise Exception("Partnership list is only available for batting data")

    def dismissal_summary(self, query_params):
        """Returns the summary of all batting dismissals under various groupings.

        Parameters
        ----------
        query_params (dict of str) : str
            A dictionary containing all the query parameters.

        Returns
        -------
        pandas.Dataframe
            A dataframe containing the query results

        Raises
        ------
        Exception
            Functions that return batting data will not work with bowling parameters
        """
        self.query.update(query_params)
        self.query["view"] = "dismissal_summary"
        if self.query["type"] == "batting":
            scraper = Scraper(self.query)
            cric_data = scraper.getPlayerData(self.player_id)

            return cric_data
        raise Exception("Dismissal summary is only available for batting data")

    def bowler_summary(self, query_params):
        """Returns the summary of stats against all bowlers faced.

        Parameters
        ----------
        query_params (dict of str) : str
            A dictionary containing all the query parameters.

        Returns
        -------
        pandas.Dataframe
            A dataframe containing the query results

        Raises
        ------
        Exception
            Functions that return batting data will not work with bowling parameters
        """
        self.query.update(query_params)
        self.query["view"] = "bowler_summary"
        if self.query["type"] == "batting":
            scraper = Scraper(self.query)
            cric_data = scraper.getPlayerData(self.player_id)

            return cric_data
        raise Exception("Bowler summary is only available for batting data")

    def fielder_summary(self, query_params):
        """Returns the summary of stats and dismissals against fielding players.

        Parameters
        ----------
        query_params (dict of str) : str
            A dictionary containing all the query parameters.

        Returns
        -------
        pandas.Dataframe
            A dataframe containing the query results

        Raises
        ------
        Exception
            Functions that return batting data will not work with bowling parameters
        """
        self.query.update(query_params)
        self.query["view"] = "fielder_summary"
        if self.query["type"] == "batting":
            scraper = Scraper(self.query)
            cric_data = scraper.getPlayerData(self.player_id)

            return cric_data
        raise Exception("Fielder summary is only available for batting data")

    def dismissal_list(self, query_params):
        """Returns the list of all dismissals.

        Parameters
        ----------
        query_params (dict of str) : str
            A dictionary containing all the query parameters.

        Returns
        -------
        pandas.Dataframe
            A dataframe containing the query results

        Raises
        ------
        Exception
            Functions that return batting data will not work with bowling parameters
        """
        self.query.update(query_params)
        self.query["view"] = "dismissal_list"
        if self.query["type"] == "batting":
            scraper = Scraper(self.query)
            cric_data = scraper.getPlayerData(self.player_id)

            return cric_data
        raise Exception("Dismissal list is only available for batting data")

    # BOWLING
    def dism_summary(self, query_params):
        """Returns the summary of all wickets by the player.

        Parameters
        ----------
        query_params (dict of str) : str
            A dictionary containing all the query parameters.

        Returns
        -------
        pandas.Dataframe
            A dataframe containing the query results

        Raises
        ------
        Exception
            Functions that return bowling data will not work with batting parameters
        """
        self.query.update(query_params)
        self.query["view"] = "dismissal_summary"
        if self.query["type"] == "bowling":
            scraper = Scraper(self.query)
            cric_data = scraper.getPlayerData(self.player_id)

            return cric_data
        raise Exception("Dismissal summary is only available for bowling data")

    def batsman_summary(self, query_params):
        """Returns the summary stats of all batters dismissed.

        Parameters
        ----------
        query_params (dict of str) : str
            A dictionary containing all the query parameters.

        Returns
        -------
        pandas.Dataframe
            A dataframe containing the query results

        Raises
        ------
        Exception
            Functions that return bowling data will not work with batting parameters
        """
        self.query.update(query_params)
        self.query["view"] = "batsman_summary"
        if self.query["type"] == "bowling":
            scraper = Scraper(self.query)
            cric_data = scraper.getPlayerData(self.player_id)

            return cric_data
        raise Exception("Batsman summary is only available for bowling data")

    def fielder_summary(self, query_params):
        """Returns the summary stats dismissals by fielders.

        Parameters
        ----------
        query_params (dict of str) : str
            A dictionary containing all the query parameters.

        Returns
        -------
        pandas.Dataframe
            A dataframe containing the query results

        Raises
        ------
        Exception
            Functions that return bowling data will not work with batting parameters
        """
        self.query.update(query_params)
        self.query["view"] = "fielder_summary"
        if self.query["type"] == "bowling":
            scraper = Scraper(self.query)
            cric_data = scraper.getPlayerData(self.player_id)

            return cric_data
        raise Exception("Fielder summary is only available for bowling data")

    def wickets_list(self, query_params):
        """Returns the list of all wickets taken.

        Parameters
        ----------
        query_params (dict of str) : str
            A dictionary containing all the query parameters.

        Returns
        -------
        pandas.Dataframe
            A dataframe containing the query results

        Raises
        ------
        Exception
            Functions that return bowling data will not work with batting parameters
        """
        self.query.update(query_params)
        self.query["view"] = "dismissal_list"
        if self.query["type"] == "bowling":
            scraper = Scraper(self.query)
            cric_data = scraper.getPlayerData(self.player_id)

            return cric_data
        raise Exception("Wickets list is only available for bowling data")
