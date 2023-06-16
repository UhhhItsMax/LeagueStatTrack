import requests
from apikey import api_key

def rank_info(id):
    api_URL = (f"https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/CNostix" + "?api_key=" + api_key)

    rank_info = requests.get(api_URL)
    rank_info = rank_info.json()
    return rank_info
        
