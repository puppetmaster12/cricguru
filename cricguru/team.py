from scraper import Scraper

# Classes
# Test = 1, ODI = 2, T20 = 3, All = 11
class Team:
    def __init__(self):
        self.query = {'type': 'team', 'template': 'results'}
        self.search_type = 'team'

    # OVERALL FIGURES
    def get_overall(self, query_params, limit=100):
        self.query.update(query_params)
        scraper = Scraper(self.query)
        cric_data = scraper.getTeamData(limit)

        return cric_data

    # INNINGS BY INNINGS
    def get_inns(self, query_params, limit=100):
        self.query.update(query_params)
        self.query['view'] = 'innings'
        cric_data = scraper.getTeamData(query, limit)

        return cric_data

    # MATCH TOTALS
    def get_matchtot(self, query_params, limit=100):
        self.query.update(query_params)
        self.query['view'] = 'match'
        cric_data = scraper.getTeamData(query, limit)

        return cric_data

    # MATCH RESULTS
    def get_matchres(self, query_params, limit=100):
        self.query.update(query_params)
        self.query['view'] = 'results'
        cric_data = scraper.getTeamData(query, limit)

        return cric_data

    # SERIES AVERAGE
    def get_series_avg(self, query_params,limit=100):
        self.query.update(query_params)
        self.query['view'] = 'series'
        cric_data = scraper.getTeamData(query, limit)

        return cric_data

    # GROUND AVERAGE
    def get_ground_avg(self, query_params,limit=100):
        self.query.update(query_params)
        self.query['view'] = 'ground'
        cric_data = scraper.getTeamData(query, limit)

        return cric_data

    # RESULTS BY HOST COUNTRY
    def get_by_host(self, query_params, limit=100):
        self.query.update(query_params)
        self.query['view'] = 'host'
        cric_data = scraper.getTeamData(query, limit)

        return cric_data

    # RESULTS BY OPPOSITION
    def get_by_opp(self, query_params, limit=100):
        self.query.update(query_params)
        self.query['view'] = 'opposition'
        cric_data = scraper.getTeamData(query, limit)

        return cric_data

    # BY YEAR
    def get_by_year(self, query_params, limit=100):
        self.query.update(query_params)
        self.query['view'] = 'year'
        cric_data = scraper.getTeamData(query, limit)

        return cric_data

    # BY SEASON
    def get_by_season(self, query_params, limit=100):
        self.query.update(query_params)
        self.query['view'] = 'season'
        cric_data = scraper.getTeamData(query, limit)

        return cric_data

    # OVERALL EXTRAS
    def get_overall_extras(self, query_params, limit=100):
        self.query.update(query_params)
        self.query['view'] = 'extras'
        cric_data = scraper.getTeamData(query, limit)

        return cric_data

    # EXTRAS BY INNINGS
    def get_extras_inn(self, query_params, limit=100):
        self.query.update(query_params)
        self.query['view'] = 'extras_innings'
        cric_data = scraper.getTeamData(query, limit)

        return cric_data
