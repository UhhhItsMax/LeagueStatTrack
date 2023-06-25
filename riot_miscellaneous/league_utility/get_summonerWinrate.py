from riot_miscellaneous.league_v4 import get_summonerWins, get_summonerLosses

def get_summonerWinrate_function(summoner_name):
    winsSoloq, winsFlexq = get_summonerWins.get_summonerWins_function(summoner_name)
    lossesSoloq, lossesFlexq = get_summonerLosses.get_summonerLosses_function(summoner_name)

    winRateSoloq = "Information not available"
    winRateFlexq = "Information not available"

    if winsSoloq != "" and lossesSoloq != "":
        winsSoloq = int(winsSoloq)
        lossesSoloq = int(lossesSoloq)
        winRateSoloq = int((round(winsSoloq / (winsSoloq + lossesSoloq), 2) * 100))

    if winsFlexq != "" and lossesFlexq != "":
        winsFlexq = int(winsFlexq)
        lossesFlexq = int(lossesFlexq)
        winRateFlexq = int((round(winsFlexq / (winsFlexq + lossesFlexq), 2) * 100))

    return winRateSoloq, winRateFlexq

get_summonerWinrate_function("nesan0103")