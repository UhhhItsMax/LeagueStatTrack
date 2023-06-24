from riot_miscellaneous.league_v4 import get_summonerWins, get_summonerLosses

def get_summonerWinrate_function(summoner_name):
    winsSoloq, winsFlexQ = get_summonerWins.get_summonerWins_function(summoner_name)
    lossesSoloq, lossesFlexq = get_summonerLosses.get_summonerLosses_function(summoner_name)

    winsSoloq, winsFlexQ = int(winsSoloq), int(winsFlexQ)
    lossesSoloq, lossesFlexq = int(lossesSoloq), int(lossesFlexq)

    winRateSoloq = int((round(winsSoloq / (winsSoloq + lossesSoloq), 2) * 100))
    winRateFlexq = int((round(winsFlexQ / (winsFlexQ + lossesFlexq), 2) * 100))


    return winRateSoloq, winRateFlexq

