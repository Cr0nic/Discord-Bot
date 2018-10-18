import discord
from discord.ext import commands
import random
import aiohttp
import asyncio


#fetch for the insult command
async def fetch(session, url):
    async with session.get(url) as response:
        return await response.text()


#insult api
URL = "https://insult.mattbas.org/api/insult"


class RartedCog:
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="insult")
    async def insult(self, ctx, *, user_insulted: str):
        async with aiohttp.ClientSession() as session:
            raw_text = await fetch(session, URL)
            text_1 = raw_text.replace("You", user_insulted, 1)
            final_phrase = text_1.replace("are", "is", 1)
            await ctx.send(final_phrase)

def setup(bot):
    bot.add_cog(RartedCog(bot))        