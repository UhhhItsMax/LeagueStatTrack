
async def get_discordusername_function(id, bot):
    user = await bot.fetch_user(id)
    if user is None:
        return "User not Found"
    else:
        return user.name