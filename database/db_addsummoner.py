from database.Database import DatabaseClass # import the DatabaseClass

async def db_addsummoner_function(author, summoner_name):
    db_instance = DatabaseClass()  # Create an instance of DatabaseClass
    db = await db_instance.get_db()  # Call get_db on the instance
    id = author.id
    async with db.cursor() as cursor:
        # Check if the user exists in the users table
        await cursor.execute('SELECT * FROM users WHERE id = ?', (id,))
        user = await cursor.fetchone()

        # If the user does not exist, insert it into the users table
        if not user:
            await cursor.execute('INSERT INTO users VALUES (?, ?)', (id, author.name))

        # Insert or update the summoner_name in the summoner table
        await cursor.execute('INSERT OR REPLACE INTO summoner (id, summonername) VALUES (?, ?)', (id, summoner_name))

    await db.commit()
