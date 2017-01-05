from ForecastDay import forecastDay
from prettytable import PrettyTable
from datetime import datetime

class ForecastStatistic():
    ForecastJson = ""

    def __init__(self,Json):
        self.ForecastJson = Json

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

    def displayStatisticTabularForm(self):
        forecastDayList = self.extractForecastInformationJson(self.ForecastJson)
        tableList = []
        fieldName = [" ", "Weather Description", "Wind (m/s)", "Temperature (C)", "Pressure (hPa)", "Humidy (%)","Cloudiness (%)", "Rain (mm)", "Snow (cm)"]

        for day in forecastDayList:
            table = PrettyTable(fieldName)
            currentDay = forecastDay(day)
            tabulatedDay = currentDay.createForecastTabularForm()
            for item in tabulatedDay :
                table.add_row(item)

            tableList.append(table)
        return tableList
