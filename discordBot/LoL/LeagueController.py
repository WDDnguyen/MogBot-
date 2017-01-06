import requests
from discordBot.LoL import LoLAPIKey
from discordBot.LoL import SummonerInformation
from discordBot.LoL import ChampionInformation

class LeagueController():
    APIKey = LoLAPIKey.acquireAPIKey()

    def __init__(self):
        return

    def requestSummonerDataURL(self,region, summonerName):
        URL = "https://" + region + ".api.pvp.net/api/lol/na/v1.4/summoner/by-name/" + summonerName + "?api_key=" + self.APIKey
        summonerRequest = requests.get(URL)
        summonerRequestJson = summonerRequest.json()
        return summonerRequestJson

    def requestAllChampionStats(self):
        URL = 'https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion?champData=stats&api_key='+self.APIKey
        requestAllChampionInformation = requests.get(URL)
        requestAllChampionInformationJson = requestAllChampionInformation.json()
        return requestAllChampionInformationJson

    def requestAllChampionLores(self):
        URL = 'https://global.api.pvp.net/api/lol/static-data/na/v1.2/champion?champData=lore&api_key='+ self.APIKey
        loreRequest = requests.get(URL)
        loreRequestJson = loreRequest.json()
        return loreRequestJson

    def acquireChampionStats(self,championName):
        allChampionStats = self.requestAllChampionStats()
        extractedChampionInformation = allChampionStats['data'][championName]
        championInformation = ChampionInformation.ChampionInformation(extractedChampionInformation)
        return championInformation.displayChampionStats()




#Unit Testing
def main():
    region = "na"
    summonerName = "akiDucky"
    controller = LeagueController()
    summonerJson = controller.requestSummonerDataURL(region,summonerName)
    print (summonerJson)

    championName = "Jhin"
    print(controller.acquireChampionStats(championName))

if __name__ == "__main__":
    main()

