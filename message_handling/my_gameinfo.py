# Die Funktion für den Command !help logik steht hier drinne
from idlelib.configdialog import is_int

from riot_miscellaneous.match_v5 import *
from useful_functions import *


async def my_gameinfo_function(summoner_name, game):

    if (game > 10):
        game = 10
    matchIdArr = get_matchId.get_matchId_function(summoner_name, game)
    matchId = matchIdArr[game - 1]
    partinum = get_num_participants.get_num_participants_function(matchId)
    partisum = get_participantssum.get_participantssum_function(matchId)
    partichamp = get_participantschamp.get_participantschamp_function(matchId)
    partistats = get_participantsstats.get_participantsstats_function(matchId)

    stringInfo = ""
    for i in range(int(partinum)):
        stringInfo += partisum[i] + " " + partichamp[i] + " " + "Kills: " + str(partistats[i][0]) + " " + "Deaths: " + str(partistats[i][1]) + " " + "Assists: " + str(partistats[i][2]) + "\n"

    output = stringInfo
    return output
    #await ctx.send(output)