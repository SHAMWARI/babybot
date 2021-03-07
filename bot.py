import discord
import dislash
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

#send_message_member
@client.command()
async def say(ctx, user_id = None, *, args = None):
	if user_id !=  None and args !=  None:
		try:
			target = await client.fetch_user(user_id)
			await target.send(args)
			await ctx.channel.send("`" + args + "` Сообщение было отправлено: " + target.mention)
		except:
			await ctx.channel.send("Не удалось отправить сообщение для данного пользователя.")
	else:
		await ctx.channel.send('Укажите сообщение')

#clear chat
@slash.command(
    name="Ну шо чистка по расписанию",  # Defaults to function name
    description="Ну, дворщиком тож не плохо",
    guild_ids=test_guilds  # If not specified, the command is registered globally
    # Global registration takes up to 1 hour
)
async def clear(ctx, amount: int):
	await ctx.channel.purge(limit=100)

#ping everyone
@client.command()
async def ping(ctx):
	ctx.author.id == 508315509398306827
	await ctx.channel.purge(limit=1)
	await ctx.channel.send('@everyone, здарова ебать!')

#kick
@slash.command(
    name="Пашол нахуй сука", # Defaults to function name
    description="Репан по ебалу",
    guild_ids=test_guilds # If not specified, the command is registered globally
    # Global registration takes up to 1 hour
)
async def kick(ctx, member: discord.Member,  *,  reason=None):
	emb = discord.Embed(
            title='🤡', description='Кикнут участник: ' + member.mention,
            color=0xff0000)
	await ctx.channel.purge(limit=1)
	await member.kick(reason=reason)
	emb.set_author(name=member.name,  icon_url=member.avatar_url)
	await ctx.send(embed=emb)

#ban
@slash.command(
    name="Бан чучело",  # Defaults to function name
    description="Кукумбит чучело в радиусе всего сервера",
    guild_ids=test_guilds 
)
async def ban(ctx, member: discord.Member,  *,  reason=None):
	await ctx.channel.purge(limit=1)
	emb = discord.Embed(
            title='🤡', description='Забанен участник: ' + member.mention,
            color=0xeeff00)
	await member.ban(reason=reason)
	emb.set_author(name=member.name,  icon_url=member.avatar_url)
	await ctx.send(embed=emb)

#unban
@slash.command(
    name="Стой десять год тюрьмы",  # Defaults to function name
    description="Ой, чучело сбежало",
    guild_ids=test_guilds  
)
async def unban(ctx, *, member: discord.Member):
	await ctx.channel.purge(limit=1)
	emb = discord.Embed(
            title='👋', description='Разбанен участник: ' + member.mention,
            color=0xeeff00)
	banned_users = await ctx.guild.bans()
	for ban_entry in banned_users:
		user = ban_entry.user
		await ctx.guild.unban(user)
		emb.set_author(name=member.name,  icon_url=member.avatar_url)
		emb.description(name='Разбанен участник:' + member.mention)
		await ctx.send(embed=emb)
		return

token = os.environ.get('TOKENBOT')
client.run(str(token))

