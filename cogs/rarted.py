import discord
from discord.ext import commands
import random
import aiohttp
import asyncio
import json
import random as r

#fetch with plain text
async def fetch_text(session, URL):
    async with session.get(URL) as response:
        return await response.text()

#fetch with json data
async def fetch_json(session, URL):
    async with session.get(URL) as response:
        return await response.json()


#api's
insult_url = "https://insult.mattbas.org/api/insult"
dog_url = "http://shibe.online/api/shibes?"
cat_url ="http://shibe.online/api/cats"
bird_url ="http://shibe.online/api/birds"

#pictures for rock paper scissor
scissor_file = discord.File("scissor_man.jpg")
rock_file = discord.File("the_rock.jpg")
paper_file = discord.File("paper_man.jpg")

#rock paper scissor compare
def compare(player_c, computer):
        results = {("Rock", "Paper"): False,
                ("Rock", "Scissor"): True,
                ("Paper", "Rock"): True,
                ("Paper", "Scissor"): False,
                ("Scissor", "Rock"): False,
                ("Scissor", "Paper"): True}
        return results[player_c, computer]


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
    async def dog_picture(self, ctx):
        async with aiohttp.ClientSession() as session:
            dog_picture = await fetch_json(session, dog_url)

            embed = discord.Embed(colour=0xf9e390)
            embed.set_image(url=dog_picture[0])

            await ctx.send(embed=embed)


    @commands.command(name="birdo")
    async def bird_picture(self, ctx):
        async with aiohttp.ClientSession() as session:
            dog_picture = await fetch_json(session, bird_url)

            embed = discord.Embed(colour=0x53c160)
            embed.set_image(url=dog_picture[0])

            await ctx.send(embed=embed)
    

    @commands.command(name="cat")
    async def cat_picture(self, ctx):
        async with aiohttp.ClientSession() as session:
            dog_picture = await fetch_json(session, cat_url)

            embed = discord.Embed(colour=0x151826)
            embed.set_image(url=dog_picture[0])

            await ctx.send(embed=embed)
    

    @commands.command(name="picture")
    async def picture(self, ctx):
        await ctx.send(file=scissor_file)
        await ctx.send(file=rock_file)
        await ctx.send(file=paper_file)

    @commands.command(name="rps")
    async def rock_paper_scissor(self, ctx, player_choose :str):
        c = {1: "Rock", 2: "Paper", 3: "Scissor"}
        computer = c[r.randint(1, 3)]
        player_c = player_choose.capitalize()
        if computer == "Rock":
            await ctx.send(file=rock_file)
        elif computer == "Paper":
            await ctx.send(file=paper_file)
        elif computer == "Scissor":
            await ctx.send(file=scissor_file)
        
        if player_c == computer:
            await ctx.send("Tie, bakka")
        elif compare(player_c, computer):
            await ctx.send("You won, dick")
        else:
            await ctx.send("UwU you lost haha")
            


def setup(bot):
    bot.add_cog(RartedCog(bot))        