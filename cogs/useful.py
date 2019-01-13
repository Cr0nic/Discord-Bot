import discord
from discord.ext import commands
import math


# async def bmi_man(bmi):
#     if bmi < 20:
#         await ctx.send("you're underweight")
#     elif 19 < bmi < 26:
#         await ctx.send("normal weight")
#     elif bmi > 25:
#         await ctx.send("you're are overweight")


# async def bmi_woman(bmi):
#     if bmi < 19:
#         await ctx.send("you're underweight")
#     elif 18 < bmi < 25:
#         await ctx.send("normal weight")
#     elif bmi > 24:
#         await ctx.send("you're are overweight")

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


    # @commands.command(name="bmi")
    # async def bodymassindex (self, ctx, weight: int, height: float, gender):
    #     bmi = weight // math.pow(height, 2) 
    #     await ctx.send(bmi)
    #     if gender == "m":
    #         bmi_man(bmi)
    #     elif gender == "f":
    #         bmi_woman(bmi)


    # make a help command
    # @commands.command(name="help")
    # async def help(self, ctx):
    #     embed = discord.Embed(colour=0x53c160)





def setup(bot):
    bot.add_cog(UsefulCog(bot))
