import requests
import os
from dotenv import load_dotenv
from riot_miscellaneous.summoner_v4 import *
from riot_miscellaneous.match_v5 import get_summonerGames

def get_gameInfo_function(summoner_name):

    matchid = get_summonerGames.get_summonerGames_function(summoner_name)

    # Get the current folder
    current_folder = os.path.dirname(os.path.abspath(__file__))

    # Get the parent folder
    parent_folder = os.path.dirname(current_folder)
    parent_folder = os.path.dirname(parent_folder)

    # Create the path to the .env file
    env_file = os.path.join(parent_folder, '.env')

    # Load the .env file
    load_dotenv(env_file)

    API_KEY = os.getenv('API_KEY')

    # api_URL for puuid
    api_URL_MatchV5 = "https://europe.api.riotgames.com/lol/match/v5/matches/" + matchid

    api_URL_MatchV5 = api_URL_MatchV5 + "?api_key=" + API_KEY
    resp = requests.get(api_URL_MatchV5)

    if resp.status_code == 200:
        game_data = resp.json()
        if game_data:
            game_info = game_data['info']['participants'][1]['championName' + 'summonerName']
    else:
        #API request failed
        player_games = "API request failed"
    


    return game_info