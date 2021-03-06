import discord
from discord.ext import commands
from discord.utils import get
from dislash.interactions import *
from dislash.slash_commands import SlashClient
import os 

PREFIX = '/'
client = commands.Bot(command_prefix = PREFIX)
client.remove_command('help')
slash = SlashClient(client)
test_guilds = [699964701098115123]

#online bot
@client.event
async def on_ready():
	print('bot connected')
	await client.change_presence(status = discord.Status.online, activity = discord.Game('/help'))

@client.event
async def on_guild_join(guild):
  channel = client.get_channel(780153347051094026) 
  log = discord.Embed(color=discord.Color.green())
  log.title = "Добавлен на сервер"
  log.add_field(name="Название", value=f"> {guild.name}", inline=False)
  log.add_field(name="Участников", value=f"> {guild.member_count - 1}", inline=False)
  log.add_field(name="Глава", value=f"> {guild.owner}", inline=False)
  log.set_footer(text=f"ID: {guild.id}")
  await channel.send(embed=log)

@client.event
async def on_guild_remove(guild):
  channel = client.get_channel(780153347051094026) 
  log = discord.Embed(color=discord.Color.red())
  log.title = "Кикнут с сервера или сервер был удален"
  log.add_field(name="Название", value=f"> {guild.name}", inline=False)
  log.add_field(name="Участников", value=f"> {guild.member_count}", inline=False)
  log.add_field(name="Глава", value=f"> {guild.owner}", inline=False)
  log.set_footer(text=f"ID: {guild.id}")
  await channel.send(embed=log)

#send_message_member
@slash.command()
async def say(ctx, user_id = None, *, args = None):
	if user_id !=  None and args !=  None:
		try:
			target = await client.fetch_user(user_id)
			await target.send(args)
			await ctx.channel.send("'" + args + "' Сообщение было отправлено: " + target.name)
		except:
			await ctx.channel.send("Не удалось отправить сообщение для данного пользователя.")
	else:
		await ctx.channel.send('Укажите сообщение')

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
async def clear(ctx, amount: int):
	await ctx.channel.purge(limit = amount)

#kick
@client.command()
async def kick(ctx, member: discord.Member,  *,  reason = None):
	emb = discord.Embed(title='🤡', description='Забанен участник:' + member.mention,  color=0xff0000)
	await ctx.channel.purge(limit = 1)
	await member.kick(reason = reason)
	emb.set_author(name = member.name,  icon_url = member.avatar_url)
	await ctx.send(embed = emb)

#ban
@client.command()
async def ban(ctx, member: discord.Member,  *,  reason = None):
	await ctx.channel.purge(limit=1)
	emb = discord.Embed(title = '🤡',  color = 0xeeff00)
	await member.ban(reason = reason)
	emb.set_author(name = member.name,  icon_url = member.avatar_url)
	await ctx.send(embed = emb)

#unban
@client.command()
async def unban(ctx, *, member: discord.Member):
	await ctx.channel.purge(limit = 1)
	emb =  discord.Embed(title = '👋',  color = 0xeeff00)
	banned_users =  await ctx.guild.bans()
	for ban_entry in banned_users:
		user =  ban_entry.user
		await ctx.guild.unban(user)
		emb.set_author(name = member.name,  icon_url = member.avatar_url)
		emb.description(name='Разбанен участник:' + member.mention)
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

token = os.environ.get('TOKENBOT')
client.run(str(token))

