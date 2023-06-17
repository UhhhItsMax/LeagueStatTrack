import requests
import os
from dotenv import load_dotenv
from riot_miscellaneous.summoner_v4 import *
from riot_miscellaneous.match_v5 import get_summonerGames
from riot_miscellaneous.league_utility import *

def get_gameInfo_function(summoner_name, historyCount):

    #matchIdArr is an array that stores the mathId, and the last index holds the wanted matchId
    matchIdArr = get_summonerGames.get_summonerGames_function(summoner_name, historyCount)
    matchid = matchIdArr[historyCount-1]

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
    game_info = []
    if resp.status_code == 200:
        game_data = resp.json()
        if game_data:
            # Gets how many players were participating
            num_participants = get_num_participants.get_num_participants_function(game_data)
            #appends each player into the game_info array
            for i in range(num_participants):
                champion_name = game_data['info']['participants'][i]['championName']
                summoner_name = game_data['info']['participants'][i]['summonerName']
                gameSubInfo = champion_name + ' ' + summoner_name
                game_info.append(gameSubInfo)
    else:
        #API request failed
        game_info.append("API request failed")
    


    return game_info, num_participants