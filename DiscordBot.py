# DiscordBot.py
import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
from message_handler_cog import MessageHandlerCog
from database.Database import DatabaseClass
from database import db_startup

class MyDiscordBot(commands.Bot):
    async def on_ready(self):
        print("Bot ist an")
        self.remove_command('help')  # Entferne den eingebauten Hilfebefehl
        await self.add_cog(MessageHandlerCog(self))  # Füge den Cog zum Bot hinzu
        db_instance = DatabaseClass()   # Create an instance of DatabaseClass
        db = await db_instance.get_db() # Call get_db on the instance
        await db_startup.db_startup_function(db)

# Lade die Umgebungsvariablen aus der .env-Datei
load_dotenv()

# Hole den Token aus den Umgebungsvariablen
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
discordBot = MyDiscordBot(command_prefix='!', intents=intents)
discordBot.run(TOKEN)
