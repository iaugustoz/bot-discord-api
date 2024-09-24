import discord
from discord.ext import commands

from commands import promo_commands

intents = discord.Intents.default()
intents.message_content = True

description = ""

# define os prefixos de comando e ademais
bot = commands.Bot(command_prefix='!', description=description, intents=intents)

@bot.event
async def on_ready():
  print()
  print()
