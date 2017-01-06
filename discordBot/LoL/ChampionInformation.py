class ChampionInformation():

    championInfo = []
    def __init__(self,championInfo):
        self.championInfo = championInfo

    def displayChampionStats(self):
        response = ""
        for item in self.championInfo['stats']:
            response += item + ": " + str(self.championInfo['stats'][item]) +"\n"
        return response

    def displayChampionName(self):
        response = self.championInfo['name']
        return response

    def displayChampionID(self):
        response = self.championInfo['title']
        return response
