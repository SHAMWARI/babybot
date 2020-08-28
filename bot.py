import discord
from discord.ext import commands
import os 

PREFIX='>'

client = commands.Bot(command_prefix=PREFIX)
client.remove_command('help')

#online bot
@client.event
async def on_ready():
	print('bot connected')

	await client.change_presence(status=discord.Status.online, activity=discord.Game('>help'))

#error argument
@client.event
async def on_command_error(ctx,error):
	pass

#clear chat
@client.command(pass_context=True)
@commands.has_permissions(administrator=True)

async def clear(ctx, amount: int):
	await ctx.channel.purge(limit=amount)

#kick
@client.command(pass_context=True)
@commands.has_permissions(administrator=True)

async def kick(ctx, member: discord.Member, *, reason=None):
	emb = discord.Embed(title='Кик', description='Кик участника', color=0xeeff00)

	await ctx.channel.purge(limit=1)
	await member.kick(reason=reason)

	emb.set_author(name=member.name, icon_url=member.avatar_url)
	emb.add_field(name='Кикнут участник',value='Кикнут участник:{}'.format(member.mention))
	
	await ctx.send(embed=emb)

#ban
@client.command(pass_context=True)
@commands.has_permissions(administrator=True)

async def ban(ctx, member: discord.Member, *, reason=None):
	emb = discord.Embed(title='Бан',description='Бан участника', color=0xeeff00)

	await ctx.channel.purge(limit=1)
	await member.ban(reason=reason)

	emb.set_author(name=member.name, icon_url=member.avatar_url)
	emb.add_field(name='Забанен участник', value='Забанен участник:{}'.format(member.mention))
	
	await ctx.send(embed=emb)

#unban
@client.command(pass_context=True)
@commands.has_permissions(administrator=True)

async def unban(ctx, *, member: discord.Member):
	await ctx.channel.purge(limit=1)
	emb = discord.Embed(title='Разбан', description='Разбан участника', color=0xeeff00)
	banned_users = await ctx.guild.bans()
	for ban_entry in banned_users:
		user = ban_entry.user
		await ctx.guild.unban(user)
		emb.set_author(name=member.name, icon_url=member.avatar_url)
		emb.add_field(name='Разбанен участник',value='Разбанен участник:{}'.format(member.mention))
		await ctx.send(embed=emb)
		return

#help
@client.command(pass_context=True)

async def help(ctx):
	await ctx.channel.purge(limit=1)
	emb=discord.Embed(title='Навигация по командам', color=0xeeff00)

	emb.add_field(name='{}clear'.format(PREFIX),value='Очистка чата',inline=False)
	emb.add_field(name='{}kick'.format(PREFIX), value='Кик участника',inline=False)
	emb.add_field(name='{}ban'.format(PREFIX), value='Бан участника',inline=False)
	emb.add_field(name='{}unban'.format(PREFIX), value='Разбан участника',inline=False)

	await ctx.send(embed=emb)

#send_message_member
@client.command()
async def send_message_member(ctx, member:discord.Member):
	await member.send(f'{member.mention}, Вставай еблан')

@clear.error
async def clear_error(ctx,error):
	if isinstance(error,commands.MissingPermissions):
		await ctx.send(f'{ctx.author.name}, У вас отсутствуют нужные права!')
	if isinstance(error,commands.MissingRequiredArgument):
		await ctx.send(f'{ctx.author.name}, Пожалуйста, укажите аргумент!')
@ban.error
async def ban_error(ctx,error):
	if isinstance(error,commands.MissingPermissions):
		await ctx.send(f'{ctx.author.name}, У вас отсутствуют нужные права!')
	if isinstance(error,commands.MissingRequiredArgument):
		await ctx.send(f'{ctx.author.name}, Пожалуйста, укажите аргумент!')

@kick.error
async def kick_error(ctx,error):
	if isinstance(error,commands.MissingPermissions):
		await ctx.send(f'{ctx.author.name}, У вас отсутствуют нужные права!')
	if isinstance(error,commands.MissingRequiredArgument):
		await ctx.send(f'{ctx.author.name}, Пожалуйста, укажите аргумент!')

@unban.error
async def unban_error(ctx,error):
	if isinstance(error,commands.MissingPermissions):
		await ctx.send(f'{ctx.author.name}, У вас отсутствуют нужные права!')
	if isinstance(error,commands.MissingRequiredArgument):
		await ctx.send(f'{ctx.author.name}, Пожалуйста, укажите аргумент!')

#token
token = os.environ.get('TOKENBOT')

client.run(str(token))
