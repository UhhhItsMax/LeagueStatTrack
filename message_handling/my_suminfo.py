#Die Funktion für den Command !help logik steht hier drinne
from riot_miscellaneous import *
from useful_functions import after_first_space
async def my_suminfo_function(ctx, message):
    messageContent = after_first_space.after_first_space_function(message.content)
    print(messageContent)
    summonerName = get_summonerName.get_summonerName_function(messageContent)
    summonerLevel = get_summonerLevel.get_summonerLevel_function(messageContent)
    encryptedID = get_encryptedID.get_encryptedID_function(messageContent)
    #summonerTier = get_summonerTier.get_summonerTier_function(encryptedAccountID)
    rankSolo, rankFlex = get_summonerRank.get_summonerRank_function(encryptedID)
    output = "Summoner: " + summonerName + " is level " + str(summonerLevel) + " Rank: " + rankSolo
    await ctx.send(output)
