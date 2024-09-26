from config.config import BOT_TOKEN
from core.create_bot import create_bot

# Cria um bot com as configs definidas
bot = create_bot()

bot.run(BOT_TOKEN)