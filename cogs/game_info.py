from discord.ext import commands
from utils import get_games_prices, get_games_data


class GamesInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def game(self, ctx):
        if ctx.invoked_subcommand is None:
            await  ctx.send(f"No, {ctx.subcommand_passed} does not exist in game")

    @game.command()
    async def price(self, ctx, *game_name):
        """Gives best price for given game based on gg.deals"""
        game_data = get_games_data(game_title=" ".join(game_name))
        game_prices = get_games_prices(game_data)
        formatted_list = "\n".join(game_prices)

        if game_prices:
            await ctx.channel.send(f"Here are some game deals:\n\n{formatted_list}")
        else:
            await ctx.channel.send("Game not found")

async def setup(bot):
    await bot.add_cog(GamesInfo(bot))