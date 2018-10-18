import discord
from discord.ext import commands
import SECRETS
import sys
import traceback
import logging
import STATICS
import requests


bot = commands.Bot(command_prefix="!")

initial_extensions = ["cogs.clear", "cogs.rarted"]

logging.basicConfig(level=logging.INFO)
# basic startup
@bot.event
async def on_ready():
    await bot.change_presence(activity=STATICS.activity)
    print("Ready")
    print("Im running on {} with the ID {}" .format(bot.user.name, bot.user.id))

if __name__ == "__main__":
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as error:
            print("Failed to load extension {}".format(extension))
            traceback.print_exc()

 
@bot.event
async def on_message(message):
    if message.content.startswith("ur gay"):
        channel = message.channel
        await channel.send("no u :stuck_out_tongue_winking_eye:")
    await bot.process_commands(message)


bot.run(SECRETS.TOKEN, bot=True)