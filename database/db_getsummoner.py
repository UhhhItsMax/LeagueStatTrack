from database.Database import DatabaseClass # import the DatabaseClass

async def db_getsummoner_function(id):
    db_instance = DatabaseClass()  # Create an instance of DatabaseClass
    db = await db_instance.get_db()  # Call get_db on the instance
    async with db.cursor() as cursor:
        # Retrieve the summoner name based on the ID
        await cursor.execute('SELECT summonername FROM summoner WHERE id = ?', (id,))
        result = await cursor.fetchone()
    await db.commit()

    # Return the summoner name if the ID was found, or None otherwise
    return result[0] if result else None
