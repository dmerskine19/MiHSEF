# business_logic/App/matches.py

from endpoints import leagueos
from auth import api_key
from business_logic.app import stages, seasons

def get_matches(season_id, stage_id, api_key):
    try:
        return leagueos.get_matches(season_id, stage_id, api_key)
    except Exception as e:
        print("An error occurred while fetching matches:", e)
        return None

def get_activeMatchIds(api_key):
    try:
        match_ids = {}
        for season_id in seasons.get_active_seasonIds(api_key):
            for stage_id in stages.get_active_stageIds(api_key):
                matches = leagueos.get_matches(season_id, stage_id, api_key)
                if matches and 'data' in matches:
                    for match in matches['data']['results']:
                        current_match_id = match['id']
                        print(f"Match ID: {current_match_id}")
                        if stage_id not in match_ids:
                            match_ids[stage_id] = []
                        match_ids[stage_id].append(current_match_id)
                else:
                    print("No valid match data found.")
        return match_ids
    except Exception as e:
        print(f"Error: {e}")
        return None

