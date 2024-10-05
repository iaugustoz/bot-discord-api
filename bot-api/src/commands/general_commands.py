from discord.ext import commands
from dotenv import load_dotenv

import json
import os

load_dotenv()

FEEDBACK_FILE = os.path.join(os.getcwd(), 'data', 'feedbacks.json')

def load_feedbacks():
    if not os.path.exists(FEEDBACK_FILE):
        print("Arquivo não encontrado. Criando um novo arquivo feedbacks.json.")
        with open(FEEDBACK_FILE, 'w') as f:
            json.dump([], f)

    try:
        with open(FEEDBACK_FILE, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("Erro ao decodificar JSON. Retornando lista vazia.")
        return []

def save_feedbacks(feedbacks):
    with open(FEEDBACK_FILE, 'w') as f:
        json.dump(feedbacks, f, indent=4)

async def feedback(ctx, *, message: str):
    feedbacks = load_feedbacks()

    new_feedback = {
        "user": str(ctx.author),
        "message": message
    }

    feedbacks.append(new_feedback)

    save_feedbacks(feedbacks)

    await ctx.send("Obrigado! 🍿 Sua opinião é o ingrediente secreto que deixa "
                   "nossas promoções ainda mais crocantes! 🌽")

async def help_me(ctx):
    await ctx.send('''🍿 **Popocas Promo - Cardápio de Comandos** 🍿
    
🔸 **/promo** - Receba as promoções mais quentinhas direto na sua tela! 🔥
🔸 **/help-me** - Precisa de ajuda? Veja todos os comandos e escolha sua pipoca favorita! 📜
🔸 **/feedback** - Envie um feedback sobre o sabor das promoções ou sugestões de novas pipocas! 📩
🔸 **/config** - Customize suas preferências de promoções! 🌽
🔸 **/stop-me** - Precisa desligar o bot? Desligue o fogão de pipocas! 🔌

✨ **Mais comandos deliciosos chegando em breve!** Fique de olho! 🍿
         ''')

async def shutdown(ctx):
    await ctx.send('Desligando o fogão de pipocas! 🍿👋')
    await ctx.bot.close()

async def setup(bot):
    bot.add_command(commands.Command(help_me, name='help-me'))
    bot.add_command(commands.Command(shutdown, name='stop-me'))
    bot.add_command(commands.Command(feedback, name="feedback"))
