import discord
import json
import collections
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
        self.log_colored('Logged in as {0}'.format(self.user.name + "#" + self.user.discriminator), 'green')
        self.load_extension('extensions.basic')
    
    async def on_command_error(self, Exception, context):
        if isinstance(Exception, commands.errors.CommandNotFound):
            pass
        # Make non-existing commands not spam the console.

    async def on_message(self, message):
        if message.author.bot:
            return
        # Prevents bot to bot interactions.

atomic = Atomic(prefix)
atomic.run(token)
