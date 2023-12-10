import discord
from discord.ext import commands
from logger import logger
from settings import PREFIX, COGS_DIR


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    logger.info(f"User: {bot.user} (ID: {bot.user.id})")


    # Loading cogs
    for cog_file in COGS_DIR.glob("*.py"):
        if cog_file.name != "__init__.py":
            cog_name = f"cogs.{cog_file.stem}"
            await bot.load_extension(cog_name)
            logger.info(f"Loaded cog: {cog_name}")


if __name__ == "__main__":
    pass
