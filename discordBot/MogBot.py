import discord
import Token
from MagicConchShell import MagicConchShell
from OpenWeatherController import OpenWeatherController

token = Token.acquireToken()
bot = discord.Client()

magicConchShellFunction = MagicConchShell()
openWeatherController = OpenWeatherController()

listOfCommands = {'!magic','!weather'}
listOfWeatherCommands = {"celsius","fahrenheit","current","forecast"}

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

    if message.content.startswith('!bot'):
        response = "\n"
        for item in listOfCommands :
            response += item + "\n"

        await bot.send_message(message.channel,"Here's a list of commands I can execute :" + response)

    elif message.content.startswith('!magic'):
        await bot.send_message(message.channel, "I'm holding a magic conch shell\n " + "What do you want to ask the magic conch shell ?\n")

        ask = await bot.wait_for_message(timeout = 15.0, author = message.author)
        if ask is None :
            await bot.send_message(message.channel,"There was no message")

        else:
            response = magicConchShellFunction.responseToCall()
            await bot.send_message(message.channel, str(response))

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
                value = str(value.content)

                if value is None:
                    await bot.send_message(message.channel,"There was no message")
                else:
                    response = openWeatherController.celsiusToFahrenheit(value)
                    await bot.send_message(message.channel, str(response))


            elif ask == '!fahrenheit':
                await bot.send_message(message.channel, "What is the value of celsius to convert to farenheit ?")

                value = await bot.wait_for_message(timeout=15.0, author=message.author)
                value = str(value.content)

                if value is None:
                    await bot.send_message(message.channel, "There was no message")
                else:
                    response = openWeatherController.celsiusToFahrenheit(value)
                    await bot.send_message(message.channel, str(response))

            elif ask == '!current' :
                await bot.send_message(message.channel, "For which city do you want to get the current temperature ?, ex:Norfolk,US")

                value = await bot.wait_for_message(timeout=15.0, author=message.author)
                value = str(value.content)

bot.run(token)

