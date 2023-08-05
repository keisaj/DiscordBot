from discord.ext import commands
from utils import get_chuck_noris_joke


class ChuckNorrisJoke(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def joke(self, ctx):
        """Get random Chuck Norris joke"""
        joke = get_chuck_noris_joke()
        await ctx.channel.send(joke)


async def setup(bot):
    await bot.add_cog(ChuckNorrisJoke(bot))
