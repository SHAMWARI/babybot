import discord
from discord.ext import commands
import os 
from discord.utils import get

PREFIX = '/'
client = commands.Bot(command_prefix = PREFIX)
client.remove_command('help')

#online bot
@client.event
async def on_ready():
	print('bot connected')
	await client.change_presence(status = discord.Status.online, activity = discord.Game('/help'))

@client.command()
async def load(ctx, extension):
	if ctx.author.id == 508315509398306827:
		client.load_extension(f'cogs.{extension}')
		await ctx.send("Загрузка...")
	else: 
		await ctx.send("Вы не разработчик бота")

@client.command()
async def unload(ctx, extension):
	if ctx.author.id == 508315509398306827:
		client.unload_extension(f"cogs.{extension}")
		await ctx.send("Коги выгружены")
	else:
		await ctx.send("Вы не разработчик бота")

@client.command()
async def reload(ctx, extension):
	if ctx.author.id == 508315509398306827:
		client.unload_extension(f"cogs.{extension}")
		client.load_extension(f"cogs.{extension}")
		await ctx.send("Перезагрузка...")
	else: 
		await ctx.send("Вы не разработчик бота")

for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
		client.load_extension(f"cogs.{filename[:-3]}")

#error argument
@client.event
async def on_command_error(ctx, error):
	pass

#clear chat
@client.command()
@commands.has_permissions(administrator = True)
async def clear(ctx, amount: int):
	await ctx.channel.purge(limit = amount)

#kick
@client.command()
@commands.has_permissions(administrator = True)
async def kick(ctx, member: discord.Member,  *,  reason = None):
	emb =  discord.Embed(title = '🤡',  color = 0xff0000)
	await ctx.channel.purge(limit = 1)
	await member.kick(reason = reason)
	emb.set_author(name = member.name,  icon_url = member.avatar_url)
	emb.add_field(name = 'Кикнут участник', value = 'Кикнут участник:{}'.format(member.mention))
	await ctx.send(embed = emb)

#ban
@client.command()
@commands.has_permissions(administrator = True)
async def ban(ctx,  member: discord.Member,  *,  reason = None):
	emb =  discord.Embed(title = '🤡',  color = 0xeeff00)
	await ctx.channel.purge(limit = 1)
	await member.ban(reason = reason)
	emb.set_author(name = member.name,  icon_url = member.avatar_url)
	emb.add_field(name = 'Забанен участник', value = 'Забанен участник:{}'.format(member.mention))
	await ctx.send(embed = emb)

#unban
@client.command()
@commands.has_permissions(administrator = True)
async def unban(ctx, *, member: discord.Member):
	await ctx.channel.purge(limit = 1)
	emb =  discord.Embed(title = '👋',  color = 0xeeff00)
	banned_users =  await ctx.guild.bans()
	for ban_entry in banned_users:
		user =  ban_entry.user
		await ctx.guild.unban(user)
		emb.set_author(name = member.name,  icon_url = member.avatar_url)
		emb.add_field(name = 'Разбанен участник', value = 'Разбанен участник:{}'.format(member.mention))
		await ctx.send(embed = emb)
		return

@clear.error
async def clear_error(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		await ctx.send(f'{ctx.author.mention},  У вас отсутствуют нужные права!')
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send(f'{ctx.author.mention},  Пожалуйста,  укажите аргумент!')

@ban.error
async def ban_error(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		await ctx.send(f'{ctx.author.mention},  У вас отсутствуют нужные права!')
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send(f'{ctx.author.mention},  Пожалуйста,  укажите аргумент!')

@kick.error
async def kick_error(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		await ctx.send(f'{ctx.author.mention},  У вас отсутствуют нужные права!')
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send(f'{ctx.author.mention},  Пожалуйста,  укажите аргумент!')

@unban.error
async def unban_error(ctx, error):
	if isinstance(error, commands.MissingPermissions):
		await ctx.send(f'{ctx.author.mention},  У вас отсутствуют нужные права!')
	if isinstance(error, commands.MissingRequiredArgument):
		await ctx.send(f'{ctx.author.mention},  Пожалуйста,  укажите аргумент!')

#token
token = os.environ('TOKEN')
client.run = (str(token))

