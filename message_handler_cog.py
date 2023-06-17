# message_handler_cog.py
import discord
from discord.ext import commands
from message_handling import *

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


    #!summonername <anySummonerName> returns the summonerName of the player
    @commands.command()
    async def summonername(self, ctx):  #wird ausgeführt, wenn !summonername im chat geschrieben wird
        #ruft die Funktion aus my_summonername auf
        await my_summonername.my_summonername_function(ctx, ctx.message)

    #!suminfo <anySummonerName> return the summonerName and the level of the player
    @commands.command()
    async def suminfo(self, ctx):  #wird ausgeführt, wenn suminfo im chat geschrieben wird
        #ruft die Funktion aus my_suminfo auf
        await my_suminfo.my_suminfo_function(ctx, ctx.message)

    #!sumgames <anySummonerName> return the last five games played by the player
    @commands.command()
    async def sumgames(self, ctx):  
        await my_sumgames.my_sumgames_function(ctx, ctx.message)
