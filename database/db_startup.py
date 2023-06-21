async def db_startup_function(db):
    async with db.cursor() as cursor:
        await cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username VARCHAR)')
        await cursor.execute('CREATE TABLE IF NOT EXISTS summoner (id INTEGER PRIMARY KEY, summonername VARCHAR)')
    await db.commit()