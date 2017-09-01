import discord
import json
import collections
from termcolor import colored

with open("index.json") as shitcode:
    config = json.load(shitcode)

client = discord.Client()
prefix = 'ATPY;'


@client.event
async def on_ready():
    print('Logged in as ' + client.user.name + client.user.discriminator)


@client.event
async def on_message(message):
    if message.content.startswith(prefix + 'meme'):
        client.send_message(message.channel, 'is this how you python?')


client.run(config.get('token'))
