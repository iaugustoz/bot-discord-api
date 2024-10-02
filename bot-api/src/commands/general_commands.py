from discord.ext import commands

async def help_me(ctx):
    await ctx.send('''
🍿 **Popocas Promo - Cardápio de Comandos** 🍿

🔸 **/promo** - Receba as promoções mais quentinhas direto na sua tela! 🔥
🔸 **/help-me** - Precisa de ajuda? Veja todos os comandos e escolha sua pipoca favorita! 📜
🔸 **/feedback** - Envie um feedback sobre o sabor das promoções ou sugestões de novas pipocas! 📩
🔸 **/config** - Customize suas preferências de promoções! 🌽
🔸 **/stop-me** - Precisa desligar o bot? Desligue o fogão de pipocas! 🔌

✨ **Mais comandos deliciosos chegando em breve!** Fique de olho! 🍿
         ''')

async def feedback(ctx):
    await ctx.send("Obrigado! 🍿 Sua opinião é o ingrediente secreto que deixa "
                   "nossas promoções ainda mais crocantes! 🌽")

async def shutdown(ctx):
    await ctx.send('Desligando o fogão de pipocas! 🍿👋')
    await ctx.bot.close()

async def setup(bot):
    bot.add_command(commands.Command(help_me, name='help-me'))
    bot.add_command(commands.Command(shutdown, name='stop-me'))
    bot.add_command(commands.Command(feedback, name="feedback"))
