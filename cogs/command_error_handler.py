import discord 
from discord.ext import commands
import traceback
import sys

class CommandErrorHandler:
    def __init__(self, bot):
        self.bot = bot

    async def on_command_error(self, ctx, error):

        if hasattr(ctx.command, "on_error"):
            return
        
        ignored = (commands.CommandNotFound, commands.UserInputError)

        if isinstance(error, ignored):
            return
        elif isinstance(error, commands.DisabledCommand):
            return await ctx.send("{} command has been disabled" .format(ctx.command))
        elif isinstance(error, commands.NoPrivateMessage):
            try:
                return await ctx.author.send("{} command can not be used in private messages" .format(ctx.command))
            except:
                pass
        elif isinstance(error, commands.BadArgument):
            if ctx.command.qualified_name == "tag list":
                return await ctx.send("i could not find that member uwu")
        

        print("ignoring exception in command {}:" .format(ctx.command), file=sys.stderr)
        traceback.print_exception(type(error), error, error.__traceback__, file=sys.stderr)

def setup(bot):
    bot.add_cog(CommandErrorHandler(bot))
