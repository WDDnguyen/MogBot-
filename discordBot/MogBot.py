import discord
import Token
from MagicConchShell import MagicConchShell
from openWeather.OpenWeatherController import OpenWeatherController
from discordBot.LoL import LeagueController
import datetime
import json

token = Token.acquirechocoBotToken()
bot = discord.Client()

magicConchShellFunction = MagicConchShell()
openWeatherController = OpenWeatherController()
leagueController = LeagueController.LeagueController()

listOfCommands = {'!magic','!weather', '!league'}
listOfMagicConchShellCommands = {}
listOfWeatherCommands = {'!celsius','!fahrenheit','!current','!forecast'}
listOfLeagueCommands = {'!champion','!summoner'}
listOfChampionCommands = {'!skin','!stats','!lore',}
listOfSummonerCommands = {'!rank'}

def capitalize(line):
    return ' '.join(s[0].upper() + s[1:] for s in line.split(' '))

def formatAnswer(answer):
    return str(answer.content).lower()

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

            if item == '!weather':
                for item in listOfWeatherCommands:
                    response += "        - " + item + "\n"
            if item == '!league':
                for item in listOfLeagueCommands:
                    response += "        - " + item + "\n"
                    if item == '!champion':
                        for item in listOfChampionCommands:
                            response += "                - " + item + "\n"
                    if item == '!summoner':
                        for item in listOfSummonerCommands:
                            response += "                - " + item + "\n"

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
        ask = formatAnswer(ask)

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
                    value = formatAnswer(value)
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
                    value = formatAnswer(value)
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
        await bot.send_message(message.channel, "Which league command do you want to execute?")

        ask = await bot.wait_for_message(timeout=15.0, author=message.author)
        ask = formatAnswer(ask)

        if ask is None:
            await bot.send_message(message.channel, "There was no command for weather")

        else:
            #Champion Mode
            if ask == "!champion" :
                await bot.send_message(message.channel, "Which champion do you want to get information on?")

                championName = await bot.wait_for_message(timeout=15.0, author=message.author)

                if championName is None:
                    await bot.send_message(message.channel, "There was no message")

                else:
                    try :
                        championName = formatAnswer(championName)
                        championName = capitalize(championName)
                        leagueController.requestChampionData(championName)

                        await bot.send_message(message.channel, "Which commands for the champion do you want to execute?")

                        command = await bot.wait_for_message(timeout=15.0, author=message.author)

                        if command is None:
                            await bot.send_message(message.channel, "There was no message")
                        else:
                            command = formatAnswer(command)
                            if command == '!stats':
                                response = "Stats for : " + leagueController.championInformation.displayChampionName() + " \n\n" + leagueController.acquireChampionStats()
                                await bot.send_message(message.channel, response)

                            elif command == '!lore':
                                response = leagueController.acquireChampionLore()
                                await bot.send_message(message.channel, response)

                            elif command == '!skin':
                                response = "List of skin for this champion : "
                                skinList = leagueController.acquireChampionSkinName()
                                for item in skinList :
                                    response += item + ", "
                                await bot.send_message(message.channel,  response)
                                await bot.send_message(message.channel, "Do you want the image of this skin? yes/no")

                                answer = await bot.wait_for_message(timeout=15.0, author=message.author)
                                answer = formatAnswer(answer)

                                if answer == 'yes':
                                    await bot.send_message(message.channel, "which one?")
                                    skinName = await bot.wait_for_message(timeout=15.0, author= message.author)
                                    skinName = formatAnswer(skinName)

                                    URL = leagueController.acquireChampionSkinImage(championName,skinName)
                                    response = URL
                                    await bot.send_message(message.channel, response)

                                else :
                                    pass
                    except json.decoder.JSONDecodeError:
                        await bot.send_message(message.channel, "There is no champion with that name")
                        pass

            elif ask == '!summoner':
                await bot.send_message(message.channel, "Which player do you want to get information on? summoner name,region")

                summonerInfo = await bot.wait_for_message(timeout=15.0,author=message.author)

                if summonerInfo is None:
                    await bot.send_message(message.channel, "There was no message")
                else :
                    try:
                        summonerInfo = formatAnswer(summonerInfo)
                        valueList = summonerInfo.split(',', 1)
                        summonerName = valueList[0]
                        summonerRegion = valueList[1]
                        leagueController.createSummonerInformation(summonerRegion,summonerName)

                    except:
                        pass

                    await bot.send_message(message.channel, "Which commands for the player do you want to execute?")

                    summonerCommand = await bot.wait_for_message(timeout=15.0, author=message.author)

                    if summonerCommand is None:
                        await bot.send_message(message.channel, "There was no message")

                    else :
                        summonerCommand = formatAnswer(summonerCommand)
                        if summonerCommand == '!rank':
                            response = "This is " + summonerName + " best champions for this season : \n"
                            championNameList = leagueController.acquireCurrentMostPlayedChampionNames()
                            for champion in championNameList:
                                response += champion + " "

                            await bot.send_message(message.channel, response)
bot.run(token)

