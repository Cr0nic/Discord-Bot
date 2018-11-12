import discord
from discord.ext import commands


class UsefulCog:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="clear")
    async def clear(self, ctx, amount: int):
        if amount < 2:
            await ctx.send("sorry boi cunt not delete")
        else:
            await ctx.channel.purge(limit=amount + 1)
            await ctx.send("deleted {} messages" .format(amount))
    


    make a help command
    @commands.command(name="help")
    async def help(self, ctx):
        embed = discord.Embed(colour=0x53c160)





def setup(bot):
    bot.add_cog(UsefulCog(bot))
