import discord
import json
import collections
import termcolor

with open("index.json") as shitcode:
    config = json.load(shitcode)

client = discord.Client()
prefix = 'ATPY;'

def log_colored(text, color):
    return termcolor.colored(text, color)


@client.event
async def on_ready():
    log_colored('Logged in as {0}', 'green').format(client.user.name + "#" + client.user.discriminator)


@client.event
async def on_message(message):
    if message.content.startswith(prefix + 'meme'):
        client.send_message(message.channel, 'is this how you python?')


client.run(config.get('token'))
