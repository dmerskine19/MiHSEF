# business_logic/App/matches.py

from endpoints import leagueos
from auth import api_key
from business_logic.app import stages


def get_matches(stage_id, api_key):
    try:
        return leagueos.get_matches(season_id, stage_id, api_key)
    except Exception as e:
        print("An error occurred while fetching matches:", e)
        return None

def get_active_matches(season_id, api_key):
    active_matches = []
    stages = fetch_stage_info(season_id, api_key)
    if stages:
        for stage in stages:
            if stage['status'] == 'inProgress':
                matches = fetch_matches(season_id, stage['id'], api_key)
                if matches:
                    active_matches.extend(matches)
    return active_matches
