from ForecastDay import forecastDay

class ForecastStatistic():
    ForecastJson = ""
    forecastDayList = []
    def __init__(self,Json):
        ForecastJson = Json
        forecastDay = self.extractForecastInformationJson(ForecastJson)
        self.displayStatistic(forecastDay)

    def extractForecastInformationJson(self,forecastRequestJson):

        forecastDayList = [[], [], [], [], [], []]
        currentForecastTime = ""
        currentForecastDay = forecastDayList[0]
        index = 1

        for threeHourForecast in forecastRequestJson["list"]:
            if currentForecastTime == "":
                currentForecastTime = threeHourForecast['dt_txt'][0:10]

            if currentForecastTime == threeHourForecast['dt_txt'][0:10]:
                currentForecastDay.append(threeHourForecast)
            else:
                forecastDayList[index - 1] = currentForecastDay
                currentForecastDay = forecastDayList[index]
                index += 1

                currentForecastDay.append(threeHourForecast)
                currentForecastTime = threeHourForecast['dt_txt'][0:10]

        return forecastDayList

    def displayStatistic(self,forecastDayList):
        for day in forecastDayList:
            currentDay = forecastDay(day)
            currentDay.displayForecastStatistic()
