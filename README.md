# LeagueStatTrack
Discord Bot that will update the Server about your League of Legends achievements


Aufbau des Projekts:

Main Source File:
    DiscordBot.py

Prefix: '!'

Message Verarbeitung:
    MessageHandlerCog

MessageHandlerCog Konvention:
    decorator ob command oder listener
        command: async def <commandname>(argumente):
                    await my_<commandname>.my_<commandname>_function

    Pro command eine datei in message_handling erstellen: my_<commandname>
        In der Datei eine Funktion erstellen: my_<commandname>_function(argumente)



FUNKTIONEN:


LEAGUE UTILITY:

    get_num_participants_function(game_data)
        INPUT: game_data from resp.json
        OUTPUT: numbers of participants in the game


LEAGUE V4:

    get_summonerRank_function(summoner_name)
        INPUT: summoner_name (String)
        OUTPUT: rankSolo (String), rankFlex (String)

    get_summonerTier_function(summoner_name)
    INPUT: summoner_name (String)
    OUTPUT: tierSolo (String), tierFlex (String)


MATCH V5

    get_gameInfo_function(summoner_name, historyCount)
        INPUT: summoner_name (String), historyCount (Int)
        OUTPUT: game_info[] (String), num_participants
        Explanation: game_info[] contains in each index of the array a String, that looks like this: <ChampionName> <SummonerName>
                    historyCount is the Game, counting backwards from the most recently played

    get_summonerGames_function(summoner_name, historyCount)
        INPUT: summoner_name (String), historyCount (Int)
        OUTPUT: player_games[] (String) 
        Explanation: contains in each index of the array a string, each one of them is a matchId


SUMMONER V4:

    get_encryptedSummonerID_function(summoner_name)
        INPUT: summoner_name (String)
        OUTPUT: encryptedSummonerID (String)

    get_puuid_function(summoner_name)
        INPUT: summoner_name (String)
        OUTPUT: puuid (String)

    get_summonerLevel_function(summoner_name)
        INPUT: summoner_name (String)
        OUTPUT: summoner_level (Int)

    get_summonerName_function(summoner_name)
        INPUT: summoner_name (String)
        OUTPUT: player_name (String)
        Explanation: If the returned player_name is "API request failed", that means the summoner doesnt exist


USEFUL FUNCTIONS:

    after_first_space_function(s)
        INPUT: s (String)
        OUTPUT: secondPart (String), firstPart (String)
        Explanation: Splits the input String right after the first space into 2 parts

    after_last_space_function(s)
        INPUT: s (String)
        OUTPUT: first_part (String), second_part (String)
        Explanation: Splits the input String into 2 seperate parts. first_part is everything before the last space, and second_part is everything after the last space