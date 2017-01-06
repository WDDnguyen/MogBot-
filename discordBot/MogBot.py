import discord
import Token
from MagicConchShell import MagicConchShell
from OpenWeatherController import OpenWeatherController
import datetime


token = Token.acquireToken()
bot = discord.Client()

magicConchShellFunction = MagicConchShell()
openWeatherController = OpenWeatherController()

listOfCommands = {'!magic','!weather', '!league'}
listOfWeatherCommands = {'!celsius','!fahrenheit','!current','!forecast'}
listOfLeagueCommands = {}

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_message(message):

    if message.author == bot.user:
        return

#HELP COMMAND

    if message.content.startswith('!bot'):
        response = "\n"
        for item in listOfCommands :
            response += item + "\n"

        await bot.send_message(message.channel,"Here's a list of commands I can execute :" + response)

#MAGIC CONCH SHELL MODE
    elif message.content.startswith('!magic'):
        await bot.send_message(message.channel, "I'm holding a magic conch shell\n " + "What do you want to ask the magic conch shell ?\n")

        ask = await bot.wait_for_message(timeout = 15.0, author = message.author)
        if ask is None :
            await bot.send_message(message.channel,"There was no message")

        else:
            response = magicConchShellFunction.responseToCall()
            await bot.send_message(message.channel, str(response))


#WEATHER MODE
    elif message.content.startswith('!weather'):
        await bot.send_message(message.channel, "Which weather command do you want me to execute?")

        ask = await bot.wait_for_message(timeout = 15.0, author = message.author)
        ask = str(ask.content)

        if ask is None :
            await bot.send_message(message.channel,"There was no command for weather")

        else :
            if ask == '!celsius':
                await bot.send_message(message.channel, "What is the value of fahrenheit to convert to celsius ?")

                value = await bot.wait_for_message(timeout=15.0, author = message.author)
                if value is None:
                    await bot.send_message(message.channel,"There was no message")
                else:
                    try:
                        value = float(value.content)
                        response = openWeatherController.celsiusToFahrenheit(value)
                        await bot.send_message(message.channel, str(response))

                    except ValueError:
                        await bot.send_message(message.channel, "This isn't an numerical value, please try again")

            elif ask == '!fahrenheit':
                await bot.send_message(message.channel, "What is the value of celsius to convert to fahrenheit?")

                value = await bot.wait_for_message(timeout=15.0, author=message.author)
                if value is None:
                    await bot.send_message(message.channel, "There was no message")
                else:
                    try:
                        value = float(value.content)
                        response = openWeatherController.fahrenheitToCelsius(value)
                        await bot.send_message(message.channel, str(response))

                    except ValueError:
                        await bot.send_message(message.channel, "This isn't an numerical value, please try again")

            elif ask == '!current' :
                await bot.send_message(message.channel, "For which city do you want to get the current statistic ? ex: Norfolk,US")

                value = await bot.wait_for_message(timeout=15.0, author=message.author)
                if value is None:
                    await bot.send_message(message.channel, "There was no message")
                else:
                    value = str(value.content).lower()
                    valueList = value.split(',',1 )
                    cityName = valueList[0]
                    areaName = valueList[1]

                    response = openWeatherController.currentWeather(cityName,areaName)

                    await bot.send_message(message.channel, response)

            elif ask == '!forecast' :
                await bot.send_message(message.channel, "For which city do you want the forecast? ex :Norfolk,US")

                value = await bot.wait_for_message(timeout=15.0, author=message.author)
                if value is None:
                    await bot.send_message(message.channel, "There was no message")
                else:
                    value = str(value.content).lower()
                    valueList = value.split(',', 1)
                    cityName = valueList[0]
                    areaName = valueList[1]

                    response = openWeatherController.forecastWeather(cityName, areaName)
                    index = 0
                    for item in response :
                        await bot.send_message(message.channel,datetime.datetime.now() + datetime.timedelta(days=index))
                        await bot.send_message(message.channel, item)
                        index += 1
#League Mode
    elif message.content.startswith('!league'):
        await bot.send_message(message.channel, "Which league command do you want to excite?")



bot.run(token)

