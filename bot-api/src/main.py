import asyncio

from config.config import BOT_TOKEN
from core.create_bot import create_bot

async def main():
    # Cria um bot com as configs definidas
    bot = create_bot()

    await bot.load_extension('src.commands.general_commands')

    await bot.start(BOT_TOKEN)

asyncio.run(main())
