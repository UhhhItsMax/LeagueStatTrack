import requests
import os
from dotenv import load_dotenv
from riot_miscellaneous.summoner_v4 import get_encryptedSummonerID

def get_summonerWins_function(summoner_name):

    encryptedSummonerID = get_encryptedSummonerID.get_encryptedSummonerID_function(summoner_name)

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

    # api_URL for summoner name
    api_URL_LeagueV4 = "https://euw1.api.riotgames.com/lol/league/v4/entries/by-summoner/" + encryptedSummonerID

    api_URL_LeagueV4 = api_URL_LeagueV4 + "?api_key=" + API_KEY
    resp = requests.get(api_URL_LeagueV4)

    rankSolo = " "
    rankFlex = " "

    if resp.status_code == 200:
        player_info = resp.json()
        if player_info:
            #wheter solo or flex queue is the first parameter, assign variables
            if(player_info[0]['queueType'] == 'RANKED_SOLO_5x5'):
                winsSolo = player_info[0]['wins']
                winsFlex = player_info[1]['wins']
            elif player_info[0]['queueType'] == 'RANKED_FLEX_SR':
                winsSolo = player_info[1]['wins']
                winsFlex = player_info[0]['wins']
            else:
                winsSolo = "no wins"
                winsFlex = "no wins"

    else:
        #API request failed
        winsSolo = "API request failed"
        winsFlex = "API request failed"

    return winsSolo, winsFlex
