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