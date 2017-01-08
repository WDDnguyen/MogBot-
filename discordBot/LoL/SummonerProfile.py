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

        print ( "Number of ID: " + str(len(currentSeasonRankedStatistic['champions'])))
        for championID in currentSeasonRankedStatistic['champions']:
            print(championID['id'])

        for champion in currentSeasonRankedStatistic['champions']:
            if mostPlayedCurrentRankedChampion == None:
                mostPlayedCurrentRankedChampion = champion
            if secondMostPlayedCurrentRankedChampion == None:
                mostPlayedCurrentRankedChampion = champion
            if thirdMostPlayedCurrentRankedChampion == None:
                thirdMostPlayedCurrentRankedChampion = champion

            elif mostPlayedCurrentRankedChampion['stats']['totalSessionsPlayed'] <= champion['stats']['totalSessionsPlayed']:
                if champion['id'] != 0:
                    thirdMostPlayedCurrentRankedChampion = secondMostPlayedCurrentRankedChampion
                    secondMostPlayedCurrentRankedChampion = mostPlayedCurrentRankedChampion
                    mostPlayedCurrentRankedChampion = champion

        MostPlayedRankedChampionsList.append(mostPlayedCurrentRankedChampion['id'])
        MostPlayedRankedChampionsList.append(secondMostPlayedCurrentRankedChampion['id'])
        MostPlayedRankedChampionsList.append(thirdMostPlayedCurrentRankedChampion['id'])
        return MostPlayedRankedChampionsList




