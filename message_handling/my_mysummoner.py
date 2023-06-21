#Die Funktion für den Command !help logik steht hier drinne
from database import db_getsummoner

async def my_myummoner_function(ctx):
    id = ctx.author.id
    summoner_name = await db_getsummoner.db_getsummoner_function(id)
    output = summoner_name
    await ctx.send(output)
