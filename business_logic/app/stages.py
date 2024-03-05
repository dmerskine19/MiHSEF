# business_logic/App/stages.py

from endpoints import leagueos
import requests


def get_stages(season_id, api_key):
    return leagueos.get_stages(season_id, api_key)


def get_activeStages(api_key):
    try:
        active_seasons = leagueos.get_active_seasons(api_key)
        season_ids = [season['id'] for season in active_seasons['data'] if season['status'] == 'inProgress']
        stage_ids = get_stages(season_ids, api_key)

    except Exception as e:
        print(f"Error: {e}")
        return None