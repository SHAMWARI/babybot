import discord
from discord.ext import commands

class main(commands.Cog):

	def __init__(self, client):
		self.client = client
		
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
	async def say(self, ctx, user_id = None, *, args = None):
		if user_id !=  None and args !=  None:
			try:
				target = await client.fetch_user(user_id)
				await target.send(args)
				await ctx.channel.send("'" + args + "' Сообщение было отправлено: " + target.name)
			except:
				await ctx.channel.send("Не удалось установить dm для данного пользователя.")
		else:
			await ctx.channel.send('Укажите сообщение')

#logs joins and kicks my bot
	@commands.event()
	async def on_guild_join(self, guild):
	  channel = client.get_channel(780153347051094026) 
	  log = discord.Embed(color=discord.Color.green())
	  log.title = "Добавлен на сервер"
	  log.add_field(name="Название", value=f"> {guild.name}", inline=False)
	  log.add_field(name="Участников", value=f"> {guild.member_count - 1}", inline=False)
	  log.add_field(name="Глава", value=f"> {guild.owner}", inline=False)
	  log.set_footer(text=f"ID: {guild.id}")
	  await channel.send(embed=log)


	@commands.event()
	async def on_guild_remove(self, guild):
	  channel = client.get_channel(780153347051094026) 
	  log = discord.Embed(color=discord.Color.red())
	  log.title = "Кикнут с сервера или сервер был удален"
	  log.add_field(name="Название", value=f"> {guild.name}", inline=False)
	  log.add_field(name="Участников", value=f"> {guild.member_count}", inline=False)
	  log.add_field(name="Глава", value=f"> {guild.owner}", inline=False)
	  log.set_footer(text=f"ID: {guild.id}")
	  await channel.send(embed=log)

def setup(client):
	client.add_cog(main(client))