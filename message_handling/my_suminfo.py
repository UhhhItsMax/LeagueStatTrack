#Die Funktion für den Command !help logik steht hier drinne
from riot_miscellaneous.summoner_v4 import *
from riot_miscellaneous.league_v4 import *
from riot_miscellaneous.league_utility import get_summonerWinrate
from useful_functions import after_first_space
async def my_suminfo_function(summoner_name):
    summonerName = get_summonerName.get_summonerName_function(summoner_name)
    if summonerName == "API request failed":
        return f"{summoner_name} Gibts nicht"
    summonerLevel = get_summonerLevel.get_summonerLevel_function(summonerName)
    tierSolo, tierFlex = get_summonerTier.get_summonerTier_function(summonerName)
    rankSolo, rankFlex = get_summonerRank.get_summonerRank_function(summonerName)
    puuid = get_puuid.get_puuid_function(summonerName)
    encryptedSummonerID = get_encryptedSummonerID.get_encryptedSummonerID_function(summonerName)
    winrateSoloq, winrateFlexq = get_summonerWinrate.get_summonerWinrate_function(summonerName)
    stringName = "Name: " + summonerName + " \n"
    stringLevel = "Level: " + str(summonerLevel) + " \n"
    stringSolo = "Rank Solo: " + tierSolo + " " + rankSolo + " \n"
    stringFlex = "Rank Flex: " + tierFlex + " " + rankFlex + " \n"
    stringPuuid = "Puuid: " + puuid + " \n"
    stringEncryptedID = "EncryptedID: " + encryptedSummonerID + " \n"
    stringWinrate = "SoloQ Winrate: " + str(winrateSoloq) + "%\n" + "FlexQ Winrate: " + str(winrateFlexq) + "%" + " \n"
    output = stringName + stringLevel + stringSolo + stringFlex + stringPuuid + stringEncryptedID + stringWinrate
    return output
