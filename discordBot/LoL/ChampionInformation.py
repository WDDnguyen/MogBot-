class ChampionInformation():

    championInfo = []
    def __init__(self,championInfo,championName):
        self.championInfo = championInfo
        self.championName = championName

    def displayChampionStats(self):
        response = ""
        for item in self.championInfo['data'][self.championName]['stats']:
            response += item +" : " + str(self.championInfo['data'][self.championName]['stats'][item]) + "\n"
        return response

    def displayChampionName(self):
        response = self.championName
        return response

    def displayChampionName(self):
        response = self.championInfo['data'][self.championName]['id']
        return response

    def displayChampionLore(self):
        response = self.championInfo['data'][self.championName]['lore']
        return response

    def acquireChampionSkinsInformation(self):
        skinOptions = []
        for item in self.championInfo['data'][self.championName]['skins']:
            skinOptions.append(item)
        return skinOptions

    def acquireChampionSkinNames(self):
        skinInformation = self.acquireChampionSkinsInformation()
        skinNames = []
        for index in range(0,len(skinInformation)) :
            skinNames.append(skinInformation[index]['name'])
        return skinNames

    def acquireChampionSkinNumber(self,skinName):
        skinInformation = self.acquireChampionSkinsInformation()
        skinNumber = ""
        skinName = skinName.lower()
        if skinName != 'default':
            skinName = skinName.title()
        for index in range(0, len(skinInformation)):
            if skinName == skinInformation[index]['name'] :
                skinNumber = skinInformation[index]['num']
        return skinNumber

    def displayAllChampionData(self):
        for item in self.championInfo['data'][self.championName]:
            print(item + " : " + str(self.championInfo['data'][self.championName][item]) + "\n")
        print("---------------------------------")

    def Exist(self):
        print (True)