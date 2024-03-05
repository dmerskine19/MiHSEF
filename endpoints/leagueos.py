# endpoints/leagueos

import requests

def get_active_seasons(api_key):
    headers = {
        'Accept': 'application/json',
        'x-leagueos-api-key': api_key
    }
    response = requests.get('https://api.leagueos.gg/seasons/active', headers=headers)
    return response.json()

def get_season_info(season_id, api_key):
    headers = {
        'Accept': 'application/json',
        'x-leagueos-api-key': api_key
    }
    response = requests.get(f'https://api.leagueos.gg/seasons/{season_id}', headers=headers)
    return response.json()

def get_stages(season_id, api_key):
    headers = {
        'Accept': 'application/json',
        'x-leagueos-api-key': api_key
    }
    response = requests.get(f'https://api.leagueos.gg/seasons/{season_id}/stages/', headers=headers)
    return response.json()

def get_matches(stage_id, api_key):
    headers = {
        'Accept': 'application/json',
        'x-leagueos-api-key': api_key
    }
    response = requests.get(f'https://api.leagueos.gg/stages/{stage_id}/matches/', headers=headers)
    return response.json()

def get_teams(match_id, api_key):
    headers = {
        'Accept': 'application/json',
        'x-leagueos-api-key': api_key
    }
    response = requests.get(f'https://api.leagueos.gg/matches/{match_id}/teams/', headers=headers)
    return response.json()
