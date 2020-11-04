import discord
import asyncio
import random
import emoji
from discord.ext import commands
from PIL import Image
import io
import typing
import aiohttp


class misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.emoji_converter = commands.EmojiConverter()
        self.emoji_list = []

    @commands.command(aliases=["em"])
    @commands.has_permissions(administrator = True)
    async def embed(self, ctx, color: typing.Optional[discord.Color] = None, *, text):
        em = discord.Embed(color=color or random.randint(0, 0xFFFFFF))
        lines = text.rsplit("\n", maxsplit=1)
        if len(lines) > 1:
          if lines[1].startswith("https://"):
            em.set_image(url=lines[1])
            text = lines[0]
        elif lines[0].startswith("https://"):
          em.set_image(url=lines[0])
          text = ""
        em.title = text
        await ctx.send(embed=em)
        await ctx.message.delete()

def setup(bot):
    bot.add_cog(misc(bot))
