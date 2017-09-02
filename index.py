import collections
import json
import os
import discord
import termcolor
from discord.ext import commands

with open("index.json") as shitcode:
    config = json.load(shitcode)

token = config.get('token')
prefix = 'ATPY;'

class Atomic(commands.Bot):
    def __init__(self, command_prefix, **options):
        super().__init__(command_prefix, **options)

    def log_colored(self, text, color):
        return print(termcolor.colored(text, color))

    async def on_ready(self):
        self.log_colored('Logged in as {0}'.format(str(self.user)), 'green')
        self.load_extension('extensions.basic')

    async def on_command_error(self, Exception, context):
        if isinstance(Exception, commands.errors.CommandNotFound):
            pass
        # Make non-existing commands not spam the console.

    async def on_message(self, message):
        # DOES NOT BREAK TOS DON'T WORRY ABOUT THIS SHITCODE
        # START TOS-COMPLIANT SHITCODE
        directory = "./logs/{0}".format(message.guild.name)
        if not os.path.exists(directory):
            os.makedirs(directory)
        directory2 = "./logs/{0}/{1}".format(message.guild.name, message.channel.name) #REEEEEE
        if not os.path.exists(directory2):
            os.makedirs(directory2)
        with open("./logs/{0}/{1}/messages.txt".format(message.guild.name, message.channel.name), "a") as myfile:
           myfile.write("{0} | {1} | {2} | {3}\n".format(message.author.name, message.guild.name, message.channel.name, message.content))
# END TOS COMPLIANT SHITCODE
        # if message.author.bot:
            # return
        # Prevents bot to bot interactions.
        # Currently breaks the bot, to be fixed.

atomic = Atomic(prefix)
atomic.run(token)
