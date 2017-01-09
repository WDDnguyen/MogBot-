import requests

from openWeather import APIKey
from openWeather.ForecastStatistic import ForecastStatistic
from openWeather.CurrentWeatherStatistic import CurrentWeatherStatistic

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
        celsius = (valueOfFahrenheit * 9/5) + 32
        return celsius

    def celsiusToFahrenheit(self,valueOfCelsius):
        fahrenheit = (valueOfCelsius - 32) * 5/9
        return fahrenheit

    def currentWeather(self,cityName,areaName):
        weatherRequestJson = self.requestCurrentWeatherURL(cityName, areaName, self.APIKey)
        currentStatistic = CurrentWeatherStatistic(weatherRequestJson, cityName)
        return currentStatistic.displayStatisticTabularForm()

    def forecastWeather(self,cityName,areaName):
        forecastRequestJson = self.requestForeCastURL(cityName, areaName, self.APIKey)
        forecastStatistic = ForecastStatistic(forecastRequestJson)
        return  forecastStatistic.displayStatisticTabularForm()



