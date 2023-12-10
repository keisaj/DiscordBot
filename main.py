from settings import DISCORD_API_SECRET
from bot import bot

if __name__ == '__main__':
    bot.run(DISCORD_API_SECRET, root_logger=True)
