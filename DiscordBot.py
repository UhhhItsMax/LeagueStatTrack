import os
from dotenv import load_dotenv
import discord
from discord.ext import commands

class MyDiscordBot(discord.Client):
    async def on_ready(self):
        print("Bot Ist An")

    async def on_message(self, message):
        print("Nachricht ist angekommen")

# Lade die Umgebungsvariablen aus der .env-Datei
load_dotenv()

# Hole den Token aus den Umgebungsvariablen
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
discordBot = MyDiscordBot(intents=intents)
discordBot.run(TOKEN)
