#Die Funktion für den Command !help logik steht hier drinne
from database import db_getsummoner

async def my_mysummoner_function(id):
    summoner_name = await db_getsummoner.db_getsummoner_function(id)
    return summoner_name
