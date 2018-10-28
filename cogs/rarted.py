import discord
from discord.ext import commands
import random
import aiohttp
import asyncio
import json

#fetch with plain text
async def fetch_text(session, url):
    async with session.get(url) as response:
        return await response.text()

#fetch with json data
async def fetch_json(session, url):
    async with session.get(url) as response:
        return await response.json()


#api's
insult_url = "https://insult.mattbas.org/api/insult"
dog_url = "http://shibe.online/api/shibes?"


class RartedCog:
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="insult")
    async def insult(self, ctx, *, user_insulted: str):
        async with aiohttp.ClientSession() as session:
            raw_text = await fetch_text(session, insult_url)
            text_1 = raw_text.replace("You", user_insulted, 1)
            final_phrase = text_1.replace("are", "is", 1)
            await ctx.send(final_phrase)

    @commands.command(name="doggo")
    async def doggo(self, ctx):
        async with aiohttp.ClientSession() as session:
            dog_picture = await fetch_json(session, dog_url)

            embed = discord.Embed(colour=0x8023c6)
            embed.set_image(url=dog_picture[0])

            await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(RartedCog(bot))        