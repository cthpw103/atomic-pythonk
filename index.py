try:
    
   import collections
   import json
   import os
   import discord
   import termcolor
   import time
   import sys
   from datetime import timezone
   from discord.ext import commands

   with open("index.json") as shitcode:
       config = json.load(shitcode)
 
   token = config.get('token')
   prefix = 'ATPY;'

   class Atomic(commands.Bot):
       def __init__(self, command_prefix, **options):
           super().__init__(command_prefix, **options)
    
       def utc_to_local(self, utc_dt):
           return utc_dt.replace(tzinfo=timezone.utc).astimezone(tz=None)
    
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
           directory3 = "./logs/{0}/{1}/{2}".format(message.guild.name, message.channel.name, message.author.name)
           if not os.path.exists(directory3):
               os.makedirs(directory3)
           directory4 = "./logs/{0}/{1}/{2}/{3}".format(message.guild.name, message.channel.name, message.author.name, self.utc_to_local(message.timestamp).strftime('%Y'))
           if not os.path.exists(directory4):
               os.makedirs(directory4)
           directory5 = "./logs/{0}/{1}/{2}/{3}/{4}".format(message.guild.name, message.channel.name, message.author.name, self.utc_to_local(message.timestamp).strftime('%Y'), self.utc_to_local(message.timestamp).strftime('%m'))
           if not os.path.exists(directory5):
               os.makedirs(directory5)
           directory6 = "./logs/{0}/{1}/{2}/{3}/{4}/{5}".format(message.guild.name, message.channel.name, message.author.name, self.utc_to_local(message.timestamp).strftime('%Y'), self.utc_to_local(message.timestamp).strftime('%m'), self.utc_to_local(message.timestamp).strftime('%d'))
           if not os.path.exists(directory6):
               os.makedirs(directory6)
           directory7 = "./logs/{0}/{1}/{2}/{3}/{4}/{5}/{6}".format(message.guild.name, message.channel.name, message.author.name, self.utc_to_local(message.timestamp).strftime('%Y'), self.utc_to_local(message.timestamp).strftime('%m'), self.utc_to_local(message.timestamp).strftime('%d'), self.utc_to_local(message.timestamp).strftime('%H'))
           if not os.path.exists(directory7):
               os.makedirs(directory7)
           with open("./logs/{0}/{1}/{2}/{3}/{4}/{5}/{6}/messages.txt".format(message.guild.name, message.channel.name, message.author.name, self.utc_to_local(message.timestamp).strftime('%Y'), self.utc_to_local(message.timestamp).strftime('%m'), self.utc_to_local(message.timestamp).strftime('%d'), self.utc_to_local(message.timestamp).strftime('%H')), "a") as myfile:
              myfile.write("\n{0} : {1}\n".format(self.utc_to_local(message.timestamp).strftime('%H:%M:%S'), message.content))
           # END TOS COMPLIANT SHITCODE
           # if message.author.bot:
             # return
           # Prevents bot to bot interactions.
           # Currently breaks the bot, to be fixed.
           await self.process_commands(message)

   atomic = Atomic(prefix)
   atomic.run(token)
except:
     e = sys.exc_info()[0]
     print('fuck. {0}'.format(e))
