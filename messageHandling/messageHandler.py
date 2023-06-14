#Hier Sollen einkommende Nachrichten zugeordnet werden der funktionalität nach
import discord

class messageHandler:
    def __init__(self):

    async def process_message(self, message: discord.Message):
        await message.channel.send("du HS")