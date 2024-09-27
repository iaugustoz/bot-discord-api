from time import sleep

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

    @bot.event
    async def on_ready():
        print('🍿 Popocas PromoBot Inicializando....')
        sleep(2)

        print('🍿 Carregando promoções...')
        sleep(3.5)

        print('\nBot carregado. As promoções começaram a aparecer')

    @bot.event
    async def on_command_error(ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'🍿 Faltou um grão pra estourar, {ctx.author}! Não deixe a receita pela metade!')
        elif isinstance(error, commands.CommandNotFound):
            await ctx.send(f'🍿 Hmm... esse sabor de pipoca não temos no cardápio, {ctx.author}! Tente outro!')


    return bot