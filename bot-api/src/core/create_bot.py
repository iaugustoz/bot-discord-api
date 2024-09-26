import discord
from discord.ext import commands
from src.config import config

def create_bot():
    intents = discord.Intents.default()
    intents.message_content = True

    description = ""

    bot = commands.Bot(
        command_prefix=config.PREFIX,
        description=description,
        intents=intents
    )

    return bot
