import os
import pathlib

from dotenv import load_dotenv

load_dotenv()

PREFIX = "!"

DISCORD_API_SECRET = os.getenv("DISCORD_API_TOKEN")

BASE_DIR = pathlib.Path(__file__).parent

CMDS_DIR = BASE_DIR / "bot/cmds"
COGS_DIR = BASE_DIR / "bot/cogs"
