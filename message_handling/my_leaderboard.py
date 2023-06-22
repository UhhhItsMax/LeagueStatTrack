from database import db_getallinformation
import discord

async def my_leaderboard_function(bot):
    allid, username, summoner_name, tier_rank = await db_getallinformation.db_getallinformation_function(bot)

    # Create a dictionary containing all the useful information
    users = [
        {"id": allid[i], "username": username[i], "summoner_name": summoner_name[i],
         "soloqueue_tier": tier_rank[i][0][0], "soloqueue_rank": tier_rank[i][1][0]}
        for i in range(len(allid))
    ]

    # Create a mapping from tier names to a numerical value representing their order
    tier_order = {"unranked": 8, "bronze": 7, "silver": 6, "gold": 5, "platinum": 4, "diamond": 3, "master": 2, "grandmaster": 1, "challenger": 0}
    rank_order = {" ":6, "V": 5, "IV": 4, "III": 3, "II": 2, "I": 1}

    # Sort the users by their soloqueue tier and rank, using the tier_order and rank_order mappings to compare tiers and ranks
    sorted_users = sorted(users, key=lambda user: (tier_order[user["soloqueue_tier"].lower()], rank_order[user["soloqueue_rank"]]))

    # Create the string from the sorted list
    output_string = ""
    for user in sorted_users:
        output_string += f'User: {user["username"]}, Summoner: {user["summoner_name"]}, SoloQ Tier: {user["soloqueue_tier"]} {user["soloqueue_rank"]}\n'

    # Create an empty leaderboard embed
    leaderboard_embed = discord.Embed(title="Leaderboard", color=discord.Color.blue())
    leaderboard_embed.set_thumbnail(url="https://preview.redd.it/0hkysettdy581.jpg?width=840&format=pjpg&auto=webp&s=4f19fd04bff830be7d6f126a55255af43610e193")
    leaderboard_embed.set_image(url="https://static.wikia.nocookie.net/leagueoflegends/images/b/bb/Garen_OriginalCentered.jpg/revision/latest/scale-to-width-down/1200?cb=20180414202112")

    # Iterate over all the sorted users
    for i, user in enumerate(sorted_users, start=1):
        # Determine the formatting for the field value based on position
        if i <= 3:
            value = f"**User: {user['username']}**\n**Summoner: {user['summoner_name']}**\n**Tier: {user['soloqueue_tier']} {user['soloqueue_rank']}**"
        else:
            value = f"User: {user['username']}\nSummoner: {user['summoner_name']}\nTier: {user['soloqueue_tier']} {user['soloqueue_rank']}"

        # Add a field for each user to the embed
        leaderboard_embed.add_field(name=f"#{i}", value=value, inline=False)

    # Send the embed in the channel
    return leaderboard_embed
    #await ctx.send(embed=leaderboard_embed)

    #await ctx.send(output_string)
