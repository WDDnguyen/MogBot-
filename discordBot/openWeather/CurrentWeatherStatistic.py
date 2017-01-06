from datetime import datetime
from prettytable import PrettyTable

from openWeather.WeatherInformation import WeatherInformation

class CurrentWeatherStatistic(WeatherInformation):
    currentWeatherInformation = []
    cityName = ""

    def __init__(self,currentWeatherInformation,cityName):
        WeatherInformation.__init__(self)
        self.cityName = cityName
        self.currentWeatherInformation = currentWeatherInformation

    def extractInformationJson(self,currentWeatherRequestJson):
        cityInformation = []

        cityCoordinates = [currentWeatherRequestJson[self.coordinates][self.longitude], currentWeatherRequestJson[self.coordinates][self.latitude]]
        cityCurrentWindSpeed = currentWeatherRequestJson[self.wind][self.windSpeed]

        cityWeather = currentWeatherRequestJson[self.weatherInfo]
        cityWeatherDescription = cityWeather[0][self.weatherDescription]

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

    def displayStatisticTabularForm(self):
        cityInformation = self.extractInformationJson(self.currentWeatherInformation)
        table = PrettyTable()
        table._set_field_names([" ",self.cityName])
        table.add_column(" ",["Coordinates (dec)","Weather Description","Wind (m/s)","Temperature (C)","Pressure (hPa)","Humidy (%)", "Cloudiness (%)"])
        table.add_column(self.cityName,[str(cityInformation[0][0]) + "," + str(cityInformation[0][1]), cityInformation[2], str(cityInformation[1]), str(self.kelvinToCelsius(cityInformation[3][1])) ,str(cityInformation[4]) , str(cityInformation[5]),str(cityInformation[6])])
        return table


    def displayStatisticDiscord(self):
        cityInformation = self.extractInformationJson(self.currentWeatherInformation)
        response = "Today's weather statistics for " + self.cityName + " at: " + str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + "\n" + cityInformation[2] + "\n" + "Coordinates of " + self.cityName + " in decimal form : " + str(cityInformation[0][0]) + " , " + str( cityInformation[0][1]) + "\n"
        response += "Wind speed : " + str(cityInformation[1]) + " meters/second" + "\n" + "Current temperature : " + str(self.kelvinToCelsius(cityInformation[3][0])) + " Celsius with a current minimal temperature of: " + str(self.kelvinToCelsius(cityInformation[3][1])) + " Celsius and current maximum temperature of : " + str(self.kelvinToCelsius(cityInformation[3][2])) + " Celsius" + "\n"
        response +="Current Pressure : " + str(cityInformation[4]) + " hPa" + "\n" + "Current Humidity : " + str(cityInformation[5]) + " %" + "\n" + "Current Cloudiness : " + str(cityInformation[6]) + " %"

        return response

    #test display
    def displayStatistic(self,cityInformation,cityName):
        print ("Today's weather statistics for " + cityName + " at: " + str(datetime.now()))
        print (cityInformation[2])
        print ("Coordinates of " + cityName + " in decimal form : " + str(cityInformation[0][0]) + " , " + str( cityInformation[0][1]))
        print ("Wind speed : " + str(cityInformation[1]) + " meters/second")
        print ("Current temperature : " + str( self.kelvinToCelsius(cityInformation[3][0])) + " Celsius with a current minimal temperature of: " + str(self.kelvinToCelsius(cityInformation[3][1])) + " Celsius and current maximum temperature of : " + str(self.kelvinToCelsius(cityInformation[3][2])) + " Celsius")
        print ("Current Pressure : " + str(cityInformation[4]) + " hPa")
        print ("Current Humidity : " + str(cityInformation[5]) + " %")
        print ("Current Cloudiness : " + str(cityInformation[6]) + " %")
