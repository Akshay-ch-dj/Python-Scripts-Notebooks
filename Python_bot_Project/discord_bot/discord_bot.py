import os
import discord
import requests
import json
# from discord.ext import commands

# Part of discord library client created
client = discord.Client()
# client = commands.Bot(command_prefix="$")


def get_meme():
    """
    Gives a random meme on call
    """
    # Give a get request to the API url
    img_response = requests.get("https://meme-api.herokuapp.com/gimme")
    # The response is converted to JSON
    img_json = json.loads(img_response.text)
    return {'image': img_json['preview'][3],
            'author': img_json['author']}


def get_quote():
    """
    Gives a random quote on call
    """
    # Give a get request to the API url
    quote_response = requests.get("https://zenquotes.io/api/random")
    # The response is converted to JSON
    quote_json = json.loads(quote_response.text)
    quote = quote_json[0]['q'] + " -" + quote_json[0]['a']
    return quote


# Use that clent to register to an event,
# The event happens as soon as the bot is ready
@ client.event
async def on_ready():
    """
    called only when the bot is ready
    """
    # prints the client.user
    print("We have got a bot to work as {0.user}".format(client))


# Now the next event, event that happens when the bot receives a messege
@ client.event
async def on_message(message):
    """
    triggers each time a messege is received,
    Not need to respond to the bot's own message
    """
    if message.author == client.user:
        return

    if message.content.startswith("$quote"):
        # Bot take it as a command - can give a response
        quote = get_quote()
        await message.channel.send(quote)

    if message.content.startswith("$meme"):
        # Bot take it as a command - can give a response
        meme = get_meme()['image']
        await message.channel.send(meme)


# Add an api
BOT_TOKEN = "ODI5MDQxNzgwOTEyNjg1MDU2.YGyXUw.jlIuDsdHxYU0ixTfE_ThuvlznVk"
# Finally run the bot, need the identification/password which is the token
client.run(BOT_TOKEN)
