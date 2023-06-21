# Database.py
import aiosqlite

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class DatabaseClass(metaclass=Singleton):
    _db = None

    async def get_db(self):
        if self._db is None:
            self._db = await aiosqlite.connect("database/main.db")
        return self._db
