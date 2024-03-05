# business_logic/App/matches.py

from endpoints import leagueos

def get_matches(stage_id, api_key):
    return leagueos.get_matches(stage_id, api_key)
