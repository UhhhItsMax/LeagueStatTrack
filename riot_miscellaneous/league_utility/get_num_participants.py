import requests
import os
from dotenv import load_dotenv
from riot_miscellaneous.summoner_v4 import *
from riot_miscellaneous.match_v5 import get_summonerGames

def get_num_participants_function(game_data):
    if game_data == None:
        return None

    num_participants = len(game_data['info']['participants'])
    return num_participants