class WeatherInformation():

    clouds = "clouds"

    coordinates = "coord"
    longitude = "lon"
    latitude = "lat"

    mainDescription = "main"
    weatherDescription = "description"
    weatherInfo = "weather"

    wind = "wind"
    windSpeed = "speed"
    windDegree = "deg"

    rainVolume = "rain"
    snowVolume = "snow"
    last3Hours = "3h"

    temperature = "temp"
    pressure = "pressure"
    humidity = "humidity"
    minimumTemperature = "temp_min"
    maximumTemperature = "temp_max"

    seaLevel = "sea_level"
    groundLevel = "grnd_level"

    def __init__(self):
        pass

    def displayStatistic(self,cityInformation):
        return

    def extractInformation(self,jsonData):
        return

    def kelvinToCelsius(self, temperatureInKelvin):
        temperatureInCelsius = temperatureInKelvin - 273.15
        return temperatureInCelsius

    def celsiusToKelvin(self, temperatureInCelsius):
        temperatureInKelvin = temperatureInCelsius + 273.15
        return temperatureInKelvin

