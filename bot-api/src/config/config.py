import os
from dotenv import load_dotenv

# Carrega variáveis de ambiente de um arquivo .env
load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')