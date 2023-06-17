#Die Funktion für den Command !help logik steht hier drinne
from riot_miscellaneous.summoner_v4 import *
from riot_miscellaneous.league_v4 import *
from useful_functions import after_first_space
async def my_suminfo_function(ctx, message):
    messageContent = after_first_space.after_first_space_function(message.content)
    print(messageContent)
    summonerName = get_summonerName.get_summonerName_function(messageContent)
    summonerLevel = get_summonerLevel.get_summonerLevel_function(messageContent)
    tierSolo, tierFlex = get_summonerTier.get_summonerTier_function(messageContent)
    rankSolo, rankFlex = get_summonerRank.get_summonerRank_function(messageContent)
    puuid = get_puuid.get_puuid_function(messageContent)
    encryptedSummonerID = get_encryptedSummonerID.get_encryptedSummonerID_function(messageContent)
    stringName = "Name: " + summonerName + " \n"
    stringLevel = "Level: " + str(summonerLevel) + " \n"
    stringSolo = "Rank Solo: " + tierSolo + " " + rankSolo + " \n"
    stringFlex = "Rank Flex: " + tierFlex + " " + rankFlex + " \n"
    stringPuuid = "Puuid: " + puuid + " \n"
    stringEncryptedID = "EncryptedID: " + encryptedSummonerID + " \n"
    #output = stringID
    output = stringName + stringLevel + stringSolo + stringFlex + stringPuuid + stringEncryptedID
    await ctx.send(output)
