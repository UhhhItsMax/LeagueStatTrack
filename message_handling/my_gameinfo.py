#Die Funktion für den Command !help logik steht hier drinne
from riot_miscellaneous.match_v5 import *
from riot_miscellaneous.summoner_v4 import *
from useful_functions import after_first_space

async def my_gameinfo_function(ctx, message):
    messageContent = after_first_space.after_first_space_function(message.content)
    print(messageContent)
    gameInfo = get_gameInfo.get_gameInfo_function(messageContent)
    #summonerName = get_summonerName.get_summonerName_function(messageContent)
    
    stringInfo = "Champion Name & Summoner Name: " + gameInfo + "\n"
    #stringName = "Name: " + summonerName + " \n"
    
    output = stringInfo
    await ctx.send(output)