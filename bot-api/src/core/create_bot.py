import discord
from discord.ext import commands
from src.config import config
import time

def create_bot():
    intents = discord.Intents.default()
    intents.message_content = True

    description = ""

    bot = commands.Bot(
        command_prefix=config.PREFIX,
        description=description,
        intents=intents
    )

    @bot.event
    async def on_ready():
        print('🍿 Popocas PromoBot Inicializando....')
        time.sleep(2)

        print('🍿 Carregando promoções...')
        time.sleep(3.5)

        print('\nBot carregado. As promoções começaram a aparecer')

    return bot


