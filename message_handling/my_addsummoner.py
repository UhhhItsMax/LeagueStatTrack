#Die Funktion für den Command !help logik steht hier drinne
from useful_functions import after_first_space
from database import db_addsummoner
from riot_miscellaneous.summoner_v4 import get_summonerName

async def my_addsummoner_function(ctx, message):
    summoner_name, trash = after_first_space.after_first_space_function(message.content)
    summoner_name = get_summonerName.get_summonerName_function(summoner_name)   # Checks if the summoner_name exists
    if summoner_name == 'API request failed':
        output = ("Summoner doesnt Exist")
    else:
        await db_addsummoner.db_addsummoner_function(ctx.author, summoner_name)
        output = ("Bist nun registriert!")

    await ctx.send(output)
