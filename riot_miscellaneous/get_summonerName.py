import requests
import os
from dotenv import load_dotenv

def get_summonerName_function(summoner_name):
    # Get the current folder
    current_folder = os.path.dirname(os.path.abspath(__file__))

    # Get the parent folder
    parent_folder = os.path.dirname(current_folder)

    # Create the path to the .env file
    env_file = os.path.join(parent_folder, '.env')

    # Load the .env file
    load_dotenv(env_file)

    API_KEY = os.getenv('API_KEY')

    # api_URL for summoner name
    api_URL_Summoner = "https://euw1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + summoner_name

    api_URL_Summoner = api_URL_Summoner + "?api_key=" + API_KEY
    resp = requests.get(api_URL_Summoner)

    if resp.status_code == 200:
        player_info = resp.json()
        if player_info:
            player_name = player_info['name']
    else:
        #API request failed
        player_name = "API request failed"

    return player_name
