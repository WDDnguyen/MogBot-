import requests
from discordBot.LoL import LoLAPIKey
from discordBot.LoL import SummonerInformation
from discordBot.LoL import ChampionInformation

class LeagueController():
    APIKey = LoLAPIKey.acquireAPIKey()
    championInformation = []

    def __init__(self):
        return

    def requestSummonerDataURL(self,region, summonerName):
        URL = "https://" + region + ".api.pvp.net/api/lol/na/v1.4/summoner/by-name/" + summonerName + "?api_key=" + self.APIKey
        summonerRequest = requests.get(URL)
        summonerRequestJson = summonerRequest.json()
        return summonerRequestJson

    def requestChampionData(self,championName):
        URL = 'http://ddragon.leagueoflegends.com/cdn/5.14.1/data/en_US/champion/'+championName+'.json'
        championData = requests.get(URL)
        championDataJson = championData.json()
        championInformation = ChampionInformation.ChampionInformation(championDataJson,championName)
        self.championInformation = championInformation

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
    summonerName = "akiDucky"
    controller = LeagueController()
    summonerJson = controller.requestSummonerDataURL(region,summonerName)
    print (summonerJson)
    print ("-------------------------------------------------------")

    championName = 'Bard'
    championSkinName = 'elderwood bard'
    controller.requestChampionData(championName)
    print(controller.acquireChampionData())
    print(controller.championInformation.displayChampionID())
    print(controller.championInformation.displayChampionLore())
    print(controller.acquireChampionStats())
    print(controller.acquireChampionSkinName())
    print(controller.acquireChampionSkinImage(championName,championSkinName))

if __name__ == "__main__":
    main()

