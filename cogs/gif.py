import discord
from discord.ext import commands
import time
import giphy_client
from giphy_client.rest import ApiException
import json
import SECRETS


api_instance = giphy_client.DefaultApi()
api_key = SECRETS.giphy_key
limit = 1
offset = 0
lang = "en"
fmt = "json"


class Gif_Cog:
    def __init__(self, bot):
        self.bot = bot


    #the commented stuff is an alternative but it always displays the same gif
    @commands.command(name="gif")
    async def gif(self, ctx, *, search:str):
        #q = search
        tag = search
        try:
            #api_response = api_instance.gifs_search_get(api_key, q, limit=limit, offset=offset, lang=lang, fmt=fmt)
            api_response = api_instance.gifs_random_get(api_key, tag=tag, fmt=fmt)
            gif_data = api_response.data
           # gif = gif_data[0]
            await ctx.send(gif_data.url)
        except ApiException as e:
            print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)


    @commands.command(name="randomgif")
    async def random_gif(self, ctx):
        try:
            api_response = api_instance.gifs_random_get(api_key, fmt=fmt)
            gif_data = api_response.data
            await ctx.send(gif_data.url)
        except ApiException as e:
            print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)



def setup(bot):
    bot.add_cog(Gif_Cog(bot))