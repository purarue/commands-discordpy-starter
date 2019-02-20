import os
import yaml
from discord import Client
from asyncio import sleep
from discord.ext import commands

root_directory = os.path.dirname(__file__)
token_file = os.path.abspath(os.path.join(root_directory, ".token.yaml"))

# bot responds when mentioned e.g. `@bot_name`
bot = commands.Bot(command_prefix=commands.when_mentioned, pm_help=None,
                    case_insensitive=False)
# If you want it to respond to a symbol instead, use this line instead:
# bot = commands.Bot(command_prefix="!", pm_help=None, case_insensitive=False)

bot.remove_command('help') # remove default help

# if a bot is mentioned with two spaces after the mention
# the command will be ignored. Fix this by removing extra spaces:
@bot.event
async def on_message(message):
    message.content = " ".join(message.content.strip().split())
    await bot.process_commands(message)

# Prints to command line when the bot is connected to discord and ready for commands
@bot.event
async def on_ready():
    print("Ready!")
    
# Here are some example commands
# once the bot is running, you can do: @bot_name hi there, @bot_name roles
# the names of the functions correspond to the command in discord
# see here for more information: 
# https://discordpy.readthedocs.io/en/rewrite/ext/commands/commands.html

@bot.command()
async def hi(message: str):
    """Says hi to a user."""
    await bot.say("Hi {}!".format(message))
    
@bot.command(pass_context=True)
async def roles(ctx):
    """Responds with a users roles"""
    roles = ["`{}`".format(role.name) for role in ctx.message.author.roles]
    await bot.say("Your roles are: {}".format(", ".join(roles)))
    
@bot.command(pass_context=True)
async def admin(ctx):
    """Test if a user has administrator on this server"""
    if ctx.message.author.server_permissions.administrator:
        await bot.say("You're admin on this server.")
    else:
        await bot.say("You don't have admin on this server...")


# on_command_error gets called whenever theres an exception in a command
@bot.command(pass_context=True)
@bot.event
async def on_command_error(error, ctx):
    
    # name of the command which caused this error
    cmd_name = ctx.invoked_with
    # "message.content represents pings like <34239482399>"
    # replace ` to prevent @everyone abuse
    args = ctx.message.content.split(">", maxsplit=1)[1].strip().replace("`", '').split()

    # prevent self-loops
    if hasattr(ctx.command, 'on_error'):
        print("on_command_error self loop occured")
        return

    if isinstance(error, commands.CommandNotFound):
        await bot.send_message(ctx.message.channel, "Could not find the command `{}`.".format(cmd_name))
    elif isinstance(error, commands.MissingRequiredArgument) and cmd_name == "hi":
        await bot.send_message(ctx.message.channel, "You didn't give me anyone to say hi to...")
    else:
        await bot.send_message(ctx.message.channel, "Other Error: {}: {}".format(type(error).__name__, error))
        raise error

if os.path.exists(token_file):
    with open(token_file) as token_f:
        token = yaml.load(token_f)["token"]
    bot.run(token)
else:
    print("Could not find token file. Put the token in {}.".format(token_file))
