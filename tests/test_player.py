from cricguru import player
import pytest

def test_career_summary():
    query_params = {
        'class': '2',
        'type' : 'allround'
    }
    
    test_player = player.Player('50710')
    test_data = test_player.career_summary(query_params)
    assert not test_data.empty, "Data unavailable or broken"
    
def test_inn_list():
    query_params = {
        'class': '2',
        'type' : 'allround'
    }
    
    test_player = player.Player('50710')
    test_data = test_player.inn_list(query_params)
    assert not test_data.empty, "Data unavailable or broken"
    
def test_match_list():
    query_params = {
        'class': '2',
        'type' : 'allround'
    }
    
    test_player = player.Player('50710')
    test_data = test_player.match_list(query_params)
    assert not test_data.empty, "Data unavailable or broken"
    
def test_cumulative_avg():
    query_params = {
        'class': '2',
        'type' : 'allround'
    }
    
    test_player = player.Player('50710')
    test_data = test_player.cumulative_avg(query_params)
    assert not test_data.empty, "Data unavailable or broken"
    
def test_reverse_cumulative():
    query_params = {
        'class': '2',
        'type' : 'allround'
    }
    
    test_player = player.Player('50710')
    test_data = test_player.reverse_cumulative(query_params)
    assert not test_data.empty, "Data unavailable or broken"
    
def test_series_avg():
    query_params = {
        'class': '2',
        'type' : 'allround'
    }
    
    test_player = player.Player('50710')
    test_data = test_player.series_avg(query_params)
    assert not test_data.empty, "Data unavailable or broken"
    
def test_ground_avg():
    query_params = {
        'class': '2',
        'type' : 'allround'
    }
    
    test_player = player.Player('50710')
    test_data = test_player.ground_avg(query_params)
    assert not test_data.empty, "Data unavailable or broken"
    
def test_match_results():
    query_params = {
        'class': '2',
        'type' : 'allround'
    }
    
    test_player = player.Player('50710')
    test_data = test_player.match_results(query_params)
    assert not test_data.empty, "Data unavailable or broken"
    
def test_match_awards():
    query_params = {
        'class': '2',
        'type' : 'allround'
    }
    
    test_player = player.Player('50710')
    test_data = test_player.match_awards(query_params)
    assert not test_data.empty, "Data unavailable or broken"
    
def test_series_awards():
    query_params = {
        'class': '2',
        'type' : 'allround'
    }
    
    test_player = player.Player('50710')
    test_data = test_player.series_awards(query_params)
    assert not test_data.empty, "Data unavailable or broken"
    
def test_partnership_summary():
    query_params = {
        'class': '2',
        'type' : 'batting',
    }
    
    test_player = player.Player('50710')
    test_data = test_player.partnership_summary(query_params)
    assert not test_data.empty, "Data unavailable or broken"
    
def test_partnership_list():
    query_params = {
        'class': '2',
        'type' : 'batting'
    }
    
    test_player = player.Player('50710')
    test_data = test_player.partnership_list(query_params)
    assert not test_data.empty, "Data unavailable or broken"
    
def test_dismissal_summary():
    query_params = {
        'class': '2',
        'type' : 'batting'
    }
    
    test_player = player.Player('50710')
    test_data = test_player.dismissal_summary(query_params)
    assert not test_data.empty, "Data unavailable or broken"
    
def test_bowler_summary():
    query_params = {
        'class': '2',
        'type' : 'batting'
    }
    
    test_player = player.Player('50710')
    test_data = test_player.bowler_summary(query_params)
    assert not test_data.empty, "Data unavailable or broken"
    
def test_fielder_summary():
    query_params = {
        'class': '2',
        'type' : 'batting'
    }
    
    test_player = player.Player('50710')
    test_data = test_player.fielder_summary(query_params)
    assert not test_data.empty, "Data unavailable or broken"
    
def test_dismissal_list():
    query_params = {
        'class': '2',
        'type' : 'batting'
    }
    
    test_player = player.Player('50710')
    test_data = test_player.dismissal_list(query_params)
    assert not test_data.empty, "Data unavailable or broken"
    
def test_dism_summary():
    query_params = {
        'class': '2',
        'type' : 'bowling'
    }
    
    test_player = player.Player('50710')
    test_data = test_player.dism_summary(query_params)
    if test_data is None:
        assert test_data is None
    else:
        assert not test_data.empty, "Data unavailable or broken"
    
def test_batsman_summary():
    query_params = {
        'class': '2',
        'type' : 'bowling'
    }
    
    test_player = player.Player('50710')
    test_data = test_player.batsman_summary(query_params)
    assert not test_data.empty, "Data unavailable or broken"
    
def test_fielder_summary():
    query_params = {
        'class': '2',
        'type' : 'bowling'
    }
    
    test_player = player.Player('50710')
    test_data = test_player.fielder_summary(query_params)
    assert not test_data.empty, "Data unavailable or broken"
    
def test_wickets_list():
    query_params = {
        'class': '2',
        'type' : 'bowling'
    }
    
    test_player = player.Player('50710')
    test_data = test_player.wickets_list(query_params)
    
    if test_data is None:
        assert test_data is None
    else:
        assert not test_data.empty, "Data unavailable or broken"
    
def test_career_avg():
    query_params = {
        'class': '2',
        'type' : 'allround'
    }
    
    test_player = player.Player('50710')
    test_data = test_player.career_avg(query_params)
    if test_data is None:
        assert test_data is None
    else:
        assert not test_data.empty, "Data unavailable or broken"
    