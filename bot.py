import discord
from discord.ext import commands
import os 
import youtube_dl
from discord.utils import get

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

#mute
@client.command()
@commands.has_permissions(administrator=True)
async def mute(ctx,member:discord.Member=None, reason=None):
	emb = discord.Embed(title='Мут', description='Мут участниа', color=0xeeff00)
	await ctx.channel.purge(limit=1)
	mute_role=discord.utils.get(ctx.message.guild.roles, name='mute')
	await member.add_roles(mute_role)
	emb.set_author(name=member.name, icon_url=member.avatar_url)
	emb.add_field(name='Замьючен участник',value='Замьючен участник:{}'.format(member.mention))
	await ctx.send(embed=emb)

#unmute
@client.command()
@commands.has_permissions(administrator=True)
async def unmute(ctx,member:discord.Member=None):
await ctx.channel.purge(limit=1)
	mute_role=discord.utils.get(ctx.message.guild.roles, name='mute')
	await member.remove_roles(mute_role)

#play
#@client.command()
#async def play(ctx, url:str):
#########################	global voice
########################	channel=ctx.message.author.voice.channel
#######################	voice=get(client.voice_clients,guild=ctx.guild)
######################	if voice and voice.is_connected():
#####################		await voice.move_to(channel)
####################	else:
###################		voice = await channel.connect()
##################		await ctx.send(f'Бот присоединился к каналу: **{channel}**')
#################	song_there = os.path.isfile('song.mp3')
################	try:
###############		if song_there:
##############			os.remove('song.mp3')
#############			print('[log] Старый файл удален')
############	except PermissionError:
###########		print('[log] Не удалось удалить файл')
##########	await ctx.send('Пожалуйста ожидайте')
#########	voice=get(client.voice_clients,guild=ctx.guild)
########	ydl_opts={
#######		'format':'bestaudio/best',
######		'postprocessors':[{
####			'key': 'FFmpegExtractAudio',
###			'preferredcodec':'mp3',
##			'preferredquality':'192'
##		}],
#	}
#	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#		print('[log]Загружаю музыку...')
#		ydl.download([url])
#	for file in os.listdir('./'):
##########		if file.endswith('.mp3'):
#########			name=file
########			print('[log] Переименовываю файл: {file}')
#######			os.rename(file,'song.mp3')
######
#####	voice.play(discord.FFmpegPCMAudio('song.mp3'),after=lambda e:print(f'[log]{name}, **__Музыка закончила свое проигрывание__**'))
#####	voice.source=discord.PCMVolumeTransformer(voice.source)
####	voice.source.volume = 1.05
###	song_name=name.rsplit('-',2)
##	await ctx.send(f'Сейчас проигрывает музыка: **{song_name[0]}**')
#
#leave
#########@client.command()
########async def leave(ctx):
#######	channel=ctx.message.author.voice.channel
######	voice=get(client.voice_clients,guild=ctx.guild)
#####	if voice and voice.is_connected():
####		await voice.disconnect()
###	else:
##		voice = await disconnect.channel()
#		await ctx.send(f'Бот отсоединился от канала: #{channel}')

#send_message_member
@client.command()
async def dm(ctx,user_id=None,*,args=None):
	if user_id != None and args != None:
		try:
			target=await client.fetch_user(user_id)
			await target.send(args)
			await ctx.channel.send("'" + args + "' Сообщение было отправлено: " + target.name)
		
		except:
			await ctx.channel.send("Не удалось установить dm для данного пользователя.")
	else:
		await ctx.channel.send('Юзер айди')

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