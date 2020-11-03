import discord
from discord.ext import commands
import asyncio
import random

class main(commands.Cog):

	def __init__(self, client):
		self.client = client

 @commands.command()
    async def cathi(self, ctx, *, text: str = "Hi..."):
        list = (
            """ຸ 　　　＿＿_＿＿
　　／　／　  ／|"
　　|￣￣￣￣|　|
　　|　　　　|／
　　￣￣￣￣""",
            f"""ຸ 　　　{text}
 　   　 ∧＿∧＿_
　　／(´･ω･`)  ／＼
　／|￣￣￣￣|＼／
　　|　　　　|／
　　￣￣￣￣""",
        )
        for i in range(3):
            for cat in list:
                await asyncio.sleep(1.5)
                await ctx.message.edit(content=cat)

#help
	@commands.command()
	async def help (self, ctx):
		await ctx.channel.purge (limit = 1)
		emb = discord.Embed (title = 'Навигация по командам', color = 0xeeff00)
		emb.add_field (name = 'clear', value = 'Очистка чата', inline = False)
		emb.add_field (name = 'kick',  value = 'Кик участника', inline = False)
		emb.add_field (name = 'ban',  value = 'Бан участника', inline = False)
		emb.add_field (name = 'unban',  value = 'Разбан участника', inline = False)
		await ctx.send (embed = emb)

#send_message_member
	@commands.command()
	@commands.has_permissions(administrator = True)
	async def say(ctx, user_id = None, *, args = None):
		if user_id !=  None and args !=  None:
			try:
				target = await client.fetch_user(user_id)
				await target.send(args)
				await ctx.channel.send("'" + args + "' Сообщение было отправлено: " + target.name)
			except:
				await ctx.channel.send("Не удалось установить dm для данного пользователя.")
		else:
			await ctx.channel.send('Укажите сообщение')

def setup(client):
	client.add_cog(User(client))