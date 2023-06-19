async def db_startup(db):
    async with db.cursor() as cursor:
        await cursor.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER)')
        await cursor.execute('CREATE TABLE IF NOT EXISTS summoner (id INTEGER, summonername VARCHAR)')
    await db.commit()