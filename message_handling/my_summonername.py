#Die Funktion für den Command !help logik steht hier drinne
from riot_miscellaneous import get_summonerName
from useful_functions import after_first_space
async def my_summonername_function(ctx, message):
    messageContent = after_first_space.after_first_space_function(message.content)
    print(messageContent)
    await ctx.send(get_summonerName.get_summonerName_function(messageContent))