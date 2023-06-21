from discord_utility import get_discordusername
from database import db_getallid, db_getsummoner
from riot_miscellaneous.league_v4 import *

async def db_getallinformation_function(bot):
    allid = await db_getallid.db_getallid_function()  # Await the coroutine
    username = []
    for i in range(len(allid)):
        username.append(await get_discordusername.get_discordusername_function(allid[i], bot))  # Await the coroutine

    summoner_name = []
    for i in range(len(allid)):
        summoner_name.append(await db_getsummoner.db_getsummoner_function(allid[i]))  # Await the coroutine


    # Initialize a 3D array with N 'layers', each of 2 rows and 2 columns
    tier_rank = [[[0 for col in range(2)] for row in range(2)] for depth in range(len(summoner_name))]
    #tier_rank[i][0][0] contains the soloqueue tier of the player and tier_rank[i][0][1] of the flexqueue, same goes to rank

    for i in range(len(summoner_name)):
        tier_rank[i][0][0], tier_rank[i][0][1] = get_summonerTier.get_summonerTier_function(summoner_name[i])
        tier_rank[i][1][0], tier_rank[i][1][1] = get_summonerRank.get_summonerRank_function(summoner_name[i])

    string = ""
    for i in range(len(summoner_name)):
        string += "User: " + username[i] + " Summoner: " + summoner_name[i] + " SoloQ: " + tier_rank[i][0][0] + tier_rank[i][1][0] + "\n"

    return allid, username, summoner_name, tier_rank
