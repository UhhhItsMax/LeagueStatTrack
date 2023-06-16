# message_handler_cog.py
import os
from discord.ext import commands
from . import my_help
from . import my_cnostix
class MessageHandlerCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    #@commands.Cog.listener()
    #async def on_message(self, message):
    #    if message.author == self.bot.user:
    #        return
    #    await message.channel.send("angekommen")

    @commands.command()
    async def help(self, ctx):  #wird ausgeführt, wenn !help im chat geschrieben wird
        #ruft die Funktion aus my_help.py auf
        await my_help.my_help_function(ctx)

    @commands.command()
    async def CNostix(self, ctx):  #wird ausgeführt, wenn !CNostix im chat geschrieben wird
        #ruft die Funktion aus my_name.py auf
        print("command aufgerufen")
        await my_cnostix.my_cnostix_function(ctx)
