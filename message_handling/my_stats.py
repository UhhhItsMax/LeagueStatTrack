import requests
from apikey import api_key

api_URL = "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/CNostix"


api_URL = api_URL + "?api_key=" + api_key
#print(api_URL)
resp = requests.get(api_URL)
#print(resp.json())
player_info = resp.json()
#print(player_info['name'])
player_name = player_info['name']
        
