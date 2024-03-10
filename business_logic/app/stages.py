# business_logic/App/stages.py

from business_logic.app import seasons
from endpoints import leagueos
from auth import api_key
import requests


def get_stages(season_id, api_key):
    return leagueos.get_stages(season_id, api_key)

def get_activeStageIds(api_key):
    try:
        season_ids = seasons.get_active_seasonIds(api_key)
        stage_ids = []
        for season_id in season_ids:
            stages = get_stages(season_id, api_key)
            stage_ids.extend(stage['id'] for stage in stages['data'])  # Extract stage IDs

        return stage_ids
 
    except Exception as e:
        print(f"Error: {e}")
        return None


