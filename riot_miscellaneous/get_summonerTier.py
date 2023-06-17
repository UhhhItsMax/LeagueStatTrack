import requests
import os
from dotenv import load_dotenv

def get_summonerTier_function(encryptedAccountID):
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
    api_URL_LeagueV4 = "https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/" + encryptedAccountID

    api_URL_LeagueV4 = api_URL_LeagueV4 + "?api_key=" + API_KEY
    resp = requests.get(api_URL_LeagueV4)
    if resp.status_code == 200:
        player_info = resp.json()
        # If there is at least one league entry
        if player_info:
            # Get the tier of the first league entry
            player_tier = player_info['tier']
        else:
            # Player is unranked
            player_tier = "Unranked"
    else:
        # API request failed
        player_tier = "API request failed"
    return player_tier
