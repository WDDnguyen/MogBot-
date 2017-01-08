class SummonerProfile():
    summonerInformation = None
    summonerRankedStatisticOfAllSeasons = None

    def __init__(self,summonerInformation,summonerRankedStatisticOfAllSeasons):
        self.summonerInformation = summonerInformation
        self.summonerRankedStatisticOfAllSeasons = summonerRankedStatisticOfAllSeasons

    def displayAllRankedStatistic(self):
        return self.summonerRankedStatisticOfAllSeasons

