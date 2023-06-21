# Die Funktion für den Command !help logik steht hier drinne
from idlelib.configdialog import is_int

from riot_miscellaneous.match_v5 import *
from riot_miscellaneous.summoner_v4 import *
from useful_functions import *


async def my_gameinfo_function(ctx, message):
    messageContent, trash = after_first_space.after_first_space_function(message.content)
    print(messageContent)
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
    matchIdArr = get_matchId.get_matchId_function(summoner_name, historyCount)
    matchId = matchIdArr[historyCount - 1]
    partinum = get_num_participants.get_num_participants_function(matchId)
    partisum = get_participantssum.get_participantssum_function(matchId)
    partichamp = get_participantschamp.get_participantschamp_function(matchId)
    partistats = get_participantsstats.get_participantsstats_function(matchId)

    stringInfo = ""
    for i in range(int(partinum)):
        stringInfo += partisum[i] + " " + partichamp[i] + " " + "Kills: " + str(partistats[i][0]) + " " + "Deaths: " + str(partistats[i][1]) + " " + "Assists: " + str(partistats[i][2]) + "\n"

    output = stringInfo
    await ctx.send(output)