import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
from utility import *

load_dotenv()

#Sets intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

#Some basic setup
token = os.getenv('TOKEN')
save_path = os.getenv('SAVE_PATH')
bot = commands.Bot(command_prefix='!', description="URN Downloader", intents=intents)

#Login status message
@bot.event
async def on_ready():
    print("Bot started. Logged in as {0.user}".format(bot))

#Main download command
@bot.command()
async def d(ctx, *args):
    if len(ctx.message.attachments) > 0:
        await ctx.send("Attachments detected....attempting to download")
        await retrieve_attachments(ctx.message, args)
    else:
        await ctx.send("No attachments have been provided")

#Actually runs the thing
bot.run(token)

