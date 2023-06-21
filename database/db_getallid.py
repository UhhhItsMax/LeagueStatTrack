import aiosqlite
from database.Database import DatabaseClass  # import the DatabaseClass


async def db_getallid_function():
    db_instance = DatabaseClass()  # Create an instance of DatabaseClass
    db = await db_instance.get_db()  # Call get_db on the instance
    async with db.execute("SELECT id FROM users") as cursor:
        results = await cursor.fetchall()

    # Extract the IDs from the tuples
    user_ids = [result[0] for result in results]

    return user_ids
