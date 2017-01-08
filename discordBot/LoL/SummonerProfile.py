class SummonerProfile():
    summonerInformation = None
    summonerRankedStatisticOfAllSeasons = None

    def __init__(self,summonerInformation,summonerRankedStatisticOfAllSeasons):
        self.summonerInformation = summonerInformation
        self.summonerRankedStatisticOfAllSeasons = summonerRankedStatisticOfAllSeasons

    def displayAllRankedStatistic(self):
        return self.summonerRankedStatisticOfAllSeasons

    def acquireMostPlayedRankedChampionsOfCurrentSeason(self):
        mostPlayedRankedChampionsList = []
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

        mostPlayedRankedChampionsList.append(mostPlayedCurrentRankedChampion)
        mostPlayedRankedChampionsList.append(secondMostPlayedCurrentRankedChampion)
        mostPlayedRankedChampionsList.append(thirdMostPlayedCurrentRankedChampion)
        return mostPlayedRankedChampionsList

    def acquireBestCurrentChampionsOfSeason(self):
        bestPlayedRankedChampionsList = []
        bestPlayedCurrentRankedChampion = None
        secondBestPlayedCurrentRankedChampion = None
        thirdBestPlayedCurrentRankedChampion = None

        currentSeasonRankedStatistic = self.summonerRankedStatisticOfAllSeasons[-1]

        for champion in currentSeasonRankedStatistic['champions']:
            championKDA = self.averageKDAOfChampion(champion['stats'])
            championScore = self.calculateScoreOfChampionByKDA(championKDA)
           # print("champion" + str(champion['id']) + " KDA : " + str(championKDA) + " SCORE : " + str(championScore) )

            if bestPlayedCurrentRankedChampion is None:
                bestPlayedCurrentRankedChampion = champion

            elif self.calculateScoreOfChampionByKDA(self.averageKDAOfChampion(bestPlayedCurrentRankedChampion['stats'])) <= championScore:
                if champion['id'] != 0:
                    thirdBestPlayedCurrentRankedChampion = secondBestPlayedCurrentRankedChampion
                    secondBestPlayedCurrentRankedChampion = bestPlayedCurrentRankedChampion
                    bestPlayedCurrentRankedChampion = champion
            elif secondBestPlayedCurrentRankedChampion is None:
                secondBestPlayedCurrentRankedChampion = champion

            elif self.calculateScoreOfChampionByKDA(self.averageKDAOfChampion(secondBestPlayedCurrentRankedChampion['stats'])) <= championScore:
                if champion['id'] != 0:
                    thirdBestPlayedCurrentRankedChampion = secondBestPlayedCurrentRankedChampion
                    secondBestPlayedCurrentRankedChampion = champion

            elif thirdBestPlayedCurrentRankedChampion is None:
                thirdBestPlayedCurrentRankedChampion = champion

            elif self.calculateScoreOfChampionByKDA(self.averageKDAOfChampion(thirdBestPlayedCurrentRankedChampion['stats'])) <= championScore:
                if champion['id'] != 0:
                    thirdBestPlayedCurrentRankedChampion = champion

        bestPlayedRankedChampionsList.append(bestPlayedCurrentRankedChampion)
        bestPlayedRankedChampionsList.append(secondBestPlayedCurrentRankedChampion)
        bestPlayedRankedChampionsList.append(thirdBestPlayedCurrentRankedChampion)
        return bestPlayedRankedChampionsList

    def winRateOfChampion(self,playerChampionStats):
        winRate = playerChampionStats['totalSessionsWon']/playerChampionStats['totalSessionsPlayed']
        return winRate

    def averageKDAOfChampion(self,playerChampionStats):
        KDA = []
        kills = playerChampionStats['totalChampionKills']/playerChampionStats['totalSessionsPlayed']
        deaths = playerChampionStats['totalDeathsPerSession']/playerChampionStats['totalSessionsPlayed']
        assists = playerChampionStats['totalAssists']/playerChampionStats['totalSessionsPlayed']
        KDA.append(kills)
        KDA.append(deaths)
        KDA.append(assists)

        return KDA

    def averageCreepScoreOfChampion(self,playerChampionStats):
        averageCreepScore = playerChampionStats['totalMinionKills']/playerChampionStats['totalSessionsPlayed']
        return averageCreepScore

    def calculateScoreOfChampionByKDA(self,averageKDA):
        score = (averageKDA[0] + averageKDA[2]) / averageKDA[1]
        return score





