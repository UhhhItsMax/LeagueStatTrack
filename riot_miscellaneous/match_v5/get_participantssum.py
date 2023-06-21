import requests
import os
from dotenv import load_dotenv
from riot_miscellaneous.match_v5 import get_num_participants


def get_participantssum_function(matchId):

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
    api_URL_MatchV5 = "https://europe.api.riotgames.com/lol/match/v5/matches/" + matchId

    api_URL_MatchV5 = api_URL_MatchV5 + "?api_key=" + API_KEY
    resp = requests.get(api_URL_MatchV5)
    parti_sum = []
    if resp.status_code == 200:
        game_data = resp.json()
        if game_data:
            # Gets how many players were participating
            num_participants = get_num_participants.get_num_participants_function(matchId)
            # appends each player into the game_info array
            for i in range(num_participants):
                summoner_name = game_data['info']['participants'][i]['summonerName']
                partiInfo = summoner_name
                parti_sum.append(partiInfo)
    else:
        # API request failed
        parti_sum.append("API request failed")

    return parti_sum