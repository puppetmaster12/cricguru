import Scraper


class Player:
    def __init__(self, player_id):
        self.search_type = "player"
        self.query = {"template": "results"}
        self.player_id = player_id
        self.cric_data = []

    def career_summary(self, query_params):
        self.query.update(query_params)
        scraper = Scraper(self.query)
        cric_data = scraper.getPlayerData(self.player_id)

        return cric_data

    def inn_list(self, query_params):
        self.query.update(query_params)
        self.query["view"] = "innings"
        scraper = Scraper(self.query)
        cric_data = scraper.getPlayerData(self.player_id)

        return cric_data

    def match_list(self, query_params):
        self.query.update(query_params)
        self.query["view"] = "match"
        scraper = Scraper(self.query)
        cric_data = scraper.getPlayerData(self.player_id)

        return cric_data

    def cumulative_avg(self, query_params):
        self.query.update(query_params)
        self.query["view"] = "cumulative"
        scraper = Scraper(self.query)
        cric_data = scraper.getPlayerData(self.player_id)

        return cric_data

    def reverse_cumulative(self, query_params):
        self.query.update(query_params)
        self.query["view"] = "reverse_cumulative"
        scraper = Scraper(self.query)
        cric_data = scraper.getPlayerData(self.player_id)

        return cric_data

    def series_avg(self, query_params):
        self.query.update(query_params)
        self.query["view"] = "series"
        scraper = Scraper(self.query)
        cric_data = scraper.getPlayerData(self.player_id)

        return cric_data

    def ground_avg(self, query_params):
        self.query.update(query_params)
        self.query["view"] = "ground"
        scraper = Scraper(self.query)
        cric_data = scraper.getPlayerData(self.player_id)

        return cric_data

    def match_results(self, query_params):
        self.query.update(query_params)
        self.query["view"] = "results"
        scraper = Scraper(self.query)
        cric_data = scraper.getPlayerData(self.player_id)

        return cric_data

    def match_awards(self, query_params):
        self.query.update(query_params)
        self.query["view"] = "awards_match"
        scraper = Scraper(self.query)
        cric_data = scraper.getPlayerData(self.player_id)

        return cric_data

    def series_awards(self, query_params):
        self.query.update(query_params)
        self.query["view"] = "awards_series"
        scraper = Scraper(self.query)
        cric_data = scraper.getPlayerData(self.player_id)

        return cric_data

    # BATTING
    def partnership_summary(self, query_params):
        self.query.update(query_params)
        self.query["view"] = "fow_summary"
        if self.query["type"] == "batting":
            scraper = Scraper(self.query)
            cric_data = scraper.getPlayerData(self.player_id)

            return cric_data
        raise Exception("Partneship summary is only available for batting data")

    def dismissal_summary(self, query_params):
        self.query.update(query_params)
        self.query["view"] = "dismissal_summary"
        if self.query["type"] == "batting":
            scraper = Scraper(self.query)
            cric_data = scraper.getPlayerData(self.player_id)

            return cric_data
        raise Exception("Dismissal summary is only available for batting data")

    def bowler_summary(self, query_params):
        self.query.update(query_params)
        self.query["view"] = "bowler_summary"
        if self.query["type"] == "batting":
            scraper = Scraper(self.query)
            cric_data = scraper.getPlayerData(self.player_id)

            return cric_data
        raise Exception("Bowler summary is only available for batting data")

    def fielder_summary(self, query_params):
        self.query.update(query_params)
        self.query["view"] = "fielder_summary"
        if self.query["type"] == "batting":
            scraper = Scraper(self.query)
            cric_data = scraper.getPlayerData(self.player_id)

            return cric_data
        raise Exception("Fielder summary is only available for batting data")

    def dismissal_list(self, query_params):
        self.query.update(query_params)
        self.query["view"] = "dismissal_list"
        if self.query["type"] == "batting":
            scraper = Scraper(self.query)
            cric_data = scraper.getPlayerData(self.player_id)

            return cric_data
        raise Exception("Dismissal list is only available for batting data")

    # BOWLING
    def dism_summary(self, query_params):
        self.query.update(query_params)
        self.query["view"] = "dismissal_summary"
        if self.query["type"] == "bowling":
            scraper = Scraper(self.query)
            cric_data = scraper.getPlayerData(self.player_id)

            return cric_data
        raise Exception("Dismissal summary is only available for bowling data")

    def batsman_summary(self, query_params):
        self.query.update(query_params)
        self.query["view"] = "batsman_summary"
        if self.query["type"] == "bowling":
            scraper = Scraper(self.query)
            cric_data = scraper.getPlayerData(self.player_id)

            return cric_data
        raise Exception("Batsman summary is only available for bowling data")

    def fielder_summary(self, query_params):
        self.query.update(query_params)
        self.query["view"] = "fielder_summary"
        if self.query["type"] == "bowling":
            scraper = Scraper(self.query)
            cric_data = scraper.getPlayerData(self.player_id)

            return cric_data
        raise Exception("Fielder summary is only available for bowling data")

    def wickets_list(self, query_params):
        self.query.update(query_params)
        self.query["view"] = "dismissal_list"
        if self.query["type"] == "bowling":
            scraper = Scraper(self.query)
            cric_data = scraper.getPlayerData(self.player_id)

            return cric_data
        raise Exception("Wickets list is only available for bowling data")
