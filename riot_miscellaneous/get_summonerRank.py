import requests
import os
from dotenv import load_dotenv

def get_summonerRank_function(encryptedID):

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
    api_URL_LeagueV4 = "https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/" + encryptedID

    api_URL_LeagueV4 = api_URL_LeagueV4 + "?api_key=" + API_KEY
    resp = requests.get(api_URL_LeagueV4)
    if resp.status_code == 200:
        player_info = resp.json()
        if player_info:
            if(player_info[0]['queueType'] == 'RANKED_SOLO_5x5'):
                rankSolo = player_info[0]['rank']
                rankFlex = player_info[1]['rank']
            elif player_info[0]['queueType'] == 'RANKED_FLEX_SR':
                rankSolo = player_info[1]['rank']
                rankFlex = player_info[0]['rank']
            else:
                rankSolo = None
                rankFlex = None

    else:
        #API request failed
        rankSolo = "API request failed"
        rankFlex = "API request failed"

    return rankSolo, rankFlex