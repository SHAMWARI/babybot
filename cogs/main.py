import discord
from discord.ext import commands

class User(commands.Cog):

	def __init__(self, client):
		self.client = client

	@client.Cog.listener()
	async def on_ready(self):
		print("Bot ready")

	@commands.command(aliases = ["user-info", "Информация"])
	async def info(self, ctx):
		await ctx.send("Hello, World!")

def setup(client):
	client.add_cog(User(client))