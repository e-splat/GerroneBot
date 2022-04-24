import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import logging
import random
from discord_slash import SlashCommand, SlashContext
from discord_slash.utils.manage_commands import create_choice, create_option

load_dotenv()

Ds_Token = os.getenv('TOKEN')
Prefix = os.getenv('PREFIX')

client = discord.Client()
bot = commands.Bot(command_prefix=Prefix)
slash = SlashCommand(bot, sync_commands=True)

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

@bot.event
async def on_ready():
    print('Bot brondo, evviva tutti quanti')

@bot.event
async def on_message(message):
    if message.author == client.user:
        return
    await bot.process_commands(message)

@bot.command(pass_context=True, aliases=['gerry','Gerry'])
async def cmd1(ctx):
    gerry1 = random.randint(1,8)
    gerry2 = str(gerry1)
    embed1 = discord.Embed(title="Ecco una foto di Gerry a caso (Gerry numero " + gerry2 + ")")
    embed1.set_image(url="https://raw.githubusercontent.com/e-splat/StorageImmagini/main/Gerry/Scotti/" + gerry2 + ".png")
    await ctx.send(embed=embed1)

@slash.slash(
    name="gerry",
    description="8 Foto di Gerry totalmente a caso",
    guild_ids=[955181531779985458]    
)    
async def _gerry(ctx: SlashContext):
    gerry1 = random.randint(1,8)
    gerry2 = str(gerry1)
    embed1 = discord.Embed(title="Ecco una foto di Gerry a caso (Gerry numero " + gerry2 + ")")
    embed1.set_image(url="https://raw.githubusercontent.com/e-splat/StorageImmagini/main/Gerry/Scotti/" + gerry2 + ".png")
    await ctx.send(embed=embed1)
    
@slash.slash(
    name="Github",
    description="Codice sorgente e repo del bot (Forckalo tutto eh)",
    guild_ids=[955181531779985458]    
)    
async def _gerry(ctx: SlashContext):
    await ctx.send("https://github.com/e-splat/GerroneBot")


bot.run(Ds_Token)
