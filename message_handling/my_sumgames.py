#Die Funktion für den Command !help logik steht hier drinne
from riot_miscellaneous.match_v5 import *
from riot_miscellaneous.summoner_v4 import *
from useful_functions import after_first_space
async def my_sumgames_function(ctx, message):
    messageContent = after_first_space.after_first_space_function(message.content)
    print(messageContent)
    summonerGames = get_summonerGames.get_summonerGames_function(messageContent)
    #summonerName = get_summonerName.get_summonerName_function(messageContent)
    
    stringGames = "Games: " + summonerGames + "\n"
    #stringName = "Name: " + summonerName + " \n"
    
    output = stringGames
    await ctx.send(output)