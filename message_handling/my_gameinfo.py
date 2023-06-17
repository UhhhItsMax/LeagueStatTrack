#Die Funktion für den Command !help logik steht hier drinne
from idlelib.configdialog import is_int

from riot_miscellaneous.match_v5 import *
from useful_functions import after_last_space
from useful_functions import after_first_space


async def my_gameinfo_function(ctx, message):
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
    gameInfo, num_participants = get_gameInfo.get_gameInfo_function(summoner_name, historyCount)

    stringInfo = "Champion Name & Summoner Name: \n"

    for i in range(num_participants):
        stringInfo += gameInfo[i] + "\n"

    output = stringInfo
    await ctx.send(output)
