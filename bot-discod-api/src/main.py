import discord
from discord import commands

from .env import *

requirments = discord.Intents.default()
requirments.message_content = True

client = commands.Bot(command_prefix='!', intents=requirments)

# Colocar a parte abaixo em um arquivo separado (analisar todo o código e fazer isso)
@client.event
async def on_ready():
  print('Bot inicializado com sucesso!')

@client.command()
async def ola(ctx):
  await ctx.send('Mensagem que o bot deverá responder quando receber "ola" ')


# comando para rodar o bot
client.run(BOT_TOKEN)