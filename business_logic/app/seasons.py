# business_logic/App/seasons.py

from endpoints import leagueos
from auth import api_key
import requests

def get_active_seasons(api_key):
    return leagueos.get_active_seasons(api_key)

def get_season_info(season_id, api_key):
    return leagueos.get_season_info(season_id, api_key)

def get_active_seasonIds(api_key):
    try:
        active_seasons = leagueos.get_active_seasons(api_key)
        season_ids = [season['id'] for season in active_seasons['data'] if season['status'] == 'inProgress']
        return season_ids
    except Exception as e:
        print(f"Error: {e}")
        return None


