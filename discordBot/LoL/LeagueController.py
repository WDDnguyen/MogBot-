import requests
from discordBot.LoL import LoLAPIKey
from discordBot.LoL import SummonerProfile
from discordBot.LoL import ChampionInformation

class LeagueController():
    APIKey = LoLAPIKey.acquireAPIKey()
    championInformation = None
    summonerProfile = None
    seasonList = ["SEASON2013","SEASON2014","SEASON2015","SEASON2016","SEASON2017"]

    def __init__(self):
        return

    def requestSummonerData(self,region, summonerName):
        URL = "https://" + region + ".api.pvp.net/api/lol/na/v1.4/summoner/by-name/" + summonerName + "?api_key=" + self.APIKey
        summonerRequest = requests.get(URL)
        summonerRequestJson = summonerRequest.json()
        return summonerRequestJson

    def requestSummonerRankedStatistic(self,summonerID):
        rankedStatisticForAllSeasons = []

        for season in self.seasonList:
            URL = 'https://na.api.pvp.net/api/lol/na/v1.3/stats/by-summoner/'+summonerID+'/ranked?season='+season+'&api_key='+self.APIKey
            summonerRankedStatisticOfSeason = requests.get(URL)
            if summonerRankedStatisticOfSeason.status_code != 400:
                summonerRankedStatisticOfSeasonJson = summonerRankedStatisticOfSeason.json()
                rankedStatisticForAllSeasons.append(summonerRankedStatisticOfSeasonJson)
        return rankedStatisticForAllSeasons

    def createSummonerInformation(self,region,summonerName):
        summonerInformation = self.requestSummonerData(region,summonerName)

        summonerName = "".join(summonerName.split())
        summonerName = summonerName.lower()

        summonerID = summonerInformation[summonerName]['id']
        summonerRankedStatistic = self.requestSummonerRankedStatistic(str(summonerID))
        summonerProfile = SummonerProfile.SummonerProfile(summonerInformation,summonerRankedStatistic)
        self.summonerProfile = summonerProfile

    def requestChampionData(self,championName):
        URL = 'http://ddragon.leagueoflegends.com/cdn/5.14.1/data/en_US/champion/'+championName+'.json'
        championData = requests.get(URL)
        championDataJson = championData.json()
        championInformation = ChampionInformation.ChampionInformation(championDataJson,championName)
        self.championInformation = championInformation

    def acquireChampionLore(self):
        return self.championInformation.displayChampionLore()

    def acquireChampionStats(self):
        return self.championInformation.displayChampionStats()

    def acquireChampionData(self):
        return self.championInformation.displayAllChampionData()

    def acquireChampionSkinName(self):
        return self.championInformation.acquireChampionSkinNames()

    def acquireChampionSkinImage(self,championName,skinName):
        championSkinNumber = self.championInformation.acquireChampionSkinNumber(skinName)
        URL = 'http://ddragon.leagueoflegends.com/cdn/img/champion/splash/'+championName+'_'+str(championSkinNumber)+'.jpg'
        return URL

#Unit Testing
def main():
    region = "na"
    summonerName = "Kawakaze K2"
    summonerID = "32399524"
    controller = LeagueController()
    summonerJson = controller.requestSummonerData(region,summonerName)
    print (summonerJson)
    print ("-------------------------------------------------------")
    controller.createSummonerInformation(region,summonerName)
    print(controller.summonerProfile.displayAllRankedStatistic())

    """championName = 'Bard'
    championSkinName = 'default'
    controller.requestChampionData(championName)
    print(controller.acquireChampionData())
    print(controller.championInformation.displayChampionName())
    print(controller.championInformation.displayChampionLore())
    print(controller.acquireChampionStats())
    print(controller.acquireChampionSkinName())
    print(controller.acquireChampionSkinImage(championName,championSkinName))
    """
if __name__ == "__main__":
    main()

