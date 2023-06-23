# message_handler_cog.py
import discord
from discord.ext import commands
from message_handling import *
from discord import app_commands

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


    #!suminfo <anySummonerName> return the summonerName and the level of the player
    @app_commands.command()
    async def suminfo(self, interaction: discord.Interaction, summoner_name: str):
        await interaction.response.defer()
        output = await my_suminfo.my_suminfo_function(summoner_name)
        await interaction.followup.send(output)

    @app_commands.command()
    async def addsummoner(self, interaction: discord.Interaction, summoner_name: str):
        id = interaction.user.id
        await interaction.response.defer()
        output = await my_addsummoner.my_addsummoner_function(id, summoner_name)
        await interaction.followup.send(output)

    @app_commands.command()
    async def mysummoner(self, interaction: discord.Interaction):
        id = interaction.user.id
        await interaction.response.defer()
        summoner_name = await my_mysummoner.my_mysummoner_function(id)
        await interaction.followup.send(summoner_name)

    @app_commands.command()
    async def gameinfo(self, interaction: discord.Interaction, summoner_name: str, game: int = None):
        if game == None:
            game = 1
        await interaction.response.defer()
        gameinfo = await my_gameinfo.my_gameinfo_function(summoner_name, game)
        await interaction.followup.send(gameinfo)

    @app_commands.command()
    async def leaderboard(self, interaction: discord.Interaction):
        await interaction.response.defer()
        embed = await my_leaderboard.my_leaderboard_function(self.bot)
        await interaction.followup.send(embed=embed)