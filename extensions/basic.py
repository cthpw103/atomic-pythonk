import discord
from discord.ext import commands

class Basic:
    def __init__(self, atomic):
        self.atomic = atomic

    @commands.command()
    async def meme(self, ctx):
        """Basically a ping."""
        await ctx.send("THIS, is how you Pythonk.")


def setup(atomic):
    atomic.add_cog(Basic(atomic))