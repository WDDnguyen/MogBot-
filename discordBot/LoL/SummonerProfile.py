class SummonerProfile():
    summonerInformation = None
    summonerRankedStatisticOfAllSeasons = None

    def __init__(self,summonerInformation,summonerRankedStatisticOfAllSeasons):
        self.summonerInformation = summonerInformation
        self.summonerRankedStatisticOfAllSeasons = summonerRankedStatisticOfAllSeasons

    def displayAllRankedStatistic(self):
        return self.summonerRankedStatisticOfAllSeasons

    def displayMostPlayedRankedChampionOfCurrentSeason(self):
        MostPlayedRankedChampionsList = []
        mostPlayedCurrentRankedChampion = None
        secondMostPlayedCurrentRankedChampion = None
        thirdMostPlayedCurrentRankedChampion = None

        currentSeasonRankedStatistic = self.summonerRankedStatisticOfAllSeasons[-1]

        for champion in currentSeasonRankedStatistic['champions']:
            if mostPlayedCurrentRankedChampion is None:
                mostPlayedCurrentRankedChampion = champion

            elif mostPlayedCurrentRankedChampion['stats']['totalSessionsPlayed'] <= champion['stats']['totalSessionsPlayed']:
                if champion['id'] != 0:
                    thirdMostPlayedCurrentRankedChampion = secondMostPlayedCurrentRankedChampion
                    secondMostPlayedCurrentRankedChampion = mostPlayedCurrentRankedChampion
                    mostPlayedCurrentRankedChampion = champion
            elif secondMostPlayedCurrentRankedChampion is None:
                secondMostPlayedCurrentRankedChampion = champion

            elif secondMostPlayedCurrentRankedChampion['stats']['totalSessionsPlayed'] <= champion['stats']['totalSessionsPlayed']:
                if champion['id'] != 0:
                    thirdMostPlayedCurrentRankedChampion = secondMostPlayedCurrentRankedChampion
                    secondMostPlayedCurrentRankedChampion = champion

            elif thirdMostPlayedCurrentRankedChampion is None:
                thirdMostPlayedCurrentRankedChampion = champion

            elif thirdMostPlayedCurrentRankedChampion['stats']['totalSessionsPlayed'] <= champion['stats']['totalSessionsPlayed']:
                if champion['id'] !=0:
                    thirdMostPlayedCurrentRankedChampion = champion

        MostPlayedRankedChampionsList.append(mostPlayedCurrentRankedChampion['id'])
        MostPlayedRankedChampionsList.append(secondMostPlayedCurrentRankedChampion['id'])
        MostPlayedRankedChampionsList.append(thirdMostPlayedCurrentRankedChampion['id'])
        return MostPlayedRankedChampionsList




