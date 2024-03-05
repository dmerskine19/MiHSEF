# business_logic/App/teams.py

from endpoints import leagueos

def get_teams(match_id, api_key):
    return leagueos.get_teams(match_id, api_key)
