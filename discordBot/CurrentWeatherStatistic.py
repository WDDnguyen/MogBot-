from datetime import datetime

from WeatherInformation import WeatherInformation

class CurrentWeatherStatistic(WeatherInformation):

    def __init__(self,currentWeatherInformation,cityName):
        WeatherInformation.__init__(self)
        currentWeatherInformation = currentWeatherInformation
        extractedInformation = self.extractInformationJson(currentWeatherInformation)
        self.displayStatistic(extractedInformation,cityName)

    def extractInformationJson(self,currentWeatherRequestJson):
        cityInformation = []

        cityCoordinates = [currentWeatherRequestJson[self.coordinates][self.longitude], currentWeatherRequestJson[self.coordinates][self.latitude]]
        cityCurrentWindSpeed = currentWeatherRequestJson[self.wind][self.windSpeed]

        cityWeather = currentWeatherRequestJson[self.weatherInfo]
        cityWeatherDescription =  "Current weather status : "+ cityWeather[0][self.weatherDescription]

        cityMain = currentWeatherRequestJson[self.mainDescription]
        cityCurrentTemperature = [cityMain[self.temperature],cityMain[self.minimumTemperature],cityMain[self.maximumTemperature]]
        cityCurrentPressure = cityMain[self.pressure]
        cityCurrentHumidity = cityMain[self.humidity]
        cityCurrentCloudiness = currentWeatherRequestJson[self.clouds]["all"]

        cityInformation.append(cityCoordinates)
        cityInformation.append(cityCurrentWindSpeed)
        cityInformation.append(cityWeatherDescription)
        cityInformation.append(cityCurrentTemperature)
        cityInformation.append(cityCurrentPressure)
        cityInformation.append(cityCurrentHumidity)
        cityInformation.append(cityCurrentCloudiness)

        return cityInformation

    def displayStatistic(self,cityInformation,cityName):
        print ("Today's weather statistics for " + cityName + " at: " + str(datetime.now()))
        print (cityInformation[2])
        print ("Coordinates of " + cityName + " in decimal form : " + str(cityInformation[0][0]) + " , " + str( cityInformation[0][1]))
        print ("Wind speed : " + str(cityInformation[1]) + " meters/second")
        print ("Current temperature : " + str( self.kelvinToCelsius(cityInformation[3][0])) + " Celsius with a current minimal temperature of: " + str(self.kelvinToCelsius(cityInformation[3][1])) + " Celsius and current maximum temperature of : " + str(self.kelvinToCelsius(cityInformation[3][2])) + " Celsius")
        print ("Current Pressure : " + str(cityInformation[4]) + " hPa")
        print ("Current Humidity : " + str(cityInformation[5]) + " %")
        print ("Current Cloudiness : " + str(cityInformation[6]) + " %")
