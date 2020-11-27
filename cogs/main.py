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

def setup(client):
	client.add_cog(main(client))