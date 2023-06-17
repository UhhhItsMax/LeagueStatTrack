import requests
import os
from dotenv import load_dotenv
from riot_miscellaneous.summoner_v4 import *

def get_summonerGames_function(summoner_name):
    
    puuid = get_puuid.get_puuid_function(summoner_name)

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
    api_URL_MatchV5 = "https://europe.api.riotgames.com/lol/match/v5/matches/by-puuid/" + puuid + "/ids?start=0&count=20"

    api_URL_MatchV5 = api_URL_MatchV5 + "&api_key=" + API_KEY
    resp = requests.get(api_URL_MatchV5)

    if resp.status_code == 200:
        player_matches = resp.json()
        if player_matches:
            player_games = player_matches[0]# + ", " +player_matches[1] + ", " + player_matches[2] + ", " + player_matches[3] + ", " + player_matches[4]
    else:
        #API request failed
        player_games = "API request failed"

    return player_games