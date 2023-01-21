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
prefix = os.getenv('PREFIX')
bot = commands.Bot(command_prefix=prefix, description="URN Downloader", intents=intents, help_command=None)

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

@bot.command()
async def help(ctx):
    embed=discord.Embed(title="DownlURNder Help", url="https://github.com/markjfannon/downlurnder",\
         description="Use {}d alongside an MP3 attachment to use the download tool!".format(prefix), color=0x34BD19)
    embed.add_field(name="Example Usage", value="{}d filename.mp3 filename".format(prefix))
    embed.set_footer(text="DownlURNder: Making remote AP project submissions easy")
    await ctx.send(embed=embed)
#Actually runs the thing
bot.run(token)

