from WeatherInformation import WeatherInformation

class forecastDay(WeatherInformation):
    timeList = []

    def __init__(self,timeList):
        WeatherInformation.__init__(self)
        self.timeList = timeList

    def extractInformation(self,item):
        cityForecastInformation = []

        cityTimeOfForecast = item["dt_txt"]
        cityForecastWindSpeed = [item[self.wind][self.windSpeed],item[self.wind][self.windDegree]]

        try :
            item[self.rainVolume][self.last3Hours]
        except KeyError :
            cityForecastRain = []
        else:
            cityForecastRain = item[self.rainVolume][self.last3Hours]

        try :
            item[self.snowVolume][self.last3Hours]
        except KeyError :
            cityForecastSnow = []
        else :
            cityForecastSnow = item[self.snowVolume][self.last3Hours]

        cityWeather = item[self.weatherInfo]
        cityWeatherDescription = "Current weather status : " + cityWeather[0][self.weatherDescription]

        cityMain = item[self.mainDescription]
        cityForecastTemperature = [cityMain[self.temperature], cityMain[self.minimumTemperature],cityMain[self.maximumTemperature]]
        cityForecastPressure = cityMain[self.pressure]
        cityForecastHumidity = cityMain[self.humidity]
        cityForecastCloudiness = item[self.clouds]["all"]

        cityForecastInformation.append(cityTimeOfForecast)
        cityForecastInformation.append(cityForecastWindSpeed)
        cityForecastInformation.append(cityWeatherDescription)
        cityForecastInformation.append(cityForecastTemperature)
        cityForecastInformation.append(cityForecastPressure)
        cityForecastInformation.append(cityForecastHumidity)
        cityForecastInformation.append(cityForecastCloudiness)
        cityForecastInformation.append(cityForecastRain)
        cityForecastInformation.append(cityForecastSnow)

        return cityForecastInformation

    def displayStatistic(self,cityForecastInformation):
        print ("Forecast for : " + cityForecastInformation[0])
        print (cityForecastInformation[2])
        print ("Wind speed : " + str(cityForecastInformation[1][0]) + " meters/second " + str(cityForecastInformation[1][0]) + " degree")
        print ("temperature : " + str(self.kelvinToCelsius(cityForecastInformation[3][0])) + " Celsius with a minimal temperature of: " + str(self.kelvinToCelsius(cityForecastInformation[3][1])) + " Celsius and maximum temperature of : " + str(self.kelvinToCelsius(cityForecastInformation[3][2])) + " Celsius")
        print ("Pressure : " + str(cityForecastInformation[4]) + " hPa")
        print ("Humidity : " + str(cityForecastInformation[5]) + " %")
        print ("Cloudiness : " + str(cityForecastInformation[6]) + " %")

        if cityForecastInformation[7] :
            print ("Rain forecast for the next three hours : " + str(cityForecastInformation[7]) + " mm")

        if cityForecastInformation[8] :
            print ("Snow forecast for the next three hours : " + str(cityForecastInformation[8]) + " cm")

        print ('--------------------------------------------------------------------------------')

    def displayForecastStatistic(self):
        for item in self.timeList:
            extractedInfo = self.extractInformation(item)
            self.displayStatistic(extractedInfo)
