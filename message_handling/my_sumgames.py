#Die Funktion für den Command !help logik steht hier drinne
from idlelib.configdialog import is_int

from riot_miscellaneous.match_v5 import *
from useful_functions import *
async def my_sumgames_function(ctx, message):
    messageContent, trash = after_first_space.after_first_space_function(message.content)
    summoner_name, historyCount = after_last_space.after_last_space_function(messageContent)
    if not is_int(historyCount):
        summoner_name += " " + historyCount
        historyCount = 1
    if historyCount == '':
        historyCount = 1
    else:
        historyCount = int(historyCount)
    if (historyCount > 10):
        historyCount = 10
    summonerGames = get_matchId.get_matchId_function(summoner_name, historyCount)
    stringGames = ""
    for i in range(historyCount):
        stringGames += "Game: " + str(i+1) + " " + summonerGames[i] + "\n"
    
    output = stringGames
    await ctx.send(output)