import requests
import APIKey

from ForecastStatistic import ForecastStatistic
from CurrentWeatherStatistic import CurrentWeatherStatistic

class OpenWeatherController():

    APIKey = APIKey.acquireKey()

    def __init__(self):
        return

    def requestCurrentWeatherURL (self,cityName, areaName, APIKey):
        weatherRequest = requests.get('http://api.openweathermap.org/data/2.5/weather?q=' + cityName + ',' + areaName + '&appid=' + APIKey)
        weatherRequestJson = weatherRequest.json()
        return weatherRequestJson

    def requestForeCastURL(self,cityName, areaName, APIKey):
        forecastRequest = requests.get('http://api.openweathermap.org/data/2.5/forecast?q=' + cityName + ',' + areaName + '&appid=' + APIKey)
        forecastRequestJson = forecastRequest.json()
        return forecastRequestJson

    def fahrenheitToCelsius(self,valueOfFahrenheit):
        fahrenheit = float(valueOfFahrenheit)
        celsius = (fahrenheit - 32) / 18
        return celsius

    def celsiusToFahrenheit(self,valueOfCelsius):
        celsius = float(valueOfCelsius)
        fahrenheit = (celsius * 16) - 32
        return fahrenheit

    def currentWeather(self,cityName,areaName,APIKey):
        weatherRequestJson = self.requestCurrentWeatherURL(cityName, areaName, APIKey)
        currentStatistic = CurrentWeatherStatistic(weatherRequestJson, cityName)
        return

    def forecastWeather(self,cityName,areaName,APIKey):
        forecastRequestJson = self.requestForeCastURL(cityName, areaName, APIKey)
        forecastStatistic = ForecastStatistic(forecastRequestJson)
        return



