from .scraper import Scraper


class Team:
    """
    The Team class contains all the functions that extract overall and teams related data.
    """

    # Methods
    # -------
    # overall(query_params, limit=30)
    #     Returns overall figures for all matches played by each team.

    # inn_by_inn(query_params, limit=30)
    #     Returns match results for each innings.

    # matchtot(query_params, limit=30)
    #     Returns total scores for each team by match.

    # matchres(query_params, limit=30)
    #     Returns results of each match.

    # series_avg(query_params, limit=30)
    #     Returns the average scores and stats for each series.

    # ground_avg(query_params, limit=30)
    #     Returns the average scores and stats based on ground played in.

    # by_host(query_params, limit=30)
    #     Returns the overall stats for each team by host team.

    # by_opp(query_params, limit=30)
    #     Returns the overall stats for each team against each opposition team.

    # by_year(query_params, limit=30)
    #     Returns the overall stats for each team by year.

    # by_season(query_params, limit=30)
    #     Returns the overall stats for each team by season.

    # overall_extras(query_params, limit=30)
    #     Returns the overall extras scored by each team and other stats related to extras.

    # extras_inn(query_params, limit=30)
    #     Returns the extras scored by innings.
    def __init__(self, is_csv=True):
        # Default query parameters for team data
        self.query = {"type": "team", "template": "results"}
        self.is_csv = is_csv

    # OVERALL FIGURES
    def overall(self, query_params, limit=30):
        """Returns the overall figures for all matches played by each team.

        Parameters
        ----------
        query_params : dict[str, list, or set or dict]
            A dictionary containing all the query parameters.
        limit : int
            The data limit for number of records returned. Default limit is 30.
        """
        # Update default query dict with query_params dict
        self.query.update(query_params)
        scraper = Scraper(self.query)
        cric_data = scraper.getTeamData(limit)
        
        if self.is_csv:
            cric_data.to_csv('overall.csv')
        else:
            return cric_data

    # INNINGS BY INNINGS
    def inn_by_inn(self, query_params, limit=30):
        """Returns match results for each innings.

        Parameters
        ----------
        query_params : dict[str, list, or set or dict]
            A dictionary containing all the query parameters.
        limit : int
            The data limit for number of records returned. Default limit is 30.

        Returns
        -------
        pandas.Dataframe
            A dataframe containing the query results
        """
        self.query.update(query_params)
        # Each data function has a unique view parameter ex. innings
        self.query["view"] = "innings"
        scraper = Scraper(self.query)
        cric_data = scraper.getTeamData(limit)

        if self.is_csv:
            cric_data.to_csv('inn_by_inn.csv')
        else:
            return cric_data

    # MATCH TOTALS
    def matchtot(self, query_params, limit=30):
        """Returns total scores for each team by match.

        Parameters
        ----------
        query_params : dict[str, list, or set or dict]
            A dictionary containing all the query parameters.
        limit : int
            The data limit for number of records returned. Default limit is 30.

        Returns
        -------
        pandas.Dataframe
            A dataframe containing the query results
        """
        self.query.update(query_params)
        self.query["view"] = "match"
        scraper = Scraper(self.query)
        cric_data = scraper.getTeamData(limit)

        if self.is_csv:
            cric_data.to_csv('matchtot.csv')
        else:
            return cric_data

    # MATCH RESULTS
    def matchres(self, query_params, limit=30):
        """Returns the overall results of each match.

        Parameters
        ----------
        query_params : dict[str, list, or set or dict]
            A dictionary containing all the query parameters.
        limit : int
            The data limit for number of records returned. Default limit is 30.

        Returns
        -------
        pandas.Dataframe
            A dataframe containing the query results
        """
        self.query.update(query_params)
        self.query["view"] = "results"
        scraper = Scraper(self.query)
        cric_data = scraper.getTeamData(limit)

        if self.is_csv:
            cric_data.to_csv('matchres.csv')
        else:
            return cric_data

    # SERIES AVERAGE
    def series_avg(self, query_params, limit=30):
        """Returns the average scores and stats for each series.

        Parameters
        ----------
        query_params : dict[str, list, or set or dict]
            A dictionary containing all the query parameters.
        limit : int
            The data limit for number of records returned. Default limit is 30.

        Returns
        -------
        pandas.Dataframe
            A dataframe containing the query results
        """
        self.query.update(query_params)
        self.query["view"] = "series"
        scraper = Scraper(self.query)
        cric_data = scraper.getTeamData(limit)

        if self.is_csv:
            cric_data.to_csv('series_avg.csv')
        else:
            return cric_data

    # GROUND AVERAGE
    def ground_avg(self, query_params, limit=30):
        """Returns the average scores and stats based on ground played in.

        Parameters
        ----------
        query_params : dict[str, list, or set or dict]
            A dictionary containing all the query parameters.
        limit : int
            The data limit for number of records returned. Default limit is 30.

        Returns
        -------
        pandas.Dataframe
            A dataframe containing the query results
        """
        self.query.update(query_params)
        self.query["view"] = "ground"
        scraper = Scraper(self.query)
        cric_data = scraper.getTeamData(limit)

        if self.is_csv:
            cric_data.to_csv('ground_avg.csv')
        else:
            return cric_data

    # RESULTS BY HOST COUNTRY
    def by_host(self, query_params, limit=30):
        """Returns the overall stats for each team by host team.

        Parameters
        ----------
        query_params : dict[str, list, or set or dict]
            A dictionary containing all the query parameters.
        limit : int
            The data limit for number of records returned. Default limit is 30.

        Returns
        -------
        pandas.Dataframe
            A dataframe containing the query results
        """
        self.query.update(query_params)
        self.query["view"] = "host"
        scraper = Scraper(self.query)
        cric_data = scraper.getTeamData(limit)

        if self.is_csv:
            cric_data.to_csv('by_host.csv')
        else:
            return cric_data

    # RESULTS BY OPPOSITION
    def by_opp(self, query_params, limit=30):
        """Returns the overall stats for each team against each opposition team.

        Parameters
        ----------
        query_params : dict[str, list, or set or dict]
            A dictionary containing all the query parameters.
        limit : int
            The data limit for number of records returned. Default limit is 30.

        Returns
        -------
        pandas.Dataframe
            A dataframe containing the query results
        """
        self.query.update(query_params)
        self.query["view"] = "opposition"
        scraper = Scraper(self.query)
        cric_data = scraper.getTeamData(limit)

        if self.is_csv:
            cric_data.to_csv('by_opp.csv')
        else:
            return cric_data

    # BY YEAR
    def by_year(self, query_params, limit=30):
        """Returns the overall stats for each team by year.

        Parameters
        ----------
        query_params : dict[str, list, or set or dict]
            A dictionary containing all the query parameters.
        limit : int
            The data limit for number of records returned. Default limit is 30.

        Returns
        -------
        pandas.Dataframe
            A dataframe containing the query results
        """
        self.query.update(query_params)
        self.query["view"] = "year"
        scraper = Scraper(self.query)
        cric_data = scraper.getTeamData(limit)

        if self.is_csv:
            cric_data.to_csv('by_year.csv')
        else:
            return cric_data

    # BY SEASON
    def by_season(self, query_params, limit=30):
        """Returns the overall stats for each team by season.

        Parameters
        ----------
        query_params : dict[str, list, or set or dict]
            A dictionary containing all the query parameters.
        limit : int
            The data limit for number of records returned. Default limit is 30.

        Returns
        -------
        pandas.Dataframe
            A dataframe containing the query results
        """
        self.query.update(query_params)
        self.query["view"] = "season"
        scraper = Scraper(self.query)
        cric_data = scraper.getTeamData(limit)

        if self.is_csv:
            cric_data.to_csv('by_season.csv')
        else:
            return cric_data

    # OVERALL EXTRAS
    def overall_extras(self, query_params, limit=30):
        """Returns the overall extras scored by each team and other stats related to extras.

        Parameters
        ----------
        query_params : dict[str, list, or set or dict]
            A dictionary containing all the query parameters.
        limit : int
            The data limit for number of records returned. Default limit is 30.

        Returns
        -------
        pandas.Dataframe
            A dataframe containing the query results
        """
        self.query.update(query_params)
        self.query["view"] = "extras"
        scraper = Scraper(self.query)
        cric_data = scraper.getTeamData(limit)

        if self.is_csv:
            cric_data.to_csv('overall_extras.csv')
        else:
            return cric_data

    # EXTRAS BY INNINGS
    def extras_inn(self, query_params, limit=30):
        """Returns the extras scored by innings.

        Parameters
        ----------
        query_params : dict[str, list, or set or dict]
            A dictionary containing all the query parameters.
        limit : int
            The data limit for number of records returned. Default limit is 30.

        Returns
        -------
        pandas.Dataframe
            A dataframe containing the query results
        """
        self.query.update(query_params)
        self.query["view"] = "extras_innings"
        scraper = Scraper(self.query)
        cric_data = scraper.getTeamData(limit)

        if self.is_csv:
            cric_data.to_csv('extras_inn.csv')
        else:
            return cric_data
