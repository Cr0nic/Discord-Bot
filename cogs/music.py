import discord 
from discord.ext import commands
import youtube_dl


class MusicCog:
    def __init__(self, bot):
        self.bot = bot
    

    # players = {}

    # @commands.command(name=music)
    # async def play(self, ctx, url:str):
    #     await bot.voice_channel.connect(channel.ctx.author)
    #     server = ctx.message.guild
    #     voice_client = bot.voice_client_in(server)
    #     player = await voice_client.create_ytdl_player(url)
    #     players[server.id] = player
    #     player.start()


    @commands.command()
    async def join(self, ctx):
        await bot.voice_channel.connect(message.ctx.author)

    @commands.command()
    async def play(self, ctx, url:str):
        await bot.voice_channel.connect(message.ctx.author)



def setup(bot):
    bot.add_cog(MusicCog(bot))



