import discord
from discord.ext import commands
import os 

client = commands.Bot(command_prefix = '>', self_bot=False)

@client.event
async def on_ready():
	print('log')


@client.command()
async def say(ctx,*,text):
	await ctx.send(embed=discord.Embed(description=text))

token = os.environ.get('TOKENBOT')
token2 = os.environ.get('TOKENBOT2')

client.run("TOKENBOT2", bot=True)
client.run(str(token))
