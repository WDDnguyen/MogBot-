import discord
import Token
from MagicConchShell import MagicConchShell
from openWeather.OpenWeatherController import OpenWeatherController
from discordBot.LoL import LeagueController
import datetime
import json

token = Token.acquireToken()
bot = discord.Client()

magicConchShellFunction = MagicConchShell()
openWeatherController = OpenWeatherController()
leagueController = LeagueController.LeagueController()

listOfCommands = {'!magic','!weather', '!league'}

def capitalize(line):
    return ' '.join(s[0].upper() + s[1:] for s in line.split(' '))

def formatMessage(message):
    formatedMessage = str(message.content).lower()
    formatedMessage = ' '.join(formatedMessage.split())
    return formatedMessage

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

        await bot.send_message(message.author,"Here's a list of commands I can execute :" + response)

#MAGIC CONCH SHELL MODE
    elif message.content.startswith('!magic'):
        await bot.send_message(message.channel, "I'm holding a magic conch shell\n " + "What do you want to ask the magic conch shell ?\n")

        ask = await bot.wait_for_message(timeout = 15.0, author = message.author)
        if ask is None :
            await bot.send_message(message.channel,"There was no message")

        else:
            response = magicConchShellFunction.responseToCall()
            await bot.send_message(message.channel, str(response))

#RICK AND MORTY MODE PLACEHOLDER
    elif message.content.startswith('!rnm'):
        await bot.send_message(message.channel, "There is no Season 3")

#WEATHER MODE
    elif message.content.startswith('!weather'):
        messageComponentList = formatMessage(message).split(' ', 2)
        weatherCommand = messageComponentList[0]
        weatherSubCommand = messageComponentList[1]
        weatherValue = messageComponentList[2]

        if weatherSubCommand == '-c':
            try:
                value = float(weatherValue)
                fahrenheitResponse = openWeatherController.celsiusToFahrenheit(value)
                await bot.send_message(message.channel, str(fahrenheitResponse))

            except ValueError:
                await bot.send_message(message.channel, "This isn't an numerical value, please try again")

        elif weatherSubCommand == '-f':
            try:
                value = float(weatherValue)
                response = openWeatherController.fahrenheitToCelsius(value)
                await bot.send_message(message.channel, str(response))

            except ValueError:
                await bot.send_message(message.channel, "This isn't an numerical value, please try again")

        elif weatherSubCommand == '-cur':

            valueList = weatherValue.split(',',1)
            cityName = valueList[0]
            areaName = valueList[1]

            currentResponse = openWeatherController.currentWeather(cityName,areaName)
            print(currentResponse)

            await bot.send_message(message.channel, currentResponse)

        elif weatherSubCommand == '-for' :

            valueList = weatherValue.split(',', 1)
            cityName = valueList[0]
            areaName = valueList[1]

            forecastResponse = openWeatherController.forecastWeather(cityName, areaName)
            index = 0
            for item in forecastResponse :
                await bot.send_message(message.channel, str(datetime.datetime.now() + datetime.timedelta(days=index)) + '\n' + item.get_string())
                index += 1
#League Mode
    elif message.content.startswith('!league'):

        messageComponentList = formatMessage(message).split(' ', 2)
        leagueCommand = messageComponentList[0]
        leagueSubCommand = messageComponentList[1]
        leagueValue = messageComponentList[2]

        if leagueSubCommand[0:2] == '-c':
            try:
                championName = capitalize(leagueValue)
                leagueController.acquireCurrentPatchVersion()
                leagueController.requestChampionData(championName)

                if leagueSubCommand[2:] == 'stats':
                    championStatResponse = "Stats for : " + leagueController.championInformation.displayChampionName() + " \n\n" + leagueController.acquireChampionStats()
                    await bot.send_message(message.channel, championStatResponse)

                elif leagueSubCommand[2:] == 'lore':
                    championLoreResponse = leagueController.acquireChampionLore()
                    await bot.send_message(message.channel, championLoreResponse)

                elif leagueSubCommand[2:] == 'skin':
                    skinResponse = "List of skin for this champion : "
                    skinList = leagueController.acquireChampionSkinName()
                    for item in skinList:
                        skinResponse += item + ", "
                    await bot.send_message(message.channel, skinResponse)
                    await bot.send_message(message.channel, "To get the skin image type the skin name in the next 30 seconds")

                    skinName = await bot.wait_for_message(timeout=30.0, author=message.author)
                    skinName = formatMessage(skinName)

                    URL = leagueController.acquireChampionSkinImage(championName, skinName)
                    response = URL
                    await bot.send_message(message.channel, response)

                else:
                    await bot.send_message(message.channel, "This is not a correct league champion command")

            except json.decoder.JSONDecodeError:
                await bot.send_message(message.channel, "There is no champion with that name")

        elif leagueSubCommand[0:2] == '-s':
            valueList = leagueValue.split(',', 1)
            summonerName = valueList[0]
            summonerRegion = valueList[1]

            try:
                await bot.send_message(message.channel, "Retrieving information...")
                leagueController.createSummonerInformation(summonerRegion,summonerName)
                if leagueSubCommand[2:] == 'most':

                    response = "This is " + summonerName + " most played champions for this season : \n"
                    championNameList = leagueController.acquireCurrentMostPlayedChampionNames()

                    for champion in championNameList:
                        response += champion + ", "

                    await bot.send_message(message.channel, response)
                    await bot.send_message(message.channel,"\n do you want to get more information on these champions? yes/no")

                    answer = await bot.wait_for_message(timeout=15.0, author=message.author)
                    answer = formatMessage(answer)

                    if answer == 'yes':
                        statResponse = " "
                        leagueController.acquireCurrentPlayedChampionStats()
                        championStatList = leagueController.acquireSpecificMostPlayedChampionStats()

                        for championStat in championStatList:
                            statResponse += championStat + "\n"

                        await bot.send_message(message.channel, statResponse)


                elif leagueSubCommand[2:] == 'best':
                    response = "This is " + summonerName + " best played champions for this season : \n"
                    championNameList = leagueController.acquireCurrentBestPlayedChampionNames()

                    for champion in championNameList:
                        response += champion + ","

                    await bot.send_message(message.channel, response)

                    await bot.send_message(message.channel, "\n do you want to get more information on these champions? yes/no")

                    answer = await bot.wait_for_message(timeout=15.0, author=message.author)
                    answer = formatMessage(answer)

                    if answer == 'yes':
                        statResponse = " "
                        leagueController.acquireCurrentPlayedChampionStats()
                        championStatList = leagueController.acquireSpecificBestPlayedChampionStats()

                        for championStat in championStatList:
                            statResponse += championStat + "\n"

                        await bot.send_message(message.channel, statResponse)


            except json.decoder.JSONDecodeError:
                await bot.send_message(message.channel, "There is no summoner with that name")

bot.run(token)

